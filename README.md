## Automated Reachouts: Streamlining Academic Communication with AI

**Automated Reachouts** is a Python-based system that leverages the power of AI to facilitate and streamline communication between students and professors in academic settings. It assists students in crafting personalized and effective emails to professors, seeking guidance, research opportunities, or potential collaborations. 

### Key Features:

* **AI-powered email crafting:** The system utilizes advanced language models like Google's Gemini and OpenAI's GPT-3.5 to generate personalized email drafts based on student information, professor research interests, and insightful narratives. 
* **Database integration:** Manages professor data efficiently using SQLite, allowing for seamless retrieval and updates. 
* **Automated email sending:** Integrates with Sendinblue's API to send crafted emails to professors at scheduled times. 
* **Customizable prompts and criteria:** Offers flexibility in tailoring prompts and evaluation criteria to specific needs and preferences. 

### Benefits:

* **Saves time and effort:** Automates the process of crafting and sending emails, freeing up students to focus on other academic tasks. 
* **Increases outreach effectiveness:** Generates personalized and compelling emails that are more likely to receive positive responses from professors. 
* **Improves communication quality:** Provides feedback and suggestions to refine email drafts, ensuring clarity, conciseness, and professionalism. 
* **Facilitates research opportunities:** Helps students connect with professors whose research aligns with their interests, potentially opening doors to valuable collaborations. 

### Repository Contents:

* **email_crafter.py:** Generates and refines email drafts using AI.
* **email_sender.py:** Sends emails with markdown content using Sendinblue's API.
* **main.py:** The main script that orchestrates the entire process.
* **professor_data_handler.py:** Manages professor data stored in SQLite.
* **prompts.py:** Contains email templates, advice, and prompts for AI models.
* **query_generator.py and search_executor.py:** Generate and execute search queries to gather information about professors' research interests. 

### Installation and Usage:

1. **Clone the repository:** `git clone https://github.com/BryanNsoh/Automated_Reachouts.git`
2. **Install dependencies:** `pip install -r requirements.txt`
3. **Configure API keys:** Set your Google Generative AI, Perplexity AI, and Sendinblue API keys in the provided JSON file templates. 
4. **Run the main script:** `python main.py`

Contributions and feedback are welcome! 

### License:

This project is licensed under the MIT License. 
