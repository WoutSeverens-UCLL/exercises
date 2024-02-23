# Write your code here
def odd_keys_dict(dictionary):
    return {
        k: v
        for k, v in dictionary.items()
        if k % 2 != 0
    }