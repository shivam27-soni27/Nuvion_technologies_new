import os
import sys
from django.core.wsgi import get_wsgi_application

# Add the path to your project directory
sys.path.append('/home/nuvion/Nuvion-Technology/nuvion/')

# Set the environment variable to your Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nuvion.settings')

application = get_wsgi_application()
