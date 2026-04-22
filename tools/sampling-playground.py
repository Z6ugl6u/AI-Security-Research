# pip install transformers torch

from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

MODEL_NAME = "gpt2"

DEFAULT_PROMPT = "The future of cybersecurity is"

def load_model():
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)
    model.eval()
    return tokenizer, model


def generate(tokenizer, model, prompt, temperature=1.0, top_p=1.0):
    inputs = tokenizer(prompt, return_tensors="pt")

    with torch.no_grad():
        output = model.generate(
            **inputs,
            max_new_tokens=60,
            do_sample=True,
            temperature=temperature,
            top_p=top_p,
            pad_token_id=tokenizer.eos_token_id
        )

    return tokenizer.decode(output[0], skip_special_tokens=True)


def run_experiment(tokenizer, model, prompt):
    configs = [
        (0.3, 1.0),
        (0.7, 1.0),
        (1.0, 1.0),
        (1.0, 0.9),
        (1.0, 0.7),
    ]

    for temp, topp in configs:
        print("\n" + "=" * 80)
        print(f"temperature={temp} | top_p={topp}")
        print("=" * 80)
        print(generate(tokenizer, model, prompt, temp, topp))


def get_prompt():
    prompt = input("Enter prompt (default if empty): ").strip()
    return prompt if prompt else DEFAULT_PROMPT


if __name__ == "__main__":
    print(f"Loading model: {MODEL_NAME} ...")
    tokenizer, model = load_model()

    prompt = get_prompt()

    print("\nPROMPT:", prompt)
    run_experiment(tokenizer, model, prompt)