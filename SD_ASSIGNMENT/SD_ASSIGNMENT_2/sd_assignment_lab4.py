#initiate a list of books
books = ["Physics", "Bangla", "English", "Chemistry"]
print(books)
#add a book to the list
books.append("Mathematics")
print(books)
#search a book in the list
def search_book(book_list, book_name):
    if book_name in book_list:
        return f"'{book_name}' is in the collection."
    else:
        return f"'{book_name}' is not in the collection."
print(search_book(books, "Physics"))
print(search_book(books, "Biology"))
#display all books in the list
print(books)
# initiate a dictionary to map member IDs to member details
members = {
    1: {"name": "Amjad", "age": 23},
    2: {"name": "Hossain", "age": 24},
    3: {"name": "Evan", "age": 25}
}
# function to get member details by ID
def get_member_details(member_id):
    return members.get(member_id, "Member not found")

# function to add a new member
def add_member(member_id, name, age):
    if member_id in members:
        return "Member ID already exists."
    else:
        members[member_id] = {"name": name, "age": age}
        return "Member added successfully."
# function to search for a member by name
def search_member_by_name(name):
    for member_id, details in members.items():
        if details["name"] == name:
            return f"Member found: ID={member_id}, Name={name}, Age={details['age']}"
    return "Member not found."
# function to display all members
def display_all_members():
    return members
print(add_member(4, "XYZ", 30))
print(search_member_by_name("Evan"))
print(display_all_members())
# initiate a tuple to represent book information (ID, title, author)
book_info = (
    (1, "Physics", "Author A"),
    (2, "Bangla", "Author B"),
    (3, "English", "Author C"),
    (4, "Chemistry", "Author D")
)

# function to search for a book by title in the tuple
def search_book_in_tuple(title):
    for book in book_info:
        if book[1] == title:
            return f"Book found: ID={book[0]}, Title={title}, Author={book[2]}"
    return "Book not found."

# function to display all books in the tuple
def display_all_books_in_tuple():
    return book_info

# Example usage
print(search_book_in_tuple("Physics"))
print(display_all_books_in_tuple())
