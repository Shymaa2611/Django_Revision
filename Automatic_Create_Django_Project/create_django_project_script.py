import os
import subprocess
import sys

# Get user input
virtual_environment = input("Enter The Name of Virtual Environment: ")
project = input("Enter The Name Of Project: ")
app = input("Enter The Name Of App: ")

# Step 1: Create virtual environment
result = subprocess.run(['python3', '-m', 'venv', virtual_environment], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print(result.stdout.decode('utf-8'))
if result.returncode != 0:
    print("Error creating virtual environment:", result.stderr.decode('utf-8'))
    sys.exit(1)

# Step 2: Define absolute paths to Python and Pip inside the virtual environment
venv_python = os.path.join(os.getcwd(), virtual_environment, 'bin', 'python')
venv_pip = os.path.join(os.getcwd(), virtual_environment, 'bin', 'pip')

# Step 3: Install Django using the virtual environment's pip
result = subprocess.run([venv_pip, 'install', 'django'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print(result.stdout.decode('utf-8'))
if result.returncode != 0:
    print(result.stderr.decode('utf-8'))
    sys.exit(1)

# Step 4: Start Django project
os.chdir(virtual_environment)
result = subprocess.run([venv_python, '-m', 'django', 'startproject', project], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print(result.stdout.decode('utf-8'))
if result.returncode != 0:
    print(result.stderr.decode('utf-8'))
    sys.exit(1)

print(os.getcwd())
print(os.listdir())

# Step 5: Run migrations
os.chdir(project)
result = subprocess.run([venv_python, 'manage.py', 'migrate'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
if result.returncode == 0:
    print("Successfully migrated")
else:
    print("Something is wrong")
    print(result.stderr.decode('utf-8'))

# Step 6: Create Django app
result = subprocess.run([venv_python, 'manage.py', 'startapp', app], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
if result.returncode == 0:
    print(f'Successfully created app!')
else:
    print('Failed to create app')
    print(result.stderr.decode('utf-8'))

# Step 7: Add new app in installed apps in settings.py
settings_path = os.path.join(os.getcwd(), project, 'settings.py')
with open(settings_path, 'r') as f:
    contents = f.readlines()

installed_apps_line = None
for i, line in enumerate(contents):
    if 'INSTALLED_APPS' in line:
        installed_apps_line = i
        break

if installed_apps_line is not None:
    indent = contents[installed_apps_line].split('INSTALLED_APPS', maxsplit=1)[0]
    new_line = f"{indent}    '{app}',\n"
    contents.insert(installed_apps_line + 1, new_line)

with open(settings_path, 'w') as f:
    contents = ''.join(contents)
    f.write(contents)

print(f'Successfully added {app} to INSTALLED_APPS in settings.py')

# Step 8: Create urls.py file in the app directory
app_directory = os.path.join(os.getcwd(), app)
urls_file_path = os.path.join(app_directory, 'urls.py')
urls_file_contents = f"""from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
]
"""

with open(urls_file_path, 'w') as f:
    f.write(urls_file_contents)

print(f'Successfully created urls.py file for app {app}!')

# Step 9: Include app urls in the project's urls.py
urls_path = os.path.join(os.getcwd(), project, 'urls.py')
urls_file_contents = f"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('{app}.urls')),
]

# Media setting
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
"""

with open(urls_path, 'w') as f:
    f.write(urls_file_contents)

print(f'Successfully included {app} URLs in the project\'s urls.py')

# Step 10: Add "import os" to settings.py
with open(settings_path, 'r') as f:
    contents = f.read()

new_contents = 'import os\n' + contents
with open(settings_path, 'w') as f:
    f.write(new_contents)

# Step 11: Add Template Settings
with open(settings_path, 'r') as f:
    contents = f.readlines()

templates_start = None
templates_end = None

for i, line in enumerate(contents):
    if 'TEMPLATES' in line.strip():
        templates_start = i
    if templates_start is not None and line.strip() == '],':
        templates_end = i + 1
        break

if templates_start is not None and templates_end is not None:
    del contents[templates_start:templates_end + 1]

new_templates = '''TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
'''

with open(settings_path, 'a') as f:
    f.writelines(new_templates)

print("Successfully updated TEMPLATES setting in settings.py")

# Step 12: Add Static settings
new_lines = [
    '\n',
    '# Static files\n',
    'STATIC_ROOT = os.path.join(BASE_DIR, "static")\n',
    'STATIC_URL = "/static/"\n',
    'STATICFILES_DIRS = [\n',
    f'    os.path.join(BASE_DIR, "{project}", "static"),\n',
    ']\n',
    '\n',
]

with open(settings_path, 'a') as f:
    f.writelines(new_lines)

print("Successfully added static files settings to settings.py")

# Step 13: Add Media settings
new_lines = '''
# Media files
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"
'''

with open(settings_path, 'a') as f:
    f.writelines(new_lines)

print("Successfully added media files settings to settings.py")

# Step 14: Collect static files
subprocess.call([venv_python, 'manage.py', 'collectstatic'], shell=True)

# Step 15: Install Pillow (for image processing, if needed)
subprocess.call([venv_pip, 'install', 'pillow'], shell=True)

# Step 16: Create static folder
os.chdir(project)
if not os.path.exists("static"):
    os.makedirs("static")
    print("Static folder created successfully.")
else:
    print("Static folder already exists.")

# Step 17: Create templates folder
os.chdir("..")
os.chdir(app)
if not os.path.exists("templates"):
    os.makedirs("templates")
    print("Templates folder created successfully.")
else:
    print("Templates folder already exists.")

