import re
from collections import defaultdict

def file_manipulation(file_path):
    word_counts = defaultdict(int)
    
    with open(file_path, 'r') as file:
        for line in file:
            line = re.sub(r'[^\w\s]', '', line).upper()
            words = line.split()
            
            for word in words:
                word_counts[word] += 1
    
    sorted_word_counts = dict(sorted(word_counts.items()))

    for word, count in sorted_word_counts.items():
        print(f"{word}: {count}")

file_path = input("Enter the target file path here:  ")
file_manipulation(file_path)
