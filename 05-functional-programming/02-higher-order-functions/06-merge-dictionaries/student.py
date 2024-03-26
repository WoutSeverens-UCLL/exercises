def merge_dictionaries(d1, d2, merge_function):
    result = {}

    for key, value in d1.items():
        result[key] = value

    for key, value in d2.items():
        if key in result:
            result[key] = merge_function(result[key], value)
        else:
            result[key] = value
    
    return result