def count_word(phrase):
    '''fonction qui prend une phrase et return le nombre de mots'''
    return len(phrase.split(' ')) #diviser la phrase en mots separees par des espaces, et ensuite compter le nombre de mots 

quit = False #d'abord, l'utilisateur ne veut pas quitter
while not quit: #repeter jusqu'a l'utilisateur veut quitter
    phrase = input("Entrez une phrase: ")
    if phrase == 'q': #utilisateur veut quitter
        quit = True
    else:
        print(f'La phrase contient {count_word(phrase)} mots') #print le nombre de mots 


