# 📞 Phone Letter Combinations HTTP Server

A simple HTTP server that generates all possible letter combinations for a given phone number based on standard number-to-letter mappings. This project is designed to demonstrate backend development, containerization with Docker, and deployment on a preinstalled Docker Ubuntu server.

---

## 🚀 Features

- **REST API Endpoint**: `/combinations` accepts a phone number (2-9) as input and returns all possible letter combinations.
- **Django Framework**: Robust and scalable backend using Python's Django.
- **Dockerized**: Fully containerized application for easy deployment.
- **Efficient Logic**: Uses Python’s `itertools` for efficient combination generation.

---

## 📂 Project Structure
```
phoneLetterCombinations/
├── combinations
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── db.sqlite3
├── Dockerfile
├── manage.py
├── phoneLetterCombinations
│   ├── asgi.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── README.md
├── requirements.txt
└── templates
```
# Project documentation


---

## ⚙️ Setup Instructions

### Prerequisites

- Python 3.12+ installed
- Docker installed
- Basic knowledge of Docker commands

### Local Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/phone-letter-combinations.git
   cd phone-letter-combinations
   
2. Install dependencies:
   ```python 
   python -m pip install -r requirements.txt
   ```
3. Run the server locally
   ```bash
   python manage.py runserver
4. Test the endpoint using Postman or curl:
   ```bash
   curl -X POST http://127.0.0.1:8000/combinations \
   -H "Content-Type: application/json" \
   -d '{"phoneNumber": "23"}'
## 🐳 Docker Deployment
### Build Docker Image
1. Build the image:
   ```BASH
   sudo docker build -t phone-letter-combinations .
2. Run the container:
   ```bash
   docker run -d -p 8000:8000 phone-letter-combinations
3. Test and running container:
   ```bash
   curl -X POST http://localhost:8000/combinations \
   -H "Content-Type: application/json" \
   -d '{"phoneNumber": "23"}'

## 📦 Deployment on Preinstalled Ubuntu Docker Server
### If you want to run it on your own ubuntu device skip to the API Usage section
1. Log in to the Ubuntu server:
   ```bash
   ssh username@server-ip
2. Transfer your docker image:
   ```bash
   docker save phone-letter-combinations | ssh username@server-ip "docker load"
3. Run the container on the server:
   ```bash
   docker run -d -p 8000:8000 phone-letter-combinations
4. Access the endpoint:

   ```bash
   curl -X POST http://<server-ip>:8000/combinations \
   -H "Content-Type: application/json" \
   -d '{"phoneNumber": "23"}'

## 🛠 API Usage
### Endpoint: /combinations

- Method: POST

- Request Body: JSON
   ```json
  {
    "phoneNumber": "23"
   }
  
- Response: JSON
   ```json
  {
    "combinations": ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
   }

### Error Responses

- 400: Invalid JSON or missing phoneNumber.
- 405: Unsupported HTTP method.
## 📋 Notes for Reviewers

- Use docker logs <container-id> to debug any issues.
- Ensure port 8000 is open on the server for external access.