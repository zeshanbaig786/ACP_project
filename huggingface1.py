import requests
import json

API_URL = "https://api-inference.huggingface.co/models/finiteautomata/bertweet-base-sentiment-analysis"
headers = {"Authorization": "Bearer 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"}


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


output = query(
    {
        "inputs": """If they are ready for elections by the end of March, then we won't dissolve the assemblies. Otherwise, we want to conduct polls by dissolving the KP and Punjab assemblies,"""
    }
)
print(output)

#jout = json.loads(output)
if 'error' in output:
    print(output['error'])
    if 'loading' in output['error']:
        waitTime = output['estimated_time']
        print(waitTime)
        sleep(waitTime)
    
    