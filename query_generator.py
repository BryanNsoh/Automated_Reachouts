import json
from typing import Dict
import google.generativeai as genai


class QueryGenerator:
    def __init__(self, google_api_key: str):
        self.google_api_key = google_api_key

    def generate_search_queries(self, student_info: Dict, professor_info: Dict) -> Dict:
        # Configure the Google Gemini Pro model
        genai.configure(api_key=self.google_api_key)
        model = genai.GenerativeModel("gemini-pro")

        previous_queries = []
        for i in range(1, 6):
            # Join previous queries into a single string
            # Check if previous_queries is empty
            if previous_queries:
                all_previous_queries = ", ".join(previous_queries)
            else:
                all_previous_queries = ""

            prompt = self._prepare_prompt(
                student_info, professor_info, all_previous_queries
            )
            response = model.generate_content(prompt)
            print(f"Query {i}: {response.text}")
            professor_info[f"Search_{i}"] = response.text
            previous_queries.append(response.text)

        return professor_info

    def _generate_new_query(
        self, student_info: Dict, professor_info: Dict, previous_queries: str
    ) -> str:
        # Construct prompt based on student and professor info, including all previous queries
        print("professor_info", professor_info)
        prompt = (
            f"Professor Info: {json.dumps(professor_info)}\n"
            f"Previous Queries: {previous_queries}\n"
            "Create a search query, unique from those above, to explore the professor's research/interests in depth. Format as a question or statement, including the professor's name, position, and Campus. The query should aim to uncover detailed insights into the professor's academic contributions and interests."
            "Example 1: What are the key research areas and contributions of [professor's name], [position] in the [Department] at [Campus]?"
            "Example 2: Identify and summarize the top 3 research interests of [professor's name] at [Campus], focusing on their impact and relevance in their field."
            "Example 3: List and provide detailed summaries of the top 5 most cited papers by [professor's name] from [Campus], highlighting their significance in the academic community."
            "Your query should be direct and aimed at gathering comprehensive information about the professor's academic profile and research achievements. You are encouraged to be creative with your approach."
        )
        return prompt

    def use_predefined_query(self, professor_info: Dict) -> Dict:
        # Append predefined queries to the professor_info dictionary
        queries = [
            f"What are the key research areas and contributions of {professor_info['Employee']}, {professor_info['Position']} in the {professor_info['Department']} at {professor_info['Campus']}?",
            f"Identify and summarize the top 3 research interests of {professor_info['Employee']} at {professor_info['Campus']}, focusing on their impact and relevance in their field.",
            f"List and provide detailed summaries of the top 5 most cited papers by {professor_info['Employee']} from {professor_info['Campus']}, highlighting their significance in the academic community.",
        ]

        # Assuming there are no existing search queries in the professor_info
        for i, query in enumerate(queries, start=1):
            professor_info[f"Search_{i}"] = query

        return professor_info
