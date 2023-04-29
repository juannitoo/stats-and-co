from django.shortcuts import render

# toutes les fonctions de scrap s'appellent bot
from .scraping.leboncoin import bot

# reportlab pdf
from .reportlab.pdf import pdf

# https://github.com/SergeyPirogov/webdriver_manager

# Create your views here.
def home(request):

    # scraping
    urls = {}
    urls['leboncoin'] = "https://www.leboncoin.fr/"
    urls['seloger'] = "https://www.seloger.com//"
    urls['locationsaintjeandeluz'] = "http://www.locationsaintjeandeluz.fr/"

    url = urls['locationsaintjeandeluz']
    # bot(url)

    # pdf 
    pdf()
   

    context={}
    # context["titre"] = h1

    return render(request, 'barnesImmo/home.html', context)
