import utils
import sorts

bookshelf = utils.load_books('books_small.csv')
bookshelf_v1 = bookshelf.copy()
bookshelf_v2 = bookshelf.copy()
long_bookshelf = utils.load_books('books_large.csv')
long_bookshelf_v2 = long_bookshelf.copy()

# for title in bookshelf:
#   print(title)

# print(ord("a"))
# print(ord(" "))
# print(ord("A"))

# Comparision functions
def by_title_ascending(book_a, book_b):
  return book_a['title_lower'] > book_b['title_lower']

def by_author_ascending(book_a, book_b):
  return book_a['author_lower'] > book_b['author_lower']

def by_total_length(book_a, book_b):
  return (len(book_a['author_lower']) + len(book_a['title_lower'])) > (len(book_b['author_lower']) + len(book_b['title_lower']))

# First sorting
# sort_1 = sorts.bubble_sort(bookshelf_v1, by_title_ascending)
# for book in sort_1:
#   print(book)
#   print("")

# Second sorting
# sort_2 = sorts.bubble_sort(bookshelf_v1, by_author_ascending)
# for book in sort_2:
#   print(book)
#   print("")

# Third sorting
# sorts.quicksort(bookshelf_v2, 0, len(bookshelf_v2) - 1, by_author_ascending)
# for book in bookshelf_v2:
#   print(book)
#   print("")

# Fourth sorting
# sort_4= sorts.bubble_sort(long_bookshelf, by_total_length)
# for book in sort_4:
#   print(book)
#   print("")

# Fifth sorting
# sorts.quicksort(long_bookshelf_v2, 0, len(long_bookshelf_v2) - 1, by_total_length)
# for book in long_bookshelf_v2:
#   print(book)
#   print("")