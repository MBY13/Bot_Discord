import boto3
import json

client = boto3.client("ecs", region_name="us-east-1")

response = client.list_tasks(
    cluster='Cluster-Bot',
    desiredStatus='RUNNING',
    launchType='FARGATE'
)

response = json.loads(json.dumps(response))
response = response['taskArns'][0]

response = client.stop_task(
    cluster='Cluster-Bot',
    task=f'{response}',
    reason='DEPLOY GITLAB'
)