
from recipe_scrapers import scrape_me
from ingredient_parser import parse_ingredient
import requests
from bs4 import BeautifulSoup
import spacy

# Send an HTTP request to the page
#url = 'https://www.allrecipes.com/recipe/285077/easy-one-pot-ground-turkey-pasta/'
#cuisine= French
#"https://www.allrecipes.com/search?q={cuisine}"
#response = requests.get(url)

# Parse the HTML content of the page using Beautiful Soup
# soup = BeautifulSoup(response.content, 'html.parser')

# Find the HTML elements that contain the links to the individual recipe pages

#recipe_lin#ks = soup.find('a', {'class': "comp mntl-card-list-items mntl-document-card mntl-card card card--no-image"}).get('href')




spices={'Earthy' : ["curry powder", "garlic powder", "onion powder", "turmeric", "vadouvan", "za'atar"],
'Floral':	["cardamom", "coriander", "fennel", "lavender", "nutmeg"," saffron", "star anise"],
'Peppery':	["allspice", "ground ginger", "peppercorns", "mustard powder", "sumac",'pepper'],
'Warm':	["cinnamon", "chile", "chili powder", "cloves", "cumin", "nutmeg", "paprika"]
}

meats= ('chuck', 'brisket', 'round roast','beef','steak','filet mignon','lamb','chicken','ground beef','ground turkey','turkey','pork')

fish= {'lean': ['bass', 'catfish', 'cod', 'flounder', 'halibut', 'monkfish', 'red snapper', 'skate', 'sole', 'tilapia'],
        'fatty':['char', 'mahi-mahi', 'salmon', 'swordfish', 'tuna']
}

oils={'Neutral oils,High': ['Canola oil', 'coconut oil', 'corn oil', 'grapeseed oil', 'peanut oil' ,'vegetable oil'],
'Flavored oils,Medium-high': ['Avocado oil', 'nut oils', 'olive oil', 'sesame oil', 'sunflower oil'],
'Solid fats,Low':['Bacon fat', 'butter', 'chicken fat', 'lard', 'margarine' ,'vegetable shortening']
}

#low smoke point burns easily
# solid fats = unhealthy

Dairy=['Milk','Half-and-Half','Heavy Cream','Buttermilk','Butter']
#cheese
herbs ={
'Basil':	['Chervil', 'cilantro', 'dill', 'Italian seasoning', 'oregano', 'mint', 'parsley'],
'Bay Leaves':	['Herbes de Provence', 'oregano', 'rosemary', 'sage', 'thyme'],
'Chervil':	['Basil, dill, parsley, tarragon'],
'Chives':	['Cilantro', 'garlic powder', 'onion powder', 'parsley'],
'Cilantro':	['Basil', 'chives', 'parsley','mint'],
'Dill':	['Basil', 'chervil', 'mint', 'parsley'],
'Marjoram':	['Herbes de Provence', 'Italian seasoning', 'oregano', 'rosemary', 'sage', 'thyme'],
'Mint':	['Basil', 'cilantro', 'dill', 'parsley'],
'Oregano':	['Bay leaves', 'herbes de Provence', 'Italian seasoning', 'rosemary', 'thyme', 'sage'],
'Parsley':	['Basil', 'chervil', 'chives', 'cilantro, dill', 'Italian seasoning', 'mint', 'tarragon'],
'Rosemary':	['Bay leaves', 'herbes de Provence', 'oregano', 'thyme', 'sage'],
'Sage':	['Bay leaves', 'herbes de Provence', 'oregano', 'rosemary', 'thyme'],
'Tarragon':	['Chervil', 'parsley'],
'Thyme':	['Bay leaves', 'herbes de Provence', 'oregano', 'rosemary', 'sage']
}



#lamb for beef- more assertive
spice=[]
for list in spices.values():
    spice += list
for list in herbs.values():
    spice += list

main=  []
main += meats
for list in fish.values():
    main += list
oil=[]
for list in oils.values():
    oil += list


def cuisine_sub(ingred_dict):
    new_recipe={}
    recipe= recipe.keys()
    subs=[]
    used=[]
    Italian_spices_herbs=['basil','thyme','oregano','rosemary','sage','bay leaves','garlic powder']
    Italian_cheeses=['Mozzarella','Parmesan','Parmesan cheese','Ricotta']
    for ing in recipe:
            #classify ingredients
            if ing in main:
                Italian_meats=['Salami', 'Soppresata', 'Prosciutto', 'Pepperoni']
                subs.append(f' Try adding more Italian spices to your {ing}')
                #add to directions
            elif ing in spice and ing not in Italian_spices_herbs :
                Italian_spices_herbs=['basil','thyme','oregano','rosemary','sage','bay leaves','garlic powder']
                flavor_prof = [i for i in spices if ing in spices[i]]
                for ingred in Italian_spices_herbs:
                    if ingred not in recipe and ingred not in used :
                        new_recipe[ingred]= ingred_dict[ing]
                        sub = ingred
                        used.append(ingred)
                        break
                subs.append(f'{ing} could be replaced by {sub}. However,{ing}, has a/n {flavor_prof} flavor that would is lost your dish!')
            elif ing in Dairy or 'cheese' in ing and ing not in Italian_cheeses:
                for ingred in Italian_cheeses:
                    if ingred not in recipe and ingred not in used:
                        new_recipe[ingred]= ingred_dict[ing]
                        sub = ingred
                        used.append(ingred)
                        break
                subs.append(f'{ing} could be replaced by {sub}.')
            elif ing in oil :
                if ing == 'olive oil':
                    subs.append(f'Olive Oil is essential in Italian Cuisine. Try adding a bit more!')
                else:
                    subs.append(f'{ing} could be replaced by Olive Oil')
                    new_recipe['olive oil']= ingred_dict[ing]
            elif 'pasta' in ing:
                subs.append('You could try making homemade pasta!')
            else:
                new_recipe[ing]=ingred_dict[ing]
    #additions
    for sp in Italian_spices_herbs:
        if sp not in used:
            if sp not in recipe:
                subs.append(f'Also, try adding 1 tsp of {sp} to your dish to give it more Italian flavor')
            else:
                subs.append(f'There is already {sp} in your dish, which is an Italain staple, mabybe try adding a bit more? ')
            break
    return subs, new_recipe
