from stats import get_num_words, count_characters, chars_to_sorted_list
import sys

def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    
    with open(path) as file:
        file_contents = file.read()

        word_count = get_num_words(file_contents)
        
        char_counts = count_characters(file_contents)
        
        sorted_chars = chars_to_sorted_list(char_counts)

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {path}...")
        print("----------- Word Count ----------")
        print(f"Found {word_count} total words")
        print("--------- Character Count -------")
        
        for char_data in sorted_chars:
            char = char_data["char"]
            count = char_data["num"]
            if char.isalpha():  # Only print alphabetical characters
                print(f"{char}: {count}")
            
        print("============= END ===============")

if __name__ == "__main__":
    main()