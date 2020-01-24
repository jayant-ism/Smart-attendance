from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    
    path('' , views.sub , name='sub') ,
    path('sub' , views.sub , name='sub') ,
    path('ok' , views.ok , name='ok') ,
    path('table' , views.table , name='table') ,
   
    path('floar' , views.floar , name='floar') ,
    path('details' , views.details , name='details') ,
   
    
    
]+static(settings.MEDIA_URL ,document_root = settings.MEDIA_ROOT ) # only for adding the pictures 
