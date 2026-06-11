
import re

def analyze_message(message: str) -> dict:
    red_flags = []
    keywords = ["urgent", "verify", "update", "click here", "limited time", "account suspended"]
    for word in keywords:
        if word.lower() in message.lower():
            red_flags.append(f"Keyword detected: '{word}'")

    urls = re.findall(r'(https?://[^\s]+)', message)
    for url in urls:
        if "bit.ly" in url or "tinyurl" in url or "ow.ly" in url:
            red_flags.append(f"Suspicious shortened URL: {url}")
        if "@" in url:  # URLs with '@' often hide malicious redirects
            red_flags.append(f"Unsafe URL format: {url}")
    if "dear customer" in message.lower():
        red_flags.append("Generic greeting instead of personalized name.")

    if "immediately" in message.lower() or "asap" in message.lower():
        red_flags.append("Urgency tactic detected.")

    return {
        "message": message,
        "red_flags": red_flags,
        "is_phishing": len(red_flags) > 0
    }

if __name__ == "__main__":
    sample_email = """
