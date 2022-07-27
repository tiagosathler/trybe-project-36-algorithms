def merge_sort(
        first_list: list[str],
        second_list: list[str],
        start: int,
        end: int) -> None:
    """
    Ordena em ordem alfabética duas listas de strings de mesmo tamanho
    de forma recursiva. Método 'merge sort' (divisão e conquista)

    Entradas:
    ---------

    first_list : list[str]
        primeira lista de strings

    second_list : list[str]
        segunda lista de strings

    start : int
        índice do início da lista

    end: int
        índice do fim da lista

    Saída:
    ------

        o algoritmo modifica as listas de entrada de forma recursiva
    """

    if end - start > 1:
        mid = (start + end) // 2
        merge_sort(first_list, second_list, start, mid)
        merge_sort(first_list, second_list, mid, end)
        merge(first_list, second_list, start, mid, end)


def comparisons(
                current_list: list[str],
                left_part: str,
                right_part: str,
                index: int,
                left_index: int,
                right_index: int) -> dict:
    """
    Compara a lista atual de strings com suas partes esquerda e direita

    Entradas:
    ---------

    current_list : list[str]
        lista atual de string a ser comparada

    left_part : list[str]
        parte esquerda da lista da lista comparada

    right_part : list[str]
        parte direita da lista da lista comparada

    index: int
        índice atual da comparação

    left_index: int
        índice atual da parte esquerda

    right_index: int
        índice atual da parte direita

    Saída:
    ------

    dicionário : dict

        "current_list": a lista atual atualizada
        "left_index": o índice atualizado da parte esquerda da lista
        "right_index": o índice atualizado da parte direita da lista
    """

    len_of_left_part = len(left_part)
    len_of_right_part = len(right_part)

    if left_index >= len_of_left_part:
        current_list[index] = right_part[right_index]
        right_index += 1

    elif right_index >= len_of_right_part:
        current_list[index] = left_part[left_index]
        left_index += 1

    elif left_part[left_index] < right_part[right_index]:
        current_list[index] = left_part[left_index]
        left_index += 1

    else:
        current_list[index] = right_part[right_index]
        right_index += 1

    return {
        "current_list": current_list,
        "left_index": left_index,
        "right_index": right_index,
    }


def merge(
        first_list: list[str],
        second_list: list[str],
        start: int,
        mid: int,
        end: int) -> None:
    """
    Faz a mesclagem das listas de string dentro da recursividade do método

    Entradas:
    ---------

    first_list : list[str]
        primeira lista de strings

    second_list : list[str]
        segunda lista de strings

    start : int
        índice do início da lista

    mid : int
        índice do meio da lista

    end: int
        índice do fim da lista

    Saída:
    ------
        o algoritmo modifica as listas de entrada de forma recursiva

    """

    left_first_list = first_list[start:mid]
    right_first_list = first_list[mid:end]

    left_second_list = second_list[start:mid]
    right_second_list = second_list[mid:end]

    left_first_list_idx, right_first_list_idx = 0, 0
    left_second_list_idx, right_second_list_idx = 0, 0

    for general_index in range(start, end):
        first_result = comparisons(
            first_list,
            left_first_list,
            right_first_list,
            general_index,
            left_first_list_idx,
            right_first_list_idx)
        first_list = first_result["current_list"]
        left_first_list_idx = first_result["left_index"]
        right_first_list_idx = first_result["right_index"]

        second_result = comparisons(
            second_list,
            left_second_list,
            right_second_list,
            general_index,
            left_second_list_idx,
            right_second_list_idx)
        second_list = second_result["current_list"]
        left_second_list_idx = second_result["left_index"]
        right_second_list_idx = second_result["right_index"]


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
    end = len(first_list)

    merge_sort(first_list, second_list, start, end)

    return first_list == second_list
