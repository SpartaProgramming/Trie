import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) #dodaj katalog do ścieżki gdzie python szuka modułów

import unittest
from trie.trie import Trie

class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()
    
    def test_add_word(self):
        """Dodajemy słowo i sprawdzamy czy istnieje"""
        self.trie.add_children(self.trie.root, "abcde")
        self.assertTrue(self.trie.check_if_in_trie(self.trie.root,"abcde"))

    def test_prefix(self):
        """Test że prefiks nie jest całym słowem"""
        self.trie.add_children(self.trie.root, "kotek")
        self.assertFalse(self.trie.check_if_in_trie(self.trie.root, "kot"))

    def test_empty_word(self):
        """Testujemy dodanie pustego słowa"""
        self.trie.add_children(self.trie.root, "")
        self.assertTrue(self.trie.root.is_end)
    
if __name__ == '__main__': 
    #unittest.main()

    suite = unittest.TestLoader().loadTestsFromTestCase(TestTrie)
    unittest.TextTestRunner().run(suite)

