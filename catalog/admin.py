from django.contrib import admin
from .models import Pipe, Valve

admin.site.site_header = "Управление"
admin.site.site_title = "Панель управления"
admin.site.index_title = "Главная страница"

admin.site.register(Pipe)
admin.site.register(Valve)