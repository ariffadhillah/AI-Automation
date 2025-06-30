import re

def parse_prompt(prompt):
    """
    Parse prompt to structured instruction.
    Only works for specific known formats for now.
    """

    if "entering an integer" in prompt and "Full Name" in prompt:
        return {
            "action": "type",
            "selector": "input[name='full_name']",
            "value": "123"
        }
    elif "click login" in prompt:
        return {
            "action": "click",
            "selector": "button[type='submit']"
        }

    return {
        "action": "unknown",
        "details": prompt
    }
