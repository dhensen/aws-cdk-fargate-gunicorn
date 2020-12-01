
## Install CDK

```
git clone <this_repo>
yarn install
```

## Working on the API locally
```
cd app
poetry install
uvicorn api:app --reload
```

## Working on the stack locally
```
cd cdk_stack
# TODO replace requirements.txt by pyproject.toml
```

## Docker

```
docker build -f app/Dockerfile -t fargate-app app
docker run -p8000:8000 fargate-app:latest
```
