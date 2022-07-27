def find_duplicate(nums: list):
    """
    Analisa uma lista não ordenada de inteiros e verifica se há pelo
    menos um repetido

    Entradas:
    ---------

    nums : list[int]
        uma lista de números inteiros não ordenados

    Saída:
    ------

    int | bool
        False:
            se a lista é vazia
            ou se seus itens não são inteiros
            ou se seus itens não inteiros positivos
            ou se não há número em duplicidade

        int: o primeiro número inteiro encontrado em duplicidade
    """

    if not(
        len(nums) > 1
        and
        all([isinstance(number, int) for number in nums])
        and
        all([number >= 0 for number in nums])
    ):
        return False

    nums.sort()

    start = 0
    end = len(nums) - 1

    while start <= end:
        mid = (start + end) // 2
        previous_number = nums[mid-1]
        if nums[mid] == previous_number:
            return previous_number
        if nums[mid] > previous_number:
            start = mid + 1
        else:
            end = mid - 1

    return False
