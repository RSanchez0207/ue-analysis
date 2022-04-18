from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import timedelta,date

from .models import SentimentOutput, EmotionOutput, SurveyResponse
from .decorators import allowed_users, unauthenticated_user

today = date.today()
yesterday = today - timedelta(days = 1)

format = yesterday.strftime('%b-%d-%y')
static_dir_str_charts = "../../static/base/charts/"
filename_SA =  static_dir_str_charts + "SA" + str(yesterday) + ".png"
filename_ER =  static_dir_str_charts + "ERFIG" + str(yesterday) + ".png"
filename_ER_TOP = static_dir_str_charts + "ERFIGTOP" + str(yesterday) + ".png"

filename_Q1 = static_dir_str_charts + "LS" + str(yesterday) + "comm.png"
filename_Q2 = static_dir_str_charts + "LS" + str(yesterday) + "prof.png"
filename_Q3 = static_dir_str_charts + "LS" + str(yesterday) + "conn.png"
filename_Q4 = static_dir_str_charts + "LS" + str(yesterday) + "avail.png"
filename_Q5 = static_dir_str_charts + "LS" + str(yesterday) + "dpa.png"

# Dashboard View
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','college','student'])
def dashboard(request):

    return render(request, 'dashboard.html', {'format': format, 
                                            'filename_SA': filename_SA,
                                            'filename_ER': filename_ER,
                                            'filename_ER_TOP': filename_ER_TOP,
                                            'filename_Q1': filename_Q1,
                                            'filename_Q2': filename_Q2,
                                            'filename_Q3': filename_Q3,
                                            'filename_Q4': filename_Q4,
                                            'filename_Q5': filename_Q5,})

# Survey History View
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','college'])
def history(request):
    survey_list = SurveyResponse.objects.all()
    return render(request, 'survey-history.html', {'survey_list': survey_list, 'format': format})

# Sentiment View
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','college','student'])
def sentiment(request):
    sentiment_list = SentimentOutput.objects.all()
    return render(request, 'sentiment-analysis.html',{'sentiment_list': sentiment_list, 
                                                        'format': format,
                                                        'filename_SA': filename_SA})

# Emotion View
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','college','student'])
def emotion(request):
    emotion_list = EmotionOutput.objects.all()
    return render(request, 'emotion-recognition.html', {'emotion_list': emotion_list,
                                                        'format': format,
                                                        'filename_ER': filename_ER,
                                                        'filename_ER_TOP': filename_ER_TOP})

# Privacy Policy View
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','college','student'])
def privacy(request):
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

