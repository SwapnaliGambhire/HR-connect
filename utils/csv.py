# function for dict value in list format

def add_value(dict_obj, key, value):
    if key not in dict_obj:
        dict_obj[key] = value
    elif isinstance(dict_obj[key], list):
        dict_obj[key].append(value)

    else:
        dict_obj[key] = [dict_obj[key], value]
