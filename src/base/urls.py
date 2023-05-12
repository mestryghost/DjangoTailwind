from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
<<<<<<< HEAD
    path('', views.home_page, name="home")
    # path('event/<str:pk>/', views.home_page, name="event")
=======
    path('', views.home_page, name="home"),
    path('event/<str:pk>/', views.event_page, name="event"),
    path('eventauth/<str:pk>/', views.event_authenticate, name="eventauth"),
    path('login/', views.login_page, name="login"),
    path('signin/', views.signin_page, name="signin"),
    path('aboutus/', views.aboutus_page, name="aboutus"),
>>>>>>> 3b3d3b382aff4fc0f01c50bcc88db5c983d6a460
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)