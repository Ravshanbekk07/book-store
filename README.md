

#               Bookstore RESTful API
        Welcome to the FreeBooks RESTful API project! This API is designed to provide a seamless experience for managing and accessing information related to authors, categories, books, customers, orders, and likes. The project focuses on offering free books and incorporates essential features such as user authentication, including login and signup. Built using Python, Django, and Django REST Framework, this API empowers developers to perform CRUD operations on various models.

#               Table of Contents
       1 Features
       2 Installation
       3 Database Design
       4 Authentication
       5 Endpoints
       6 Usage
      
#                Features
        CRUD Operations:

        Create, Read, Update, and Delete functionality for the following models:
                Authors
                Categories
                Books
                Customers
                Orders
                Likes

#              Authentication:

        Secure your API with basic authentication.
        Allow users to sign up and log in to access personalized features.

#              Free Books:

        Provide information and management capabilities for free books.

#               Installation

        1. Clone the repository:
        https://github.com/Ravshanbekk07/book-store.git
        2. Install Dependencies:
        cd book-store
        pip install -r requirements.txt
        3.Apply Database Migrations:
        python manage.py migrate
        4. Run the Development Server:
        python manage.py runserver
        

        Access the API at http://localhost:8000/.

#               Database Design

        The project follows a well-structured database design with models for authors, categories, books, customers, orders, and likes. Relationships between models are clearly defined using Django's ORM.

#                Authentication

        Secure your API with basic authentication, ensuring only authorized users can perform certain operations. User-friendly signup and login functionality are provided.

#                Endpoints

        Explore a variety of endpoints to perform CRUD operations on different models:

                * /authors/: CRUD operations for authors.
                * /categories/: CRUD operations for categories.
                * /books/: CRUD operations for books.
                * /customers/: CRUD operations for customers.
                * /orders/: CRUD operations for orders.
                * /likes/: CRUD operations for likes.
       For detailed documentation on each endpoint, refer to the API documentation.

#                Usage


        To interact with the API, use the provided authentication mechanism. Examples and guidelines can be found in the detailed API documentation.
