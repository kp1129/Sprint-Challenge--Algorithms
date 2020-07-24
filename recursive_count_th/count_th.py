'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # case to rule out
    if len(word) < 2:
        # cannot be the string we're looking for
        return 0
    else:
        # base case
        if word[:2] == "th":
            return 1 + count_th(word[1:])
        else:
            # everything else
            return 0 + count_th(word[1:])
