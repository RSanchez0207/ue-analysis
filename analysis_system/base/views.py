from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import timedelta,date

from .models import SentimentOutput, EmotionOutput, SurveyResponse

# Dashboard View
@login_required(login_url='login')
def dashboard(request):
    today = date.today()
    yesterday = today - timedelta(days = 1)
    format = yesterday.strftime('%b-%d-%y')
    return render(request, 'dashboard.html', {'format': format})

# Survey History View
@login_required(login_url='login')
def history(request):
    today = date.today()
    yesterday = today - timedelta(days = 1)
    survey_list = SurveyResponse.objects.all()
    format = yesterday.strftime('%b-%d-%y')
    return render(request, 'survey-history.html', {'survey_list': survey_list, 'format': format})

# Sentiment View
@login_required(login_url='login')
def sentiment(request):
    sentiment_list = SentimentOutput.objects.all()
    today = date.today()
    yesterday = today - timedelta(days = 1)
    format = yesterday.strftime('%b-%d-%y')
    return render(request, 'sentiment-analysis.html',{'sentiment_list': sentiment_list, 'format': format })

# Emotion View
@login_required(login_url='login')
def emotion(request):
    emotion_list = EmotionOutput.objects.all()
    today = date.today()
    yesterday = today - timedelta(days = 1)
    format = yesterday.strftime('%b-%d-%y')
    return render(request, 'emotion-recognition.html', {'emotion_list': emotion_list, 'format': format})

# Privacy Policy View
@login_required(login_url='login')
def privacy(request):
    today = date.today()
    yesterday = today - timedelta(days = 1)
    format = yesterday.strftime('%b-%d-%y')
    return render(request, 'privacy-policy.html', {'format': format})

# Login Page View
def loginPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')

        else:
            messages.success(request,("Incorrect Username or Password Detected, Please try again."))
            return render(request, 'login.html')
    
    else:
        return render(request, 'login.html')

# Logout View
def logoutUser(request):
    logout(request)
    return redirect('login')

