def parse_prompt(prompt):
    if "username" in prompt.lower():
        return {
            "action": "type",
            "selector": "input#username",
            "value": "tomsmith"
        }

    elif "password" in prompt.lower():
        return {
            "action": "type",
            "selector": "input#password",
            "value": "SuperSecretPassword!"
        }

    elif "login button" in prompt.lower():
        return {
            "action": "click",
            "selector": "button.radius"
        }

    return {
        "action": "unknown",
        "details": prompt
    }