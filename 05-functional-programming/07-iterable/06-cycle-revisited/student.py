def cycle(values):
    # If values is an iterator, we need to make a copy
    values = list(values)
    while True:
        for value in values:
            yield value
