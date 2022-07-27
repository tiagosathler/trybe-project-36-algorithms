def study_schedule(permanence_period: list[tuple], target_time: int) -> int:
    """
    Analisa a quantidade de estudantes que estudam durante o horário alvo
    utilizando um algoritmo de força bruta com complexidade de O(n)

    Entradas:
    ---------

    permanence_period : list[tuple]
        (start: int, end: int):
            tupla com o intervalo de estudo de um um estudante

    target_time: int
        horário alvo objeto com parâmetro de pesquisa da lista

    Saída:
    ------

    count: int
        contagem de estudantes que estudam durante o horário alvo
        ou 'None' caso target_time seja nulo ou se houver alguma tupla inválida
    """
    if target_time is None:
        return None

    count = 0

    for (start, end) in permanence_period:
        if not (isinstance(start, int) and isinstance(end, int)):
            return None
        elif start <= target_time <= end:
            count += 1

    return count
