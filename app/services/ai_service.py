import time

def generate_summary(task_description: str):
    retries = 0
    while retries < 2:
        try:
            return f"Structured Summary:\n{task_description}\n\nStatus: Processed"
        except Exception:
            retries += 1
            time.sleep(1)
    return "AI service temporarily unavailable."
