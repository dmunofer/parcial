def minion_game():

    str= input('Introduce la palabra para jugar: ')
    kevin = 0
    stuart = 0
    vocales = 'AEIOU'

    for e in range((len(str))):
        if str[e] in vocales:
            kevin += (len(str)-e)
        else:
            stuart +=(len(str)-e)

    if stuart > kevin :
        print('Stuart wins with', stuart, 'points')

    elif kevin > stuart:
        print('Kevin wins with', kevin, 'points')

    else:
        print('Draw')
