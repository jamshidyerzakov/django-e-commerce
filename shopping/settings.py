import os
from datetime import timedelta

from django.utils.translation import gettext_lazy as _
import environ


environ.Env.read_env(env_file='.env.example')


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


SECRET_KEY = os.environ.get('SECRET_KEY', "345sfgddfg345efdgsdfg345rgdfsg")

DEBUG = os.environ.get('DEBUG')

ALLOWED_HOSTS = ['*']
CORS_ORIGIN_ALLOW_ALL = True

DOMAIN = os.environ.get("DOMAIN")
SITE_NAME = os.environ.get("SITE_NAME")

AUTH_USER_MODEL = 'accounts.User'

# Application definition

INSTALLED_APPS = [
    'modeltranslation',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # my apps
    'accounts',
    'address',
    'category',
    'product',
    'cart',
    'order',

    # 3rd-party
    'rest_framework',
    'django_filters',
    'corsheaders',
    'drf_yasg',
    'djmoney',

    'phonenumber_field',
    'django_countries',
    'generic_relations',

    #auth
    'djoser',
    'rest_framework.authtoken',
    'oauth2_provider',
    'social_django',
    'rest_framework_social_oauth2',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'shopping.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, '')]
        ,
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

WSGI_APPLICATION = 'shopping.wsgi.application'

# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': os.environ.get("PSQL_DB_NAME", 'umarket'),
#         'USER': os.environ.get('PSQL_DB_USER', 'umarket'),
#         'PASSWORD': os.environ.get('PSQL_DB_PASSWORD', '$umarket$'),
#         'HOST': os.environ.get('PSQL_DB_HOST', '127.0.0.1'),
#         'PORT': os.environ.get('PSQL_DB_PORT', '5432'),
#     }
# }

# social auth

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.environ.get('GOOGLE_OAUTH2_KEY')
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.environ.get('GOOGLE_OAUTH2_SECRET')

SOCIAL_AUTH_FACEBOOK_KEY = os.environ.get('FACEBOOK_OAUTH2_KEY')
SOCIAL_AUTH_FACEBOOK_SECRET = os.environ.get('FACEBOOK_OAUTH2_SECRET')

# SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']


SOCIAL_AUTH_MAILRU_OAUTH2_KEY = os.environ.get('MAILRU_OAUTH2_KEY')
SOCIAL_AUTH_MAILRU_OAUTH2_SECRET = os.environ.get('MAILRU_OAUTH2_SECRET')


SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.social_auth.associate_by_email',
    'core.auth.pipelines.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
)


AUTHENTICATION_BACKENDS = (
    'social_core.backends.facebook.FacebookAppOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.google.GoogleOAuth2',
    'rest_framework_social_oauth2.backends.DjangoOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)


# rest

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
        'rest_framework_social_oauth2.authentication.SocialAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 20,
}

# smtp to send confirmation email

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.environ.get('SMTP_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('SMTP_HOST_PASSWORD')
EMAIL_PORT = 587

# djoser auth

DJOSER = {
    'PASSWORD_RESET_CONFIRM_URL': '#/password/reset/confirm/{uid}/{token}',
    'USERNAME_RESET_CONFIRM_URL': '#/username/reset/confirm/{uid}/{token}',
    'ACTIVATION_URL': 'auth/{uid}/{token}',
    'SEND_ACTIVATION_EMAIL': True,
    'SERIALIZERS':
        {
            "user_create": "core.auth.djoser.CustomUserCreateSerializer",
        }
    # )
    ,
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=15),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,

    'AUTH_HEADER_TYPES': ('JWT',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=15),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}

# logging
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'handlers': {
#         'console': {
#             'class': 'logging.StreamHandler',
#         },
#     },
#     'root': {
#         'handlers': ['console'],
#         'level': 'WARNING',
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['console'],
#             'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
#             'propagate': False,
#         },
#     },
# }

# Password validation

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


# Internationalization

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


LANGUAGES = (
    ('ru', _('Russian')),
    ('uz', _('Uzbek')),
)


STATIC_URL = '/static/'
STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [STATIC_DIR]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
