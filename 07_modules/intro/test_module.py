print('Jestem w pliku test!!!!')

months = ['jan', 'feb', 'mar', 'apr']

def find_longest_word(sequence):
    """Finds the longest element in a sequence"""
    longest_word = ''
    for word in sequence:
        if len(word) > len(longest_word):
            longest_word = word

    return longest_word

def find_shortest_word(sequence):
    """Finds the longest element in a sequence"""
    shortest_word = ''
    for word in sequence:
        if len(word) < len(shortest_word):
            shortest_word = word

    return shortest_word