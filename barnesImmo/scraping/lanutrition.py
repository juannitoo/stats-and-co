from .imports import *

print('lanutrition scraping chargé')

def bot_lanutrition(url):

    chrome_options = webdriver.ChromeOptions() 
    ua = UserAgent()
    user_agent = ua.random
    chrome_options.add_argument('--no-sandbox') # obligé en 1er si nécessaire
    chrome_options.add_argument('--headless') # unlock devtools fail
    chrome_options.add_argument(f'--user-agent={user_agent}') # unlock devtools fail


    driver = webdriver.Chrome(
        service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()), 
        chrome_options=chrome_options
        )
    driver.get(url)

    title = driver.title

    data = OrderedDict()

    ############################################################################

    h4 = driver.find_elements(By.TAG_NAME, 'h4')

    for i, titre in enumerate(h4) :
        if i < 3:
          data[f"tableau{i+1}"] = [[titre.text],[""]] # je crée une fausse ligne pour "span" les entetes des tableaux
        elif i >= 3:
          data[f"tableau4"] = [['Corps gras, (tous à moins de 5mg/portion)'],[""]]         
          data[f"tableau{i+2}"] = [[titre.text],[""]] 
        elif i >= 7:
            break

    print('titre :', data)

    tableaux = driver.find_elements(By.TAG_NAME, 'table')
    entetes = [] 

    for i, tableau in enumerate(tableaux) :
        
        if i == 0 :
            entetes_list = tableau.find_elements(By.CSS_SELECTOR, 'tbody tr td')[0:3]
            for element in entetes_list:
                entetes.append(element.text)

        sublist = []
        subsublist = []

        # je supprime les mg/portions qui bugguent
        content_temp = tableau.find_elements(By.CSS_SELECTOR, 'tbody tr td')[3:]

        if i == 3:
            # corps gras
            content_temp = tableau.find_elements(By.CSS_SELECTOR, 'tbody tr td')[1:]
            
        for j, element in enumerate(content_temp):
            subsublist.append(element.text)
            if (j+1)%3 == 0:
                sublist.append(subsublist)
                subsublist = []
            if (j+1)%3 != 0 and j == len(content_temp)-1:
                sublist.append(subsublist)

        if i == 3:
            data[f"tableau{i+1}"] += [" "] + [" "] # pour le span de mg/portion
        else:
            data[f"tableau{i+1}"] += [entetes] + [" "] # pour le span de mg/portion

        data[f"tableau{i+1}"] += sublist
        if i >= 7:
            break
          
    # pour générer un fichier html de se qui est scrapé
    html = driver.find_element(By.TAG_NAME, 'html').get_attribute("outerHTML")

    driver.quit()

    print(f"entetes : {entetes}")
    print(f"data : {data}")

    nom_fichier = re.split(r'\.', url)[1]
    with open(f'save_scrap/{nom_fichier}.html', 'w') as fichier:
        fichier.write(str(html))

    return data