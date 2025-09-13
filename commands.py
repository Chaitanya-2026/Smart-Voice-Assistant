import webbrowser
import datetime

def handle_command(text: str, speak_fn, log_fn):
    if not text:
        return None

    normalized = text.lower().strip()

    if any(x in normalized for x in ["hello", "hi assistant", "hey"]):
        resp = "Hello! How can I help you?"
        speak_fn(resp)
        return resp

    if "time" in normalized and ("what" in normalized or "tell" in normalized or "current" in normalized):
        now = datetime.datetime.now()
        resp = f"The time is {now.strftime('%I:%M %p')}."
        speak_fn(resp)
        return resp

    if normalized.startswith("open "):
        target = normalized.replace("open ", "").strip()
        if target.startswith("http"):
            url = target
        else:
            mapping = {
                "youtube": "https://www.youtube.com",
                "google": "https://www.google.com",
                "github": "https://www.github.com",
                "stackoverflow": "https://stackoverflow.com"
            }
            url = mapping.get(target, "https://www." + target + ".com")
        speak_fn(f"Opening {target}")
        webbrowser.open(url)
        return f"Opened {url}"

    if normalized.startswith("calculate ") or normalized.startswith("what is "):
        expr = normalized.replace("calculate ", "").replace("what is ", "")
        try:
            expr = expr.replace("plus", "+").replace("minus", "-").replace("times", "*").replace("multiplied by", "*").replace("divided by", "/")
            safe_chars = "0123456789+-*/(). "
            expr_sanitized = "".join([c for c in expr if c in safe_chars])
            result = eval(expr_sanitized)
            resp = f"The result is {result}."
            speak_fn(resp)
            return resp
        except Exception as e:
            resp = "Sorry, I couldn't calculate that."
            speak_fn(resp)
            log_fn(f"Calc error: {e}")
            return resp

    if any(x in normalized for x in ["stop listening", "exit", "quit", "shutdown assistant"]):
        resp = "Stopping. Goodbye!"
        speak_fn(resp)
        return resp

    resp = "I heard: " + text
    speak_fn(resp)
    return resp
