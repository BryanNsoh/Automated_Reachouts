## Automated Reachouts: Streamlining Academic Communication with AI-powered Personalization and Factual Grounding

**Automated Reachouts** is a Python-based system that leverages the power of AI to facilitate and streamline communication between students and professors in academic settings. It goes beyond simply generating personalized emails by also conducting **web searches using the Perplexity API**. This ensures that each email is grounded in **factual and relevant information** about the professor and their research, significantly increasing the chances of a positive response. 

### Key Features:

* **AI-powered email crafting:** The system utilizes advanced language models like Google's Gemini and OpenAI's GPT-3.5 to generate personalized email drafts based on student information, professor research interests, and insightful narratives. 
* **Web search integration:** Leverages the Perplexity API to conduct targeted web searches, gathering relevant information about the professor and their research. This ensures that emails are well-informed and demonstrate genuine interest. 
* **Database integration:** Manages professor data efficiently using SQLite, allowing for seamless retrieval and updates. 
* **Automated email sending:** Integrates with Sendinblue's API to send crafted emails to professors at scheduled times. 
* **Customizable prompts and criteria:** Offers flexibility in tailoring prompts and evaluation criteria to specific needs and preferences. 

### Benefits:

* **Saves time and effort:** Automates the process of crafting and sending emails, freeing up students to focus on other academic tasks. 
* **Increases outreach effectiveness:** Generates personalized and compelling emails that are **grounded in factual information**, significantly increasing the likelihood of a positive response from professors. 
* **Improves communication quality:** Provides feedback and suggestions to refine email drafts, ensuring clarity, conciseness, and professionalism. 
* **Facilitates research opportunities:** Helps students connect with professors whose research aligns with their interests, potentially opening doors to valuable collaborations. 

### How Web Search Integration Works:

The `query_generator.py` and `search_executor.py` modules work together to:

1. **Generate search queries:** Based on the professor's information and research interests, the system generates targeted search queries aimed at gathering relevant and detailed information. 
2. **Execute queries and retrieve results:** These queries are then executed using the Perplexity API, and the retrieved results are incorporated into the email draft. 

This ensures that the email content is not only personalized but also demonstrates the student's genuine interest and understanding of the professor's work. 

### Installation and Usage:

1. **Clone the repository:** `git clone https://github.com/BryanNsoh/Automated_Reachouts.git`
2. **Install dependencies:** `pip install -r requirements.txt`
3. **Configure API keys:** Set your Google Generative AI, Perplexity AI, and Sendinblue API keys in the provided JSON file templates. 
4. **Run the main script:** `python main.py`

Contributions and feedback are welcome! 

### License:

This project is licensed under the MIT License. 
