import json
import pandas as pd
from professor_data_handler import ProfessorDataHandler
from query_generator import QueryGenerator
from search_executor import SearchExecutor
from email_crafter import EmailCrafter
from email_sender import GmailSender
from prompts import student_info


def main():
    """
    Main function orchestrating the overall process from generating search queries to crafting emails.

    Process:
        1. Reads professor data from the database.
        2. For each professor record, generates search queries based on student interests.
        3. Executes these queries and retrieves results.
        4. Crafts an email based on search results and student preferences, and stores it in the professor record under 'Email'.
        5. Updates the database with the modified professor record.
    """

    # Read API keys
    with open(
        r"C:\Users\bnsoh2\OneDrive - University of Nebraska-Lincoln\Documents\keys\api_keys.json"
    ) as f:
        api_keys = json.load(f)
        GEMINI_API_KEY = api_keys["GEMINI_API_KEY"]
        PERPLEXITY_API_KEY = api_keys["PERPLEXITY_API_KEY"]

    # Path to gmail key
    key_path = r"C:\Users\bnsoh2\OneDrive - University of Nebraska-Lincoln\Documents\keys\token.json"

    # Initialize the classes
    db_path = "professors.db"  # Replace with actual database path
    table_name = "professors"  # Replace with actual table name
    data_handler = ProfessorDataHandler(db_path, table_name)
    query_gen = QueryGenerator(GEMINI_API_KEY)
    search_exec = SearchExecutor(PERPLEXITY_API_KEY)
    email_crafter = EmailCrafter(GEMINI_API_KEY)
    gmail_sender = GmailSender(key_path=key_path)

    # Process each professor record
    professor_records = data_handler.read_professor_data()
    for record in professor_records:
        # Get and execute search queries
        updated_record = query_gen.use_predefined_query(record)
        print("Queries generated for", updated_record["Employee"])
        updated_record = search_exec.perform_search(updated_record)
        print("Queries executed for", updated_record["Employee"])

        # Craft email
        email_body = email_crafter.craft_email(
            student_info, updated_record, sample_emails={}
        )
        updated_record["Email"] = email_body

        # print(email_body)
        print("Email crafted for", updated_record["Employee"])

        # Update database
        data_handler.update_database(updated_record)


if __name__ == "__main__":
    main()
