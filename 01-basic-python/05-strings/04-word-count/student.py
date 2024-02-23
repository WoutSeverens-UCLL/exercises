# Write your code here
def word_count(string):
    if len(string) != 0:
        return len(string.split(' '))
    return 0 