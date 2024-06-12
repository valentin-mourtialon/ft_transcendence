# Setup

`pip install --upgrade pip`

`pip install pipenv`

[`pipenv install`](https://docs.pipenv.org/basics/#example-pipenv-workflow)

[`pipenv install Django`](https://docs.djangoproject.com/en/5.0/topics/install/)

[`pipenv install "psycopg[binary]"`](https://www.psycopg.org/psycopg3/docs/basic/install.html)

```
pipenv shell

django-admin startproject projectName
cd projectName
python manage.py startapp featureName
```

replace
- `projectName` with the name of the project
- `featureName` with the name of a module/feature

# Views

Modify html files with:

```
[...]
{% load static %}

[...]
    <link rel="stylesheet" href="{% static 'assets/bootstrap/css/bootstrap.min.css' %}">
    <link rel="stylesheet" href="{% static 'assets/css/Footer-Basic-icons.css' %}">
[...]

<form>
    {% csrf_token %}
    [...]
</form>
```

# Database connection

Modify `DATABASES` variable in `projectName/settings.py`:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'db',
        'USER': 'user',
        'PASSWORD': 'password',
        'HOST': 'postgres',
        'PORT': '5432',
    }
}
```

# [Authentication](https://docs.djangoproject.com/en/5.0/ref/contrib/auth/)

## [Custom User Model](https://docs.djangoproject.com/en/5.0/topics/auth/customizing/#specifying-a-custom-user-model)

Source code:
- [AbstractBaseUser](https://github.com/django/django/blob/stable/5.0.x/django/contrib/auth/base_user.py#L59)
- [PermissionsMixin](https://github.com/django/django/blob/stable/5.0.x/django/contrib/auth/models.py#L242)
- [AbstractUser](https://github.com/django/django/blob/stable/5.0.x/django/contrib/auth/models.py#L334)

<!-- TODO -->

`AUTH_USER_MODEL = 'featureName.CustomUser'`

## [Custom User Manager](https://docs.djangoproject.com/en/5.0/topics/auth/customizing/#writing-a-manager-for-a-custom-user-model)

Source code:
- [BaseUserManager](https://github.com/django/django/blob/stable/5.0.x/django/contrib/auth/base_user.py#L23)
- [UserManager](https://github.com/django/django/blob/stable/5.0.x/django/contrib/auth/models.py#L136)

<!-- TODO -->

## [Custom Form](https://docs.djangoproject.com/en/5.0/topics/auth/customizing/#custom-users-and-the-built-in-auth-forms)

Source code:
- [UserCreationForm](https://github.com/django/django/blob/stable/5.0.x/django/contrib/auth/forms.py#L157)
- [UserChangeForm](https://github.com/django/django/blob/stable/5.0.x/django/contrib/auth/forms.py#L178)

<!-- TODO -->

## [Custom Admin](https://docs.djangoproject.com/en/5.0/topics/auth/customizing/#custom-users-and-django-contrib-admin)

Source code:
- [UserAdmin](https://github.com/django/django/blob/stable/5.0.x/django/contrib/auth/admin.py#L44)

<!-- TODO -->

## [Custom Backend](https://docs.djangoproject.com/en/5.0/topics/auth/customizing/#writing-an-authentication-backend)

<!-- TODO -->


## Password validation

https://docs.djangoproject.com/en/5.0/topics/auth/passwords/#password-validation
https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html

TODO: modify the validators so they don't refuse entered passwords but only displays the password strength



# References

[Project examples](https://github.com/topics/django-project)

[Django Social Network](https://github.com/manjurulhoque/django-social-network)
