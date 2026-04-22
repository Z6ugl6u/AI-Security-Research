# pip install transformers matplotlib

import matplotlib.pyplot as plt
from transformers import AutoTokenizer

list_tokenizers = [
    "bert-base-uncased",
    "gpt2",
    "roberta-base",
    "distilbert-base-uncased",
    "albert-base-v2"
]

DEFAULT_TEXT = "Hello, how are you doing today?"

def visualize_tokenizer(tokenizer_name, text):
    tokenizer = AutoTokenizer.from_pretrained(tokenizer_name)

    tokens = tokenizer.tokenize(text)
    token_ids = tokenizer.convert_tokens_to_ids(tokens)

    plt.figure(figsize=(10, 5))
    plt.bar(range(len(tokens)), token_ids)

    plt.xticks(range(len(tokens)), tokens, rotation=45, ha='right')
    plt.xlabel("Tokens")
    plt.ylabel("Token IDs")
    plt.title(f"{tokenizer_name}\n{text}")

    plt.tight_layout()
    plt.show()


def choose_tokenizer():
    print("\nAvailable tokenizers:")
    for i, name in enumerate(list_tokenizers):
        print(f"{i} → {name}")

    choice = input("\nChoose tokenizer index (default 0): ").strip()

    if choice == "":
        return list_tokenizers[0]

    try:
        idx = int(choice)
        return list_tokenizers[idx]
    except (ValueError, IndexError):
        print("Invalid choice → fallback to default (0)")
        return list_tokenizers[0]


def get_text():
    text = input("\nEnter text (default if empty): ").strip()
    return text if text else DEFAULT_TEXT


if __name__ == "__main__":
    tokenizer_name = choose_tokenizer()
    text = get_text()

    print(f"\nUsing tokenizer: {tokenizer_name}")
    print(f"Text: {text}\n")

    visualize_tokenizer(tokenizer_name, text)