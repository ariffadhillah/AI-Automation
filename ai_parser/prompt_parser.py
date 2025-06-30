import re

def parse_prompt(prompt):
    """
    Parse prompt to structured instruction.
    Only works for specific known formats for now.
    """

    if "entering an integer" in prompt and "Full Name" in prompt:
        return {
            "action": "type",
            "selector": "input#username",
            "value": "123"
        }

    elif "Password" in prompt and "integer" in prompt:
        return {
            "action": "type",
            "selector": "input#password",
            "value": "123456"
        }

    elif "click" in prompt and "login button" in prompt:
        return {
            "action": "click",
            "selector": "button.radius"
        }

    else:
        return {
            "action": "unknown",
            "details": prompt
        }
