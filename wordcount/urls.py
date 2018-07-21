from django.urls import path
from . import views


urlpatterns = [
    # path('admin/', admin.site.urls),

    path('', views.homepage, name = 'home'),
    path('wordcount/', views.count, name = 'count'),
    path('about-pages/', views.aboutpage, name = 'about')

]
