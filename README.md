<h1>Book API</h1>
    <h2>Overview:</h2>
    <p>
        This project consists of two Python scripts, <strong>main.py</strong> and <strong>show_books.py</strong>, that collaborate to create a straightforward Book API. Utilizing Flask, a micro web framework for Python, the API interacts with an external service, the OpenLibrary API, to retrieve book data.
    </p>
    <h2>Functionalities:</h2>
    <ul>
        <li><strong>main.py:</strong> This script establishes a Flask web server, exposing an endpoint (/books), to retrieve information about the first 10 books from the external OpenLibrary API. It utilizes the OpenLibrary API to fetch data about fiction books and returns this data in JSON format upon receiving a GET request.</li>
        <li><strong>show_books.py:</strong> This script sends a GET request to the /books endpoint of the Flask server and displays the retrieved book information in a formatted manner.</li>
    </ul>
    <h2>Input:</h2>
    <ul>
        <li><strong>main.py:</strong> This script expects a GET request sent to the /books endpoint of the Flask server.</li>
        <li><strong>show_books.py:</strong> No input is required for this script. It sends a GET request to the /books endpoint of the Flask server to fetch book information.</li>
    </ul>
    <h2>Output:</h2>
    <ul>
        <li><strong>main.py:</strong> Generates a JSON response containing information about the first 10 fiction books obtained from the OpenLibrary API.</li>
        <li><strong>show_books.py:</strong> Prints the book information retrieved from the Flask server in a formatted manner.</li>
    </ul>
    <h2>Endpoints:</h2>
    <ul>
        <li><strong>/books:</strong> This endpoint of the Flask server retrieves information about the first 10 books from the external OpenLibrary API. Upon receiving a GET request, it fetches data from the OpenLibrary API and returns it in JSON format.</li>
    </ul>
    <h2>URL to Access the API:</h2>
    <p>The Flask server runs locally on the machine at <a href="http://127.0.0.1:5000">http://127.0.0.1:5000</a>.</p> 
    <p>To access the API, send a GET request to <a href="http://127.0.0.1:5000/books">http://127.0.0.1:5000/books</a>.</p>
    <h2>Dependencies:</h2>
    <ul>
        <li>Flask: <code>pip install Flask</code></li>
        <li>Requests: <code>pip install requests</code></li>
    </ul>
    <h2>Usage:</h2>
    <ol>
        <li>Start the Flask server by running <strong>main.py</strong>.</li>
        <li>Send a GET request to the Flask server using <strong>show_books.py</strong> to display book information.</li>
    </ol>
    <p><strong>Note:</strong> Ensure that the Flask server (<strong>main.py</strong>) is running before sending a request using <strong>show_books.py</strong>.</p>
    <p>This project provides a simple example of building and consuming a RESTful API using Python and Flask.</p>
