import copy

veg = {
    'beef' : 'tofu',
    'steak' : 'seitan',
    'pork' : 'tofu',
    'fish' : 'tofu',
    'ham' : 'tofurkey',
    'turkey': 'tofurkey',
    'bacon' : 'tempeh',
    'chicken' : 'tofu',
    'sausage' : 'soyrizo',
    'hot dog' : 'soyrizo'
}
non_veg = {v: k for k, v in veg.items()}
ing = {'olive oil': '0.25 cups', 'onion': '1 large', 'thyme leaf': '2 teaspoons', 'sage': '1 teaspoon', 'Kosher salt and ground black pepper': 'to taste', 'garlic': '2 cloves', 'tomato paste': '1 tablespoon', 'Worcestershire sauce': '3 tablespoons', 'panko breadcrumbs': '0.75 cups', 'chicken broth': '0.5 cups', 'ground turkey': '3 pounds', 'eggs': '2 large', 'ketchup': '0.5 cups'}
def make_veg(ings):
    ingredients = dict(ings)
    changed_keys = []
    new_keys = []
    for i in ingredients.keys():
        if 'broth' in i:
            new_keys.append(('vegetable broth', ingredients[i]))
            changed_keys.append(i)
        else:
            for j in veg.keys():
                if (j in i) and ('broth' not in i):
                    new_key = i.replace(j, veg[j])
                    new_keys.append((new_key, ingredients[i]))
                    changed_keys.append(i)
    for n in new_keys:
        ingredients[n[0]] = n[1]
    for k in changed_keys:
        del ingredients[k]
    return ingredients
def make_veg_step(step):
    step_copy = copy.copy(step)
    for i in veg.keys():
        if i in step_copy:
            step_copy = step_copy.replace(i, veg[i])
    return step_copy
            
def make_non_veg(ings):
    ingredients = dict(ings)
    changed_keys = []
    new_keys = []
    for i in ingredients.keys():
        if 'broth' in i:
            new_keys.append(('chicken broth', ingredients[i]))
            changed_keys.append(i)
        else:
            for j in non_veg.keys():
                if (j in i) and ('broth' not in i):
                    new_key = i.replace(j, non_veg[j])
                    new_keys.append((new_key, ingredients[i]))
                    changed_keys.append(i)
    for n in new_keys:
        ingredients[n[0]] = n[1]
    for k in changed_keys:
        del ingredients[k]
    return ingredients
def make_nonveg_step(step):
    step_copy = copy.copy(step)
    for i in non_veg.keys():
        if i in step_copy:
            step_copy = step_copy.replace(i, non_veg[i])
    return step_copy
# print(make_veg(ing))
# print(non_veg)