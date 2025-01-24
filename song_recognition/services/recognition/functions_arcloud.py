import re


def get_value_for_key(dictionary, target_key):
    if isinstance(dictionary, dict):
        for key, value in dictionary.items():
            if key == target_key:
                return value  # Key found, return its value
            if isinstance(value, dict):
                result = get_value_for_key(value, target_key)
                if result is not None:
                    return result  # Key found in a deeper level of the dictionary
    return None  # Key not found in the entire dictionary


def escape_ansi(line):
    ansi_escape = re.compile(r'(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~]')
    return ansi_escape.sub('', line)


def get_all_keys_with_positions(dictionary, parent_key='', separator='_'):
    keys_with_positions = {}

    for key, value in dictionary.items():
        current_key = f"{parent_key}{separator}{key}" if parent_key else key
        if isinstance(value, dict):
            keys_with_positions.update(
                get_all_keys_with_positions(value, current_key, separator))
        else:
            keys_with_positions[current_key] = value

    return keys_with_positions


def generic_items(dict_or_list):
    if type(dict_or_list) is dict:
        return dict_or_list.items()
    if type(dict_or_list) is list:
        return enumerate(dict_or_list)


def get_keys(dictionary):
    result = []
    for key, value in generic_items(dictionary):
        if type(value) is dict or type(value) is list:
            new_keys = get_keys(value)
            result.append(key)
            for innerkey in new_keys:
                result.append(f'{key}/{innerkey}')
        else:
            result.append(key)
    return result
