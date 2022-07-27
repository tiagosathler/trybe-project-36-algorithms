def is_palindrome_iterative(word: str) -> bool:
    """
    Analisa uma palavra se é palíndroma ou não usando um
    algoritmo iterativo.

    Entradas:
    ---------

    word : string
        uma palavra a ser analisada (case insensitive)


    Saída:
    ------

    True | False:
        a resposta se é palíndroma
        False caso a palavra for vazia
    """

    if not word:
        return False

    length_of_word = len(word)
    mid = length_of_word // 2

    for index in range(length_of_word):
        if (index < mid - length_of_word % 2):
            if (word[index] != word[0 - index - 1]):
                return False
        else:
            return True
