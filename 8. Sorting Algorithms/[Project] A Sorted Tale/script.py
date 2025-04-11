import utils
import sorts

# Load the bookshelf
bookshelf = utils.load_books('books_small.csv')

# Step 1 - Print all book titles
print("Initial Titles:")
for book in bookshelf:
    print(book['title'])

# Step 2 - Unicode testing
print("Code point of 'a':", ord("a"))
print("Code point of ' ':", ord(" "))
print("Code point of 'A':", ord("A"))

# Step 6 - Comparison functions
def by_title_ascending(book_a, book_b):
    return book_a['title_lower'] > book_b['title_lower']

def by_author_ascending(book_a, book_b):
    return book_a['author_lower'] > book_b['author_lower']

# Step 7 - Sort by title
print("\nSorting by title:")
sort1 = sorts.bubble_sort(bookshelf, by_title_ascending)
for book in sort1:
    print(book['title'])

# Step 9 - Copy bookshelf properly
import copy
bookshelf_v1 = copy.deepcopy(bookshelf)

# Step 10 - Sort by author
print("\nSorting by author:")
sort2 = sorts.bubble_sort(bookshelf_v1, by_author_ascending)
for book in sort2:
    print(book['author'])

# Step 16 - Sort by Length
def by_total_length(book_a,book_b):
    return len(book_a['author_lower']) + len(book_a['title_lower']) > len(book_b['author_lower']) + len(book_b['title_lower'])


bookshelf_v2=copy.deepcopy(bookshelf)
print("----------------")
print("Book Shelf Version 02")
sorts.quicksort(bookshelf_v2, 0, len(bookshelf_v2) - 1, by_author_ascending)
print(bookshelf_v2)


x = utils.load_books('books_large.csv')

print('Bubble Sort --- Books_large.csv')
# sort_book_large = sorts.bubble_sort(x,by_total_length)
# print(sort_book_large)

sorts.quicksort(x,0,len(x)-1,by_total_length)
print(x)




