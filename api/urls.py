from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.getRoutes),
    path('users/', views.GetUsers),
    path('users/<str:key>/', views.GetUser),
    path('AuthenticateUser/',views.AuthenticateUser),
    path('CreateUser/',views.CreateUser),
    path('Products/',views.GetProducts),
    path('Products/id/',views.GetProduct)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
