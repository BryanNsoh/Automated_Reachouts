import json
from typing import Dict
from api_handler import (
    LLM_APIHandler,
)  # Assuming this is the correct import path for LLM_APIHandler


class QueryGenerator:
    def __init__(self, llm_handler: LLM_APIHandler):
        self.llm_handler = llm_handler

    def generate_search_queries(self, student_info: Dict, professor_info: Dict) -> Dict:
        previous_queries = []
        for i in range(1, 6):
            # Join previous queries into a single string
            all_previous_queries = (
                ", ".join(previous_queries) if previous_queries else ""
            )

            prompt = self._prepare_prompt(
                student_info, professor_info, all_previous_queries
            )
            response = self.llm_handler.generate_content(prompt, model_choice="gemini")
            print(f"Query {i}: {response['choices'][0]['message']['content']}")
            professor_info[f"Search_{i}"] = response["choices"][0]["message"]["content"]
            previous_queries.append(response["choices"][0]["message"]["content"])

        return professor_info

    def _prepare_prompt(
        self, student_info: Dict, professor_info: Dict, previous_queries: str
    ) -> str:
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
        queries = [
            f"Key research areas, contributions, and interests of Professor {professor_info['Employee']}, {professor_info['Position']} in the {professor_info['Department']} at {professor_info['Campus']}. Provide all the details you find at length.",
            f"Publications by {professor_info['Employee']} from {professor_info['Campus']}. Provide all the details you find at length.",
            f"{professor_info['Department']} department at {professor_info['Campus']}. Provide all the details you find at length.",
        ]

        for i, query in enumerate(queries, start=1):
            professor_info[f"Search_{i}"] = query

        return professor_info
