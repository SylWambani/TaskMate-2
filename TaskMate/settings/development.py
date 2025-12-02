from .commonsettings import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-^astq&#u=)k!_%r52gi10%o8$v_o_2vt$0&qoztdfa)5xmk_x-'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'taskmate',
        'HOST': '127.0.0.1',
        'USER': 'root',
        'PASSWORD': 'Wambani2000.',
        'PORT': '3306',
    }
}
