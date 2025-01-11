disk_capacity_mb = 1.44
pages_per_book = 100
lines_per_page = 50
chars_per_line = 25
bytes_per_char = 4
book_size_bytes = pages_per_book * lines_per_page * chars_per_line * bytes_per_char
disk_capacity_bytes = disk_capacity_mb * 1024 * 1024
number_of_books = disk_capacity_bytes // book_size_bytes
print("Количество книг, помещающихся на дискету:", int(number_of_books))