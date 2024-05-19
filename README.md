# React Frontend and FastAPI Backend Integration for User Authentication

This repository demonstrates the integration of a frontend built with React and a backend built with FastAPI, allowing users to register and log in.

## Features

User Registration: Users can create a new account by providing their email and password.
User Login: Registered users can log in with their credentials.
Token-based Authentication: User authentication is handled using JWT (JSON Web Tokens).
Secure Communication: All data exchange between the frontend and backend is protected using HTTPS.

## Technologies Used
Frontend: React, Ant Design UI library
Backend: FastAPI, SQLAlchemy, Postgresql (for database)
Authentication: JWT (JSON Web Tokens)

## Getting Started
### Prerequisites
Node.js and npm (or yarn) installed on your machine
Python 3.x and pip installed on your machine

## Installation
Clone this repository to your local machine:

bash
```
git clone https://github.com/your-username/your-repository.git
```
Navigate to the frontend directory:

bash
```
cd frontend
```
Install frontend dependencies:

bash
```
npm install
```

Navigate to the backend directory:

bash
```
cd ../backend
```

Install backend dependencies:

bash
```
pip install -r requirements.txt
```

Configuration
Configure environment variables:

***Create a .env file in the backend directory.***

Define the following environment variables in the .env file:

plaintext
Copy code
```
DATABASE_HOSTNAME=localhost
DATABASE_PORT=5432
DATABASE_PASSWORD=your-password
DATABASE_NAME=your-db-name
DATABASE_USERNAME=your-db-username e.g. postgres

SECRET_KEY=your-secret-key

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=30
```

## Running the Application
Start the backend server:

bash
```
uvicorn app.main:app --reload
```
Start the frontend development server on another terminal:

bash
```
npm start
```
Open your browser and navigate to **http://localhost:3000** to view the application.

### Usage
Register a new account by providing your email and password.
Log in with your registered credentials.
Explore the application features, such as profile management, etc.

## Folder Structure
bash
Copy code
```
├── frontend/            # React frontend
│   ├── public/
│   └── src/
│       ├── assets/      # Images
|       |── Auth/        # Contains the Login and Signup information
│       ├── pages/       # Application pages (e.g., Home, Login, Register)
│       ├── App.js       # Main React component
│       └── index.js     # Entry point
│
└── backend/             # FastAPI backend
    ├── app/
    │   ├── routers/     # API route definitions
    │   ├── models.py    # SQLAlchemy models
    │   ├── config.py    # Application configurations
    │   ├── database.py  # Database connection functions
    │   ├── crud.py      # Crud operation functions
    │   └── main.py      # FastAPI application instance
    │   ├── oauth2.py    # JWT functions
    │   └── schemas.py   # Pydantic schemas
    │   └── utils.py     # Utilities functions
    │
    └── .env             # Environment variables
```
Contributing

<p>Contributions are welcome! Feel free to submit issues or pull requests.</p>
