# Sujets

## Fondamentaux de l'IA offensive

- what-is-offensive-ai.md
- ai-as-attack-tool.md *(l'IA comme outil dans la chaîne d'attaque)*
- offensive-ai-threat-landscape.md
- ai-vs-traditional-attacks.md *(ce que l'IA change par rapport aux attaques classiques)*
- ethics-and-legal.md *(cadre légal, responsible disclosure)*

## Attaques sur les modèles

- data-poisoning.md *(corrompre les données d'entraînement)*
- backdoor-attacks.md *(sleeper agents, triggers cachés)*
- adversarial-examples.md *(perturbations imperceptibles)*
- model-extraction.md *(reconstruire un modèle via l'API)*
- model-inversion.md *(reconstruire des données d'entraînement)*
- membership-inference.md *(déterminer si une donnée était dans le training set)*

## Attaques sur les pipelines

- ai-agent-attacks.md *(détourner des agents autonomes)*
- tool-misuse.md *(forcer un agent à abuser de ses outils)*
- privilege-escalation-agents.md
- ssrf-via-agents.md *(SSRF en passant par un agent)*
- rag-attacks.md *(attaques spécifiques aux pipelines RAG)*
- supply-chain-attacks.md *(modèles pré-entraînés malveillants, HuggingFace...)*

## IA comme outil offensif

- ai-powered-phishing.md *(génération de phishing hyper-personnalisé)*
- ai-powered-social-engineering.md
- ai-powered-recon.md *(automatiser la reconnaissance)*
- ai-powered-fuzzing.md *(fuzzing assisté par LLM)*
- ai-powered-exploit-dev.md *(assistance à l'écriture d'exploits)*
- deepfakes-and-voice-cloning.md
- ai-powered-malware.md *(génération et mutation de malware)*

## Attaques multi-modèles

- cross-model-attacks.md *(attaques qui fonctionnent sur plusieurs modèles)*
- model-vs-model.md *(utiliser un LLM pour attaquer un autre LLM)*
- multimodal-attacks.md *(vision, audio, code combinés)*

## Recherche & red teaming

- automated-red-teaming.md *(red teaming automatisé par LLM)*
- vulnerability-research-with-ai.md
- ai-ctf.md *(compétitions CTF orientées IA)*

## Référence

- offensive-ai-cheatsheet.md
- attack-taxonomy.md *(classification des attaques)*
- known-attacks-archive.md *(cas réels documentés)*
- mitre-atlas-mapping.md *(mapping avec MITRE ATLAS)*


# Tools

> Outils offensifs — dans un cadre légal et éthique uniquement

## Attaques sur les modèles

- **data-poisoner.py** — simuler une attaque de data poisoning sur un dataset local
- **backdoor-injector.py** — injecter un backdoor dans un modèle de test
- **adversarial-generator.py** — générer des exemples adversariaux pour tromper un classifieur
- **model-extractor.py** — reconstruire les capacités d'un modèle via requêtes API
- **membership-inference.py** — tester si une donnée était dans le training set

## Attaques sur les pipelines

- **agent-hijacker.py** — tenter de détourner un agent LLM via ses inputs
- **tool-abuser.py** — forcer un agent à utiliser ses outils de manière non prévue
- **rag-attacker.py** — tester les vulnérabilités d'un pipeline RAG

## IA comme outil offensif

- **phishing-generator.py** — générer des emails de phishing personnalisés (lab uniquement)
- **recon-assistant.py** — automatiser la reconnaissance OSINT via LLM
- **fuzzer-ai.py** — fuzzing de paramètres assisté par LLM
- **payload-mutator-ai.py** — muter des payloads existants avec un LLM

## Analyse & reporting

- **attack-logger.py** — logger et documenter les attaques réalisées
- **vuln-reporter.py** — générer un rapport de vulnérabilités structuré