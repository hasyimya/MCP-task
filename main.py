import os
import openai

# Load your OpenAI API key from environment variable
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise Exception("Please set your OPENAI_API_KEY as an environment variable.")

openai.api_key = "sk-proj- 17lh7nc1dbSmml1y6URAni4GliF7qzU8ECpC9erfFtmiqqTjKsnYc5TW__A8dpGXb4Jvy9hHg3T3BlbkFJvTIblH86Mi55z_iTaoEstTyCPJksSfgqRWpMR1QWUDuMEVBY2b4_kcL70WhccjeOpHj4FrGhEA"

#Read log file function
def read_incident_logs(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

# Analyze logs using OpenAI
def analyze_logs(log_text):
    prompt = (
        "You are an AI assistant analyzing campaign system incident logs. "
        "Identify the most common recurring issues, categorize them, and suggest possible root causes. "
        "Then, generate a summary report with recommendations for the engineering team.\n\n"
        f"Incident Logs:\n{log_text}\n\n"
        "Summary Report:"
    )

    # Constructs a natural language prompt for the AI
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=400,
        temperature=0.2,
        n=1
    )
    return response.choices[0].text.strip()

def main():
    log_file = input("Enter path to incident log file (e.g., incident_log.txt): ").strip()
    if not os.path.exists(log_file):
        print("Log file not found.")
        return

    # Prompts the user to enter the path to a log file, checks whether the file exists. If not, it prints an error and exits
    logs = read_incident_logs(log_file)
    print("\nAnalyzing incident logs, please wait...\n")
    report = analyze_logs(logs)
    print("\n=== Summary Report ===\n")
    print(report)

    # Prints the RCA report directly in the terminal or notebook output
    output_file = "incident_analysis_report.txt"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(report)
    print(f"\nReport saved to: {output_file}")

if __name__ == "__main__":
    main()
