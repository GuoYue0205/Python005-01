"""
Django settings for MyDjango project.

Generated by 'django-admin startproject' using Django 2.2.13.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
# 项目路径
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 密钥
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*)#2ov42j-j29!zsyw&lm1r1$($k5bz(sfu-#+(#%l3wp(vy7p'

# 调试模式
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# 域名访问权限
ALLOWED_HOSTS = []

# app列表 系统默认数据位置不可更改，如要添加，加置最后
# Application definition
INSTALLED_APPS = [
    # 内置的后台管理系统
    'django.contrib.admin',
    # 内置的用户认证系统
    'django.contrib.auth',
    # 所有model元数组
    'django.contrib.contenttypes',
    # 会话 表示当前访问网站的用户身份
    'django.contrib.sessions',
    # 消息提示
    'django.contrib.messages',
    # 静态资源路径
    'django.contrib.staticfiles',
    # 注册自己的app
    'index',
    'douban',
]

# 中间件是request和response对象之间的钩子
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'MyDjango.urls'
# 模版设置
TEMPLATES = [
    {
        # 定义模版引擎
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 设置模版路径
        'DIRS': [],
        # 是否在app里查找模版文件
        'APP_DIRS': True,
        # 用于requestcontext上下文的调用函数
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

WSGI_APPLICATION = 'MyDjango.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
# 数据库默认是sqlite，django使用pymysql或者sqlclient去连接数据库
# pip3 install mysqlclient
# pip3 install pymysql
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
DATABASES = {
    # 默认数据库
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'testdb',
        'USER': 'root',
        'PASSWORD': 'guoyue19900205',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
    # 生产环境可能有第二个数据库
    # 'db1': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'testdb',
    #     'USER': 'root',
    #     'PASSWORD': 'guoyue19900205',
    #     'HOST': '127.0.0.1',
    #     'PORT': '3306',
    # }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators
# 密码验证
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
# https://docs.djangoproject.com/en/2.2/topics/i18n/
# 语言编码
LANGUAGE_CODE = 'en-us'
# 时区
TIME_ZONE = 'UTC'
# 国际化相关配置
USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
# 静态文件保存位置
STATIC_URL = '/static/'
STATICFILES_DIR=[
    os.path.join(BASE_DIR, '/static/'),
]