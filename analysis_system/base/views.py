from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import timedelta,date

from .models import SentimentOutput, EmotionOutput, SurveyResponse, CENGGSentimentOutput, CENGGEmotionOutput
from .decorators import allowed_users

today = date.today()
yesterday = today - timedelta(days = 1)

format_today = today.strftime('%b-%d-%y')
format_yesterday = yesterday.strftime('%b-%d-%y')

static_dir_str_charts = "../../static/base/charts/"
filename_SA =  static_dir_str_charts + "SA" + str(yesterday) + ".png"
filename_ER =  static_dir_str_charts + "ERFIG" + str(yesterday) + ".png"
filename_ER_TOP = static_dir_str_charts + "ERFIGTOP" + str(yesterday) + ".png"

# College Overall Results
filename_Q1 = static_dir_str_charts + "LS" + str(yesterday) + "comm.png"
filename_Q2 = static_dir_str_charts + "LS" + str(yesterday) + "prof.png"
filename_Q3 = static_dir_str_charts + "LS" + str(yesterday) + "conn.png"
filename_Q4 = static_dir_str_charts + "LS" + str(yesterday) + "avail.png"
filename_Q5 = static_dir_str_charts + "LS" + str(yesterday) + "dpa.png"

# Engineering Results
cengg_filename_Q1 = static_dir_str_charts + "CENGGLS" + str(yesterday) + "comm.png"
cengg_filename_Q2 = static_dir_str_charts + "CENGGLS" + str(yesterday) + "prof.png"
cengg_filename_Q3 = static_dir_str_charts + "CENGGLS" + str(yesterday) + "conn.png"
cengg_filename_Q4 = static_dir_str_charts + "CENGGLS" + str(yesterday) + "avail.png"
cengg_filename_Q5 = static_dir_str_charts + "CENGGLS" + str(yesterday) + "dpa.png"
cengg_SA = static_dir_str_charts + "cengg_SA" + str(yesterday) + ".png"
cengg_ER = static_dir_str_charts + "cengg_ERFIG" + str(yesterday) + ".png"
cengg_ER_TOP = static_dir_str_charts + "cengg_ERFIGTOP" + str(yesterday) + ".png"

# General Overall Results
general_filename_Q1 = static_dir_str_charts + "LS" + str(yesterday) + "GENcomm.png"
general_filename_Q2 = static_dir_str_charts + "LS" + str(yesterday) + "GENprof.png"
general_filename_Q3 = static_dir_str_charts + "LS" + str(yesterday) + "GENconn.png"
general_filename_Q4 = static_dir_str_charts + "LS" + str(yesterday) + "GENavail.png"
general_filename_Q5 = static_dir_str_charts + "LS" + str(yesterday) + "GENdpa.png"

# Dashboard View
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','college','student'])
def dashboard(request):

    return render(request, 'dashboard.html', {'format_today': format_today,
                                            'format_yesterday': format_yesterday, 
                                            'filename_SA': filename_SA,
                                            'filename_ER': filename_ER,
                                            'filename_ER_TOP': filename_ER_TOP,
                                            'filename_Q1': filename_Q1,
                                            'filename_Q2': filename_Q2,
                                            'filename_Q3': filename_Q3,
                                            'filename_Q4': filename_Q4,
                                            'filename_Q5': filename_Q5,
                                            'cengg_filename_Q1': cengg_filename_Q1,
                                            'cengg_filename_Q2': cengg_filename_Q2,
                                            'cengg_filename_Q3': cengg_filename_Q3,
                                            'cengg_filename_Q4': cengg_filename_Q4,
                                            'cengg_filename_Q5': cengg_filename_Q5,
                                            'general_filename_Q1': general_filename_Q1,
                                            'general_filename_Q2': general_filename_Q2,
                                            'general_filename_Q3': general_filename_Q3,
                                            'general_filename_Q4': general_filename_Q4,
                                            'general_filename_Q5': general_filename_Q5,
                                            'cengg_SA': cengg_SA,
                                            'cengg_ER': cengg_ER,
                                            'cengg_ER_TOP': cengg_ER_TOP })


# Survey History View
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','college'])
def history(request):
    survey_list = SurveyResponse.objects.all()
    cengg_survey_list = SurveyResponse.objects.filter(collegeDepartments = 'College of Engineering (CENGG)')
    return render(request, 'survey-history.html', {'survey_list': survey_list, 
                                                   'format_today': format_today, 
                                                   'format_yesterday': format_yesterday,
                                                   'cengg_survey_list': cengg_survey_list,})

# Sentiment View
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','college','student'])
def sentiment(request):
    sentiment_list = SentimentOutput.objects.all()
    cengg_sentiment_list = CENGGSentimentOutput.objects.all()
    return render(request, 'sentiment-analysis.html',{'sentiment_list': sentiment_list, 
                                                        'format_today': format_today,
                                                        'format_yesterday': format_yesterday,
                                                        'filename_SA': filename_SA,
                                                        'cengg_sentiment_list': cengg_sentiment_list,
                                                        'cengg_SA': cengg_SA})

# Emotion View
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','college','student'])
def emotion(request):
    emotion_list = EmotionOutput.objects.all()
    cengg_emotion_list = CENGGEmotionOutput.objects.all()
    return render(request, 'emotion-recognition.html', {'emotion_list': emotion_list,
                                                        'format_today': format_today,
                                                        'format_yesterday': format_yesterday,
                                                        'filename_ER': filename_ER,
                                                        'filename_ER_TOP': filename_ER_TOP,
                                                        'cengg_ER': cengg_ER,
                                                        'cengg_ER_TOP': cengg_ER_TOP,
                                                        'cengg_emotion_list': cengg_emotion_list})

# Privacy Policy View
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','college','student'])
def privacy(request):
    return render(request, 'privacy-policy.html', {'format_today': format_today,'format_yesterday': format_yesterday })

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

