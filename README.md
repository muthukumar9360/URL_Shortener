# Django URL Shortener

A simple Django web application that allows users to shorten URLs and view previously shortened URLs.  

## Features
- Shorten long URLs to short codes
- View all converted URLs
- Easy-to-use web interface
- CSRF-protected forms

---

## Prerequisites

- Python 3.8+
- pip (Python package manager)
- Git (optional, for cloning the repository)

---

## Setup Instructions

### 1. Clone the repository (optional)

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Create a virtual environment

It's recommended to use a virtual environment to manage dependencies.

```bash
# On Windows
python -m venv env

# On Mac/Linux
python3 -m venv env
```

### 3. Activate the virtual environment

```bash
# On Windows
env\Scripts\activate

# On Mac/Linux
source env/bin/activate
```

You should now see `(env)` at the start of your terminal prompt.

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

> **Note:** If `requirements.txt` doesn't exist, create it using:  
> ```bash
> pip freeze > requirements.txt
> ```

### 5. Set up environment variables

Create a `.env` file in your project root and add any necessary variables. Example:

```
SECRET_KEY=your_django_secret_key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

### 6. Apply migrations

```bash
python manage.py migrate
```

### 7. Run the development server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.  
You can now use the URL shortener app.

---

## Project Structure

```
your-project/
│
├── urls_shortener/           # Django app
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── models.py
│   ├── views.py
│   └── urls.py
│
├── project_name/             # Django project folder
│   ├── settings.py
│   └── urls.py
│
├── manage.py
├── requirements.txt
└── README.md
```

---

## Optional Commands

- Create superuser/admin:  
```bash
python manage.py createsuperuser
```

- Check for broken migrations:  
```bash
python manage.py makemigrations
python manage.py migrate
```

- Run tests:  
```bash
python manage.py test
```

---

## License

This project is licensed under the MIT License.

---

## Author

**Your Name** – [Your GitHub](https://github.com/your-username)
