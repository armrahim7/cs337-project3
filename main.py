from navigator import *
from vegetarian import *
import webbrowser
import re

def main():
    url = input('Enter URL of recipe: ')
    recipe_obj = navigator(url)
    recipe = recipe_obj[0]
    ingredients_dict = recipe_obj[1]
    # print(ingredients_dict)
    # ingredients = []
    hard_coded=['next','back','repeat','how','help','ingredients','exit']
    # for i in ingredients_dict.keys():
    #     ingredients.append(i + ', ' + ingredients_dict[i])
    boo = True
    curr = 0
    prev= None
    options = ['Options: \n',
               'Type "next" to go to next step.\n',
               'Type "back" to go to previous step.\n',
               'Type a number to go to that step. \n',
               'Type "repeat" to repeat current step.\n',
               'Type "how" to open a link to a YouTube search on how to perform current step.\n',
               'Type "what temperature" to get the temperature needed for the current step.\n',
               'Type "what is...(rest of your question)" to get a Google search for your general query.\n',
               'Type "how to...(rest of your question)" to open a link to a YouTube search on your question.\n',
               'Type "help" to show these options again. \n',
               'Type "ingredients" to get a list of ingredients and their measurements. \n',
               'Type "make vegetarian" to get a list of vegetarian ingredients/substitutions and their measurements, as well as the original. \n',
               'Type "make step vegetarian" to get a vegetarian version of the current step. \n'
               'Type "make non-vegetarian" to get a list of non-vegetarian ingredients/substitutions and their measurements, as well as the original. \n',
               'Type "make step non-vegetarian" to get a non-vegetarian version of the current step. \n'
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
            print('Original: ')
            print(ingredients_dict)
            print('Vegetarian: ')
            print(make_veg(ingredients_dict))
        elif query == 'make step vegetarian':
            print(make_veg_step(step))
        elif query == 'make non-vegetarian':
            print('Original: ')
            print(ingredients_dict)
            print('Non-Vegetarian: ')
            print(make_non_veg(ingredients_dict))
        elif query == 'make step non-vegetarian':
            print(make_nonveg_step(step))
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
        elif query == 'exit':
            print('Goodbye!')
            boo = False
        else:
            print('Incorrect command. Please enter a valid command.')

main()

