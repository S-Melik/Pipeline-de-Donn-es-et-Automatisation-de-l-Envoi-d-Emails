
# Pipeline de Données et Automatisation de l'Envoi par Email

## Description
Ce projet implique l'extraction de données d'une base de données, leur manipulation et nettoyage, et l'envoi des données nettoyées et manipulées sous forme de fichier Excel par email à des destinataires spécifiques.

## Table des Matières
- [Description](#description)
- [Fichiers](#fichiers)
- [Technologies](#technologies)
- [Installation et Utilisation](#installation-et-utilisation)
- [Flux de Travail du Projet](#flux-de-travail-du-projet)
- [Contribuer](#contribuer)
- [Licence](#licence)

## Fichiers
- `Extract.py`: Script pour extraire et manipuler les données d'une base de données.
- `extracted_data.csv`: Données extraites au format CSV.
- `results.xlsx`: Données manipulées et nettoyées enregistrées sous forme de fichier Excel.
- `Sendmail.py`: Script pour envoyer le fichier Excel par email.

## Technologies
- Python
- SQL
- Excel

## Installation et Utilisation

### Extraction et Manipulation des Données
```bash
python Extract.py
```

### Envoi par Email
1. Mettre à jour `Sendmail.py` avec les adresses email des destinataires et les détails du serveur SMTP.
2. Exécuter le script pour envoyer le fichier Excel par email.
```bash
python Sendmail.py
```

## Flux de Travail du Projet
1. Extraire et manipuler les données de la base de données avec `Extract.py`.
2. Nettoyer les données et les enregistrer sous forme de `results.xlsx`.
3. Utiliser `Sendmail.py` pour envoyer le fichier Excel aux destinataires spécifiés.

## Contribuer
Les contributions sont les bienvenues ! Veuillez cloner ce dépôt et soumettre des pull requests.

## Licence
Ce projet est sous licence MIT.
