import os
import json
import requests


class BingHelper:
    def __init__(self):
        subscription_key = os.environ.get("SUBSCRIPTION_KEY")
        search_term = "Microsoft"
        search_url = "https://api.bing.microsoft.com/v7.0/news/search"
        headers = {"Ocp-Apim-Subscription-Key": subscription_key}
        params = {"q": search_term, "textDecorations": True, "textFormat": "HTML"}
        response = requests.get(search_url, headers=headers, params=params)
        response.raise_for_status()
        search_results = json.dumps(response.json())
        print(search_results)