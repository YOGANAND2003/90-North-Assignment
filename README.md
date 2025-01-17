# Chat Application (chat_project)

A simple web-based chat application built with **Django**. This project allows users to chat in real-time without storing messages in a database, making it a lightweight solution for temporary communication.

---

## Table of Contents

1. Project Overview
2. Technologies Used
3. Installation
4. Configuration
5. Usage
6. Project Structure
7. Features


---

## Project Overview

This project is a simple web-based chat application where users can:

- **User Authentication**: Users can sign up and log in to the chat app.
- **User List**: View other registered users and select one to chat with.
- **Real-time Messaging**: Users can send and receive messages during their session.
- **No Persistent Storage**: The messages are not stored in a database and will be lost when the page is refreshed.

---

## Technologies Used

- **Frontend**:
  - HTML5, CSS3

- **Backend**:
  - Python
  - Django

---

## Installation

To run this project on your local machine, follow these steps:

### Prerequisites

- Python 3.x
- Pip (Python package installer)

### Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/chat-application.git
   cd chat_project
   ```

2. **Install the dependencies**:
   It is recommended to use a virtual environment to manage dependencies.
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   pip install django
   pip install channels

   ```

   If you're using Flask instead of Django, you'll need to install Flask and any required libraries.

3. **Run the server**:

   - For **Django**:
     ```bash
     python manage.py runserver
     ```

---

## Configuration

1. **Environment Variables**:
   If your app requires sensitive data like secret keys or other configurations, manage them using environment variables. You can use `django-environ` or `python-dotenv` to manage environment variables.

---

## Usage

1. **Run the server**:
   ```bash
   python manage.py runserver   # Django

2. **Access the application**:
   - Open your browser and go to [http://localhost:8000](http://localhost:8000) for Django
3. **Interacting with the App**:
   - Register a new user or log in with your existing credentials.
   - View the list of other users and select one to start chatting.

---

## Project Structure
```chat_project/               # Main project folder
├── chat/                   # Django app folder
│   ├── migrations/         # Database migrations
│   │   └── __init__.py     # Empty file for migrations
│   ├── templates/          # HTML templates folder
│   │   └── chat/           # App-specific templates
│   │       ├── home.html   # Chat homepage
│   │       ├── signup.html # Signup page
│   │       ├── login.html  # Login page
|   |       ├── chat_room.html  # Chat page
│   ├── __init__.py         # App initialization
│   ├── admin.py            # Admin configuration
│   ├── apps.py             # App configuration
│   ├── models.py           # Database models
|   ├── consumers.py
│   ├── urls.py             # App-specific URLs
│   ├── views.py            # View functions
│   └── tests.py            # Tests (optional)
├── chat_project/           # Project settings folder
│   ├── __init__.py         # Initialization file
│   ├── asgi.py             # ASGI configuration
│   ├── settings.py         # Project settings
│   ├── urls.py             # Project-level URLs
│   ├── wsgi.py             # WSGI configuration
├── db.sqlite3              # SQLite database file
├── manage.py               # Django management script
```

## Features

- **User Registration and Login**: Allows users to sign up and log in.
- **Real-time Messaging**: Sends and receives messages in real-time without database storage.
- **Responsive Design**: The application is responsive and works on both mobile and desktop devices.

---


### Future Improvements

- **Real-time Messaging**: Implement WebSockets for real-time communication.
- **Message History**: Implement a database to store and retrieve message history.
- **File Attachments**: Allow users to send images, documents, etc.
- **Push Notifications**: Integrate push notifications for new messages.
