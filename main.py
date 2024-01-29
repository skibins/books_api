from flask import Flask, jsonify
import requests

app = Flask(__name__)


def get_books_from_openlibrary_api():
    # URL for fetching books data from OpenLibrary API
    url = "https://openlibrary.org/subjects/fiction.json?limit=10"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        books = []
        for doc in data.get('works', []):
            # Extracting authors' names from the response
            authors = [author['name'] for author in doc.get('authors', [])]
            book = {
                'title': doc.get('title', ''),
                'author': ', '.join(authors),
                'id': doc.get('key', '').split('/')[-1]
            }
            books.append(book)
        return books
    else:
        return None


@app.route('/books', methods=['GET'])
def get_books():
    # Fetching books from OpenLibrary API
    books = get_books_from_openlibrary_api()
    if books:
        # Returning books data as JSON response
        return jsonify(books)
    else:
        # Returning error message if failed to fetch books
        return jsonify({"message": "Failed to fetch books from OpenLibrary API"}), 500


if __name__ == '__main__':
    # Running the Flask application
    app.run(debug=True)
