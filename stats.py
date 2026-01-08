def get_word_count(book_text):   
        words = book_text.split()
        counter = 0
        for word in words:  
                counter += 1
        return f"Found {counter} total words"

def get_character_counts(book_text):
	char_set = set(book_text.lower())
	char_counts = {}
	for char in char_set:
		counter =  0
		for next_char in book_text:
			if next_char.lower() == char:
				counter += 1
		char_counts[char] = counter
	return char_counts

def sort_character_counts(char_dict):
	desc_char_dict = {char: num for char, num in sorted(char_dict.items(), key=lambda item: item[1], reverse=True)}
	return desc_char_dict
	
