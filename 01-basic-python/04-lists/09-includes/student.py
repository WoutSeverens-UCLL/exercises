# Write your code here
def includes(xs, ys):
    for j in ys:
        if j not in xs:
            return False
    return True