# Generated by Django 4.0.4 on 2022-04-13 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmotionOutput',
            fields=[
                ('label', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('score', models.FloatField()),
            ],
            options={
                'db_table': 'emotionoutput',
            },
        ),
        migrations.CreateModel(
            name='SentimentOutput',
            fields=[
                ('comments', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('sentiments', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'sentimentoutput',
            },
        ),
        migrations.CreateModel(
            name='SurveyResponse',
            fields=[
                ('timestamp', models.CharField(max_length=40)),
                ('concerns', models.CharField(max_length=20)),
                ('generalDepartments', models.CharField(blank=True, max_length=100, null=True)),
                ('collegeDepartments', models.CharField(blank=True, max_length=100, null=True)),
                ('scoreOne', models.IntegerField()),
                ('scoreTwo', models.IntegerField()),
                ('scoreThree', models.IntegerField()),
                ('scoreFour', models.IntegerField()),
                ('scoreFive', models.IntegerField()),
                ('comments', models.CharField(max_length=300)),
                ('survey_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'surveyresponse',
            },
        ),
    ]
