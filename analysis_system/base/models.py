from django.db import models

# Survey Table
class SurveyResponse(models.Model):
    timestamp = models.CharField(max_length=40)
    concerns = models.CharField(max_length=20)
    generalDepartments = models.CharField(max_length=100, blank=True, null=True)
    collegeDepartments = models.CharField(max_length=100, blank=True, null=True)
    scoreOne = models.IntegerField()
    scoreTwo = models.IntegerField()
    scoreThree = models.IntegerField()
    scoreFour = models.IntegerField()
    scoreFive = models.IntegerField()
    comments = models.CharField(max_length=300)
    survey_id = models.CharField(max_length=10, primary_key=True, null=False, blank=False)
    class Meta:
        db_table = "surveyresponse"
def __str__(self):
    return self.comments

# Emotion Recognition Output from ER
class EmotionOutput(models.Model):
    label = models.CharField(max_length=20, primary_key=True)
    score = models.FloatField()
    comments = models.CharField(max_length=100, null=True)
    class Meta:
        db_table = "emotionoutput"
def __str__(self):
    return self.label

# Sentiment Output from SA
class SentimentOutput(models.Model):
    comments = models.CharField(max_length=100, primary_key=True)
    sentiments = models.CharField(max_length=30)
    class Meta:
        db_table = "sentimentoutput"
def __str__(self):
    return self.label

# CENGG Sentiment Output from SA
class CENGGSentimentOutput(models.Model):
    comments = models.CharField(max_length=100, primary_key=True)
    sentiments = models.CharField(max_length=30)
    class Meta:
        db_table = "cenggsentimentoutput"
def __str__(self):
    return self.label

# CENGG ER Output from ER
class CENGGEmotionOutput(models.Model):
    label = models.CharField(max_length=100)
    score = models.CharField(max_length=30)
    comments = models.CharField(max_length=100, primary_key=True)
    class Meta:
        db_table = "cenggemotionoutput"
def __str__(self):
    return self.label