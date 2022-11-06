names = ['chain mail', 'shield', 'helmet',
        'mace', 'sword',
        'pickaxe', 'axe',
        'bread', 'beer',
        'milk', 'meat']

categories = ['Armor', 'Weapon', 'Tool', 'Food', 'Drink']

materials = ['copper', 'iron', 'steel', 'wheat', 'pig']

goods = []

def good_listing(list, material, name):
    list.append(material + ' ' + name)
    return

def good_cycle(list,material_list, good_list):
    if type(material_list) != str:
        for material in material_list:
            for good in good_list:
                good_listing(list, material, good)
    else:
        for good in good_list:
            good_listing(list, material_list, good)

good_cycle(goods, materials[:3], names[:7]) #create armor, weapons, tools
good_cycle(goods, materials[3], names[7:9]) #create wheat goods
good_cycle(goods, materials[4], names[9:11]) #create pig goods

# for good in goods:
#     print(good)

dict_names = {categories[0]:names[:3],
              categories[1]:names[3:5],
              categories[2]:names[5:7],
              categories[3]:[names[7], names[10]],
              categories[4]:[names[8], names[9]]} #[9:11] - works, [9,11] - don't work

# print(dict_names['Food'])
#
# print('bread' in dict_names['Food'])

# dict_material = {categories[0]:materials[:3],
#                  categories[1]:materials[:3],
#                  categories[2]:materials[:3],
#                  categories[3]:materials[7:9],
#                  categories[4]:materials[9:11]}
# material = {'copper':category[:2], 'iron':category[:2], 'steel':category[:2],
#             'wheat':category[3], 'pig':category[4]}

# for element in category.keys():
#     print(element)


