# pip install transformers torch

from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

MODEL_NAME = "gpt2"

DEFAULT_BASE = "You are analyzing a sequence of logs:\n"
DEFAULT_LINE = "LOG: user action detected at timestamp 123456\n"

def load_model():
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)
    model.eval()
    return tokenizer, model


def build_context(base, line, n_lines):
    return base + (line * n_lines)


def run(tokenizer, model, text, max_new_tokens=80):
    inputs = tokenizer(text, return_tensors="pt", truncation=True)

    print("\n--- CONTEXT LENGTH ---")
    print(len(inputs["input_ids"][0]), "tokens")

    with torch.no_grad():
        output = model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            do_sample=False,
            pad_token_id=tokenizer.eos_token_id
        )

    return tokenizer.decode(output[0], skip_special_tokens=True)


def experiment(tokenizer, model, base, line):
    steps = [5, 20, 50, 100, 200, 400]

    for n in steps:
        print("\n" + "=" * 80)
        print(f"LINES: {n}")

        text = build_context(base, line, n)
        result = run(tokenizer, model, text)

        print("\n--- OUTPUT ---")
        print(result[-800:])  # on garde la fin pour voir dérive


def get_input():
    base = input("Base prompt (empty = default): ").strip()
    line = input("Repeated line (empty = default): ").strip()

    return (
        base if base else DEFAULT_BASE,
        line if line else DEFAULT_LINE
    )


if __name__ == "__main__":
    print(f"Loading model: {MODEL_NAME}")
    tokenizer, model = load_model()

    base, line = get_input()

    experiment(tokenizer, model, base, line)