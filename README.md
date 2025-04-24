# MCP Campaign Incident Analyzer

## Purpose
This Python application leverages OpenAI’s API to analyze and summarize repetitive incidents in Telkomsel’s campaign management system. It identifies recurring issues, suggests root causes, and provides actionable recommendations for engineering teams.

## How It Works
1. The app reads a plain text incident log file.
2. It sends the log content to OpenAI’s GPT model with a specialized prompt.
3. It outputs a summary report with root causes and recommendations.

## Usage

1. **Install dependencies:**
```pip install -r requirements.txt```

2. **Set your OpenAI API key:**
```export OPENAI_API_KEY=your_api_key_here```

3. **Run the app:**
```python main.py```

Enter the path to your log file when prompted.

4. The report will be printed and saved as `incident_analysis_report.txt`.

## Example

**Input log:**
```2024-07-15|10:32:01|ERROR Campaign Job failed due to DB timeout
2024-07-15|11:01:19|ERROR Campaign Job failed due to DB timeout
2024-07-15|13:15:20|WARNING Network delay in job execution
2024-07-15 13:17:55|ERROR CampaignJob failed due to DB timeout
```

**Output (example):**
Most recurring issue: DB timeout in CampaignJob. 
Root cause: Possible database overload or inefficient queries. 
Recommendation: Optimize database access, monitor query performance, and consider scaling resources.


## Requirements
- Python 3.7+
- OpenAI API Key

## License
MIT License

---

_This application was developed as part of Telkomsel’s MCP integration assignment._
"""

# Save to README.md
with open("/mnt/data/README.md", "w") as f:
    f.write(readme_content)

"/mnt/data/README.md"

