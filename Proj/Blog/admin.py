from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register(books_user)
admin.site.register(poems_user)
admin.site.register(musics_user)



# Terminal --> cd  p4/Proj  --> python manage.py createsuperuser
# username : farzan (mitooni har chi bezari) --> Email address: farzanrahmani70@gmail.com
# Password : 23572357  --> Bypass password validation and create user anyway? [y/N]:
# --> y --. Superuser created successfully. -->from .models import *
# --> admin.site.Register(User)
# --> 127.0.0.1:8000/admin/ --> username va password --> login --> django administration