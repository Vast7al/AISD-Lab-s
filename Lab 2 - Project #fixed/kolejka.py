# Element dodany jako pierwszy zostaje również "zdjęty" jako pierwszy, co można rozumieć przez analogię do kolejki w sklepie.
from typing import Any
from ListaJednokierunkowa import LinkedList
from Stos import Stack


class Queue:
    def __init__(self):
        self.methodsChest = LinkedList()
        self.methodsChest2 = Stack()

    def __str__(self):
        temporaryString = []
        temporaryPrinted = self.methodsChest
        for x in range(len(temporaryPrinted)):
            temporaryString.append(temporaryPrinted.node(x).value)
            variable = ', '.join(temporaryString)
        return("" + (variable) + "")

    def __len__(self):
        return len(self.methodsChest)

    def enqueue(self, element: Any):
        return self.methodsChest.push2(element)

    def dequeue(self):
        return self.methodsChest.pop()

    def peek(self):
        firstElement = self.methodsChest.node(0)
        print(firstElement.value)


queue = Queue()
assert len(queue) == 0
queue.enqueue('klient1')
queue.enqueue('klient2')
queue.enqueue('klient3')
assert str(queue) == 'klient1, klient2, klient3'
client_first = queue.dequeue()
assert client_first == 'klient1'
value = client_first
assert str(queue) == 'klient2, klient3'
assert len(queue) == 2
queue.peek()
print(queue)
