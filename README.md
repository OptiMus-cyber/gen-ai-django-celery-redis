
# Image Generator with Django and Celery

![Django](https://img.shields.io/badge/Django-3.2+-brightgreen)
![Celery](https://img.shields.io/badge/Celery-5.2+-blue)
![Redis](https://img.shields.io/badge/Redis-6.2+-red)
![Python](https://img.shields.io/badge/Python-3.8+-yellow)

This project is a Django application that generates images using the Stability AI’s Text-to-Image generation API. It leverages Celery for parallel processing to manage asynchronous calls to the API.

## Features

- Generate images in parallel using Celery
- Use Stability AI’s Text-to-Image generation API
- Store image URLs and metadata in the Django model

## Table of Contents

- [Prerequisites](#prerequisites)
- [Setup and Installation](#setup-and-installation)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [API Usage](#api-usage)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.8+
- Django 3.2+
- Celery 5.2+
- Redis 6.2+
- Stability AI account with API key

## Setup and Installation

### 1. Clone the Repository

```bash
https://github.com/OptiMus-cyber/gen-ai-django-celery-redis.git
cd gen-ai-django-celery-redis
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Redis

Ensure Redis is installed and running on your system. You can install Redis from [here](https://redis.io/download).

### 5. Apply Migrations

```bash
python manage.py migrate
```

### 6. Create a Superuser

```bash
python manage.py createsuperuser
```

## Configuration

### 1. Stability AI API Key

Create a `.env` file in your project root and add your Stability AI API key:

```env
STABILITY_API_KEY=your_api_key_here
```

### 2. Celery Configuration

Add the following configuration to your Django settings file (`settings.py`):

```python
# Celery Configuration
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'django-db'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Asia/Kolkata'
```


## Running the Application

### 1. Start Redis Server

Make sure your Redis server is running:

```bash
redis-server
```

### 2. Start Celery Workers

In a new terminal window, navigate to your project directory and start the Celery workers:

```bash
celery -A imagenerator worker --loglevel=info
```

### 3. Run Django Development Server

In your project directory, start the Django development server:

```bash
python manage.py runserver
```

## API Usage

To generate images, you can send a POST request to the `/generate-images/` endpoint with the required prompts. Example JSON payload:

```json
{
  "prompts": ["A red flying dog", "A piano ninja", "A footballer kid"]
}
```

## Example Request

```bash
curl -X POST http://127.0.0.1:8000/generate-images/ \
-H "Content-Type: application/json" \
-d '{"prompts": ["A red flying dog", "A piano ninja", "A footballer kid"]}'
```

## Contributing

Contributions are welcome! Please read the [contributing guidelines](CONTRIBUTING.md) first.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Developed with 💻 by [Prakash Singh Rautela](https://github.com/OptiMus-cyber)

### Instructions to Include in Your Project Directory

1. **requirements.txt**: Ensure you have a `requirements.txt` file with the necessary dependencies.
   ```plaintext
   Django>=3.2,<4.0
   celery>=5.2,<6.0
   redis>=3.5,<4.0
   requests>=2.25,<3.0
   python-dotenv>=0.17,<1.0
   ```

2. **Project Structure**: Ensure your project structure resembles:
   ```plaintext
   imagenerator/
   ├── imagenerator/
   │   ├── __init__.py
   │   ├── settings.py
   │   ├── celery.py
   │   ├── urls.py
   │   └── wsgi.py
   ├── imageapp/
   │   ├── __init__.py
   │   ├── tasks.py
   │   ├── models.py
   │   ├── views.py
   │   ├── urls.py
   │   └── ...
   ├── manage.py
   ├── .env
   ├── requirements.txt
   ├── README.md
   └── .   `
   ```