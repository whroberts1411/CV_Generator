
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from pdf import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('accept/', views.accept, name='accept'),
    path('cv/<int:id>/', views.cv, name='cv'),
    path('list/', views.list, name='list'),
    path('update/<int:id>/', views.update, name='update'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)