import requests

API_URL = "https://api-inference.huggingface.co/models/ProsusAI/finbert"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
	"inputs": "I like you. I love you",
})