import re
from collections import Counter

def analyze_text(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()

            # Task 1: Total number of words in the file
            words = text.split()
            total_words = len(words)

            # Task 2: Total number of characters in the file (not including whitespace)
            total_characters = len(re.sub(r'\s', '', text))

            # Task 3: The average word length in the file
            if total_words > 0:
                average_word_length = total_characters / total_words
            else:
                average_word_length = 0

            # Task 4: The frequency of each word in the file
            word_frequency = Counter(words)

            return {
                "Total number of words": total_words,
                "Total number of characters (excluding whitespace)": total_characters,
                "Average word length": average_word_length,
                "Word frequency": word_frequency
            }
    except FileNotFoundError:
        return "File not found"

file_path = "transcript.txt"

analysis_result = analyze_text(file_path)

if isinstance(analysis_result, dict):
    print("Analysis results:")
    for key, value in analysis_result.items():
        if key == "Word frequency":
            print(f"{key}:")
            for word, frequency in value.items():
                print(f"{word}: {frequency}")
        else:
            print(f"{key}: {value}")
else:
    print(analysis_result)





