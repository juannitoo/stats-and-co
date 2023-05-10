# Attention, ce dossier ne fait pas parti de ce repo et doit être placé dans son venv perso pour installer
# les dépendances chrome et chromedriver avant de créer l'image via docker
# je m'évite là de créer un repo spécial pour ca sur githu.

# pour s'en servir, il faut faire un couper coller hors du dossier racine stats-and-co et de son venv

https://gallery.ecr.aws/lambda/python

https://github.com/umihico/docker-selenium-lambda


 chromium --headless=new --print-to-pdf https://developer.chrome.com/

# pour déployer :
la première fois tous les jours il faut se relogguer avec docker avec une commande trouvable sur le repo aws ecr puis :

docker build -t selenium_lanutrition_ss_json .

docker tag selenium_lanutrition_ss_json:latest 214622732998.dkr.ecr.eu-west-3.amazonaws.com/selenium:selenium-lanutrition-ss-json

docker push 214622732998.dkr.ecr.eu-west-3.amazonaws.com/selenium:selenium-lanutrition-ss-json
