MCP Campaign Incident Analyzer
Purpose
This Python application leverages OpenAI’s API to analyze and summarize repetitive incidents in Telkomsel’s campaign management system. It identifies recurring issues, suggests root causes, and provides actionable recommendations for engineering teams.

How It Works
The app reads a plain text incident log file.

It sends the log content to OpenAI’s GPT model with a specialized prompt.

It outputs a summary report with root causes and recommendations.

Usage
Install dependencies:

nginx
Copy
pip install -r requirements.txt
Set your OpenAI API key:

arduino
Copy
export OPENAI_API_KEY=your_api_key_here
Run the app:

css
Copy
python main.py
Enter the path to your log file when prompted.

The report will be printed and saved as incident_analysis_report.txt.

Example
Input log:

vbnet
Copy
2024-07-15 10:32:01 ERROR CampaignJob failed due to DB timeout
2024-07-15 11:01:19 ERROR CampaignJob failed due to DB timeout
2024-07-15 13:15:20 WARNING Network delay in job execution
2024-07-15 13:17:55 ERROR CampaignJob failed due to DB timeout
Output (example):

pgsql
Copy
Most recurring issue: DB timeout in CampaignJob. Root cause: Possible database overload or inefficient queries. Recommendation: Optimize database access, monitor query performance, and consider scaling resources.
Requirements
Python 3.7+

OpenAI API Key

License
MIT License
