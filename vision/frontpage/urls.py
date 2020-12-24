from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'frontpage'
urlpatterns = [
    path('', views.index, name='home'),
    # path('', views.clothes, name='clothes'),
    path('list/', views.show_list, name='list'),
    path('result/',views.result,name='result'),
    path('api/', views.image_list, name='image_list')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
