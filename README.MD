# 7Dif - Détection de Différences entre Images

Ce projet est un programme en Python permettant de charger deux images, de détecter les différences entre elles, et de générer une nouvelle image mettant en évidence les zones où les pixels diffèrent.

## Prérequis

Avant de commencer, assurez-vous d'avoir Python installé sur votre système.

## Installation

1. Clonez le dépôt vers votre machine locale :

git clone https://github.com/Lumantis/7Dif.git

2. Accédez au répertoire du projet :

cd 7Dif

3. Installez les dépendances en exécutant la commande suivante :

pip install -r requirements.txt

## Utilisation

1. Exécutez le programme en utilisant la commande suivante :

python main.py

2. Une interface utilisateur s'ouvrira avec un bouton "Charger les images".

3. Cliquez sur "Charger les images" pour sélectionner les deux images à comparer.

4. Cliquez sur "Scan" pour détecter les différences entre les deux images.

5. Une nouvelle image sera générée et affichée, montrant les régions où les pixels diffèrent en rouge et les parties similaires en bleu.

## Gestion des Erreurs

- Si une image ne peut pas être chargée, le programme affichera un message d'erreur.
- Si les images ont des tailles différentes, le programme affichera un message d'erreur.

## Auteur

André Monteiro

## Licence

Ce projet est sous licence MIT