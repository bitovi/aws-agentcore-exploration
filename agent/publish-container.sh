aws ecr create-repository --repository-name repka-agentcore --region us-east-1
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 755521597925.dkr.ecr.us-east-1.amazonaws.com
docker buildx build --platform linux/arm64 -t 755521597925.dkr.ecr.us-east-1.amazonaws.com/repka-agentcore:latest --push .
aws ecr describe-images --repository-name repka-agentcore --region us-east-1