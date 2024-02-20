from pathlib import Path
import os

my_secret_key = os.environ.get('MY_SECRET_KEY')
app_password = os.environ.get('APP_PASSWORD')

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = my_secret_key

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition
INSTALLED_APPS = [
    'rest_framework',
    'channels',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'life_lens',
    'rest_framework_simplejwt',
    'corsheaders',
    'users',
    'djoser',
]

CHANNEL_LAYERS = {
    'default': {
        'BACKEND' : 'channels_redis.core.RedisChannelLayer',
        'CONFIG' : {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    
]

REST_FRAMEWORK = {
     'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}


SIMPLE_JWT = {
   'AUTH_HEADER_TYPES': ('JWT', 'Bearer',),
}


ROOT_URLCONF = 'server.urls'



TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'build')],   #build
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

WSGI_APPLICATION = 'server.wsgi.application'
ASGI_APPLICATION = 'server.asgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000", 
    "http://127.0.0.1:3000",
    "http://127.0.0.1",
    "http://localhost"
]


CORS_ALLOW_ALL_ORIGINS = False 
CORS_ALLOW_CREDENTIALS = True 


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'
""" STATICFILES_DIR = [
    os.path.join(BASE_DIR, 'build/static')
] """
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'ERROR',  # Log only errors and higher severity
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG',  # Log only errors and higher severity
    },
    'loggers': {
    'django': {
        'handlers': ['console'],
        'level': 'DEBUG', 
        'propagate': True,
    },
    'django.request': {
        'handlers': ['console'],
        'level': 'DEBUG',
    },
    'rest_framework_simplejwt': {
        'handlers': ['console'],
        'level': 'DEBUG',
    },
}
}

AUTH_USER_MODEL = 'users.UserAccount'

DEFAULT_FROM_EMAIL = 'lifelensauth@gmail.com'


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST='smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'lifelensauth@gmail.com'
EMAIL_HOST_PASSWORD = 'rrtwudkhrgnxrdqj'
EMAIL_USE_TLS = True

DJOSER = {
    'LOGIN_FIELD' : 'email',
    'SET_CREATE_PASSWORD_RETYPE' : True,
#Reducing Scope
#    'USERNAME_CHANGED_EMAIL_CONFIRMATION' : True, 
#    'PASSWORD_CHANGED_EMAIL_CONFIRMATION' : True,
#   'SEND_CONFIRMATION_EMAIL' : True,
    'SET_PASSWORD_RETYPE' : True,
#    'PASSWORD_RESET_CONFIRM_URL' : 'password/reset/confirm/{uid},{token}',
#   'USERNAME_RESET_CONFIRM_URL' : 'email/reset/confirm/{uid},{token}',
#   'ACTIVATION_URL' : 'activate/{uid}/{token}',
#   'SEND_ACTIVATION_EMAIL' : True,
    'SERIALIZERS' : {
        'user_create' : 'users.serializers.UserCreateSerializer', 
        'user' : 'users.serializers.UserCreateSerializer', 
        'user_delete' : 'djoser.serializers.UserDeleteSerializer', 
    },
#    'EMAIL' : {
#        'activation' : 'templates/email/activation.html' //file doesnt exist
#    }

}