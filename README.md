# Inventory Management System API

This is a backend API for an **Inventory Management System** built using **Django Rest Framework** (DRF). The system supports CRUD operations for inventory items and integrates with **JWT-based authentication** for secure access. **PostgreSQL** is used as the database, and **Redis** is utilized for caching frequently accessed items.

## Features

- JWT Authentication for secure API access.
- Create, Read, Update, and Delete (CRUD) operations for inventory items.
- Redis caching to improve performance for reading items.
- Unit tests to ensure all functionalities are working as expected.
- Logging for tracking API usage and errors.

## Tech Stack

- **Backend Framework**: Django Rest Framework (DRF)
- **Database**: PostgreSQL
- **Caching**: Redis
- **Authentication**: JWT (JSON Web Tokens)
- **Testing**: Django's test framework
- **Logging**: Django logging

## Installation

Follow these steps to set up and run the project locally.

### Prerequisites

- **Python 3.8**
- **PostgreSQL**
- **Redis**
- **Git**


### Clone the Repository

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/your-username/inventory_project.git
   cd inventory_project


## API Endpoints
## Authentication:
  - **POST /api/token/: Obtain JWT access and refresh tokens.**
  - **POST /api/token/refresh/: Refresh access token.**
## CRUD Operations:
    POST /api/items/: Create a new inventory item.
    GET /api/items/{id}/: Retrieve a specific inventory item.
    PUT /api/items/{id}/: Update a specific inventory item.
    DELETE /api/items/{id}/: Delete a specific inventory item.

## Redis Caching
Redis is used to cache GET /api/items/{id}/ requests to improve performance. The first request fetches the item from the database, and subsequent requests fetch it from Redis.
