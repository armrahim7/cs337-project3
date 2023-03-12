import copy
healthy = {
    'bacon' : 'sun-dried tomatoes',
    'butter' : 'canola oil',
    'white rice' : 'brown rice',
    'ricotta cheese': 'cottage cheese',
    'heavy cream': 'coconut cream',
    'brown sugar': 'white sugar',
    'beef' : 'chicken',
}
unhealthy = {
    'sesame oil' : 'butter',
    'canola oil' : 'butter',
    'olive oil' : 'butter',
    'vegetable oil' : 'butter',
    'mustard oil' : 'butter',
    'peanut oil' : 'butter',
    'sugar': 'corn syrup',
    'milk' : 'heavy cream',
    'brown rice' : 'white rice',
    'whole wheat bread' : 'white bread',
    'salmon' : 'beef',
    'chicken' : 'beef',
    'turkey bacon': 'bacon'
    #remove words 'whole grain', 'whole wheat', 'fat free', 'lowfat', 'low fat', 'sugar-free', 'sugar free', 'low sugar'
}
remove_words = ['whole grain', 'whole wheat', 'fat free', 'lowfat', 'low fat', 'sugar-free', 'sugar free', 'low sugar']
# ing = {'Burgundy wine': ['3 cups', ''], 'onions': ['2 ', 'chopped'], 'carrots': ['2 ', 'chopped'], 'brandy': ['2 tablespoons', ''], 'garlic': ['2 cloves', 'crushed'], 'black peppercorns': ['10 ', 'whole'], 'salt': ['1 teaspoon', ''], 'parsley': ['1 sprig', 'fresh'], 'bay leaf': ['1 ', ''], 'beef chuck roast': ['2 pounds', 'cubed'], 'olive oil': ['4 tablespoons', 'divided'], 'bacon': ['0.25 pounds', 'cubed'], 'all-purpose flour': ['3 tablespoons', ''], 'tomato paste': ['1 tablespoon', ''], 'beef broth': ['1 can', '(10.5 ounce)'], 'salt and pepper': ['to taste', 'to taste'], 'butter': ['4 tablespoons', ''], 'mushrooms': ['1 pound', ['fresh', 'sliced']]}
ing = {'sesame oil': ['0.25 cups', ''], 'lemon juice': ['0.25 cups', ''], 'soy sauce': ['0.25 cups', ''], 'brown sugar': ['2 tablespoons', 'or more to taste'], 'sesame seeds': ['1 tablespoon', ''], 'ground mustard': ['1 teaspoon', ''], 'ground ginger': ['1 teaspoon', ''], 'garlic powder': ['0.25 teaspoons', ''], 'salmon steak': ['4 ', '(6 ounce)']}
def make_healthy(ings):
    ingredients = dict(ings)
    changed_keys = []
    new_keys = []
    for i in ingredients.keys():
        for j in healthy.keys():
            if (j in i):
                new_key = i.replace(j, healthy[j])
                new_keys.append((new_key, ingredients[i]))
                changed_keys.append(i)
    for n in new_keys:
        ingredients[n[0]] = n[1]
    for k in changed_keys:
        del ingredients[k]
    return ingredients
def make_healthy_step(step):
    step_copy = copy.copy(step)
    for i in healthy.keys():
        if i in step_copy:
            step_copy = step_copy.replace(i, healthy[i])
    return step_copy

def make_unhealthy(ings):
    ingredients = dict(ings)
    changed_keys = []
    new_keys = []
    for i in ingredients.keys():
        for k in remove_words:
            if k in i:
                new_key = i.replace(k, '')
                new_keys.append((new_key, ingredients[i]))
                changed_keys.append(i)
        for j in unhealthy.keys():
            if (j in i):
                if 'brown' in i:
                    new_key = i.replace('brown ', '')
                    new_key = new_key.replace(j, unhealthy[j])
                else:
                    new_key = i.replace(j, unhealthy[j])
                new_keys.append((new_key, ingredients[i]))
                changed_keys.append(i)
    for n in new_keys:
        ingredients[n[0]] = n[1]
    for k in changed_keys:
        del ingredients[k]
    return ingredients
def make_unhealthy_step(step):
    step_copy = copy.copy(step)
    for i in unhealthy.keys():
        if (i in step_copy):
            step_copy = step_copy.replace('brown ', '')
            step_copy = step_copy.replace(i, unhealthy[i])
    return step_copy
