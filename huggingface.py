import requests
import json

API_URLS = [
    "https://api-inference.huggingface.co/models/finiteautomata/bertweet-base-sentiment-analysis",
    "https://api-inference.huggingface.co/models/cardiffnlp/twitter-roberta-base-sentiment",
    "https://api-inference.huggingface.co/models/j-hartmann/emotion-english-distilroberta-base",
    "https://api-inference.huggingface.co/models/ProsusAI/finbert",
]

headers = {"Authorization": "Bearer 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"}


def query(payload):
    data = json.loads('{"all_data":[]}')

    for url in API_URLS:
        response = requests.post(url, headers=headers, json=payload)
        output = response.json()
        if "error" in output:
            print(output["error"])
            if "loading" in output["error"]:
                waitTime = output["estimated_time"]
                print(waitTime)
                sleep(waitTime)
        else:
            data["all_data"].append(response.json())
    return data


result = query(
    {
        "inputs": """Today, we are going to learn about a popular framework that many companies are using for the development of their web applications. We will learn the core aspects of this framework in this Django Tutorial."""
    }
)
print(result)
