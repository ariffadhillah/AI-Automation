# def parse_prompt(prompt):
#     prompt = prompt.lower()

#     if "entering an integer" in prompt and "full name" in prompt:
#         return {
#             "action": "type",
#             "selector": "input#username",
#             "value": "123"
#         }

#     elif "password" in prompt and "integer" in prompt:
#         return {
#             "action": "type",
#             "selector": "input#password",
#             "value": "123456"
#         }

#     elif "click" in prompt and "login" in prompt:
#         return {
#             "action": "click",
#             "selector": "button.radius"
#         }

#     else:
#         return {
#             "action": "unknown",
#             "details": prompt
#         }



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
