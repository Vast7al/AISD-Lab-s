#Elementy w stosie są układane jeden na drugim, co oznacza że nowa wartośc znajdzie się na końcu kolejki. 
#Przy usuwaniu "zdejmowany" jest ostatni element kolejki, czyli ten który jest obecnie "na szczycie".
from typing import Any
from ListaJednokierunkowa import LinkedList


class Stack:
    def __init__(self):
        # skrzynia, z ktorej mozna wyciągnąć metody uzyte w przypadku list jednokierunkowych
        self.methodsChest = LinkedList()
    # metoda len użyta z listy jednokierunkowej
    def __len__(self):
        return len(self.methodsChest) #zwroc metodę len ze skrzyni methodsChest, ktora przechowuje metody z listy jednokierunkowej(LinkedList)
    # metoda print
    def printed(self):
        temporaryPrinted=self.methodsChest
        for x in range(len(temporaryPrinted)):#wykorzystuje metode len, ktora leci po calej dlugosci x-sa
         print(str(temporaryPrinted.node(x).value)) #tutaj ma wypisac wszystkie wartosci z metody node,pod ktora sa podstawiane po kolei wartosci iksa i z dopiskiem
                                                    #.value, zeby przedstawic wartosc a nie adresy w pamięci
    def push(self, element: Any):
        value=element #wartosc podanego elementu w push
        temporaryPush=self.methodsChest
        temporaryPush.push(value)  #tutaj analogicznie, wykorzystana zostala metoda push z LinkedList + nie trzeba nic zmieniac bo w przypadku push,ostatni element
                                   #bedzie tym tzw. top_value czyli ostatnim elementem
    def pop(self):
        popValue=self.methodsChest.pop()
        while (self.methodsChest.head != None): #konieczna jest pętla, poniewaz pop w domyslnym zamysle, ma usunac pierwszy element, a nie ostatni
            #wiec dopoki nasz self.head nie bedzie juz wskazywac na nic, to niech zwroci ostatni element na liscie(head na koncu)
            return popValue


#stack = Stack()
#assert len(stack) == 0
#stack.push(3)
#stack.push(10)
#stack.push(1)
#stack.push(4)
#assert len(stack) == 4
#top_value = stack.pop()
#assert top_value == 4
#stack.printed()