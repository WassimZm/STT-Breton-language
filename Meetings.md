## Friday, May 9, 2025: Wassim & Loic : Visio
* Discuter les résultat de l'évaluation du modéle "vosk-model-br-25.02" sur la dataset "Banque Sonore Dialectes Bretonnes".
* Discuter les problématiques de la dataset ( Les instances "graphie locale", balises HTML : br ... etc ).
* Proposer une phase de web scraping pour reconstruire proprement le jeu de données .
* Le fine-tuning du modèle de Gweltaz nécessite l'utilisation de Kaldi.
* Ne pas utiliser Kaldi pour le fine-tuning, car il est complexe et nécessite beaucoup de temps et ressources.
* Utiliser Kaldi seulement pour l'évaluation, puis passer vers le fine tuning du modéle whisper.

## Tuesday, May 13, 2025: Wassim & Alice & Loic
* Discuter les points abordés lors de la réunion précédente ( évaluation du modéle Vosk & Web scrapping ).
* Dans le cadre de la dataset "Banque sonore Breronne", Il est possible de séparer le fichier .tsv en deux fichiers ( Breton standard & dialectale ).
* Gweltaz a entrainé son modèle sur le breton standards ( la transcription avec Yuna se fait d'une façon standard ).
* Avant l’évaluation ou l’entraînement de Anaouder, il faut passer par la phase de **la normalisation & tokenisation** des données.
* Gweltaz a fourni un script pour la normalisation et tokenisation à https://github.com/gweltou/ostilhou/blob/main/scripts/MCV_score_utts.py .
* Utiliser app.diagrams.net pour créer des schémas.
* Débuter l’évaluation du modèle Whisper.
