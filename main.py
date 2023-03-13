from navigator import *
from vegetarian import *
from double import *
from healthy import *
from cuisine_sub import *
import webbrowser
import re

def main():
    url = input('Enter URL of recipe: ')
    recipe_obj = navigator(url)
    recipe = recipe_obj[0]
    ingredients_dict = recipe_obj[1]
    hard_coded=['next','back','repeat','how','help','ingredients','exit']
    boo = True
    curr = 0
    prev= None
    options = ['Options: \n',
               'Type "next" to go to next step.\n',
               'Type "back" to go to previous step.\n',
               'Type a number to go to that step. \n',
               'Type "repeat" to repeat current step.\n',
               'Type "how" to open a link to a YouTube search on how to perform current step.\n',
               'Type "tools" to get a list of tools used in the current step. \n',
               'Type "what temperature" to get the temperature needed for the current step.\n',
               'Type "what is...(rest of your question)" to get a Google search for your general query.\n',
               'Type "how to...(rest of your question)" to open a link to a YouTube search on your question.\n',
               'Type "how long" to get the amount of time the step takes. \n',
               'Type "help" to show these options again. \n',
               'Type "ingredients" to get a list of ingredients and their measurements. \n',
               'Type "make vegetarian" or "make non-vegetarian" to get a list of vegetarian or non-vegetarian ingredients/substitutions and their measurements, respectively. \n',
               'Type "make step vegetarian" or "make step non-vegetarian" to get a vegetarian or non-vegetarian version of the current step, respectively. \n',
               'Type "make healthy" or "make unhealthy" to get a list of healthy or non-healthy ingredients/substitutions and their measurements, respectively. \n',
               'Type "make step healthy" or "make step unhealthy" to get a healthy or non-healthy version of the current step, respectively. \n'
               'Type "double step" or "half step" to double or half the quantities in the current step, respectively. \n',
               'Type "double ingredients" or "half ingredients" to double or half the quantities of all the ingredients, respectively. \n',
               'Type "cuisine" to modify your recipe into Italian Style. \n',
               'Type "exit" to exit program. \n']
    o = ''.join(options)
    print(o)
    while(boo):
        if prev == curr:
            query= input('How else can I help? \n')
            step = list(recipe[curr].keys())[0]
        else:
            step = list(recipe[curr].keys())[0]
            print(f'Step {curr+1}: ' + step)
            query = input('Please enter a command. \n')
        prev = curr
        if query == 'next':
            if curr==(len(recipe)-1):
                print('This is the end of the recipe. Please enter another command.')
            else:
                curr+=1
        elif query == 'back':
            if curr==0:
                print('This is the beginning of the recipe. Please enter another command.')
            else:
                curr-=1
        elif query.isnumeric():
            if(int(query)>len(recipe) or int(query)<1):
                print('Invalid step number. Please enter a valid step number.')
            else:
                curr = int(query)-1
        elif query == 'repeat':
            curr += 0
            print(f'Step {curr+1}: ' + step)
        elif query == 'how':
            if(len(recipe[curr][step]['ingredients'])) and (len(recipe[curr][step]['cooking words'])):
                if(len(recipe[curr][step]['ingredients'])):
                    ings = '+'.join(recipe[curr][step]['ingredients'])
                word = recipe[curr][step]['cooking words']
                search = f'how+to+{word}+{ings}'
                webbrowser.open(f'https://www.youtube.com/results?search_query={search}')
            else:
                quer = '+'.join(list(recipe[curr].keys())[0].split())
                webbrowser.open(f'https://www.youtube.com/results?search_query=how+to+{quer}')
        elif query == 'tools':
            print(recipe[curr][step]['utensils'])
        elif query == 'what temperature':
            temp = recipe[curr][step]['temperature']
            if(temp):
                print(temp)
            else:
                print('Sorry the current step does not have any temperature related tasks.')
        elif query.startswith('what is'):
            q = '+'.join(query.split())
            webbrowser.open(f'https://www.google.com/search?q={q}')
        elif query.startswith('how to'):
            q = '+'.join(query.split())
            webbrowser.open(f'https://www.youtube.com/results?search_query={q}')
        elif query == 'help':
            print(o)
        elif query == 'ingredients':
            print(ingredients_dict)
        elif query == 'make vegetarian':
            ingredients_dict=make_veg(ingredients_dict)
            print(ingredients_dict)
        elif query == 'make step vegetarian':
            print(make_veg_step(step))
        elif query == 'make non-vegetarian':
            ingredients_dict=make_non_veg(ingredients_dict)
            print(ingredients_dict)
        elif query == 'make step non-vegetarian':
            print(make_nonveg_step(step))
        elif query == 'make healthy':
            ingredients_dict = make_healthy(ingredients_dict)
            print(ingredients_dict)
        elif query == 'make step healthy':
            print(make_healthy_step(step))
        elif query == 'make unhealthy':
            ingredients_dict = make_unhealthy(ingredients_dict)
            print(ingredients_dict)
        elif query == 'make step unhealthy':
            print(make_unhealthy_step(step))
        elif query == 'double step':
            print(double_step(step))
        elif query == 'double ingredients':
            ingredients_dict = double_ings(ingredients_dict)
            print(ingredients_dict)
        elif query == 'half step':
            print(half_step(step))
        elif query == 'half ingredients':
            ingredients_dict = half_ings(ingredients_dict)
            print(ingredients_dict)
        elif query == 'cuisine':
            sub=cuisine_sub(ingredients_dict)
            ingredients_dict= sub[1]
            print(ingredients_dict)
            print('The following substitions were made:\n')
            for change in sub[0]:
                print(change,end='\n')
        elif query not in hard_coded :
            query = query.lower()
            if 'how long' in query:
                sol=None
                doc = nlp(step)
                prev= False
                for i in doc:
                    if i.pos_ == 'NUM':
                        prev=i.text
                    if prev:
                        if 'minute' in i.text or 'hour'in i.text:
                            sol = prev + ' ' + i.text
                            prev= False
                if sol is not None:
                    print(sol)
                else:
                    print('Sorry, I am unable to help with this')
            elif 'how much' in query:
                found= False
                found_ing = None
                for ing in recipe[curr][step]['ingredients']:
                    if ing in query and ing in step.lower() and not found:
                        found=True
                        found_ing = ing
                        new_step = step.replace(",", "")
                        spl = new_step.split()
                        ans = []
                        bool = False
                        try:
                            ind = spl.index(ing)
                            for i in reversed(range(ind)):
                                new_spl = spl[i].replace("/", "")
                                if new_spl.isnumeric():
                                    ans.append(spl[i])
                                    bool = True
                                    break
                                else:
                                    ans.append(spl[i])
                        except:
                            print('Sorry I cannot help with that')
                if(found and (not bool)):
                    if found_ing in ingredients_dict.keys():
                        print(ingredients_dict[found_ing])
                    else:
                        for mat in ingredients_dict.keys():
                            if found_ing in mat :
                              print(ingredients_dict[mat])
                elif(bool):
                    print(' '.join(ans))
                else:
                    print('Sorry the ingredient is not in this step.')
            else:
                print('Incorrect command. Please enter a valid command.')
        elif query == 'exit':
            print('Goodbye!')
            boo = False
        else:
            print('Incorrect command. Please enter a valid command.')

main()

#DEMO
#Vegetarian: https://www.allrecipes.com/recipe/24074/alysias-basic-meat-lasagna/
#Non-Vegetarian: https://www.allrecipes.com/recipe/244716/shirataki-meatless-meat-pad-thai/
#Healthy: https://www.allrecipes.com/recipe/16167/beef-bourguignon-i/
#Unhealthy: https://www.allrecipes.com/recipe/228285/teriyaki-salmon/
#Cuisine (Italian) Transformation:
#       https://www.allrecipes.com/recipe/229293/korean-saewoo-bokkeumbap-shrimp-fried-rice/
#       https://www.allrecipes.com/recipe/73303/mexican-rice-iii/
#One more recipe to best show transformations: https://www.allrecipes.com/recipe/212721/indian-chicken-curry-murgh-kari/
#List of queries:
        # next,back,repeat - move pointer for current step
        # any integer within 1 and the number of steps: jumps to that step
        # how - YouTube search on how to perform current step
        # tools- list of tools
        # what temperature - temperature of current step
        # what is ... - Google search of query
        # how to ... - YouTube search of query
        # how long- amount of time of the step if listed in the step
        # help - list of options
        # ingredients - dictionary of ingredients, their amounts, and any descriptors
        #               format - {ing: ['amount', 'descriptor']}
        # make (vegetarian/non-vegetarian/healthy/unhealthy) - returns dictionary of transformed version of recipe ingredients
        # make step (vegetarian/non-vegetarian/healthy/unhealthy) - returns transformed version of current step
        # (double/half) step - returns current step with modified quantitites
        # (double/half) ingredients - returns dictionary of ingredients with modified quantities
        # cuisine - returns dictionary of Italian version of recipe ingredients
        # exit - exits the program


