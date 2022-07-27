def is_palindrome_recursive(
        word: str, low_index: int, high_index: int) -> bool:
    """
    Analisa uma palavra se é palíndroma ou não usando um
    algoritmo recursivo. A análise é feita entre comparando-se
    o caractere nos índices 'low_index' e 'high_index'

    Entradas:
    ---------

    word : string
        uma palavra a ser analisada (case insensitive)

    low_index: int
        índice inferior para análise da string de 'word'

    high_index: int
        índice superior para análise da string de 'word'

    Saída:
    ------

    True | False:
        a resposta se é palíndroma
        ou False caso a palavra for vazia

    Exemplo:
        word = "SOCOS"

        (low_index, high_index)

        (0, 4) => 'S' == 'S' ? -> True
        (1, 3) => 'O' == 'O' and is_palindrome_recursive(word, 0, 4)
        (2, 2) => 'C == 'C' and is_palindrome_recursive(word, 1, 3)
    """
    if len(word) == 0:
        return False

    if 0 <= high_index - low_index <= 1:
        return word[low_index].casefold() == word[high_index].casefold()

    else:
        return (
            word[low_index].casefold() == word[high_index].casefold()
            and
            is_palindrome_recursive(word, low_index + 1, high_index - 1))
