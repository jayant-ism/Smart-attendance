from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    
    path('' , views.index , name='index') ,
    path('submit' , views.submit, name='submit') ,
    path('start' , views.start, name='start') ,
    path('server' , views.server, name='server') ,
    path('disp' , views.disp, name='disp') ,
    path('attend' , views.attend, name='attend') ,
    
    
]+static(settings.MEDIA_URL ,document_root = settings.MEDIA_ROOT ) # only for adding the pictures 
