from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginPage, name="login"),
    path("logout/",views.logoutUser, name="logout"),

    path('dashboard/', views.dashboard, name="dashboard"),
    path('survey-history/', views.history, name="survey-history"),
    path('sentiment-analysis/', views.sentiment, name="sentiment-analysis"),
    path('emotion-recognition/', views.emotion, name="emotion-recognition"),
    path('privacy-policy/', views.privacy, name="privacy-policy"),
]

