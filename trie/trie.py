class Node:
    """
    Reprezentuje pojedynczy węzeł drzewa Trie
    :param litera: Znak przechowywany w węźle
    :type litera: str lub none
    """
    def __init__(self,litera):
        self.children = {} # słownik litera:węzeł
        self.value = litera
        self.is_end = False #czy tu konczy się drzewo

    def __str__(self):
        return f"Node: {self.value}, children: {self.children.keys()}"

    def __repr__(self):
        return self.__str__()
    
class Trie:
    """
    Reprezentacja drzewa Trie do przechowywania słów.

    Metody:
        add_children(node, word): dodaje litery słowa do drzewa.
        print_trie(): wypisuje drzewo w formie tekstowej.
        check_if_in_trie(node, word): sprawdza, czy słowo istnieje.
        print_words(): wypisuje wszystkie słowa w drzewie.
    """
    def __init__(self): 
        self.root = Node(None) #inicjalizuj korzeń

    def add_children(self, node, word):
        if not word: 
            node.is_end = True
            return
         
        c=word[0] #pierwsza litera
        rest=word[1:] #końcówka słowa

        for key, value in node.children.items():
            if key == c:
                node = value #ustaw, że teraz to jest nowy węzeł, przechodzimy do węzła z literą
                self.add_children(value,rest)
                return
        
        node.children[c] = Node(c) #na tym poziomie nie ma tej litery, więc ją dodaj jako węzeł
        self.add_children(node.children.get(c),rest) #teraz jak już jest, wejdź do tego węzła i buduj drzewo.

    def _print_node(self,node,poziom):
        for node_child in node.children.values():
            print(" "*poziom + f"->{node_child.value} {'.' if node_child.is_end else ''}")
            self._print_node(node_child,poziom+1)

    def print_trie(self):
       self._print_node(self.root,poziom=0)


    def check_if_in_trie(self,node,word): 
        """
        Sprawdza, czy dane słowo istnieje w drzewie.

        :param node: Węzeł startowy
        :type node: Node
        :param word: Słowo do sprawdzenia
        :type word: str
        :return: True jeśli znaleziono, False w przeciwnym razie
        :rtype: bool
        """

        if not word: 
            if node.is_end == True:
                return True
            else:
                return False
         
        c=word[0] #pierwsza litera
        rest=word[1:] #końcówka

        for key, value in node.children.items():
            if key == c:
                node = value #ustaw, że teraz to jest nowy węzeł, przechodzimy do węzła z literą
                return self.check_if_in_trie(value,rest)
                
        return False


    def _return_all_words(self,node,poziom,prefix):
        """
        Rekurencyjnie wypisuje wszystkie słowa w drzewie.

        :param node: węzeł początkowy
        :param poziom: poziom zagnieżdzenia
        :param prefix: prefiks słowa
        """
        for node_child in node.children.values():
            prefix_t = ""
            prefix_t = prefix + node_child.value
            if node_child.is_end:
                print(prefix_t)
            self._return_all_words(node_child,poziom+1,prefix_t)


    def print_words(self):
        """
        Wypisuje wszystkie słowa zapisane w drzewie.
        """
        self._return_all_words(self.root,prefix="",poziom=0)


if __name__ == "__main__":
    Drzewo = Trie()
    Drzewo.add_children(Drzewo.root,"acbb")
    Drzewo.add_children(Drzewo.root,"avbb") 
    Drzewo.add_children(Drzewo.root,"rvbb") 
    Drzewo.add_children(Drzewo.root,"acbnm") 

    Drzewo.print_trie()
    Drzewo.print_words()
    print(Drzewo.check_if_in_trie(Drzewo.root,"a",))





