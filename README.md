
# Pipeline de Données et Automatisation de l'Envoi d'Emails

## Description

Ce projet automatise un processus de pipeline de données, incluant l'extraction de données d'une base de données, l'exécution de fonctions spécifiques sur les données extraites, et l'envoi des résultats par email. Le projet comprend deux scripts principaux :

1. `Extract.py` - Partie du pipeline de données, il extrait les données de la base de données, les traite et enregistre les résultats.
2. `Sendemail.py` - Envoie un email avec les données traitées en pièce jointe.

## Vue d'Ensemble du Projet

- Extraction automatisée de données à partir d'une base de données.
- Traitement et analyse des données.
- Envoi automatisé d'emails avec les données traitées en pièce jointe.

## Structure du Projet

- `Extract.py` : Extrait les données de la base de données (`extracted_data.csv`), les traite et enregistre les résultats.
- `Sendemail.py` : Envoie un email avec les données traitées en pièce jointe (`results.xlsx`).

## Technologies

- Python

## Installation et Utilisation

### Prérequis

- Python 3.x
- Serveur MySQL

### Installation

1. **Cloner le dépôt** :
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Installer les dépendances Python** :
    ```sh
    pip install -r requirements.txt
    ```

3. Configurer les paramètres de la base de données et des emails dans les scripts respectifs.

### Instructions d'Utilisation

#### Extraction et Traitement des Données

1. Exécuter le script `Extract.py` pour extraire les données de la base de données et effectuer les fonctions requises :
    ```bash
    python Extract.py
    ```

2. Ce script génèrera deux fichiers :
    - `extracted_data.csv` - Les données brutes extraites de la base de données.
    - `results.xlsx` - Les données traitées.

#### Envoi d'Email

1. Exécuter le script `Sendemail.py` pour envoyer un email avec les données traitées en pièce jointe :
    ```bash
    python Sendemail.py
    ```

## Configuration

### Configuration de la Base de Données

Mettre à jour le script `Extract.py` avec les détails de connexion à votre base de données :

### Configuration de l'Email

Mettre à jour le script `Sendemail.py` avec les détails de votre serveur de messagerie et les informations du destinataire :

```python
# Exemple de configuration de l'email
smtp_server = 'smtp.example.com'
smtp_port = 587
sender_email = 'youremail@example.com'
password = 'yourpassword'
receiver_email = 'receiver@example.com'
```

## Contributeurs

Melik Soufiane

## Licence

Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.


