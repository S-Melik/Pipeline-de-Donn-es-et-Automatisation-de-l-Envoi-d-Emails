# Pipeline-de-Données-et-Automatisation-de-l-Envoi-par-Email

## Description
Ce projet implique l'extraction de données d'une base de données, leur nettoyage, et l'envoi des données nettoyées sous forme de fichier Excel par email à des destinataires spécifiques.

## Table des Matières
- [Description](#description)
- [Fichiers](#fichiers)
- [Technologies](#technologies)
- [Installation et Utilisation](#installation-et-utilisation)
- [Flux de Travail du Projet](#flux-de-travail-du-projet)
- [Contribuer](#contribuer)
- [Licence](#licence)

## Fichiers
- `Extract.py`: Script pour extraire et nettoyer les données d'une base de données.
- `extracted_data.csv`: Données extraites au format CSV.
- `results.xlsx`: Données nettoyées enregistrées sous forme de fichier Excel.
- `Sendmail.py`: Script pour envoyer le fichier Excel par email.

## Technologies
- Python
- SQL
- Excel

## Installation et Utilisation

### Extraction et Nettoyage des Données
```bash
python Extract.py
