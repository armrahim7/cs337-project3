skip_words = ['degree', 'degrees', 'degree.', 'degrees.', 'degree,', 'degrees,',
              'minute', 'minutes','minute.', 'minutes.', 'minute,', 'minutes,', 
              'hour', 'hours', 'hour.', 'hours.', 'hour,', 'hours,', 
              'seconds', 'seconds.', 'seconds,',
              'days', 'day','days.', 'day.','days,', 'day,',
              'to', 'or']
def double_ings(ings):
    ingredients = dict()
    for i in ings.keys():
        if ings[i][0] == 'to taste':
            ingredients[i] = ings[i]
        else:
            amount = ings[i][0].split()
            num = float(amount[0])*2
            if(len(amount)>1):
                new_amount = str(num) + ' ' + amount[1]
            else:
                new_amount = str(num)
            new_val = [new_amount, ings[i][1]]
            ingredients[i] = new_val
    return ingredients
def double_step(step):
    split_step = step.split()
    for ind, i in enumerate(split_step):
        try:
            num = float(i)*2
            if split_step[ind+1] not in skip_words:
                split_step[ind] = str(num)
        except:
            pass
    return ' '.join(split_step)

def half_ings(ings):
    ingredients = dict()
    for i in ings.keys():
        if ings[i][0] == 'to taste':
            ingredients[i] = ings[i]
        else:
            amount = ings[i][0].split()
            num = float(amount[0])/2
            if(len(amount)>1):
                new_amount = str(num) + ' ' + amount[1]
            else:
                new_amount = str(num)
            new_val = [new_amount, ings[i][1]]
            ingredients[i] = new_val
    return ingredients
def half_step(step):
    split_step = step.split()
    for ind, i in enumerate(split_step):
        try:
            num = float(i)/2
            if split_step[ind+1] not in skip_words:
                split_step[ind] = str(num)
        except:
            pass
    return ' '.join(split_step)


print(half_step('Heat remaining 2 tablespoons oil in the same skillet. Add chopped onions; cook and stir until just tender, about 2 to 3 minutes. Stir in reserved onions and carrots from the marinade; mix well, then use a slotted spoon to transfer vegetables into the bowl with beef.'))