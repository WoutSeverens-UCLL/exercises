# Write your code here
def remove_duplicates(xs):
    found = set()
    result = []

    for x in xs: 
        if x not in found:
            result.append(x)
            found.add(x)
    return result

print(remove_duplicates([1,1,2,3,5,9,9]))