from django.contrib import admin
from django.urls import path
from about.views import index
from blog.views import index
from faperta.views import index
from feb.views import index
from fh.views import index
from fisip.views import index
from fk.views import index
from fkip.views import index
from ft.views import index
from home.views import index
from pascasarjana.views import index
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', index ),
    path('blog/', index ),
    path('faperta/', index ),
    path('feb/', index ),
    path('fh/', index ),
    path('fisip/', index ),
    path('fk/', index ),
    path('fkip/', index ),
    path('ft/', index ),
    path('home/', index ),
    path('pascasarjana/', index ),
    path('views/', index)
    
    
]
