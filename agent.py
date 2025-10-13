import os
import requests

from strands import Agent, tool

from bedrock_agentcore.memory.integrations.strands.config import AgentCoreMemoryConfig, RetrievalConfig
from bedrock_agentcore.memory.integrations.strands.session_manager import AgentCoreMemorySessionManager

from strands_tools import calculator # Import the calculator tool
from strands_tools import current_time # Import current_time tool
from strands.tools.mcp.mcp_client import MCPClient

from bedrock_agentcore.runtime import BedrockAgentCoreApp
from bedrock_agentcore_starter_toolkit.operations.gateway.client import GatewayClient
from strands.models import BedrockModel

from mcp.client.streamable_http import streamablehttp_client


# Integrate with Bedrock AgentCore
app = BedrockAgentCoreApp()

MEMORY_ID = os.getenv("BEDROCK_AGENTCORE_MEMORY_ID")
REGION = os.getenv("AWS_REGION")
CLIENT_ID = os.getenv("AWS_ACCESS_KEY_ID")
CLIENT_SECRET = os.getenv("AWS_SECRET_ACCESS_KEY")
TOKEN_URL = os.getenv("BEDROCK_AGENTCORE_TOKEN_URL")

MODEL_ID = "us.anthropic.claude-3-7-sonnet-20250219-v1:0"

ci_sessions = {}
current_session = None

model_id = "openai.gpt-oss-120b-1:0"
model = BedrockModel(
    model_id=model_id,
    streaming=False, # Streaming seems to break tool calls on occasion?
    region_name="us-east-1" #Specify your AWS region here. Default is us-east-1
)

def _create_streamable_http_transport(headers=None):
    global access_token

    url = "https://api.repkam09.com/api/mcp/stream"
    access_token = "cmljaGFyZC10b2tlbg=="
    headers = {**headers} if headers else {}
    headers["Authorization"] = f"Bearer {access_token}"
    return streamablehttp_client(
        url,
        headers=headers
    )

@app.entrypoint
def strands_agent_bedrock(payload, context):
    """
    Invoke the agent with a payload
    """
    global current_session

    if not MEMORY_ID:
        print("Memory not configured. Please set the BEDROCK_AGENTCORE_MEMORY_ID environment variable.")
        return {"error": "Memory not configured"}

    print("Payload:", payload)
    print("Context:", context)
    print("MEMORY_ID:", MEMORY_ID)
    print("REGION:", REGION)

    actor_id = context.headers.get('X-Amzn-Bedrock-AgentCore-Runtime-Custom-Actor-Id', 'user') if hasattr(context, 'headers') else 'user'

    print("Actor ID:", actor_id)

    session_id = getattr(context, 'session_id', 'default')
    current_session = session_id

    memory_config = AgentCoreMemoryConfig(
        memory_id=MEMORY_ID,
        session_id=session_id,
        actor_id=actor_id,
        retrieval_config={
            f"/users/{actor_id}/facts": RetrievalConfig(top_k=3, relevance_score=0.5),
            f"/users/{actor_id}/preferences": RetrievalConfig(top_k=3, relevance_score=0.5)
        }
    )

    with mcp_client:
        mcp_tools = mcp_client.list_tools_sync()
        print(f"Discovered {mcp_tools} MCP tools.")
        print("MCP Tools:", [tool.tool_name for tool in mcp_tools])
        agent = Agent(
            model=model,
            session_manager=AgentCoreMemorySessionManager(memory_config, REGION),
            tools=mcp_tools,
            system_prompt="You're a helpful assistant. You have access to some basic tools to help you.",
            trace_attributes={
                "user.id": "mrepka@bitovi.com",
                "tags": [
                    "Python-AgentSDK",
                    "Observability-Tags",
                    "CloudWatch-Demo"
                ]
            }  
        )

        user_input = payload.get("prompt", "")
        result = agent(user_input)
        
        # return response.message['content'][0]['text']
        # return {"response": result.message.get('content', [{}])[0].get('text', str(result))}
        return result

mcp_client = MCPClient(_create_streamable_http_transport)

if __name__ == "__main__":
    app.run()