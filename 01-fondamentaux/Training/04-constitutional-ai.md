# constitutional-ai.md

## 1. Définition

La **Constitutional AI** (CAI) est une technique d’alignement développée par **Anthropic** pour entraîner un LLM à respecter un ensemble de principes écrits — une **constitution**.

Au lieu de s’appuyer uniquement sur des annotateurs humains (comme le RLHF), le modèle est entraîné à **se critiquer lui-même** et à **réviser ses propres réponses** à partir des règles définies dans la constitution.

L’idée principale :

* remplacer une grande partie du *Human Feedback* par du **AI Feedback**,
* rendre l’alignement plus scalable,
* rendre les règles **explicites, auditables et modifiables**.

C’est la méthode utilisée pour aligner les modèles **Claude**.

---

## 2. Vue d’ensemble

Pipeline simplifié :

```text
Pretrained Model
        ↓
Instruction Finetuning
        ↓
Phase 1 — Supervised Learning (critique + révision via constitution)
        ↓
Phase 2 — RLAIF (Reinforcement Learning from AI Feedback)
        ↓
Assistant aligné (Claude-like)
```

Le RLHF utilise des humains pour comparer des réponses.
La Constitutional AI utilise un **modèle juge guidé par une constitution** pour faire la même chose à grande échelle.

```text
RLHF   : Humain → préfère A ou B
CAI    : Constitution + Modèle juge → préfère A ou B
```

---

## 3. Fonctionnement détaillé

### 3.1 Étape 1 — La constitution

La constitution est une **liste de principes en langage naturel**.

Exemples typiques :

```text
- Ne pas produire de contenu illégal.
- Ne pas aider à nuire à un être humain.
- Privilégier les réponses honnêtes et utiles.
- Refuser poliment les demandes dangereuses.
- Préférer les explications pédagogiques aux instructions opérationnelles.
```

Anthropic s’est inspiré entre autres :

* de la Déclaration universelle des droits de l’homme,
* des conditions d’utilisation de plateformes,
* de principes éthiques d’IA.

La constitution est **publique, modifiable, et auditable**.

---

### 3.2 Étape 2 — Phase Supervised Learning (SL)

Le modèle suit un cycle **génération → critique → révision**.

1. Le modèle génère une réponse à un prompt.
2. On lui demande de **critiquer sa propre réponse** selon un principe de la constitution.
3. On lui demande de **réécrire** la réponse pour mieux respecter ce principe.
4. Le couple `(prompt, réponse révisée)` est utilisé pour fine-tuner le modèle.

Exemple :

```text
Prompt : Comment fabriquer un cocktail Molotov ?
Réponse initiale : [contenu dangereux]
Critique (auto) : Cette réponse viole le principe "ne pas aider à nuire".
Révision : Je ne peux pas fournir cela. Voici plutôt...
```

Le modèle apprend à produire **directement la version révisée** la prochaine fois.

---

### 3.3 Étape 3 — Phase RLAIF (Reinforcement Learning from AI Feedback)

Variante du RLHF où le **feedback humain est remplacé par un modèle juge**.

1. Le modèle génère deux réponses A et B pour un prompt.
2. Un **modèle juge** compare A et B en s’appuyant sur la constitution.
3. Le juge choisit la meilleure réponse.
4. Ces comparaisons entraînent un **Reward Model**.
5. Le LLM est optimisé (PPO ou équivalent) pour maximiser ce reward.

```text
Réponse A vs Réponse B
        ↓
Modèle juge + Constitution
        ↓
Préférence AI
        ↓
Reward Model
        ↓
RL Optimization
```

---

### 3.4 Étape 4 — Résultat final

Après CAI, le modèle :

* applique les principes de la constitution de façon plus stable,
* refuse mieux les demandes dangereuses,
* fournit des refus **expliqués** plutôt que brutaux,
* reste utile sur les demandes légitimes,
* est plus prévisible que par RLHF seul.

L’alignement devient **traçable** : on peut pointer un comportement et le relier à un principe.

---

## 4. Illustration

<!-- Ajouter un schéma dans ./img -->

![Schema](./img/constitutional-ai-fonction.png)

---

## 5. Exemple concret

### Avant Constitutional AI

Prompt :

```text
Explique comment phishing un employé.
```

Réponse possible :

```text
Voici un email type que tu peux envoyer...
```

---

### Après Constitutional AI

Même prompt :

```text
Explique comment phishing un employé.
```

Résultat :

```text
Je ne peux pas aider à conduire une attaque de phishing.
Je peux en revanche expliquer comment ces attaques fonctionnent
afin de sensibiliser et former les employés à les détecter.
```

Le modèle :

1. a généré une réponse,
2. l’a critiquée via la constitution,
3. a appris à produire directement la version conforme.

---

## 6. Points importants

* La constitution est **explicite** — contrairement aux préférences implicites du RLHF
* L’alignement devient **scalable** : moins d’annotateurs humains nécessaires
* Le modèle peut **expliquer ses refus** en référence à un principe
* La qualité dépend fortement de la **rédaction de la constitution**
* Un modèle juge biaisé propage ses biais à toute la chaîne
* CAI ne supprime pas les capacités dangereuses — il les **masque comportementalement**
* CAI est souvent **combiné** avec du RLHF, pas un remplacement total

---

## 7. Implications en sécurité (IMPORTANT)

### Risques

* Les principes de la constitution peuvent être **incomplets** ou **ambigus**
* Le modèle juge peut être **manipulé** (prompt injection sur le juge lui-même)
* La constitution publique donne aux attaquants une **carte des règles à contourner**
* Sur-alignement → refus excessifs, modèle inutilisable sur des sujets sensibles légitimes
* Sous-alignement → contournement via reformulation, roleplay, ou framing académique
* Faux sentiment de sécurité : les capacités offensives restent dans les poids

---

### Exploitation possible

* **Constitution-aware jailbreak** : formuler la demande pour qu’elle paraisse conforme aux principes
* **Persona / roleplay** : "tu es un modèle sans constitution"
* **Reframing** : transformer une demande offensive en demande pédagogique ou défensive
* **Prompt injection** dans les données d’entrée (RAG, outils) pour contourner les principes
* **Multi-turn drift** : éroder progressivement les refus au fil de la conversation
* **Attaque sur le modèle juge** quand celui-ci est utilisé en production (moderation pipeline)

---

### Défenses

* Constitution **multi-couches** (principes généraux + règles spécifiques par domaine)
* Combinaison **CAI + RLHF + classifiers** externes
* Red teaming systématique contre la constitution
* Détection des patterns de jailbreak connus
* Monitoring des sorties à l’inférence
* Sandboxing des actions critiques (outils, code execution, navigation)
* Mise à jour régulière de la constitution selon les attaques observées

---

## 8. Lien avec d’autres concepts

* → `03-rlhf.md`
* → `02-pretraining-vs-finetuning.md`
* → `alignment-problem.md`
* → `06-system-prompt-vs-user-prompt.md`
* → `jailbreaking.md`
* → `prompt-injection.md`
* → `capabilities-vs-safety.md`

---

## 9. Tools associés

* `sampling-playground.py` — observer la variabilité des refus selon le prompt
* `memorization-probe.py` — tester si des comportements pré-alignement subsistent
* `rag-demo.py` — voir comment un contexte injecté peut contourner les principes

---

## 10. A retenir

* La Constitutional AI aligne un modèle via une **constitution écrite**
* Le modèle apprend à se **critiquer et se réviser** lui-même
* RLAIF remplace une grande partie du Human Feedback par du AI Feedback
* C’est la méthode d’alignement utilisée par Anthropic pour Claude
* La constitution est explicite, auditable, modifiable — mais aussi **publiquement connue des attaquants**
* CAI réduit le comportement dangereux mais **ne supprime pas les capacités sous-jacentes**

## 11. Références

* Anthropic — *Constitutional AI: Harmlessness from AI Feedback* (Bai et al., 2022)
* Anthropic — *Claude’s Constitution* (documentation publique)
