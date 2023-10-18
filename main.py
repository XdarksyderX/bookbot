def count_words(book_content):
	return len(book_content.split())

def count_letters(book_content):
	result = {}
	for letter in book_content:
		if letter.lower() in result:
			result[letter.lower()] += 1
		else:
			result[letter.lower()] = 1
	return count_letters

def print_report(book_path):
	with open(book_path) as book_content:
		counted_letters = count_letters(book_content)
		words = count_words(book_content)
		print(f"--- Begin report of {book_path} ---")
		print(f"{words} words found in the document\n")
		ordered_letters = list(counted_letters).sort()
		for letter in counted_letters:
			print(f"The '{letter}' character was found {counted_letters[letter]} times")
		print("--- End report ---")

if __name__ == "__main__":
	print_report('books/frankestein.txt')

