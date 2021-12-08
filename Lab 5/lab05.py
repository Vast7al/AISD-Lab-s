# Wskazówki
# Elementy bez dzieci nazywane są liścmi
# Najwyższy węzeł jest korzeniem dziecka
# In order - przejście poprzeczne
# 1.Odwiedzanie rozpoczynamy od skrajnie lewego liścia, następnie kierujemy się do rodzica i do jego prawego dziecka.
# 2.Następnie kierujemy się do rodzica o 2 poziomy wyżej i powtarzamy powyższy schemat.
# Post order - przejście wsteczne
# 1.Odwiedzanie rozpoczynamy od skrajnie lewego liścia, następnie kierujemy się do prawego sąsiada i do ich wspólnego rodzica.
# 2.Następnie kierujemy się do lewego liścia sąsiedniego węzła na tym samym poziomie i powtarzamy powyższy schemat.
# Pre order - przejście wzdłużne
# 1.Odwiedzanie rozpoczynamy od wyznaczonego węzła (np. korzenia) i odwiedzamy jego lewe dziecko, a następnie lewe dziecko poziom niżej.
# 2.Po dotarciu do liścia odwiedzamy jego sąsiedni (prawy) węzeł. Schemat powtarzamy dla prawego dziecka korzenia.
# pip install binarytree
from typing import Any
from binarytree import Node


class BinaryNode:
    def __init__(self, value: Any, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def is_leaf(BinaryNode):  # Ocenia, czy wartość jednego węzla jak i drugiego jest rowna None, wtedy w zaleznosci od tego czy dany wezel jest lisciem czy nie, zwroci falsz lub prawde
        if BinaryNode.value == None:
            print("Brak wartości")
        if(BinaryNode.left == None and BinaryNode.right == None):
            return False
        else:
            return True

    # Metoda upewnia się, czy podanej wartości już nie ma w drzewie, jeśli jej nie ma, to zastąp self.left podaną wartością(dodaj nową wartość w skrocie)
    def add_left_child(self, value: Any):
        if (value == self.value):
            print("Wartości w drzewie nie mogą się powtarzać")
        else:
            self.left = BinaryNode(value)

    # tutaj analogicznie co dla powyższej funkcji, tylko zamiast left, mamy self.right
    def add_right_child(self, value: Any):
        if (value == self.value):
            print("Wartości w drzewie nie mogą się powtarzać")
        else:
            self.right = BinaryNode(value)

    def traverse_in_order(self):
        if (self.left != None):  # 1.jeżeli bieżący węzeł ma lewe dziecko, to wykonaj na nim metodę in_order
            self.left.traverse_in_order()

        print(self.value)  # 2.odwiedź bieżący węzeł #czyli print

        if (self.right != None):  # 3.jeżeli bieżący węzeł ma prawe dziecko, to wykonaj na nim metodę in_order
            self.right.traverse_in_order()

    def traverse_post_order(self):

        if (self.left != None):  # 1.jeżeli bieżący węzeł ma lewe dziecko, to wykonaj na nim metodę post_order
            self.left.traverse_post_order()
        if (self.right != None):  # 2.jeżeli bieżący węzeł ma prawe dziecko, to wykonaj na nim metodę post_order
            self.right.traverse_post_order()

        print(self.value)  # 3.odwiedź bieżący węzeł #czyli print

    def traverse_pre_order(self):
        print(self.value)  # 1.odwiedź bieżący węzeł #print jak wczesniej

        if (self.left != None):  # 2.jeżeli bieżący węzeł ma lewe dziecko, to wykonaj na nim metodę pre_order
            self.left.traverse_pre_order()
        if (self.right != None):  # 3.jeżeli bieżący węzeł ma prawe dziecko, to wykonaj na nim metodę pre_order
            self.right.traverse_pre_order()
    # Potrzebne, bez tego rowniez dziala, ale wysypuje na starcie adres pamięci

    def __str__(self):
        return str(self.value)


class BinaryTree:
    def __init__(self, root):
        self.root = BinaryNode(root)
    # Początkowo, musimy się upewnić czy do argumentu wrzucamy BinaryNode czy BinaryTree, potem wykonujemy mniej więcej podobną rzecz co w "in order" w BinaryNode,
    # tylko dla BinaryTree wrzucamy .root

    def traverse_in_order(self):
        if (self == BinaryNode):
            if (self.left != None):
                BinaryTree.traverse_in_order(self.left)
            print(self.value)
            if (self.right != None):
                BinaryTree.traverse_in_order(self.right)
        if (self == BinaryTree):
            if (self.root.left != None):
                BinaryTree.traverse_in_order(self.root.left)
            print(self.root.value)
            if (self.root.right != None):
                BinaryTree.traverse_in_order(self.root.right)
    # Tutaj analogicznie co wyzej, tylko ze printa wrzucamy w inne miejsca w celu odwiedzenia danego węzla w innej kolejności niz wczesniej.

    def traverse_post_order(self):
        if (self == BinaryNode):
            if (self.left != None):
                BinaryTree.traverse_post_order(self.left)

            if (self.right != None):
                BinaryTree.traverse_post_order(self.right)
            print(self.value)
        if (self == BinaryTree):
            if (self.root.left != None):
                BinaryTree.traverse_post_order(self.root.left)

            if (self.root.right != None):
                BinaryTree.traverse_post_order(self.root.right)
            print(self.root.value)
    # Dziala to tak samo jak w komentarzu wyzej, po prostu nasze "odwiedzenie węzla" dzieje się w innym miejscu, juz na samym początku.

    def traverse_pre_order(self):
        if (self == BinaryNode):
            print(self.value)
            if (self.left != None):
                BinaryTree.traverse_pre_order(self.left)

            if (self.right != None):
                BinaryTree.traverse_pre_order(self.right)
        if (self == BinaryTree):
            print(self.root.value)
            if (self.root.left != None):
                BinaryTree.traverse_pre_order(self.root.left)

            if (self.root.right != None):
                BinaryTree.traverse_pre_order(self.root.right)

# Opisana ponizej funkcja, przypisuje sobie listę z funkcji tree_list, do naszej listy w funkcji, potem w warunkach uwzględniane jest to,
# czy podany sum_value jest rowny, czy mniejszy od wartości korzenia (do kazdego warunku inny komentarz), potem przeszukujemy listę i jeśli
# suma naszych wartości w liscie jest równa podanej sumie w argumencie funkcji, to zwróć wartości


def all_equal_paths(tree: BinaryTree, sum_value: Any):
    lista = tree_list(tree.root)
    if (sum_value < tree.root.value):
        print("Podana wartość jest mniejsza od korzenia")
    if (sum_value == tree.root.value):
        print("Wartość podana jest taka sama jak korzenia, czyli", sum_value)
    for x in range(len(lista)):
        if(sum(lista[x]) == sum_value):
            print(lista[x])

# Tutaj funkcja posiada początkowy warunek, ktory określa czy dane drzewo w ogole ma jakiekolwiek wartosci (wtedy po prostu zwraca tree.value),
# idąc dalej, jeśli tree.left ma jakieś wartości (czyli nie jest None) to rozszerz listę o wartości znajdujące się w calym tree.left(rekurencyjnie)
# analogicznie to samo w przypadku tree.right, na sam koniec zwracamy gotową listę, potrzebną do metody all_equal_paths


def tree_list(tree):
    lista = []
    if (tree.left == None or tree.right == None):
        return [[tree.value]]
    if (tree.left != None):
        lista.extend([tree.value] + x for x in tree_list(tree.left))
    if (tree.right != None):
        lista.extend([tree.value] + x for x in tree_list(tree.right))
    return lista

# sprawdzenie funkcji all_equal_paths
#bt = BinaryTree(1)
# bt.root.add_right_child(3)
# bt.root.add_left_child(2)
# bt.root.left.add_right_child(5)
# bt.root.left.add_left_child(7)
# bt.root.right.add_left_child(6)
# bt.root.right.add_right_child(7)
#all_equal_paths(bt, 10)
# sprawdzenie traversali w drzewie
# binary=BinaryNode(10)
# tree=BinaryTree(binary)
# tree.root.add_left_child(9)
# tree.root.add_right_child(2)
# tree.root.left.add_left_child(1)
# tree.root.left.add_right_child(3)
# tree.root.right.add_left_child(4)
# tree.root.right.add_right_child(6)
# tree.root.traverse_pre_order()
# Sprawdzenie warunków
#tree = BinaryTree(10)
#assert tree.root.value == 10
# tree.root.add_right_child(2)
#assert tree.root.right.value == 2
#assert tree.root.right.is_leaf() is False
# tree.root.add_left_child(2)
# tree.root.left.add_left_child(1)
#assert tree.root.left.is_leaf() is True
# rysowanie drzewa
#root = Node(1)
#root.left = Node(2)
#root.right = Node(3)
#root.left.right = Node(5)
# root.left.left=Node(7)
# root.right.left=Node(6)
# root.right.right=Node(7)
# print(root)
