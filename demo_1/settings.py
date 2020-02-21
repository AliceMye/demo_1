"""
Django settings for demo_1 project.

Generated by 'django-admin startproject' using Django 3.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'q9fh38)$8c8xe!or=dlgom$n-0$&e8%l)as_-36s3vf6$1!@!+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app01.apps.App01Config',
    'rest_framework',
    'corsheaders'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',

]

ROOT_URLCONF = 'demo_1.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
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

WSGI_APPLICATION = 'demo_1.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
     'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'demo_1',
        'USER':'root',
        'PORT':3306,
        'HOST':'127.0.0.1',
        'PASSWORD':'123'
     }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'


import datetime
import django
# 设置token过期时间时间
JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=3600),
    # token前缀
    'JWT_AUTH_HEADER_PREFIX': 'JWT',
}

#引用Django自带的User表，继承使用时需要设置
AUTH_USER_MODEL = 'app01.User'

# 允许跨域
CORS_ORIGIN_ALLOW_ALL = True



# 配置django缓存 - 采用redis数据库
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/10",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "CONNECTION_POOL_KWARGS": {"max_connections": 100}
        }
    }
}


# 配置日志
# 路径

# BASE_DIR不
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#
# # 环境变量操作： BASE_DIR与app01文件夹都要添加到环境变量
# import sys
#
# sys.path.insert(0, BASE_DIR)
#
# APPS_DIR = os.path.join(BASE_DIR, 'app01')
# sys.path.insert(1, APPS_DIR)
#
#
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'formatters': {
#         'verbose': {
#             'format': '%(levelname)s %(asctime)s %(module)s %(lineno)d %(message)s'
#         },
#         'simple': {
#             'format': '%(levelname)s %(module)s %(lineno)d %(message)s'
#         },
#     },
#     'filters': {
#         'require_debug_true': {
#             '()': 'django.utils.log.RequireDebugTrue',
#         },
#     },
#     'handlers': {
#         'console': {
#             'level': 'DEBUG',
#             'filters': ['require_debug_true'],
#             'class': 'logging.StreamHandler',
#             'formatter': 'simple'
#         },
#         'file': {
#             # 实际开发建议使用WARNING
#             'level': 'INFO',
#             'class': 'logging.handlers.RotatingFileHandler',
#             # 日志位置,日志文件名,日志保存目录必须手动创建，注：这里的文件路径要注意BASE_DIR代表的是小luffyapi
#             'filename': os.path.join(os.path.dirname(BASE_DIR), "logs", "luffy.log"),
#             # 日志文件的最大值,这里我们设置300M
#             'maxBytes': 300 * 1024 * 1024,
#             # 日志文件的数量,设置最大日志数量为10
#             'backupCount': 10,
#             # 日志格式:详细格式
#             'formatter': 'verbose',
#             # 文件内容编码
#             'encoding': 'utf-8'
#         },
#     },
#     # 日志对象
#     'loggers': {
#         'django': {
#             'handlers': ['console', 'file'],
#             'propagate': True,  # 是否让日志信息继续冒泡给其他的日志处理系统
#         },
#     }
# }