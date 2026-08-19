# 🛡️ Phishing Email Analyzer

Projet éducatif de cybersécurité développé en Python permettant d'analyser des fichiers `.eml` afin de détecter différents indicateurs de phishing.

## ✨ Fonctionnalités

- Analyse et parsing des emails
- Détection de mots-clés suspects
- Analyse des URLs
- Détection des incohérences entre l'expéditeur et le champ `Reply-To`
- Détection des pièces jointes potentiellement dangereuses
- Calcul d'un score de risque transparent de 0 à 100
- Historique des analyses avec SQLite
- Interface web développée avec Flask
- Tests automatisés avec Pytest

## 🛠️ Technologies utilisées

- **Python 3**
- **Flask**
- **SQLite**
- **Pytest**
- **HTML / CSS**
- **Git / GitHub**
- **Linux / WSL**

## 🚀 Installation et lancement

Créer un environnement virtuel :

```bash
python -m venv .venv
