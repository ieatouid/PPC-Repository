
import sys
from collections import Counter

# Function to count the vowels in a text file
def count_vowels(file_path):

    vowels = "aeiou"

    try:
        # Open and read the text file
        with open(file_path, 'r') as file:
            text = file.read().lower()

        # Count how frequently each vowel appears
        counts = Counter(char for char in text if char in vowels)

        return counts

    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        sys.exit(1)


# Main program
if __name__ == "__main__":

    # Check that a file path was supplied
    if len(sys.argv) != 2:
        print("Usage: python3 frequency.py <file_path>")
        sys.exit(1)

    # Get the file path from the command line
    file_path = sys.argv[1]

    # Calculate and display vowel frequency
    result = count_vowels(file_path)

    print(result)

