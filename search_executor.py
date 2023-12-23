import requests
import json
from typing import Dict
from prompts import perplexity_system_msg


class SearchExecutor:
    """
    Executes search queries and retrieves the results.

    Attributes:
        perplexity_api_key (str): API key for Perplexity AI services.

    Methods:
        perform_search(professor_record: Dict) -> Dict:
            Executes search queries present in the professor record and updates the record with the results.
    """

    def __init__(self, perplexity_api_key: str):
        self.perplexity_api_key = perplexity_api_key
        self.url = "https://api.perplexity.ai/chat/completions"
        # Set the headers with the authorization and content type
        self.headers = {
            "Authorization": f"Bearer {self.perplexity_api_key}",
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

    def perform_search(self, professor_record: Dict) -> Dict:
        for i in range(1, 4):  # replace 2 with 6
            search_key = f"Search_{i}"
            result_key = f"Result_{i}"
            if search_key in professor_record:
                query = professor_record[search_key]
                response = self._execute_query(query)
                professor_record[result_key] = response
        return professor_record

    def _execute_query(self, query: str) -> str:
        payload = {
            "model": "pplx-70b-online",
            "messages": [
                {
                    "role": "system",
                    "content": f"{perplexity_system_msg}",
                },
                {"role": "user", "content": query},
            ],
        }
        try:
            # Use the headers from the class attribute
            response = requests.post(self.url, json=payload, headers=self.headers)
            response.raise_for_status()
            response = json.loads(response.text)
            response = response["choices"][0]["message"]["content"]
            print(response)  # For debugging
            return response
        except requests.RequestException as e:
            print(f"Error: {e}")
