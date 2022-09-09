def count_word(phrase):
    return len(phrase.split(' '))


while (phrase := input('Entrez une phrase: ')) != 'q':
    print(f'La phrase contient {count_word(phrase)} mots')


