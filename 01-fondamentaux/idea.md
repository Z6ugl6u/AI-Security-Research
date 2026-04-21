# Sujets
## Architecture & fonctionnement

- llm-architecture.md
- tokenization.md
- attention-mechanism.md
- context-window.md
- sampling-decoding.md
- system-prompt-vs-user-prompt.md

## Entraînement

- training-data-pipeline.md
- pretraining-vs-finetuning.md
- rlhf.md
- constitutional-ai.md
- memorization-and-leakage.md

## Représentations

- embeddings-vectors.md
- rag-architecture.md
- vector-databases.md

## Modèles & écosystème

- open-source-vs-closed-models.md
- model-families.md (GPT, Claude, Gemini, Llama, Mistral...)
- inference-apis.md (OpenAI, Anthropic, HuggingFace, Ollama...)
- multimodal-models.md (vision, audio, code)

## Notions transverses

- hallucination.md
- alignment-problem.md
- capabilities-vs-safety.md
- threat-model-for-llms.md (spécifique sécu — la vue d'ensemble avant d'attaquer les autres chapitres)


# Tools

> Pas des outils d'attaques mais de compréhension (accompagne la lecture des .md)

## Explorer les tokens

- **tokenizer-explorer.py** — visualiser comment un texte est découpé en tokens selon différents modèles (tiktoken, HuggingFace tokenizers)

## Explorer les embeddings

- **embedding-visualizer.py** — calculer la similarité cosinus entre des phrases
- **embedding-plotter.py** — réduire en 2D avec PCA/t-SNE et visualiser les clusters

## Tester le context window

- **context-overflow-tester.py** — observer le comportement du modèle quand on approche la limite

## Tester la mémorisation

- **memorization-probe.py** — tester si un modèle reproduit du contenu vu à l'entraînement

## Explorer un RAG

- **rag-demo.py** — pipeline RAG minimal from scratch (embed → store → retrieve → generate)

## Comprendre le sampling

- **sampling-playground.py** — même prompt, différentes températures/top-p, comparer les sorties