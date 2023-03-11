import spacy
import speech_recognition as sr
from ingredient_parser import parse_ingredient
from recipe_scrapers import scrape_me
nlp = spacy.load('en_core_web_lg')
# cooking_words()
f = open('cook_words.txt', 'r')
cooking_library = f.read().splitlines()
g = open('utensils.txt', 'r')
utensils_library = g.read().splitlines()
rec = sr.Recognizer()
useless_words = ['and', 'or']
time_words = ['minute', 'minutes', 'hour', 'hours', 'seconds', 'half-hour', 'half hour', 'half an hour']
heat_words = ['medium heat', 'high heat', 'low heat', 'medium-low heat', 
              'medium-high heat', 'medium low heat', 'medium high heat']
steps_array = []
def navigator(url):
    recipe = scrape_me(url)
    instructions = recipe.instructions_list()
    ingredients = recipe.ingredients()
    separate_ingredients = []
    final_instructions = []
    parsed_ingredients = dict()
    for i in instructions:
        if '. ' in i:
            r_split = i.split('. ')
            for j in r_split:
                final_instructions.append(j)
        else:
            final_instructions.append(i)
    for i in ingredients:
        p = parse_ingredient(i)
        spl = p['name'].split()
        for j in spl:
            if j in useless_words:
                pass
            else:
                doc = nlp(j)[0]
                separate_ingredients.append(doc.lemma_.lower())
        if p['quantity'] == '':
            parsed_ingredients[p['name']] = ['to taste', p['comment']]
        else:
            parsed_ingredients[p['name']] = [p['quantity'] + ' ' + p['unit'], p['comment']]
    for r in final_instructions:
        recipe_dict = dict()
        recipe_obj = dict()
        verbs = []
        ings = []
        uts = []
        temp = None
        time = None
        spl = r.split()
        if ('degrees' in spl):
            ind = spl.index('degrees')
            temp = spl[ind-1] + ' ' + spl[ind] + ' ' + spl[ind+1]
        for x in heat_words:
            if x in r:
                xind = r.index(x)
                temp = r[xind:xind+len(x)]
        doc = nlp(r)
        for i in doc:
            if i.lemma_.lower() in cooking_library:
                verbs.append(i)
            # if i.dep_ == 'dobj':
            #     ings.append(i)
            if (i.lemma_.lower() in separate_ingredients):
                ings.append(i.text)
            if (i.lemma_.lower() in utensils_library) or (i.text.lower() in utensils_library):
                uts.append(i)
        recipe_obj['ingredients'] = ings
        recipe_obj['utensils'] = uts
        recipe_obj['temperature'] = temp
        if(len(verbs)):
            recipe_obj['cooking words'] = verbs[0]
        else:
            recipe_obj['cooking words'] = verbs
        recipe_dict[r] = recipe_obj
        steps_array.append(recipe_dict)
    # print(steps_array)
    # # print(parsed_ingredients)
    # # print(separate_ingredients)
    return [steps_array, parsed_ingredients]


# navigator("https://www.foodnetwork.com/recipes/food-network-kitchen/best-turkey-meatloaf-recipe-7217376")
