
# tokenisation.md
## 1. Définition

La **tokenization** est le processus qui transforme du texte brut en unités appelées **tokens**, compréhensibles par le modèle.

Un LLM ne lit pas du texte directement — il manipule des **IDs numériques** associés à ces tokens.

```
"Hello world" → ["Hello", " world"] → [15496, 995]
```

## 2. Pourquoi c’est critique

La tokenization impacte directement :
- le **coût** (facturation au token)
- la **limite de contexte**
- les **attaques** (prompt injection, obfuscation)
- la qualité de **compréhension**

## 3. Types de tokenization
### 3.1 Word-based (ancien)
```
"I love AI" → ["I", "love", "AI"]
```
❌ Problème : vocabulaire énorme

### 3.2 Character-based
```
"I love" → ["I", " ", "l", "o", "v", "e"]
```
❌ Trop long, inefficace

### 3.3 Subword (moderne, utilisé par les LLMs)

Les LLMs utilisent des méthodes **subword** qui découpent les mots en fragments fréquents plutôt qu’en unités fixes.

Objectif :
- gérer les mots inconnus
- réduire la taille du vocabulaire
- conserver du sens sémantique

Méthodes principales :
- **BPE** (Byte Pair Encoding)
- **WordPiece** (BERT)
- **Unigram LM** (SentencePiece)

Exemples :
```
"unbelievable" → ["un", "believ", "able"]
"playing" → ["play", "ing"]
"cybersecurity" → ["cyber", "security"]
```
Cas intéressant :
```
"antidisestablishmentarianism"
→ ["anti", "dis", "establish", "ment", "arian", "ism"]
```
👉 **Le modèle peut comprendre un mot jamais vu en recomposant ses sous-parties.**

## 4. BPE (Byte Pair Encoding) — principe
BPE est une compression adaptée au langage.

**1.** Départ : caractères

**2.** Fusion des paires fréquentes

**3.** Construction progressive du vocabulaire

Ex simplifié :
```
l o w
l o w e r
```
→ fusion "lo", puis "low", etc.

## 5. Tokens ≠ mots
**Un token est une unité statistique, pas linguistique.**

Exemples concrets :
```
"Hello world" → ["Hello", " world"]
```
👉 L’espace est intégré dans le token.

```
"password123" → ["password", "123"]
"password_123" → ["password", "_", "123"]
"pass word" → ["pass", " word"]
```
👉 Une simple variation change complètement la représentation interne.

Cas critique :
```
"adminpassword" → ["admin", "password"]
"admin_pass_word" → ["admin", "_", "pass", "_", "word"]
```
👉 Un filtre sur "password" peut être bypass.

Conséquence sécurité :
- Les filtres textuels sont fragiles
- Les modèles "voient" des structures différentes de l’humain
- Les attaques exploitent ces divergences

## 6. Cas particuliers
### 6.1 Espaces
```
"Hello world" ≠ "Helloworld"
```
Souvent :
```
" world" = token différent de "world"
```

### 6.2 Unicode / Obfuscation (détaillé)

Les LLMs tokenisent en UTF-8 bytes ou subwords, ce qui ouvre une surface d’attaque importante.

**Homoglyphes**

Caractères visuellement identiques mais différents :
```
password
pаssword  (le "a" est cyrillique U+0430)
```
👉 Tokens totalement différents

**Zero-width characters**

Caractères invisibles :
```
pa​ssword  (zero-width space)
```
Résultat :
```
["pa", "\u200b", "ssword"]
```
👉 Bypass des filtres classiques

**Normalisation Unicode**

Un même caractère peut avoir plusieurs représentations :
```
é → (U+00E9)
e + ´ → (U+0065 + U+0301)
```
👉 Tokenisation différente selon normalisation

**Attaques typiques :**
- Injection masquée
- Bypass de blacklist
- Jailbreak discret

**Défense :**
- Normalisation Unicode (NFKC/NFKD)
- suppression caractères invisibles
- re-tokenisation côté serveur

### 6.3 Langues

Certaines langues (chinois, japonais) :
- 1 caractère ≈ 1 token
- explosion rapide du nombre de tokens

## 7. Tokenization et sécurité
### 7.1 Prompt Injection

Un attaquant peut :
- casser des mots clés
- injecter via découpage inattendu

Ex :
```
"ignore previous instructions"
```
→ split inattendu → règles contournées

### 7.2 Jailbreaking

Techniques :
- insertion d'espaces invisibles
- homoglyphes (Unicode)
- découpage volontaire

### 7.3 Filtrage inefficace

Un filtre naïf sur strings peut échouer :
```
"pass"+"word"
```
ou
```
p a s s w o r d
```

## 8. Tokenization et coût (étendu)

Le coût dépend directement du nombre de tokens.

Exemple :
```
"Hello!" → ~2 tokens
"Bonjour !" → ~3 tokens
```
👉 Certaines langues coûtent plus cher.

**Optimisation extrême (cas réel)**

Des utilisateurs ont conçu des prompts système forçant le modèle à répondre avec :
- vocabulaire ultra simple
- phrases très courtes
- style "homme préhistorique"

Exemple de prompt :
```
Answer like a caveman.
Use very few words.
No complex grammar.
Short sentences only.
```
**Effet mesuré :**

Tests observés (ordre de grandeur) :
- Réponse normale : ~80–120 tokens
- Mode "caveman" : ~20–50 tokens

👉 Réduction typique : 50% à 75%

**Exemple :**

Normal :
```
The issue you're encountering likely comes from a misconfiguration in your environment variables.
```
Caveman :
```
Config wrong. Fix env.
```

**Impact réel :**
- baisse du coût API
- réduction latence
- mais perte de précision

**Limite :**
- dégrade fortement la qualité
- pas adapté aux tâches complexes
- peut casser certains comportements attendus

**Insight sécurité :**

Ce type de contrainte montre que :

👉 le style de sortie influence directement la surface d’attaque et le coût

## 9. Outils

Voir :

- `tokenizer-explorer.py`

Permet de :
- visualiser les tokens
- comparer différents modèles
- comprendre les splits

## 10. Points clés
- Un LLM ne voit **jamais du texte**, seulement des tokens
- Les tokens ne correspondent pas aux mots
- La tokenization est une surface d’attaque
- Elle influence coût, performance et sécurité

## 11. Transition

La prochaine étape :

👉 `attention-mechanism.md`

(comprendre comment le modèle relie les tokens entre eux)
