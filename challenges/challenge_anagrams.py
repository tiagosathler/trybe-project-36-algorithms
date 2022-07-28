def quick_sort(current: list, start: int, end: int) -> None:
    """
    Ordena em ordem alfabética uma lista de strings de forma recursiva.
    Método 'quick sort' (divisão e conquista)

    Entradas:
    ---------

    current : list[str]
        lista de strings

    start : int
        índice do início da lista

    end: int
        índice do fim da lista

    Saída:
    ------

    None:
        o algoritmo modifica seus próprios argumentos de forma recursiva
    """

    if start < end:
        p = partition(current, start, end)
        quick_sort(current, start, p - 1)
        quick_sort(current, p + 1, end)


def partition(current: list, start: int, end: int) -> int:
    """
    Faz o particionamento da lista (divisão) em fragmento menor
    (dentro da recursividade da chamada) e organiza a posição dos
    elementos da lista em ordem alfabética

    Entradas:
    ---------

    current : list[str]
        a lista de strings

    start : int
        índice do início da lista

    end: int
        índice do fim da lista

    Saída:
    ------

    d : int
        o índice do delimitador

    """
    pivot = current[end]

    d = start - 1

    for i in range(start, end):
        if current[i] <= pivot:
            d += 1
            current[i], current[d] = current[d], current[i]

    current[d + 1], current[end] = current[end], current[d + 1]

    return d + 1


def is_anagram(first_string: str, second_string: str) -> bool:
    """
    Analisa duas palavras se são anagramas uma da outra (case insensitive)

    Entradas:
    ---------

    first_word : string
        primeira string a ser comparada com a segunda

    second_word : string
        segunda string a ser comparada com a primeira

    Saída:
    ------

    True | False:
        a resposta se as duas strings são anagramas entre si
    """

    if len(first_string) != len(second_string):
        return False

    first_list = list(first_string.lower())
    second_list = list(second_string.lower())

    start = 0
    end = len(first_list) - 1

    quick_sort(first_list, start, end)

    quick_sort(second_list, start, end)

    return first_list == second_list
