from math import factorial
from collections import Counter
from itertools import permutations

def count_permutations(word: str) -> int:
   
    letter_counts = Counter(word)
    
    total_permutations = factorial(len(word))
    
    for count in letter_counts.values():
        total_permutations //= factorial(count)
    
    return total_permutations

def generate_permutations(word: str) -> list:
    perm_set = set(permutations(word))
    
    perm_list = [''.join(p) for p in perm_set]
    
    return perm_list

if __name__ == "__main__":
    word = "abc"
    print(f"Number of permutations for '{word}': {count_permutations(word)}")
    permutations_list = generate_permutations(word)
    print(f"Permutations for '{word}': {permutations_list}")