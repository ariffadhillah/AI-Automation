import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from ai_parser.prompt_parser import parse_prompt

prompt = "Try entering an integer in the 'Full Name' field"
instruksi = parse_prompt(prompt)

print("🔍 Prompt:", prompt)
print("📦 Instruksi:", instruksi)
