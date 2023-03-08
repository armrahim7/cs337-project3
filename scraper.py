from bs4 import BeautifulSoup as bs
import requests
from recipe_scrapers import scrape_me
def scrape(url):
    recipe_steps = []
    ingredient_list = []
    page = requests.get(url)
    soup = bs(page.content, 'html.parser')
    recipe = soup.find_all("ol", {"class": "comp mntl-sc-block-group--OL mntl-sc-block mntl-sc-block-startgroup"})[0]
    steps = recipe.find_all("li",{"class": "comp mntl-sc-block-group--LI mntl-sc-block mntl-sc-block-startgroup"})
    ingredients = soup.find_all("ul", {"class": "mntl-structured-ingredients__list"})
    for ing in ingredients:
        ingredient_list.append(ing.text.rstrip().split('\n'))
    ingredient_list = [i.strip() for i in ingredient_list[0] if i]
    for step in steps:
        recipe_steps.append(step.p.text.rstrip()[1:])
    final = []
    for r in recipe_steps:
        if '. ' in r:
            r_split = r.split('. ')
            for j in r_split:
                final.append(j)
        else:
            final.append(r)
    return (final, ingredient_list)
def cooking_words():
    cook_words = []
    page = requests.get("https://diannej.com/2013/100-action-verbs-from-julia-child-recipes/")
    soup = bs(page.content, 'html.parser')
    lst = soup.find_all("div", {"class":"entry-content"})[0]
    # print(lst)
    word_lst = lst.find_all("ol")[0]
    words = word_lst.find_all("li")
    for w in words:
        cook_words.append(w.text.lower())
    cook_words.extend(['add', 'bake', 'place', 'microwave', 'defrost', 
    'thaw', 'refrigerate', 'freeze', 'chill', 'heat', 'cook', 'dice','preheat', 'pound','dip','layer'])
    with(open('cook_words.txt', 'w')) as f:
        for i in cook_words:
            f.write(i + '\n')

# print(scrape("https://www.allrecipes.com/recipe/223042/chicken-parmesan/"))
#cooking_words()
# print(scrape_me("https://www.allrecipes.com/recipe/223042/chicken-parmesan/").instructions_list())

    