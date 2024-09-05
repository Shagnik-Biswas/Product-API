# Product API

The **Product API** is a RESTful API for managing a product catalog. It supports CRUD operations for products, search functionality by name, description, and category, and also calculates a product's popularity score based on sales data. This API is built with Django, pymongo (MongoDB), and supports both synchronous and asynchronous operations.

---

## Table of Contents
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Running Without Docker](#running-without-docker)
  - [Running With Docker](#running-with-docker)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)

---

## Features

- **CRUD operations**: Create, Read, Update, Delete products
- **Search**: Search products by name, description, and category
- **Product Popularity**: Calculate product popularity based on sales data
- **Real-time inventory updates**

---

## Tech Stack

- **Backend**: Django, pymongo (MongoDB)
- **Database**: MongoDB (with cloud cluster)
- **Containerization**: Docker
- **Deployment**: Docker Compose

---

## Getting Started

### Prerequisites

Make sure you have the following installed:
- Python 3.x
- MongoDB Cluster (if running without Docker)
- Docker (optional for containerized setup)
- Docker Compose (optional for containerized setup)

### Running Without Docker

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Shagnik-Biswas/product-api.git
   cd product-api

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt

4. **Set up environment variable**:

   Create a .env file in the root directory and provide the following variables for MongoDB connection:
   
   ```bash
   mongo_username=YOUR_MONGO_USERNAME
   password=YOUR_MONGO_PASSWORD
   cluster=YOUR_CLUSTER
   key=YOUR_KEY
5. **Run the application**:
   ```bash
   python manage.py runserver

 6. Visit the API: Open your browser or Postman and navigate to http://localhost:8000/ to access the API.

### Running With Docker

1. **Clone the repository**:
   
   ```bash
   git clone https://github.com/Shagnik-Biswas/product-api.git
   cd product-api

2. **Build and start the Docker containers**:
   
   ```bash
   docker-compose up --build

3. Access the API: Open your browser or Postman and navigate to http://localhost:8000/ to interact with the API.

## API Endpoints

### Product API

#### **1. Create a Product**
- **Endpoint:** `POST /api/products/`
- **Description:** Creates a new product.
- **Request Body:**
  
  ```json
  {
    "name": "Product Name",
    "description": "Product Description",
    "price": 19.99,
    "inventory_count": 100,
    "category": "Category Name",
    "sales": 0
  }

- **Response:**
  
  ```json
  {
  "message": "Product created",
  "id": "product_id"
}

### 2. Retrieve Products

- **Endpoint:** `GET /api/products/`
- **Description:** Retrieve all products or search by name, description, and category.
- **Query Parameters:**
  - `name` (optional): Filter products by name.
  - `description` (optional): Filter products by description.
  - `category` (optional): Filter products by category.
- **Responses:**
  - **200 OK:**
    
    ```json
    [
      {
        "id": "product_id",
        "name": "string",
        "description": "string",
        "price": "number",
        "inventory_count": "number",
        "category": "string",
        "sales": "number"
      }
    ]
    
### 3. Retrieve a Product by ID

- **Endpoint:** `GET /api/products/{product_id}/`
- **Description:** Retrieve a product by its ID.
- **Responses:**
  - **200 OK:**
    
    ```json
    {
      "id": "product_id",
      "name": "string",
      "description": "string",
      "price": "number",
      "inventory_count": "number",
      "category": "string",
      "sales": "number"
    }
    ```
  - **404 Not Found:**
    
    ```json
    {
      "error": "Product not found"
    }

### 4. Update a Product

- **Endpoint:** `PUT /api/products/{product_id}/`
- **Description:** Update an existing product.
- **Request Body:**
  
  ```json
  {
    "name": "string",
    "description": "string",
    "price": "number",
    "inventory_count": "number",
    "category": "string",
    "sales": "number"
  }

- **200 OK:**
  
    ```json
    {
    "message": "Product updated"
    }
    ```
    - **404 Not Found:**
      
    ```json
    {
      "error": "Product not found"
    }
    ```
  - **404 Not Found:**
    
    ```json
    {
      "error": "Product not found"
    }
    
### 5. Delete a Product

- **Endpoint:** `DELETE /api/products/{product_id}/`
- **Description:** Delete a product by its ID.
- **Responses:**
  - **200 OK:**
    
    ```json
    {
      "message": "Product deleted"
    }
    ```
  - **404 Not Found:**
    
    ```json
    {
      "error": "Product not found"
    }
    
### 6. Calculate Product Popularity

- **Endpoint:** `GET /api/products/{product_id}/popularity/`
- **Description:** Calculate product popularity based on sales.
- **Responses:**
  - **200 OK:**
    
    ```json
    {
      "product_id": "product_id",
      "popularity_score": "number"
    }
    ```
  - **404 Not Found:**
    
    ```json
    {
      "error": "Product not found"
    }
    ```
    
## Contributing

We welcome contributions to improve this project! Here are some ways you can contribute:

### Reporting Issues

If you encounter any issues, please report them by creating a new issue in the repository. Provide as much detail as possible about the problem, including steps to reproduce and any relevant error messages.

### Suggesting Enhancements

If you have ideas for new features or improvements, please suggest them by creating a new issue. Include a detailed description of the enhancement and how it would benefit the project.

### Contributing Code

1. **Fork the Repository**

   Click the "Fork" button on the top-right of the repository page to create your own copy of the repository.

2. **Clone Your Fork**

   ```bash
   git clone https://github.com/yourusername/product-api.git
   cd product-api

3. **Create a New Branch**

   ```bash
   git checkout -b your-branch-name

4. **Make Your Changes**

   Implement your changes in the codebase.
   
5. **Commit Your Changes**

   ```bash
   git add .
   git commit -m "Describe your changes"

6. **Push Your Changes**

   ```bash
   git push origin your-branch-name

7. **Create a Pull Request**

   Go to the repository on GitHub and create a pull request from your branch. Provide a clear description of the changes and why they should be merged.

### Code of Conduct

Please adhere to the project's code of conduct while contributing. Be respectful and considerate to others, and follow the guidelines outlined in the repository.

Thank you for your contributions!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Happy coding! 🚀


