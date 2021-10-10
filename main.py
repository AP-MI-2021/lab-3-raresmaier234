def print_menu():
    print("2. Determinarea celei mai lungi secvente cu proprietatea ca numerele sunt divizibile cu k.")
    print("3. Determinarea celei mai lungi secvente cu proprietatea ca numerele sunt in progresie aritmetica.")
    print("4. Iesire")


def citire_date():
    """
    :return: lista citita
    """
    l = []
    n = int(input("Dati numarul de numere: "))
    for x in range(n):
        l.append(int(input("l[" + str(x) + "]=")))
    return l


def element_div_k(ls, k):
    """
    :param ls: lista de nr intregi
    :param k: valoarea cu care x trebuie sa fie divizibil
    :return: False daca un nr nu este div cu k, altfel va returna True
    """
    for x in ls:
        if x % k != 0:
            return False
    return True


def arithmetic_progression(lst):
    """
    :param lst: reprezinta lista citita
    :return: daca True daca o subscventa este progresie aritmetica
    """
    if(len(lst)>1):
        ratia = lst[1]-lst[0]
    for x in range(2, len(lst)):
        if lst[x] - lst[x-1] != ratia:
            return False
    return True


def get_longest_arithmetic_progression(lst):
    """
    :param lst: reprezinta lista citita
    :return: cea mai lunga subsecventa a unei progresii aritmetice
    """
    lista = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if arithmetic_progression(lst[i:j+1]) and len(lista) < len(lst[i:j+1]):
                lista = lst[i:j+1]
    return lista


def test_get_longest_arithmetic_progression():
    assert get_longest_arithmetic_progression([2, 2, 2, 3, 4]) == [2, 2, 2]
    assert get_longest_arithmetic_progression([1, 1, 2]) == [1, 1]
    assert get_longest_arithmetic_progression([2, 3, 4, 5, 7]) == [2, 3, 4, 5]


def get_longest_div_k(lst, k):
    """
    :param lst: reprezinta lista de nr intregi
    :param k: reprezinta valoarea cu care fiecare element din lista trebuie sa fie divizibila
    :return: va returna lista conform cerintei 1.
    """
    subsecventa = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if element_div_k(lst[i:j + 1], k) and len(subsecventa) < len(lst[i:j + 1]):
                subsecventa = lst[i:j + 1]
    return subsecventa


def test_get_longest_div_k():
    assert get_longest_div_k([2, 4, 6, 7], 2) == [2, 4, 6]
    assert get_longest_div_k([1, 2, 3, 4], 1) == [1, 2, 3, 4]
    assert get_longest_div_k([2, 2, 3, 6, 9], 3) == [3, 6, 9]


def main():
    while True:
        print("1. Citire date.")
        print_menu()
        optiune = input("Alegeti optiunea: ")
        if optiune == '1':
            sir = citire_date()
            print_menu()
            optiune = input("Alegeti optiunea: ")
            if optiune == '2':
                k = int(input("Dati valoarea lui k: "))
                print(f"Subsecventa maxima este: {get_longest_div_k(sir, k)}")
            elif optiune == '3':
                print(f"Subscventa maxima este: {get_longest_arithmetic_progression(sir)}")
            elif optiune == '4':
                return False
        elif optiune == '4':
            return False


test_get_longest_div_k()
test_get_longest_arithmetic_progression()


if __name__ == "__main__":
    main()
