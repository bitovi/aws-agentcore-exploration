## AgentCore Example

Getting Started
https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agentcore-get-started-toolkit.html

This REALLY seems to be Python only at the moment.

Create a Python Virtual Environment:

```
    python -m venv venv
    source venv/bin/activate
```

Install the required packages:

```shell
    pip install -r requirements.txt
```

## Run the Agent

```shell
    python agent.py
```

Run the Frontend

```shell
    streamlit run frontend.py
```

Example app is using a Python AI Agent Library called `strands` to interact with the user.
https://strandsagents.com/latest/documentation/docs/user-guide/deploy/deploy_to_bedrock_agentcore/
"Build production-ready, multi-agent AI systems in a few lines of code"

Open a browser to see the chat:

```text
  You can now view your Streamlit app in your browser.
  Local URL: http://localhost:8501
```

To build the Infrastructure

```
npm run cdk deploy
```

Resulted in this:

```
 infra@0.1.0 cdk
> cdk deploy

Stack synthesized successfully

✨  Synthesis time: 3.05s

Need to perform AWS calls for account 755521597925, but no credentials have been configured
```

First need to run `npm run cdk bootstrap`

To configure `aws` cli credentils, use `aws configure` and grab keys from Browser

Got Environment Boostrapped

Now running Deploy results in this:

```


Do you wish to deploy these changes (y/n)? y
InfraStack: deploying... [1/1]
InfraStack: creating CloudFormation changeset...
[███████████████████████▏··································] (2/5)

4:47:18 PM | CREATE_IN_PROGRESS   | AWS::CloudFormation::Stack | InfraStack
4:47:21 PM | CREATE_IN_PROGRESS   | AWS::IAM::Role             | RepkaBedrockAgentRole
```

And finally...

```
 ✅  InfraStack

✨  Deployment time: 48.68s

Stack ARN:
arn:aws:cloudformation:us-east-2:755521597925:stack/InfraStack/4c61e550-a61a-11f0-8b45-0652d9425cb9

✨  Total time: 51.09s
```

AgentCore Config

```
pip install bedrock-agentcore-starter-toolkit
```

Now you are ready, make sure you have set AWS env variables and secret.

```
agentcore configure --entrypoint agent.py -n strands_agentcore -r us-east-1 -er "arn:aws:iam::755521597925:role/RepkaBedrockAgentRole"
```

Results in this

```

Enable long-term memory extraction? (yes/no) [no]: yes
✓ Configuring short-term + long-term memory
Will create new memory with mode: STM_AND_LTM
Memory configuration: Short-term + Long-term memory enabled
Generated .dockerignore
Generated Dockerfile: /Volumes/Bitovi/aws-agentcore-example/Dockerfile
Generated .dockerignore: /Volumes/Bitovi/aws-agentcore-example/.dockerignore
Setting 'strands_agentcore' as default agent
╭────────────────────────────────────────────────────────────────────────────────────── Configuration Success ───────────────────────────────────────────────────────────────────────────────────────╮
│ Configuration Complete                                                                                                                                                                             │
│                                                                                                                                                                                                    │
│ Agent Details:                                                                                                                                                                                     │
│ Agent Name: strands_agentcore                                                                                                                                                                      │
│ Runtime: Docker                                                                                                                                                                                    │
│ Region: us-east-1                                                                                                                                                                                  │
│ Account: 755521597925                                                                                                                                                                              │
│                                                                                                                                                                                                    │
│ Configuration:                                                                                                                                                                                     │
│ Execution Role: arn:aws:iam::755521597925:role/RepkaBedrockAgentRole                                                                                                                               │
│ ECR Repository: Auto-create                                                                                                                                                                        │
│ Authorization: IAM (default)                                                                                                                                                                       │
│                                                                                                                                                                                                    │
│                                                                                                                                                                                                    │
│ Memory: Short-term memory (30-day retention)                                                                                                                                                       │
│                                                                                                                                                                                                    │
│ 📄 Config saved to: /Volumes/Bitovi/aws-agentcore-example/.bedrock_agentcore.yaml                                                                                                                  │
│                                                                                                                                                                                                    │
│ Next Steps:                                                                                                                                                                                        │
│    agentcore launch                                                                                                                                                                                │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
(.venv) mark@bitovi-m2 aws-agentcore-example
```

Attempt to launch

```
agentcore launch --code-build
```

See: https://aws.github.io/bedrock-agentcore-starter-toolkit/api-reference/cli.html#configure-an-agent
This can also be used as `agentcore launch --local` to run the agent locally, and invoked locally with `agentcore invoke '{"prompt": "Test locally"}' --local` this requires AWS credentials to be set with `aws configure`. Throws a ton of errors around exporting logs to localhost:4317.

Can set environment variables with `agentcore launch --env API_KEY=abc123 --env DEBUG=true`

```
(.venv) mark@bitovi-m2 aws-agentcore-example % agentcore status
✅ MemoryManager initialized for region: us-east-1
🔎 Retrieving memory resource with ID: strands_agentcore_mem-9iGRmBGvp4...
  ✅ Found memory: strands_agentcore_mem-9iGRmBGvp4
╭───────────────────────────────────────────────────────────────────────────────── Agent Status: strands_agentcore ──────────────────────────────────────────────────────────────────────────────────╮
│ Ready - Agent deployed and endpoint available                                                                                                                                                      │
│                                                                                                                                                                                                    │
│ Agent Details:                                                                                                                                                                                     │
│ Agent Name: strands_agentcore                                                                                                                                                                      │
│ Agent ARN: arn:aws:bedrock-agentcore:us-east-1:755521597925:runtime/strands_agentcore-lIdpKbBAl8                                                                                                   │
│ Endpoint: DEFAULT (READY)                                                                                                                                                                          │
│ Region: us-east-1 | Account: 755521597925                                                                                                                                                          │
│                                                                                                                                                                                                    │
│ Memory: STM+LTM (provisioning...) (strands_agentcore_mem-9iGRmBGvp4)                                                                                                                               │
│          ⚠️  Memory is provisioning. STM will be available once ACTIVE.                                                                                                                             │
│                                                                                                                                                                                                    │
│ Deployment Info:                                                                                                                                                                                   │
│ Created: 2025-10-10 20:55:56.580748+00:00                                                                                                                                                          │
│ Last Updated: 2025-10-10 20:56:28.889957+00:00                                                                                                                                                     │
│                                                                                                                                                                                                    │
│ 📋 CloudWatch Logs:                                                                                                                                                                                │
│    /aws/bedrock-agentcore/runtimes/strands_agentcore-lIdpKbBAl8-DEFAULT --log-stream-name-prefix "2025/10/10/[runtime-logs]"                                                                       │
│    /aws/bedrock-agentcore/runtimes/strands_agentcore-lIdpKbBAl8-DEFAULT --log-stream-names "otel-rt-logs"                                                                                          │
│                                                                                                                                                                                                    │
│ 🔍 GenAI Observability Dashboard:                                                                                                                                                                  │
│    https://console.aws.amazon.com/cloudwatch/home?region=us-east-1#gen-ai-observability/agent-core                                                                                                 │
│                                                                                                                                                                                                    │
│ ⏱️  Note: Observability data may take up to 10 minutes to appear after first launch                                                                                                                 │
│                                                                                                                                                                                                    │
│ 💡 Tail logs with:                                                                                                                                                                                 │
│    aws logs tail /aws/bedrock-agentcore/runtimes/strands_agentcore-lIdpKbBAl8-DEFAULT --log-stream-name-prefix "2025/10/10/[runtime-logs]" --follow                                                │
│    aws logs tail /aws/bedrock-agentcore/runtimes/strands_agentcore-lIdpKbBAl8-DEFAULT --log-stream-name-prefix "2025/10/10/[runtime-logs]" --since 1h                                              │
│                                                                                                                                                                                                    │
│ Ready to invoke:                                                                                                                                                                                   │
│    agentcore invoke '{"prompt": "Hello"}'                                                                                                                                                          │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
(.venv) mark@bitovi-m2 aws-agentcore-example
```

Okay! That seems to be an agent. Waiting for the memory to deploy...

Running the invoke doesnt work.

```
agentcore invoke '{"prompt": "Hello"}'
╭────────────────────────────────────────────────────────────── strands_agentcore ───────────────────────────────────────────────────────────────╮
│ Session: 3490af41-4ac9-4ab3-9b63-183d39e5fef7                                                                                                  │
│ Request ID: 9f2723af-e5b9-4158-b148-0bd90f4dc1b7                                                                                               │
│ ARN: arn:aws:bedrock-agentcore:us-east-1:755521597925:runtime/strands_agentcore-lIdpKbBAl8                                                     │
│ Logs: aws logs tail /aws/bedrock-agentcore/runtimes/strands_agentcore-lIdpKbBAl8-DEFAULT --log-stream-name-prefix "2025/10/10/[runtime-logs]"  │
│ --follow                                                                                                                                       │
│       aws logs tail /aws/bedrock-agentcore/runtimes/strands_agentcore-lIdpKbBAl8-DEFAULT --log-stream-name-prefix "2025/10/10/[runtime-logs]"  │
│ --since 1h                                                                                                                                     │
│ GenAI Dashboard: https://console.aws.amazon.com/cloudwatch/home?region=us-east-1#gen-ai-observability/agent-core                               │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

Invocation failed: An error occurred (RuntimeClientError) when calling the InvokeAgentRuntime operation: Received error (500) from runtime. Please
check your CloudWatch logs for more information.
```

However, I can see the result in the CloudWatch logs. So it IS kinda working.
"User says "Hello" again. Just reply with greeting.Hello! How can I help you today?User input: Hello"

````
{
    "timestamp": "2025-10-10T21:08:50.550Z",
    "level": "ERROR",
    "message": "Invocation failed (0.505s)",
    "logger": "bedrock_agentcore.app",
    "requestId": "da94c66a-fc55-4f10-9c66-30f43514d55f",
    "sessionId": "3490af41-4ac9-4ab3-9b63-183d39e5fef7",
    "errorType": "KeyError",
    "errorMessage": "'text'",
    "stackTrace": [
        "Traceback (most recent call last):\n",
        "  File \"/usr/local/lib/python3.13/site-packages/bedrock_agentcore/runtime/app.py\", line 343, in _handle_invocation\n    result = await self._invoke_handler(handler, request_context, takes_context, payload)\n             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
        "  File \"/usr/local/lib/python3.13/site-packages/bedrock_agentcore/runtime/app.py\", line 414, in _invoke_handler\n    return await loop.run_in_executor(None, ctx.run, handler, *args)\n           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
        "  File \"/usr/local/lib/python3.13/concurrent/futures/thread.py\", line 59, in run\n    result = self.fn(*self.args, **self.kwargs)\n",
        "  File \"/usr/local/lib/python3.13/site-packages/opentelemetry/instrumentation/threading/__init__.py\", line 171, in wrapped_func\n    return original_func(*func_args, **func_kwargs)\n",
        "  File \"/app/agent.py\", line 43, in strands_agent_bedrock\n    return response.message['content'][0]['text']\n           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^\n",
        "KeyError: 'text'\n"
    ],
    "location": "/usr/local/lib/python3.13/site-packages/bedrock_agentcore/runtime/app.py:_handle_invocation:364"
}```

Maybe because I'm not using an anthropic model, we're parsing the output wrong?

To redeploy after changing code all you need seems to be to --code-build again, takes a few minutes.

````
agentcore launch --code-build
```


