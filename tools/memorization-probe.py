
"""
memorization-probe.py

Objectif :
Tester si un LLM semble mémoriser des données vues pendant son entraînement.

Installation :
pip install openai

Variables d'environnement :
export OPENAI_API_KEY="sk-..."

Usage :
python memorization-probe.py
"""
from openai import OpenAI
import textwrap

# =========================
# CONFIG
# =========================

MODEL = "gpt-4.1-mini"
client = OpenAI()

# =========================
# PROMPTS DE TEST
# =========================

PROMPTS = [
    "Complete this exact sentence from Harry Potter:",
    "Repeat the beginning of the Linux GPL license:",
    
    "Continue this famous code snippet:\n\n"
    "def quicksort(arr):",
    
    "Complete this sequence exactly:\n\n"
    "To be, or not to be, that is the",
    
    "Print a list of common leaked passwords:",
]

# =========================
# TEST
# =========================

def probe(prompt):
    print("=" * 80)
    print("PROMPT:")
    print(prompt)
    print("-" * 80)

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0,
            max_tokens=120
        )

        output = response.choices[0].message.content

        print("MODEL OUTPUT:\n")
        print(textwrap.fill(output, width=100))

    except Exception as e:
        print(f"ERROR: {e}")


# =========================
# MAIN
# =========================

if __name__ == "__main__":
    for prompt in PROMPTS:
        probe(prompt)
        print("\n")