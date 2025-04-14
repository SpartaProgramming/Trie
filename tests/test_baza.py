import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) #dodaj katalog do ścieżki gdzie python szuka modułów

import unittest
from trie.trie import Trie

def Test_Bazy(plik):
    """Dodaje bazę do drzewa i zwraca czas wykonania operacji"""
    baza = open(plik,"r") #baza haseł
    hasla=[]
    lines = baza.readlines()

    for line in lines:
        line_cut = line.strip()
        hasla.append(line_cut)

    start_time = time.time()
    Drzewo = Trie()
    for h in hasla:
        Drzewo.add_children(Drzewo.root,h)
    algorithm_time = time.time() - start_time

    print(f"Czas wczytywania bazy {plik}: {algorithm_time}") 
    #Drzewo.print_trie()
    return Drzewo,hasla

def szukanie_slowa_trie(Drzewo, slowo):
    start_time = time.time()
    if Drzewo.check_if_in_trie(Drzewo.root,slowo):
        print("Znaleziono")
    else:
        print("Nie znaleziono")
    algorithm_time = time.time() - start_time
    print(f"Czas szukania: {algorithm_time}") 
    
def szukanie_slowa_lista(baza, slowo):  
    start_time = time.time()
    if slowo in baza:
        print("Znaleziono")
    else:
        print("Nie znaleziono")
    algorithm_time = time.time() - start_time
    print(f"Czas szukania: {algorithm_time}") 

if __name__ == '__main__': 
    [d1,hasla1]=Test_Bazy("s1.txt")
    [d2,hasla2]=Test_Bazy("s2.txt")
    # [d3,hasla3]=Test_Bazy("s3.txt")

    # slowo = "pterichthyodes"
    # szukanie_slowa_lista(hasla3,slowo)
    # szukanie_slowa_trie(d3,slowo)

    slowo = "writer"
    szukanie_slowa_lista(hasla2,slowo)
    szukanie_slowa_trie(d2,slowo)

  
