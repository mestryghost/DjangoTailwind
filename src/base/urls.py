from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.home_page, name="home")
    # path('event/<str:pk>/', views.home_page, name="event")
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)