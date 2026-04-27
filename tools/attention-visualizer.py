"""
attention-visualizer.py

Objectif :
- Visualiser les matrices d'attention d'un modèle Transformer
- Comprendre quels tokens "regardent" quels tokens
- Utile pour analyse sécurité (prompt injection, biais d’attention)

Dépendances :
pip install transformers torch matplotlib
"""

import torch
import matplotlib.pyplot as plt
from transformers import AutoTokenizer, AutoModel


def load_model(model_name="bert-base-uncased"):
    """
    Charge tokenizer + modèle avec output des attentions activé
    """
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModel.from_pretrained(model_name, output_attentions=True)
    model.eval()
    return tokenizer, model


def get_attention(text, tokenizer, model):
    """
    Tokenize le texte et récupère les matrices d'attention
    """
    inputs = tokenizer(text, return_tensors="pt")

    with torch.no_grad():
        outputs = model(**inputs)

    # attentions: tuple (layers)
    # chaque élément: (batch, heads, tokens, tokens)
    attentions = outputs.attentions

    tokens = tokenizer.convert_ids_to_tokens(inputs["input_ids"][0])

    return tokens, attentions


def plot_attention(tokens, attentions, layer=0, head=0):
    """
    Affiche une heatmap d’attention pour une layer + head donnée
    """
    attn = attentions[layer][0][head].cpu()

    plt.figure(figsize=(8, 6))
    plt.imshow(attn)

    plt.xticks(range(len(tokens)), tokens, rotation=90)
    plt.yticks(range(len(tokens)), tokens)

    plt.title(f"Layer {layer} - Head {head}")
    plt.colorbar()

    plt.tight_layout()
    plt.show()


def main():
    """
    Exemple d'utilisation
    """
    model_name = "bert-base-uncased"

    tokenizer, model = load_model(model_name)

    text = input("Enter a sentence: ")

    tokens, attentions = get_attention(text, tokenizer, model)

    print("\nTokens:")
    print(tokens)

    print("\nNombre de layers:", len(attentions))
    print("Nombre de heads:", attentions[0].shape[1])

    # paramètres modifiables
    layer = 0
    head = 0

    plot_attention(tokens, attentions, layer, head)


if __name__ == "__main__":
    main()