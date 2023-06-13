# Back

# 실행할 가상환경에서 작성 해주세요.
```
pip install django-allauth django-rest-auth djangorestframework djangorestframework-jwt django-filter
```

# setting.py와 같은 폴더에 my_setting.py를 추가해주세요
#### my_setting.py
```
DATABASES = {
    'default' : {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_39',
        'USER': 'root',
        'PASSWORD': 'aivle',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
SECRET_KEY = "django-insecure-+d@0e(gyc7+e8yl6=5*jab^6hcj=*bj^=ub!xcnw$$h3&n%r4o"
```
### SECRET_KEY는 SETTING.py에 있는 SECRET_KEY를 복사해서 붙여넣어 주세요
