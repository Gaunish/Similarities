from nltk.tokenize import sent_tokenize

def lines(a, b):
    """Return lines in both a and b"""

    result = []
    for line in a.split("\n"):
        if line in b.split("\n"):
            if line != "":
                result.append(line)

    return result

def sentences(a, b):
    """Return sentences in both a and b"""

    result = []
    sent_a = sent_tokenize(a)
    sent_b = sent_tokenize(b)

    for line in sent_a:
        if line in sent_b:
            if line !='' and line.strip() not in result:
                result.append(line.strip())


    return result


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""

    a = a.split(" ")
    result = []
    #splits 1 text into a list whose elements are single words
    for word in a:
        listofsubs = find_substrings(word.strip(":;,."), n)
        for sub in listofsubs:
            if b.find(sub) != -1:
                if sub not in result:
                   result.append(sub)

    return result

def find_substrings(a, n):
    """Return list of substrings of length n"""
    result = []
    i = 0
    while (i + n) < len(a) + 1:
        result.append(a[i:i+n])
        i += 1
    return result