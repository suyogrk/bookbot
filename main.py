from typing import Optional,List, Dict,Any
from stats import get_num_words, get_num_characters, get_sorted_list
import sys

def get_book_text(filepath: str) -> Optional[str]:
    """
    Reads a file and returns its contents as a string. If the file does not exist or
    an IO error occurs, prints an error message and returns None.

    Parameters:
    filepath (str): Path to the file to read.

    Returns:
    Optional[str]: The contents of the file, or None if an error occurs.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        return None
    except IOError as e:
        print(f"Error reading file: {e}")
        return None


def print_report(book_path: str, total_words: int, sorted_list: List[Dict]) -> None:
    """
    Prints out a report containing the word count and character count for a given book.

    Parameters:
    book_path (str): Path to the book file to analyze.
    total_words (int): Total number of words found in the book.
    sorted_list (List[Dict]): List of dictionaries containing the character count for each character in the book. The dictionaries should contain the keys 'char' and 'num', where 'char' is the character and 'num' is the number of times it appears in the book.

    Returns:
    None
    """
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        print(f"{item['char']}: {item['num']}")

def main(filepath: Optional[str]  =None) -> None:
    """
    Analyzes a book and prints out word count and character count.

    Parameters:
    filepath (str): Path to the book file to analyze.

    Returns:
    None
    """

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    

    # if filepath is None:
    #     filepath = "books/frankenstein.txt"  # Default

    book_text = None
    if filepath is not None:
        book_text = get_book_text(filepath)


    if book_text is None:
        return 
    
    total_words = get_num_words(book_text)
    char_count = get_num_characters(book_text)
    sorted_list = get_sorted_list(char_count)


    print_report(book_path=filepath, total_words=total_words, sorted_list=sorted_list)

    



if __name__ == "__main__":
    main()