# Django CRUD Todo Application

A comprehensive full-stack todo list application built with Django, featuring complete CRUD (Create, Read, Update, Delete) operations with a modern, responsive Bootstrap UI.

## 🚀 Features

- **Complete CRUD Operations**: Create, read, update, and delete todos
- **Rich Todo Data Model**: Each todo includes:
  - Title and description
  - Email and phone number contact information
  - Priority levels (High, Medium, Low)
  - Programming language tags (Python, Java, C, Other)
  - Difficulty level (0-5 scale)
  - Due dates
  - Completion status
- **Responsive Bootstrap UI**: Clean, modern interface that works on all devices
- **Form Validation**: Built-in Django form validation and error handling
- **Admin Interface**: Django admin panel for backend management
- **Static Files Management**: Properly configured static file serving

## 🛠️ Technology Stack

- **Backend**: Django 5.1.4
- **Frontend**: HTML5, CSS3, Bootstrap 5.3.3
- **Database**: SQLite (default)
- **Form Handling**: Django Forms with CSRF protection
- **Phone Number Validation**: django-phonenumber-field

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## ⚡ Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/Nickysinghal/CRUD-todo-django.git
cd CRUD-todo-django
```

### 2. Create Virtual Environment (Recommended)

```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install Django==5.1.4
pip install django-phonenumber-field==8.1.0
```

### 4. Database Setup

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 6. Run the Development Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` to access the application.

## 📱 Application Structure

```
CRUD-todo-django/
├── manage.py                 # Django management script
├── mytodo/                   # Main project directory
│   ├── __init__.py
│   ├── settings.py          # Django settings
│   ├── urls.py              # Main URL configuration
│   ├── wsgi.py              # WSGI configuration
│   └── asgi.py              # ASGI configuration
├── todo/                     # Todo app directory
│   ├── __init__.py
│   ├── admin.py             # Admin panel configuration
│   ├── apps.py              # App configuration
│   ├── models.py            # Todo data model
│   ├── views.py             # View functions
│   ├── urls.py              # App URL patterns
│   ├── tests.py             # Test cases
│   └── migrations/          # Database migrations
├── templates/todo/          # HTML templates
│   ├── index.html           # Main todo list page
│   └── update.html          # Todo update form
├── staticfiles/             # Collected static files
└── db.sqlite3              # SQLite database
```

## 🎯 Usage Guide

### Adding a New Todo

1. Fill out the form on the main page with:
   - **Title**: Brief description of the task
   - **Description**: Detailed task information
   - **Email**: Contact email address
   - **Phone**: 10-digit phone number
   - **Priority**: Select High, Medium, or Low
   - **Languages**: Choose applicable programming languages
   - **Difficulty**: Set difficulty level (0-5)
   - **Due Date**: Select target completion date

2. Click "Add Task" to save the todo

### Managing Todos

- **View**: All todos are displayed in a table with all relevant information
- **Complete**: Click the "Complete" button to mark a todo as finished
- **Update**: Click the "Update" button to modify todo details
- **Delete**: Click the "Delete" button to remove a todo

## ⚙️ Configuration

### Settings

Key configuration options in `mytodo/settings.py`:

- **DEBUG**: Set to `False` for production
- **ALLOWED_HOSTS**: Configure for your domain
- **STATIC_ROOT**: Path for collected static files
- **DATABASES**: Database configuration (SQLite by default)

### URL Configuration

- Main site redirects `/` to `/todo/`
- Admin panel available at `/admin/`
- Todo app URLs:
  - `/todo/` - Main todo list
  - `/todo/create/` - Create new todo
  - `/todo/complete/<id>/` - Mark as complete
  - `/todo/delete/<id>/` - Delete todo
  - `/todo/update/<id>/` - Update todo

## 🗄️ Database Model

The `Todo` model includes the following fields:

| Field | Type | Description |
|-------|------|-------------|
| title | CharField | Task title (max 30 chars) |
| description | TextField | Task description (max 55 chars) |
| completed | BooleanField | Completion status |
| email | EmailField | Contact email |
| phone | PhoneNumberField | Contact phone number |
| priority | CharField | High/Medium/Low priority |
| languages | CharField | Programming language tags |
| difficulty | IntegerField | Difficulty level (0-5) |
| due_date | DateField | Target completion date |

## 🎨 UI Features

- **Bootstrap 5.3.3**: Modern, responsive design
- **Form Controls**: Styled input fields, dropdowns, and sliders
- **Color-coded Table**: Easy-to-read todo display
- **Responsive Layout**: Works on desktop and mobile devices
- **Form Validation**: Client and server-side validation

## 🚀 Deployment

### For Production

1. Set `DEBUG = False` in settings.py
2. Configure `ALLOWED_HOSTS` with your domain
3. Set up a production database (PostgreSQL recommended)
4. Configure static file serving
5. Use a production WSGI server like Gunicorn

### Sample Production Settings

```python
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## 🧪 Testing

Run the test suite:

```bash
python manage.py test
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🐛 Issues and Support

If you encounter any issues or have questions, please [open an issue](https://github.com/Nickysinghal/CRUD-todo-django/issues) on GitHub.

## 🏗️ Future Enhancements

- User authentication and authorization
- Todo categories and tags
- Search and filter functionality
- Email notifications for due dates
- REST API endpoints
- Mobile app integration
- Task assignment and collaboration features

---

**Built with ❤️ using Django**