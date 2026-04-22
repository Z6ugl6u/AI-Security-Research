# Sujets

## Fondamentaux de la défense

- what-is-llm-security.md
- defense-in-depth.md *(approche multicouche)*
- attack-surface-mapping.md *(cartographier les surfaces d'attaque)*
- threat-model-defense.md
- security-by-design.md *(intégrer la sécurité dès la conception)*

## Sécurisation des inputs

- input-sanitization.md
- input-validation.md
- prompt-structure-best-practices.md *(messages structurés vs concaténation)*
- delimiter-hardening.md
- instruction-hierarchy.md *(priorité des instructions)*

## Sécurisation des outputs

- output-filtering.md
- pii-detection.md *(détection d'informations personnelles)*
- content-policy-enforcement.md
- output-validation.md *(vérifier que la sortie correspond à ce qu'on attend)*

## Détection des attaques

- injection-detection.md
- jailbreak-detection.md
- anomaly-detection.md *(détecter les comportements anormaux)*
- prompt-classification.md *(classifier les inputs suspects)*

## Architecture défensive

- llm-firewalls.md *(LlamaGuard, NeMo Guardrails, Rebuff...)*
- sandboxing-agents.md *(isoler les agents LLM)*
- least-privilege-principle.md *(moindre privilège appliqué aux LLMs)*
- rag-security.md *(sécuriser le pipeline RAG)*
- multi-llm-architecture.md *(un LLM de modération devant le LLM principal)*

## Monitoring & réponse

- logging-and-auditing.md
- alerting.md
- incident-response.md
- red-teaming.md *(tester ses propres systèmes)*

## Hardening des modèles

- system-prompt-hardening.md *(écrire un system prompt résistant)*
- fine-tuning-for-safety.md
- adversarial-training.md

## Référence

- defense-cheatsheet.md
- secure-deployment-checklist.md
- owasp-llm-top10.md *(mapping avec le Top 10 OWASP LLM)*


# Tools

> Outils pour détecter, filtrer et monitorer

## Détecter les attaques

- **injection-detector.py** — scorer le risque d'injection d'un input
- **jailbreak-detector.py** — détecter les patterns de jailbreak connus
- **anomaly-scorer.py** — détecter les inputs statistiquement anormaux

## Filtrer les inputs/outputs

- **input-sanitizer.py** — nettoyer et valider un input avant de l'envoyer au LLM
- **output-filter.py** — filtrer les sorties sensibles (PII, secrets, contenu interdit)
- **pii-redactor.py** — détecter et masquer automatiquement les PII

## Tester sa défense

- **red-team-runner.py** — lancer une campagne de red teaming automatisée
- **defense-scorer.py** — évaluer le niveau de protection d'un système sur une échelle
- **system-prompt-auditor.py** — analyser un system prompt et identifier les faiblesses

## Monitoring

- **prompt-logger.py** — logger tous les échanges avec métadonnées
- **alert-monitor.py** — monitorer en temps réel et alerter sur les patterns suspects
- **audit-report.py** — générer un rapport d'audit des interactions