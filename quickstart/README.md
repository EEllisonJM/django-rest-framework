# Create the project directory
mkdir tutorial
cd tutorial

# Create a virtual environment to isolate our package dependencies locally
python3 -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`

# Install Django and Django REST framework into the virtual environment
pip install django
pip install djangorestframework

# Set up a new project with a single application
django-admin startproject tutorial .  # Note the trailing '.' character
cd tutorial
django-admin startapp quickstart
cd ..

# Now sync your database for the first time:
python manage.py migrate

# We'll also create an initial user named 'admin' with a password of 'admin'. We'll authenticate as that user later in our example.
python manage.py createsuperuser --email admin@example.com --username admin




