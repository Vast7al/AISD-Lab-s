# Lista jednokierunkowa jest sekwencją połączonych ze sobą węzłów. Każdy z nich zawiera wartość (data lub value) oraz wskaźnik do następnego elementu (next).
# Wskaźnikiem do pierwszege elementu listy jest head, a wskaźnikiem do ostatniego elementu jest tail.
from typing import Any


class Node:
    def __init__(self, value: Any):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node

    def push(self, value: Any):  # przypisujemy nową wartość wezla do nodePush,potem nasz nastepny wezel ma miec wartosc heada(czyli ma byc tym pierwszym wezlem)
        # a sam head ma wartosc node'a
        nodePush = Node(value)
        nodePush.next = self.head
        self.head = nodePush

    def push2(self, value: Any):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def append(self, value: Any):
        node = Node(value)
        temporary = self.head
        if (temporary == None):  # dopoki nasz head nie wskazuje na jakikolwiek wezel, to oznacza ze nasza lista nie ma zadnych wartosci
            print("Podana lista jest pusta")
        else:
            # 1.dopoki head.next na cos wskazuje, to zamieniaj wartosc heada na head.next,a potem head.next zamien na wartosc node'a
            while(temporary.next is not None):
                # 2.inaczej tlumaczac, dopoki next w headzie wskazuje na jakas wartosc, to head bedzie wskazywal na nastepnego i nastepnego node'a,
                # dopoki nie bedzie mial na co wskazywac,a potem juz tylko podmien wartosc samego heada.next na dodawanego node'a
                temporary = temporary.next
        temporary.next = node

    def node(self, at: int):
        index = at
        temporary = self.head
        if(at >= 0):  # nasza wpisywana wartosc ma byc wieksza,badz rowna 0 (nie mozemy wskazac ujemnego indeksa, bo po prostu takich nie ma)
            # np w zasiegu liczby 2, ma podmieniac wartosc heada na head.next(czyli na nastepny wezel), jesli petla sie skonczy
            for x in range(index):
                # to ma zwrocic nam wartosc szukanego wezla
                temporary = temporary.next
        elif (at < 0):
            print("Podany indeks jest ponizej 0")
        return temporary

    def insert(self, value: Any, after: Node):
        # nodeInsert.next ma wskazywac na następna wartość po podanym wezle w parametrze,a potem ma zamienic wartosc z wezla next,
        # na podany przez nas wezel
        nodeInsert = Node(value)
        nodeInsert.next = after.next
        after.next = nodeInsert

    def pop(self):
        string = "Usuniety pierwszy element z listy -> "
        temporaryPop = self.head
        value = temporaryPop.value
        # W skrocie, nasza petla ma sie zatrzymac w momencie, dopoki self.head nie jest rowne None(czyli na pierwszej wartosci)
        while(temporaryPop is not None):
            # jest sie zatrzyma, to nasz node ma miec wartosc nastepnego node'a (next.node)
            self.head = temporaryPop.next
            return temporaryPop.value  # bez .value zwroci nam jedynie adres pamięci
        print(string+str(value))

    def remove_last(self):
        string = "Usuniety ostatni element z listy -> "
        temporaryLast = self.head
        # tutaj w zasadzie analogicznie co w pop, tylko ze warunek jest taki, ze dopoki self.head.next nie wskazuje na none
        while(temporaryLast.next != None):
            # czyli nie dochodzi do ostatniej wartosci, to ma wskazywac na coraz dalsze wezly,az nie dojdzie do ostatniego
            # i nie zmieni jego wartosci na None, a samą wartość usunietego wezla przechowuje zmienna wynik.
            headValue = temporaryLast
            wynik = headValue.next  # do wyswietlenia/zwrocenia wyniku wyrzuconego elementu
            temporaryLast = temporaryLast.next
        headValue.next = None
        print(string+str(wynik.value))
        return(wynik.value)

    def remove(self, after: Node):
        temporaryRemove = self.head
        # w skrocie, dopoki nasz head nie jest wskazanym node'm, head ma wskazywac na coraz to nastepne wartosci
        if (temporaryRemove is not after):
            # jak juz wskaze na naszą wartosc w parametrze, to zamienia wartosc heada na tą we wskazanym parametrze, a potem podmienia wartosc samego node'a
            # na node'a o kolejke dalej
            temporaryRemove = temporaryRemove.next
        temporaryRemove = temporaryRemove.next
        after.next = temporaryRemove.next
        return temporaryRemove
    # funkcja print

    def __str__(self):
        printNode = self.head
        printed = ""  # potrzebny nam po to, aby zmiescic cale wyrazenie w cudzyslowie
        string = " -> "
        while (printNode is not None):  # dopóki jakikolwiek wezel jest na liscie
            if (printNode.next is not None):
                printed = printed+str(printNode.value)+string
            else:
                printed = printed+str(printNode.value)
            printNode = printNode.next
        return printed
    # funkcja len

    def __len__(self):
        len = 0
        temporaryLen = self.head
        # w skrocie, dopóki head na cokolwiek wskazuje, zmienna len +1 a sam head wskazuje na następną wartość (next)
        while (temporaryLen is not None):
            temporaryLen = temporaryLen.next
            len += 1
        return len


#list_ = LinkedList()
# assert list_.head == None  # ✔
# list_.push(1)
# list_.push(0)
# assert str(list_) == '0 -> 1'  # ✔
# list_.append(9)
# list_.append(10)
# assert str(list_) == '0 -> 1 -> 9 -> 10'  # ✔
#middle_node = list_.node(at=1)
#list_.insert(5, after=middle_node)
#assert str(list_) == '0 -> 1 -> 5 -> 9 -> 10'
#first_element = list_.node(at=0)
#returned_first_element = list_.pop()
#assert first_element.value == returned_first_element
#last_element = list_.node(at=3)
#returned_last_element = list_.remove_last()
#assert last_element.value == returned_last_element
#assert str(list_) == '1 -> 5 -> 9'
#second_node = list_.node(at=1)
# list_.remove(second_node)
#assert str(list_) == '1 -> 5'
