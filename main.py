import json
from professor_data_handler import ProfessorDataHandler, DatabaseSetupManager
from query_generator import QueryGenerator
from search_executor import SearchExecutor
from email_crafter import EmailCrafter
from email_sender import BrevoEmailSender
from prompts import student_info
import google.generativeai as genai


def main():
    """
    Main function orchestrating the overall process from generating search queries to crafting emails.

    Process:
        1. Reads professor data from the database.
        2. For each professor record, generates search queries based on student interests.
        3. Executes these queries and retrieves results.
        4. Crafts an email based on search results and student preferences, and stores it in the professor record under 'Email'.
        5. Sends the email to the professor.
        6. Updates the database with the modified professor record.
    """

    # Read API keys
    key_path = r"C:\Users\bnsoh2\OneDrive - University of Nebraska-Lincoln\Documents\keys\api_keys.json"
    with open(key_path) as f:
        api_keys = json.load(f)
        GEMINI_API_KEY = api_keys["GEMINI_API_KEY"]
        PERPLEXITY_API_KEY = api_keys["PERPLEXITY_API_KEY"]
        BREVO_API_KEY = api_keys["BREVO_API_KEY"]

    # Initialize the Google Gemini Pro model
    genai.configure(api_key=GEMINI_API_KEY)
    gemini_model = genai.GenerativeModel("gemini-pro")

    # Initialize the DatabaseSetupManager and set up the database path
    db_manager = DatabaseSetupManager("professors_db_template.db")
    db_path = db_manager.select_or_create_database_folder()

    # Initialize ProfessorDataHandler with the new database path
    table_name = "professors"
    data_handler = ProfessorDataHandler(str(db_path), table_name)

    # Initialize other classes
    query_gen = QueryGenerator(gemini_model)
    search_exec = SearchExecutor(PERPLEXITY_API_KEY)
    email_crafter = EmailCrafter(gemini_model)
    email_sender = BrevoEmailSender(BREVO_API_KEY)

    # Process each professor record
    professor_records = data_handler.read_professor_data()
    professor_records = [x for x in professor_records if x.get("Sent", 0) == 0]

    for record in professor_records:
        # Get and execute search queries
        updated_record = query_gen.use_predefined_query(record)
        print("Queries generated for", updated_record["Employee"])
        updated_record = search_exec.perform_search(updated_record)
        print("Queries executed for", updated_record["Employee"])

        # Craft email
        email_data = email_crafter.craft_email(student_info, updated_record)
        email_body = email_data["body"]
        subject_line = email_data["subject"]

        email_to_send = {
            "Contact": updated_record["Contact"],
            "Email_To_Send": email_body,
            "Subject": subject_line,
            "Sent": 0,
        }

        email_sender.send_email([email_to_send])  # Send the email with the subject line

        # Update database
        full_email_content = f"Subject: {subject_line}\n\n{email_body}"
        updated_record["Email_To_Send"] = full_email_content
        data_handler.update_database(updated_record)


if __name__ == "__main__":
    main()
