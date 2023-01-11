import requests
import json,time

API_URLS = [
    "https://api-inference.huggingface.co/models/finiteautomata/bertweet-base-sentiment-analysis",
    "https://api-inference.huggingface.co/models/cardiffnlp/twitter-roberta-base-sentiment",
    "https://api-inference.huggingface.co/models/j-hartmann/emotion-english-distilroberta-base",
    "https://api-inference.huggingface.co/models/ProsusAI/finbert",
]

headers = {"Authorization": "Bearer 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"}

class HuggingFace:        
    def query(self,payload):
        data = json.loads('{"all_data":[]}')
        data1 = dict(inputs=payload, 
            options=dict(wait_for_model=True))

        for url in API_URLS:
            response = requests.post(url, headers=headers, data=json.dumps(data1))
            output = response.json()
            if "error" in output:
                print(output["error"])
                if "loading" in output["error"]:
                    waitTime = output["estimated_time"]
                    print(waitTime)
                    time.sleep(waitTime)
            else:
                #data["all_data"].append(url)
                # for dat in output[0]:
                #     print(dat['label'],dat['score'])
                splits = url.split('/')
                model_name = splits[len(splits)-2]+'|'+splits[len(splits)-1]
                output[0].insert(0,{'model':model_name})
                print((output[0][0]))
                #output[0]['url'] = url
                data["all_data"].append(output[0])
        return data


# result = query(
#     {
#         "inputs": """Today, we are going to learn about a popular framework that many companies are using for the development of their web applications. We will learn the core aspects of this framework in this Django Tutorial."""
#     }
# )
# print(result)
