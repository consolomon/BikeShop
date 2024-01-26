from pathlib import Path
import os       

BASE_DIR = Path(__file__).resolve().parent.parent
# some other settings
# your code here
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')