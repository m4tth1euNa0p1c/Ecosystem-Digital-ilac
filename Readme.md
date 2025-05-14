# Python API Interaction ILAC Assignement

## Description

Ce projet illustre comment récupérer et parser un fichier JSON personnalisé hébergé via GitHub Pages, puis afficher son contenu en console avec Python.

## Structure du projet

```

assignement/
├── .gitignore
├── README.md
├── requirements.txt
├── custom\_data.json               # Fichier JSON custom accessible via GitHub Pages
├── data/
│   └── custom\_data.json           # Optionnel : copie locale des données
├── src/
│   ├── **init**.py
│   └── fetch\_parse.py             # Script principal : récupération et parsing JSON
├── tests/
│   ├── **init**.py
│   ├── test\_fetch.py              # Tests unitaires pour la récupération HTTP
│   └── test\_parse.py              # Tests unitaires pour le parsing JSON
├── docs/
│   ├── report.pdf                 # Rapport PDF final
│   ├── screenshots/
│   │   ├── folder\_structure.png
│   │   └── terminal\_output.png
│   └── presentation.pptx          # Support de présentation (facultatif)
├── .github/
│   ├── workflows/
│   │   └── ci.yml                 # Pipeline GitHub Actions (lint, tests)
│   └── pages/
│       └── custom\_data.json       # Version publique pour GitHub Pages
└── LICENSE                        # (Facultatif)

```

## Installation

1. **Cloner le dépôt**  
   ```bash
   git clone https://github.com/m4tth1euNa0p1c/Ecosystem-Digital-ilac.git
   cd Ecosystem-Digital-ilac
   ```

2. **Créer et activer l’environnement virtuel**

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate
   ```

3. **Installer les dépendances**

   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

## Création du fichier JSON personnalisé

* Créez un fichier `custom_data.json` (à la racine ou dans `data/`) contenant au moins 3 objets JSON.
* Chaque objet doit comporter :

  * `name` (string)
  * `description` (string)
  * `specifications` (object)
  * `tags` (array)
  * Tout autre champ pertinent à votre thème (instruments, livres, films…).

Exemple :

```json
[
  {
    "name": "Guitare électrique",
    "description": "Instrument à cordes amplifié, utilisé dans le rock.",
    "specifications": { "brand": "Fender", "model": "Stratocaster", "strings": 6 },
    "tags": ["cordes", "rock"]
  },
  …
]
```

## Hébergement via GitHub Pages

1. Rendez-vous dans les **Settings → Pages** de votre dépôt.
2. Sélectionnez la branche `main` (ou `master`) et le dossier `/pages` (ou `/root`).
3. Vérifiez que votre `custom_data.json` est accessible publiquement, par exemple :

   ```
[   https://<username>.github.io/<repository-name>/custom_data.json](https://github.com/m4tth1euNa0p1c/Ecosystem-Digital-ilac/blob/main/custom_data.json)
   ```

## Exécution du script

```bash
python src/fetch_parse.py
```