"""
Django settings for reservation project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 's1d&xdqm#2gbz$=y^tt7c*@j1-1pw$p)$3i6b80fhi%6$8jagy'

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
    'login',  # allauth의 템플릿을 오버라이트 하기 위해 allauth 보다 위 쪽에 위치
    'booking',
    'widget_tweaks',  # 폼 위젯, 인풋태그를 수정하기 위한 패키지

    # Allauth Settings
    'django.contrib.sites', # 비슷한 컨텐츠나 사이트가 여러개 필요할 때
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.naver',
    'allauth.socialaccount.providers.kakao',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'reservation.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'reservation.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    # 기본 제공 유효성검사
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

    # 커스터마이징 유효성검사
    # {
    #     'NAME': 'login.validators.CustomPasswordValidator',
    # }
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'ko'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

# Auth Settings

AUTH_USER_MODEL = "login.User"

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

ACCOUNT_SIGNUP_REDIRECT_URL = ""
LOGIN_REDIRECT_URL = "../booking"
ACCOUNT_LOGOUT_ON_GET = True  # 로그아웃 누르면 로그아웃 페이지 거치지 않고 바로 실행
ACCOUNT_LOGOUT_URL = "index"
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_SESSION_REMEMBER = True
# SESSION_COOKIE_AGE = 3600  # 로그인 유지 기간(초 단위)
ACCOUNT_SIGNUP_FORM_CLASS = "login.forms.SignupForm" # 회원가입시 커스텀필드 추가하고 싶을 때
ACCOUNT_PASSWORD_INPUT_RENDER_VALUE = True # 회원가입 오류발생시 비밀번호 초기화하지 않기
ACCOUNT_EMAIL_VARIFICATION = "optional" # 이메일 인증 방법 (mandatory, optional, none)
ACCOUNT_CONFIRM_EMAIL_ON_GET = True # 이메일 인증링크 클릭시 바로 인증되게 끔
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = "account_email_confirmation_done" 
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = "account_email_confirmation_done"
PASSWORD_RESET_TIMEOUT_DAYS = 3 # 비밀번호 초기화시 인증링크의 유효기간
ACCOUNT_EMAIL_SUBJECT_PREFIX = ""  # allauth 이메일인증 메일에서 도메인이 앞에 붙는거 없애주기

# Allauth: social login settings
SOCIALACCOUNT_LOGIN_ON_GET = True
SOCIALACCOUNT_AUTO_SIGNUP = True



# Eamil Settings
EMAIL_BACKENDS = "django.core.mail.backends.console.EmailBackend"

SOCIALACCOUNT_PROVIDERS = {
    'kakao': {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        'APP': {
            'client_id': '137fbb43f322c27b892072c70a3062c6',
            'secret': 'M955Y1lAyztgalErEP7D3KawwdfDSkAK',
            'key': ''
        }
    },
    'naver': {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        'APP': {
            'client_id': 'hdFKYSFJToB97ZEocnGC',
            'secret': '0YH_sbwBkc',
            'key': ''
        }
    }
}