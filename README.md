
# Automated Reachouts

## Description
Automated Reachouts is a comprehensive system designed to automate academic outreach and communication. It uses AI to generate personalized emails, catering to students seeking academic guidance or opportunities from professors. The system handles end-to-end email crafting and sending processes, including database interactions and content customization.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Components](#components)
- [Contributing](#contributing)
- [License](#license)

## Installation

### Prerequisites
- Python 3.8 or higher
- SQLite for database management
- Google Generative AI and Perplexity AI API keys
- Sendinblue API key for email transmission

### Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Automated-Reachouts.git
   cd Automated-Reachouts
   ```
2. Install required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure API keys in the provided JSON file templates.

## Usage

### Steps to Run
1. Ensure all API keys are set in `api_keys.json`.
2. Run `main.py` to initiate the process:
   ```bash
   python main.py
   ```
3. The system will automatically process data, craft emails, and send them.

### Components
- **Email Crafting**: Creates personalized emails using AI.
- **Data Handling**: Manages professor data and performs database interactions.
- **Email Transmission**: Sends out crafted emails to professors.

## Components

- `email_crafter.py`: Generates and refines email drafts.
- `email_sender.py`: Sends emails using markdown content.
- `main.py`: Main script orchestrating the entire process.
- `professor_data_handler.py`: Handles professor data stored in SQLite.
- `prompts.py`: Contains email templates and advice.
- `query_generator.py` and `search_executor.py`: Manage search queries.

## Contributing
Contributions and feedback are welcome! 
