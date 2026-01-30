def add_menu(characters, classes, races, items): 
    from menu import menu
    result = menu(["Name", "Class", "Level", "Race", "Attributes", "Skills", "Inventory", "Return without saving"],
    number=[2],
    writable=[0],
    num_min=0,
    num_max=100,
    toggle=[1, 3, 4, 5, 6],
    tog_opts=[["On", "Off"], [[i.get('name', None).title() for i in classes], [1]], [[i.get('name', None) for i in races], [3]], [[i.get('name', None) for i in items], [6]]])   
    selected_index = result['index']
    if selected_index == 7:
        return characters
    else:
        characters.append({"name": ''.join(result['writable'][0]), "class": result['toggles'][1], "level": result['numbers'][2], "race": result['toggles'][3], "attributes": result['toggles'][4], "skills": result['toggles'][5], "inventory": result['toggles'][6], "stats": {"dmg": 0, "dex": 0, "int": 0, "con": 0, "cha": 0}})
        return characters