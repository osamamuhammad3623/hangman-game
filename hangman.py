import random

def replace_with_discovered(word, discovered, guessed_char):
    new_word = ''
    for i in range(0, len(word)):
        if guessed_char == word[i]:
            new_word += guessed_char
        elif discovered[i] != '_':                          # if discovered[i] is already discovered before
            new_word += discovered[i]
        else:
            new_word += '_'
    
    return new_word

def display_with_spaces(some_word):
    for letter in some_word: print(letter , end=' ')
    print('\n')

def count_word_size(word):
    discovered = ''
    for i in range(0, len(word)):
        discovered += '_'
    return discovered

list_of_words = ['sports', 'science', 'integration', 'vision', 'backend'] # you can add words as many as you want!
word = random.choice(list_of_words)
discovered = count_word_size(word)

mistakes = 0
discovered_characters = 0
completed = False

while (completed is False):

    display_with_spaces(discovered)
    guessed = input('Guess a character in the word: ')
    if guessed in word:
        print('Correct guess!')
        discovered = replace_with_discovered(word, discovered, guessed)
        # the counter is not increaed by 1 !
        # the counter is increased by string.count(character) because the word might have the character more than once!
        discovered_characters += word.count(guessed)
        if discovered_characters == len(word):
            print('The word is ' + word)
            completed = True
            print('You\'ve done it!')

    else:
        mistakes +=1
        if mistakes < 3:
            print('Sorry! You have ' + str(3-mistakes) + ' attempts left!')
        else:
            print('Man is dead!')
            break
