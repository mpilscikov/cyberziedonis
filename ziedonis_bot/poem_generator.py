from ziedonis_bot.poem_reader import (
    get_poems_list,
    remove_new_lines_and_spaces,
)

from random import choice, choices


def get_random_poem():

    poems_list = get_poems_list()
    random_poem = choice(poems_list)

    return random_poem


def get_gibberish_poem(poems_amount):

    from .constants import LINES_IN_GIBBERISH
    
    words = _choose_random_poem_words(poems_amount)
    poem = ''
    
    for i in range(LINES_IN_GIBBERISH-1):
        poem += _generate_giberish_line(words)
    
    else:
        poem += _generate_giberish_line(words, is_last_line=True)

    return poem


def _choose_random_poem_words(poems_amount):

    poems = '\n'.join(
        (
            get_random_poem() 
            for i in range(poems_amount)
        )
    )

    poems = remove_new_lines_and_spaces(poems)
    words = poems.split(' ')

    return words


def _generate_giberish_line(words, is_last_line = False):

    from .constants import (
        WORDS_IN_GIBBERISH_LINE,
        ENDING_SYMBOL_GIBBERISH_LINE,
        ENDING_SYMBOL_GIBBERISH_LINE_LAST,
    )

    ending_symbol = ENDING_SYMBOL_GIBBERISH_LINE_LAST if is_last_line else ENDING_SYMBOL_GIBBERISH_LINE 

    line_content = ' '.join(
        (
            word
            for word in choices(words, k=WORDS_IN_GIBBERISH_LINE)
        )
    )

    line = f'{line_content.lower().capitalize()}{ending_symbol}\n'
    return line
