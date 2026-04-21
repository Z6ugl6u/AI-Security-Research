# 🤖 AI Security Research

> Référence technique condensée sur la sécurité des systèmes d'intelligence artificielle — attaque, défense, et tout ce qui se trouve entre les deux.

---

## ⚠️ Disclaimer

Ce repo est **à but éducatif uniquement**. Les techniques documentées ici sont partagées pour comprendre, détecter et défendre les systèmes IA. Ne jamais les utiliser contre des systèmes sans autorisation explicite.

---

## 🗂️ Structure

```
AI-Security-Research/
├── 01-fondamentaux/
│   ├── llm-architecture.md
│   ├── training-data-pipeline.md
│   └── embeddings-vectors.md
├── 02-prompt-injection/
│   ├── direct-injection.md
│   ├── indirect-injection.md
│   ├── rag-poisoning.md
│   └── payload-cheatsheet.md
├── 03-jailbreaking/
│   ├── techniques-overview.md
│   ├── bypass-strategies.md
│   └── multi-turn-attacks.md
├── 04-defenses/
│   ├── input-sanitization.md
│   ├── output-filtering.md
│   └── llm-firewalls.md
├── 05-offensive-ai/
│   ├── data-poisoning.md
│   ├── adversarial-examples.md
│   ├── model-extraction.md
│   └── ai-agent-attacks.md
├── tools/
│   ├── README.md
│   ├── prompt-injector.py
│   ├── jailbreak-tester.py
│   └── payload-fuzzer.py
└── labs-writeups/
    └── tryhackme-ai-path.md
```

---

## 🧭 Par où commencer ?

| Profil | Point d'entrée |
|--------|----------------|
| Débutant | `01-fondamentaux/llm-architecture.md` |
| Pentesteur | `02-prompt-injection/direct-injection.md` |
| Défenseur | `04-defenses/input-sanitization.md` |
| Chercheur | `05-offensive-ai/ai-agent-attacks.md` |

---

## 📚 Ressources

- [OWASP Top 10 for LLMs](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
- [MITRE ATLAS](https://atlas.mitre.org/)
- [LLM Security](https://llmsecurity.net)
- [TryHackMe AI Path](https://tryhackme.com)
