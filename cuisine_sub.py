
from recipe_scrapers import scrape_me
from ingredient_parser import parse_ingredient

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
'Warm':	["cinnamon", "chile", "chili powder", "cloves", "ground cumin", "cumin", "nutmeg", "paprika", "adobo"]
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

sauces = {
    'soy sauce': 'agrodolce',
    'oyster sauce': 'prosecco mignonette',

}


#lamb for beef- more assertive
spice=[]
for lst in spices.values():
    spice += lst
for lst in herbs.values():
    spice += lst

main=  []
main += meats
for lst in fish.values():
    main += lst
oil=[]
for lst in oils.values():
    oil += lst


def cuisine_sub(ingred_dict):
    new_recipe={}
    recipe= ingred_dict.keys()
    subs=[]
    used=[]
    Italian_spices_herbs=['basil','thyme','oregano','rosemary','sage','bay leaves','garlic powder', 'adobo']
    Italian_cheeses=['Mozzarella','Parmesan','Parmesan cheese','Ricotta']
    for ing in recipe:
            #classify ingredients
            if ing in main:
                Italian_meats=['Salami', 'Soppresata', 'Prosciutto', 'Pepperoni']
                subs.append(f'There were some Italian spices added to the ingredients for your {ing}')
                #add to directions
            elif ing in spice and ing not in Italian_spices_herbs :
                flavor_prof = [i for i in spices if ing in spices[i]]
                for ingred in Italian_spices_herbs:
                    if ingred not in recipe and ingred not in used :
                        new_recipe[ingred]= ingred_dict[ing]
                        sub = ingred
                        used.append(ingred)
                        break
                subs.append(f'{ing} was replaced by {sub}.')
                if(len(flavor_prof)):
                    subs.append(f'However,{ing} has a(n) {flavor_prof[0]} flavor that would be lost in your dish!')
            elif ing in Dairy or 'cheese' in ing and ing not in Italian_cheeses:
                for ingred in Italian_cheeses:
                    if ingred not in recipe and ingred not in used:
                        new_recipe[ingred]= ingred_dict[ing]
                        sub = ingred
                        used.append(ingred)
                        break
                subs.append(f'{ing} was replaced by {sub}.')
            elif ing in oil :
                if ing == 'olive oil':
                    subs.append(f'Olive Oil is essential in Italian Cuisine. Try adding a bit more!')
                else:
                    subs.append(f'{ing} was replaced by Olive Oil')
                    new_recipe['olive oil']= ingred_dict[ing]
            elif ing in sauces:
                subs.append(f'{ing} was replaced by {sauces[ing]}')
                new_recipe[sauces[ing]] = ingred_dict[ing]
            elif 'pasta' in ing:
                subs.append('You could try making homemade pasta! Type "how to make homemade pasta" for a instructions link.')
            else:
                new_recipe[ing]=ingred_dict[ing]
    #additions
    for sp in Italian_spices_herbs:
        if sp not in used:
            if sp not in recipe:
                 new_recipe[sp]= ingred_dict[ing]
            else:
                subs.append(f'There is already {sp} in your dish, which is an Italian staple, mabybe try adding a bit more? ')
            break
    return subs, new_recipe


# ing = {'vegetable oil': ['1 tablespoon', ''], 'rice': ['1 cup', 'long grain white'], 'chicken broth': ['1.5 cups', ''], 'tomato': ['1 ', 'seeded and chopped'], 'onion': ['0.5 ', 'finely chopped'], 'green bell pepper': ['0.5 ', 'finely chopped'], 'jalapeno pepper': ['1 ', ['fresh', 'chopped']], 'cilantro': ['0.5 cups', 'chopped fresh'], 'chicken bouillon': ['1 cube', ''], 'garlic': ['1 clove', 'halved'], 'ground cumin': ['0.5 teaspoons', ''], 'salt and pepper': ['to taste', 'to taste']}
# print(cuisine_sub(ing)[0])