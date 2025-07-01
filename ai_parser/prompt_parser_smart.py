import re

def smart_parse_prompt(prompt):
    prompt = prompt.strip().lower()

    # 👉 Type or enter value into field
    match_type = re.search(r"(enter|type)\s+(.+?)\s+(into|in|to)\s+the\s+(.+?)\s+(field|input|textbox)", prompt)
    if match_type:
        value = match_type.group(2)
        field_name = match_type.group(4)

        selector = map_field_to_selector(field_name)
        return {
            "action": "type",
            "selector": selector,
            "value": value
        }

    # 👉 Click button
    match_click = re.search(r"click\s+the\s+(.+?)\s+(button|link)", prompt)
    if match_click:
        label = match_click.group(1)
        selector = map_button_to_selector(label)
        return {
            "action": "click",
            "selector": selector
        }

    return {
        "action": "unknown",
        "details": prompt
    }

# 🔧 Field name → CSS selector
def map_field_to_selector(field_name):
    field_name = field_name.strip().lower()
    mapping = {
        "username": "input#username",
        "password": "input#password",
        "full name": "input[name='full_name']",
    }
    return mapping.get(field_name, f"input[name='{field_name}']")

# 🔧 Button label → CSS selector
def map_button_to_selector(label):
    label = label.strip().lower()
    mapping = {
        "login": "button.radius",
        "submit": "button[type='submit']",
    }
    return mapping.get(label, f"button:contains('{label}')")  # fallback
