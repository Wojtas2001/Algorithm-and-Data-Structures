


def possible(u, v, w):

    w_tab = [False]*26
    for i in range(len(u)):
        w_tab[ord(u[i])-ord('a')] = True
    for i in range(len(v)):
        w_tab[ord(v[i])-ord('a')] = True

    for i in range(len(w)):
        if w_tab[ord(w[i])-ord('a')] != True:
            return False

    return True


print(possible('abc', 'def', 'cde'))