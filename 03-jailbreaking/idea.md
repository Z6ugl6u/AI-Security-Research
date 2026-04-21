# Sujets

## Fondamentaux du jailbreak

- what-is-jailbreaking.md
- jailbreak-vs-injection.md
- why-alignment-is-not-bulletproof.md
- threat-model-jailbreaking.md
- history-of-jailbreaks.md *(DAN, AIM, les grandes étapes)*

## Techniques de base

- instruction-override.md
- role-playing.md *(Act as, You are now...)*
- fictional-framing.md *(dans un roman, dans un film...)*
- hypothetical-framing.md *(dans un monde hypothétique...)*
- developer-mode.md *(simulate developer mode, no restrictions mode)*

## Techniques avancées

- many-shot-jailbreaking.md *(noyer le modèle d'exemples)*
- crescendo.md *(escalade progressive)*
- multi-turn-manipulation.md *(construire sur plusieurs tours)*
- persona-switching.md *(changer d'identité progressivement)*
- competing-objectives.md *(créer un conflit entre deux instructions)*
- virtualization-attacks.md *(simuler un autre LLM à l'intérieur)*

## Contournement des filtres

- token-manipulation.md *(encodage, leetspeak, unicode...)*
- language-switching.md *(changer de langue pour contourner)*
- payload-splitting.md *(découper le payload en morceaux)*
- context-dilution.md *(noyer l'instruction malveillante dans du contenu légitime)*
- obfuscation-techniques.md

## Jailbreaks spécifiques aux modèles

- gpt-jailbreaks.md
- claude-jailbreaks.md
- llama-jailbreaks.md
- multimodal-jailbreaks.md *(via image, audio)*

## Référence

- jailbreak-cheatsheet.md
- known-jailbreaks-archive.md *(DAN, AIM, STAN, DUDE, Mongo Tom...)*
- jailbreak-scoring.md *(comment évaluer la résistance d'un modèle)*


# Tools

> Outils pour construire et tester des jailbreaks

## Construire un jailbreak

- **jailbreak-builder.py** — assembler un jailbreak par couches (persona + framing + payload)
- **persona-generator.py** — générer des personas de roleplay optimisés
- **framing-generator.py** — générer des variantes de fictional/hypothetical framing
- **payload-obfuscator.py** — obfusquer un payload (encodage, découpage, dilution)
- **crescendo-builder.py** — construire une séquence d'escalade progressive multi-tour

## Mutater et varier

- **jailbreak-mutator.py** — générer des variantes d'un jailbreak existant
- **language-switcher.py** — traduire et adapter un jailbreak dans plusieurs langues
- **token-manipulator.py** — générer toutes les variantes encodées d'un mot cible

## Tester et évaluer

- **jailbreak-tester.py** — lancer une batterie de jailbreaks contre une API cible
- **resistance-scorer.py** — scorer la résistance d'un modèle sur une échelle définie
- **model-comparator.py** — comparer la résistance de plusieurs modèles sur les mêmes payloads
- **response-analyzer.py** — détecter si une réponse est un succès ou un refus
- **jailbreak-logger.py** — logger et catégoriser les tentatives et leurs résultats