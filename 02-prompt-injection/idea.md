# Sujets

## Fondamentaux de l'injection

- what-is-prompt-injection.md
- why-llms-are-vulnerable.md
- injection-vs-jailbreak.md *(différence importante souvent confondue)*
- threat-model-prompt-injection.md

## Injection directe

- direct-injection-basics.md
- instruction-override.md
- role-hijacking.md
- system-prompt-exfiltration.md
- token-smuggling.md *(leetspeak, unicode, zero-width spaces...)*
- delimiter-injection.md

## Injection indirecte

- indirect-injection-basics.md
- injection-via-web-pages.md
- injection-via-documents.md *(PDF, Word, CSV...)*
- injection-via-emails.md
- injection-via-api-results.md
- multimodal-injection.md *(texte caché dans des images)*

## RAG & pipelines

- rag-poisoning.md
- vector-db-attacks.md
- supply-chain-poisoning.md
- metadata-injection.md

## Techniques avancées

- chained-injection.md *(multi-step, pivot)*
- persistent-injection.md *(persist-and-trigger)*
- context-window-manipulation.md
- many-shot-injection.md

## Référence

- payload-cheatsheet.md
- encoding-tricks.md *(base64, rot13, unicode, hex...)*
- detection-bypass.md *(contourner les filtres de détection)*


# Tools

> Outils pour tester et détecter les injections de prompt

## Tester une cible

- **prompt-injector.py** — envoyer une liste de payloads contre une API cible et logger les réponses
- **injection-scanner.py** — scanner automatique qui classe les vulnérabilités par sévérité

## Générer des payloads

- **payload-fuzzer.py** — mutations et variations automatiques d'un payload de base
- **encoding-generator.py** — générer toutes les variantes encodées d'un payload (base64, leetspeak, unicode...)

## Détecter les injections

- **injection-detector.py** — analyser un input utilisateur et scorer le risque d'injection
- **system-prompt-probe.py** — tester si un système fuite son system prompt

## Tester les RAG

- **rag-poisoning-tester.py** — injecter des documents malveillants dans une base vectorielle de test
- **retrieval-monitor.py** — monitorer ce qui est récupéré par le RAG pour une requête donnée