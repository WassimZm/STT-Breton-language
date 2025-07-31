## Thursday, July 24, 2025: Wassim & Alice :
- Faire le Plan de mémoire : commencer la rédaction.
- l'évaluation dépend de plusieurs facteurs ( exigence en fonction de l'usage + variations : cas d'utilisation ).
- Intégrer les données de Gweltaz meme si on les utilise pas.
- Expliquer la préparation des données pour le Fine Tunning dans la partie des données.
- Essayer d'utiliser le GPU de Kaggle + Utiliser Google Collab.
- Aborder le problème de code swittching dans la mémoire.
- Indiquer les avantages et les inconvéniants pour chaque dataset.

## Thursday, July 16, 2025: Wassim & Alice :
- Commencer par la rédaction du mémoire, puis l'article scientifique.
- Faire un plan de la mémoire et l’envoyer à Alice (au plus tard jeudi prochain).
- Inclure un état de l’art dans le mémoire, et préciser les traveaux de Gweltaz.
- Expliquer toutes les expériences réalisées dans le cadre du stage dans la mémoire.
- Indiquer que le stage s'inscrit dans le cadre du projet YAR.
- Fine-tuning du modèle Whisper **Tiny** sur les données de Yuna.
- Préciser les jeux de données utilisés pour l'entraînement des modèles pré-entraînés (Whisper, Wav2Vec, Vosk ...) et expliquer leur architectures.
- Essayer de comprendre le fonctionnement de Wav2vec.
- Organiser les différents groupes de données de Yuna et utiliser 20 % pour l'entraînement, 80 % pour l’évaluation en chaque groupe.
- Les données de Yuna représentent plus de 6 heures d’audio.
- Évaluer le modèle Wav2Vec sur les mêmes données.
- Comparer les performances des modèles Whisper ( tiny, small, base ).

## Tuesday, June 17, 2025: Wassim & Alice & Loic & Mélanie & Yuna :
- Discuter les problèmes qui conçernent les données de Dastum.
- Faire entrainer Whisper au lieu de Vosk.
- La présence du français dans quelques audio à transcrire.



## Wednesday, June 11, 2025: Wassim & Alice & Loic :
- Using Data Wrangler to visualize better the instances.
- Instance number 6173 is interesting.
- Create a new data frame that contains WER, CER, Transcription and Ground truth before and after cleaning. The data frame summarizes all th work.
- Counting the average wer & cer for every city & department.
- Graphie locale & Peurunvan : correction in the df.
- Proposition to use a Python script code for evaluation instead of Notebook ( execution in Terminal ).
- Whisper has a weak performance, even after the specefication of the language ( Breton "br" ), tho the performance is varying depending on the model ( Meduim, Large, Turbo ... etc ).
- The need of GPU for evaluating and Fine-Tunning Whisper models.

## Tuesday, June 3, 2025: Wassim & Alice & Loic ( Visio ) :
- Séparer la dataset "Banque sonore des DIalectes Bretonnes" ( en 3 catégories : par département )
- Le script que Loic a envoyé peut etre efficace pour l'évaluation ( chaque instance = element )
- Faire une evaluation pour chaque categorie ( departement ) et comparer.
- Utiliser df pour avoir la colonne City.
- Evaluer Whisper avant Fine-Tunning.
- Faire une analyse sur les instances de la dataset "Banque sonore" pour adapter le data-cleaning de Gweltaz.
- Organiser l'espace de travail.

## Monday, May 27, 2025: Wassim & Alice & Loic : Visio
- Discuter le problème de l'évaluation ( pour le WER ) sur la Banque Sonore des dialectes bretonnes.
- Proposer l'évaluation du modèle de Gweltaz sur : la partie test de Common Voice / aprés la modification des régles + ponctuations faites par Gweltaz ( le - ).
- Utiliser la librairie que loic a envoyé : https://gitlab.com/prebens-phd-adventures/universal-edit-distance et proposer ma propre segmentation pour l'évaluation.
- le modèle Vosk performe mieux pour le Breton standard ( entire dataset : WER 73%, only standard : 69% ).
- Récupèrer et Evaluer un modèle whisper.
- Proposition de Fine tunning un Modèle Whisper Multilingue.
- Mardi 3 Juin : Loic à Paris 8.

## Tuesday, May 13, 2025: Wassim & Alice & Loic
* Discuter les points abordés lors de la réunion précédente ( évaluation du modéle Vosk & Web scrapping ).
* Dans le cadre de la dataset "Banque sonore Breronne", Il est possible de séparer le fichier .tsv en deux fichiers ( Breton standard & dialectale ).
* Gweltaz a entrainé son modèle sur le breton standards ( la transcription avec Yuna se fait d'une façon standard ).
* Avant l’évaluation ou l’entraînement de Anaouder, il faut passer par la phase de **la normalisation & tokenisation** des données.
* Gweltaz a fourni un script pour la normalisation et tokenisation à https://github.com/gweltou/ostilhou/blob/main/scripts/MCV_score_utts.py .
* Utiliser app.diagrams.net pour créer des schémas.
* Débuter l’évaluation du modèle Whisper.

## Friday, May 9, 2025: Wassim & Loic : Visio
* Discuter les résultat de l'évaluation du modéle "vosk-model-br-25.02" sur la dataset "Banque Sonore Dialectes Bretonnes".
* Discuter les problématiques de la dataset ( Les instances "graphie locale", balises HTML : br ... etc ).
* Proposer une phase de web scraping pour reconstruire proprement le jeu de données .
* Le fine-tuning du modèle de Gweltaz nécessite l'utilisation de Kaldi.
* Ne pas utiliser Kaldi pour le fine-tuning, car il est complexe et nécessite beaucoup de temps et ressources.
* Utiliser Kaldi seulement pour l'évaluation, puis passer vers le fine tuning du modéle whisper.
