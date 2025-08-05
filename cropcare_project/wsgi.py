# C:\Users\Gourav Rajput\CropCareConnect\cropcare_project\wsgi.py

import os
from django.core.wsgi import get_wsgi_application

# Add these lines for superuser creation
import django
from django.conf import settings
from django.contrib.auth import get_user_model

# Ensure Django is set up before trying to access models
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cropcare_project.settings')
django.setup()

# Superuser creation logic
# THIS IS TEMPORARY AND SHOULD BE REMOVED AFTER FIRST SUCCESSFUL LOGIN
try:
    User = get_user_model()
    username = os.environ.get('DJANGO_SUPERUSER_USERNAME')
    password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')
    email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@example.com') # Provide a default email

    if username and password:
        if not User.objects.filter(username=username).exists():
            print(f"Creating superuser: {username}")
            User.objects.create_superuser(username=username, password=password, email=email)
        else:
            print(f"Superuser {username} already exists. Skipping.")
    else:
        print("DJANGO_SUPERUSER_USERNAME or DJANGO_SUPERUSER_PASSWORD environment variables not set. Skipping superuser creation.")
except Exception as e:
    print(f"Error during superuser creation in wsgi.py: {e}")
# END TEMPORARY SUPERUSER CREATION LOGIC

application = get_wsgi_application()