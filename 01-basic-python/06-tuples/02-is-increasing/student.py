# Write your code here
def is_increasing(ns):
    ms = ns[1:]
    pair = (list(zip(ns, ms)))
    for (i, j) in pair:
            if i > j:
                return False
    return True

print(is_increasing([1,2,3]))