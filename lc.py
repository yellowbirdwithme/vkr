with open('meden.tok.txt', encoding = 'UTF-8') as ynd:
    with open('meden.tok.lc.txt', 'w', encoding = 'UTF-8') as lc:
        lc.write(ynd.read().lower())
