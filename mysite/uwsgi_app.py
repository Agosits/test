import sys
import os

reload(sys)
sys.setdefaultencoding('utf8')
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
