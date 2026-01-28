import os
import msvcrt



def menu(options, **mod):
    number = mod.get('number', [])
    writable = mod.get('writable', [])
    toggle = mod.get('toggle', [])
    default_TF = mod.get('default_vals', [])
    num_min = mod.get('num_min', None)
    num_max = mod.get('num_max', None)
    tog_opts = mod.get('tog_opts', [[True, False]])
    states = {i: 0 for i in toggle} 
    text_data = {i: [] for i in writable}
    index = 0
    num = {}
    for i in number:
        num[i] = 1
    tog = {}
    
    toggle_options_map = {}
    default_opts = [True, False]
    specified_indices = set()
    
    for item in tog_opts:
        if isinstance(item, list) and len(item) == 2 and isinstance(item[1], list):
            toggle_options_map[tuple(item[1])] = item[0]
            specified_indices.update(item[1])
        elif isinstance(item, list):
            default_opts = item
    
    for i in toggle:
        found = False
        for indices, opts in toggle_options_map.items():
            if i in indices:
                tog[i] = opts[0]
                found = True
                break
        if not found:
            tog[i] = default_opts[0]
    
    while True:
        os.system('cls')
        for i, option in enumerate(options):
            prefix = "> " if i == index else "  " 
            if i in writable:
                print(f"{prefix}{option}: {''.join(text_data[i])}")
            elif i in toggle:
                print(f"{prefix}{option}: {tog[i]}")
            elif i in number:
                print(f"{prefix}{option} <{num[i]}>")
            else:
                print(f"{prefix}{option}")

        key = msvcrt.getch()

        if key in (b'\x00', b'\xe0'):
            key = msvcrt.getch()
            if key == b'H': 
                index = (index - 1) % len(options)
            elif key == b'P':
                index = (index + 1) % len(options)
            elif key == b"K":
                if index in number:
                    if num_min is None or num[index] > num_min:
                        num[index] -= 1
                elif index in toggle:
                    current_opts = default_opts
                    for indices, opts in toggle_options_map.items():
                        if index in indices:
                            current_opts = opts
                            break
                    current_pos = current_opts.index(tog[index])
                    tog[index] = current_opts[(current_pos - 1) % len(current_opts)]
            elif key == b"M":
                if index in number:
                    if num_max is None or num[index] < num_max:
                        num[index] += 1
                elif index in toggle:
                    current_opts = default_opts
                    for indices, opts in toggle_options_map.items():
                        if index in indices:
                            current_opts = opts
                            break
                    current_pos = current_opts.index(tog[index])
                    tog[index] = current_opts[(current_pos + 1) % len(current_opts)]
        elif key == b'\r':
            if index in writable:
                return {'index': index, 'numbers': num, 'toggles': tog, 'writable': text_data}
            elif index in toggle:
                states[index] *= -1
            else:
                return {'index': index, 'numbers': num, 'toggles': tog, 'writable': text_data}
        elif key == b'\b':
            if index in writable and text_data[index]:
                text_data[index].pop()
        else:
            if index in writable:
                try:
                    text_data[index].append(key.decode('utf-8'))
                except:
                    pass

"""
MENU FUNCTION ATTRIBUTES GUIDE:

options: List of menu option names (required)
    Example: ["Option 1", "Option 2", "Option 3"]

number: List of indices that should be numeric inputs (arrows change value)
    Example: number=[0, 2] makes options at index 0 and 2 numeric

writable: List of indices that should be text inputs (type to enter text)
    Example: writable=[1] makes option at index 1 a text field

toggle: List of indices that should be toggle options (arrows cycle through values)
    Example: toggle=[2, 3] makes options at index 2 and 3 toggleable

num_min: Minimum value for numeric inputs (optional)
    Example: num_min=1 prevents numbers from going below 1

num_max: Maximum value for numeric inputs (optional)
    Example: num_max=100 prevents numbers from going above 100

tog_opts: Custom toggle options (defaults to [True, False])
    Format 1 - All toggles use same options: 
        tog_opts=[["Easy", "Medium", "Hard"]]
    Format 2 - Specific toggles use specific options:
        tog_opts=[["On", "Off"], [["Low", "Medium", "High"], [0, 2]]]
        This means: Default is On/Off, but indices 0 and 2 use Low/Medium/High

EXAMPLE CALL WITH ALL ATTRIBUTES:
"""
"""
result = menu(
    ["Player Count", "Player Name", "Difficulty", "Sound", "Music Volume", "Confirm"],
    number=[0, 4],
    writable=[1],
    toggle=[2, 3],
    num_min=1,
    num_max=4,
    tog_opts=[["On", "Off"], [["Easy", "Medium", "Hard"], [2]]]
)

selected_index = result['index']
player_count = result['numbers'][0]
music_volume = result['numbers'][4]
player_name = ''.join(result['writable'][1])
difficulty = result['toggles'][2]
sound = result['toggles'][3]

print(f"Selected: {selected_index}")
print(f"Player Count: {player_count}")
print(f"Player Name: {player_name}")
print(f"Difficulty: {difficulty}")
print(f"Sound: {sound}")
print(f"Music Volume: {music_volume}")

"""
