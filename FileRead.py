import string
def count_words(filename):
    word_count = {}
    with open(filename, 'r') as file:
        text = file.read()
        text = text.lower()
        text = text.translate(str.maketrans('', '', string.punctuation))
        words = text.split()
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1
    for word in sorted(word_count):
        print(f"{word}: {word_count[word]}")

# Example usage
count_words("C:\\Users\\Shashwata\\Downloads\\sample-1.txt")