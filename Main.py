list_of_needs = set(['iron', 'wood', 'plastic'])
factory1 = set(['table', 'chair', 'wood'])
factory2 = set(['iron', 'copper', 'glass', 'wood', 'plastic'])
factory3 = set(['plastic', 'lamp', 'ink', 'glass'])
def searching_for_items(needs, *a):
    counter = 0
    for i in a:
        counter += 1
        if needs.issubset(i):
            return "factory number",counter,"has all the needed items"
    return "of the factories had the needed items"
print(searching_for_items(list_of_needs, factory1, factory2, factory3))
