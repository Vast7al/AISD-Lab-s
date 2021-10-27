# Element dodany jako pierwszy zostaje również "zdjęty" jako pierwszy, co można rozumieć przez analogię do kolejki w sklepie.
from typing import Any
from ListaJednokierunkowa import LinkedList
from Stos import Stack


class Queue:
    def __init__(self):
        self.methodsChest = LinkedList()
        self.methodsChest2 = Stack()

    def printed(self):
        temporaryString = []
        string = ''
        temporaryPrinted = self.methodsChest
        for x in range(len(temporaryPrinted)):
            temporaryString.append(temporaryPrinted.node(x).value)
            variable = ', '.join(temporaryString[::-1])
        print("'" + (variable) + "'")

    def __len__(self):
        return len(self.storageChest)

    def enqueue(self, element: Any):
        (self.methodsChest.push(element))


queue = Queue()
queue.enqueue('klient1')
queue.enqueue('klient2')
queue.enqueue('klient3')
#assert str(queue) == 'klient1, klient2, klient3'
queue.printed()
