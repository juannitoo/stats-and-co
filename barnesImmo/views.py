from django.shortcuts import render

# toutes les fonctions de scrap s'appellent bot
from .scraping.leboncoin import bot_leboncoin
from .scraping.lanutrition import bot_lanutrition

# reportlab pdf
from .reportlab.pdf import pdf

from .reportlab.lanutrition import lanutrition_pdf

# https://github.com/SergeyPirogov/webdriver_manager

# Create your views here.
def home(request):

    # scraping
    urls = {}
    urls['leboncoin'] = "https://www.leboncoin.fr/"
    urls['seloger'] = "https://www.seloger.com//"
    urls['locationsaintjeandeluz'] = "http://www.locationsaintjeandeluz.fr/"
    urls['lanutrition'] = "https://www.lanutrition.fr/les-aliments-riches-en-oxalate"

    url = urls['lanutrition']

    demarer_scraping = True

    if demarer_scraping:
        data = bot_lanutrition(url)
    else :
        data = {
            'tableau1': [
                ['Les légumes et légumes secs, entiers ou en jus'], 
                [''],
                ['Niveau élevé\n(plus de 10 mg/portion)', 'Niveau modéré\n(5 à 10 mg/portion)', 'Niveau bas\n(moins de 5 mg/portion)'], 
                [''],
                ['Aubergine, cuite', 'Artichaut', 'Asperge'], 
                ['Aubergines, cuites', 'Carottes, cuites', 'Avocat'], 
                ['Betteraves, cuites ***', 'Carottes, jus', 'Brocoli'], 
                ['Blettes, crues ou cuites ***', 'Chou frisé, cuit', 'Champignons'], 
                ['Carotte crue', 'Choucroute', 'Chou rouge'], 
                ['Céleri cru', 'Fenouil, cuit', 'Chou vert'], 
                ['Chicorée crue', 'Haricots de Lima, cuits', 'Chou-fleur'], 
                ['Chou cavalier cuit', 'Olives noires (10 grosses)', 'Choux de Bruxelles'], 
                ['Epinards, crus ou cuits ***', 'Panais, cuit', 'Cresson'], 
                ['Feuilles de moutarde, crues', 'Persil, cru', 'Endive'], 
                ['Haricots blancs ou lingots', 'Petits pois, en conserve', 'Laitue'], 
                ['Haricots verts', 'Pois cassés', 'Maïs doux'], 
                ['Lentilles, cuites', 'Scarole, crue', 'Navet'], 
                ['Okra **', 'Tomate, jus', 'Oignons, crus ou cuits'], 
                ['Olives vertes (10 grosses)', ' ', 'Petits pois, frais ou surgelés'], 
                ['Patates douces, cuites ***', ' ', 'Radis'], 
                ['Piment rouge cru', ' ', ' '], 
                ['Pissenlit cuit', ' ', ' '], 
                ['Poireau', ' ', ' '], 
                ['Poivrons, crus', ' ', ' '], 
                ['Pommes de terre, frites, chips, cuites à l’eau ou au four', ' ', ' '], 
                ['Rutabagas, cuits', ' ', ' '], 
                ['Soja, fromage', ' ', ' '], 
                ['Soja, lait **', ' ', ' '], 
                ['Soja, tempeh', ' ', ' '], 
                ['Soja, tofu **', ' ', ' '], 
                ['Soja, yaourt **', ' ', ' '], 
                ['Tomate,crue, fraîche ou en conserve', ' ']
            ]
        }

    # pdf()
    lanutrition_pdf(data)
   

    context={}
    # context["titre"] = h1

    return render(request, 'barnesImmo/home.html', context)
