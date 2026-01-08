import sys
from stats import get_word_count, get_character_counts, sort_character_counts

def get_book_text(filepath):
	file_contents = ""
	with open(filepath) as f:
		file_contents = f.read()
	return file_contents	


def main():
	try:
		argument = sys.argv[1]
		if not argument:
			print("Usage: python3 main.py <path_to_book>")
			sys.exit(1)
		else:

			book_path = argument
			word_count_str = get_word_count(get_book_text(book_path))
			full_char_dict = sort_character_counts(get_character_counts(get_book_text(book_path)))
	
			print("============ BOOKBOT ============")
			print(f"Analyzing book found at {book_path}...")
			print("----------- Word Count ----------")
			print(word_count_str)
			print("--------- Character Count -------")	
			for char in full_char_dict:
				if char.isalpha():
					print(f"{char}: {full_char_dict.get(char)}")
			print("============= END ===============")	
	except IndexError:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)	


main()
