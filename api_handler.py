import openai
import google.generativeai as genai
from retry import retry
import json
import logging

# Logger setup
logging.basicConfig(level=logging.INFO)


class LLM_APIHandler:
    def __init__(self, key_path):
        self.load_api_keys(key_path)
        openai.api_key = self.openai_api_key
        genai.configure(api_key=self.gemini_api_key)

    def load_api_keys(self, key_path):
        with open(key_path, "r") as file:
            api_keys = json.load(file)
            self.gemini_api_key = api_keys["GEMINI_API_KEY"]
            self.openai_api_key = api_keys["OPENAI_API_KEY"]

    @retry(tries=5, delay=1, backoff=2)
    def generate_openai_content(self, prompt, model="gpt-3.5"):
        try:
            response = openai.ChatCompletion.create(
                model=model,
                messages=[
                    {
                        "role": "system",
                        "content": "Address the provided query fully and directly. Obeying all instuctions.",
                    },
                    {"role": "user", "content": prompt},
                ],
            )
            return response
        except Exception as e:
            logging.error(f"Error in OpenAI API call: {e}")
            raise

    @retry(tries=5, delay=1, backoff=2)
    def generate_gemini_content(self, prompt):
        try:
            model = genai.GenerativeModel("gemini-pro")
            return model.generate_content(prompt)
        except Exception as e:
            logging.error(f"Error in Gemini API call: {e}")
            raise

    def generate_content(self, prompt, model_choice="gemini"):
        if model_choice == "openai":
            return self.generate_openai_content(prompt)
        elif model_choice == "gemini":
            return self.generate_gemini_content(prompt)
        else:
            raise ValueError("Invalid model choice. Choose 'openai' or 'gemini'.")


# Example usage
if __name__ == "__main__":
    key_path = r"C:\Users\bnsoh2\OneDrive - University of Nebraska-Lincoln\Documents\keys\api_keys.json"  # Replace with your key file path
    handler = LLM_APIHandler(key_path)

    # Example prompt
    prompt = "Write a short story about a wizard."
    model_choice = "gemini"  # Can be 'openai' or 'gemini'
    try:
        response = handler.generate_content(prompt, model_choice)
        print(response)
    except Exception as e:
        logging.error(f"Failed to generate content: {e}")
