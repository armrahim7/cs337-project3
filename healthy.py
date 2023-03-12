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
# ing = {'Burgundy wine': ['3 cups', ''], 'onions': ['2 ', 'chopped'], 'carrots': ['2 ', 'chopped'], 'brandy': ['2 tablespoons', ''], 'garlic': ['2 cloves', 'crushed'], 'black peppercorns': ['10 ', 'whole'], 'salt': ['1 teaspoon', ''], 'parsley': ['1 sprig', 'fresh'], 'bay leaf': ['1 ', ''], 'beef chuck roast': ['2 pounds', 'cubed'], 'olive oil': ['4 tablespoons', 'divided'], 'bacon': ['0.25 pounds', 'cubed'], 'all-purpose flour': ['3 tablespoons', ''], 'tomato paste': ['1 tablespoon', ''], 'beef broth': ['1 can', '(10.5 ounce)'], 'salt and pepper': ['to taste', 'to taste'], 'butter': ['4 tablespoons', ''], 'mushrooms': ['1 pound', ['fresh', 'sliced']]}
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
