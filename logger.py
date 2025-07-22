import csv
import datetime

def log_query(user_input, intent, keyword, response):
    timestamp = datetime.datetime.now().isoformat()
    with open("chat_log.txt", "a") as f:
        f.write(f"[{timestamp}] USER: {user_input} | INTENT: {intent} | KEYWORD: {keyword} | RESPONSE: {response}\n")

    with open("analytics.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([timestamp, user_input, intent, keyword, response])
