import requests

# Sending GET request to API to fetch books data
response = requests.get("http://127.0.0.1:5000/books")
# Parsing the response as JSON
books = response.json()

if books:
    # Printing each book's details in the specified format
    for book in books:
        print(f"Book Id: {book['id']}, Book title: {book['title']}, Book author: {book['author']}")
else:
    # Printing error message if failed to fetch books data
    print("Failed to fetch books from API")