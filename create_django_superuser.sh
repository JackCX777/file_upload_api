#! /usr/bin/env bash


# Using bash/sh

#echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser($PROD_USER,$PROD_USER_EMAIL,$PROD_USER_PASS)" | python manage.py shell
#echo "from django.contrib.auth.models import User; User.objects.create_superuser($PROD_USER,$PROD_USER_EMAIL,$PROD_USER_PASS)" | python manage.py shell
#&& source create_superuser_prod.sh



# Using python command

#RUN python -c "import django; django.setup(); \
#   from django.contrib.auth.management.commands.createsuperuser import get_user_model; \
#   get_user_model()._default_manager.db_manager('$DJANGO_DB_NAME').create_superuser( \
#   username='$DJANGO_SU_NAME', \
#   email='$DJANGO_SU_EMAIL', \
#   password='$DJANGO_SU_PASSWORD')"

#python manage.py shell -c "from django.contrib.auth.models import User; \
#                           User.objects.filter(username='admin1').exists() or \
#                           User.objects.create_superuser('admin1',
#                           'admin1@example.com', 'admin1')"



# Using Django

#DJANGO_SUPERUSER_USERNAME=testuser \
#DJANGO_SUPERUSER_EMAIL
#DJANGO_SUPERUSER_PASSWORD=testpass \
#python manage.py createsuperuser --noinput