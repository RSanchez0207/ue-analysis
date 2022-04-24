from django.core.management.base import BaseCommand

# Sentiment Analysis
import pandas as pd
from datetime import date, timedelta
import seaborn as sns
import matplotlib.pyplot as plt

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

class Command(BaseCommand):
    help = "A command to run Sentiment Analysis for CENGG Department"

    def handle(self, *args, **options):
        def sentiment_score(sentence):
            sid_obj = SentimentIntensityAnalyzer()

            sentiment_dict = sid_obj.polarity_scores(sentence)
            
            if sentiment_dict['compound'] >= 0.05 :
                result = "Positive"
        
            elif sentiment_dict['compound'] <= - 0.05 :
                result = "Negative"

            else :
                result = "Neutral"

            return result

        # Open File
        sheetID = '1i73xYnbaWpPsx6RjaUljmC3zIo8VP0muRzls8-lP8MY'
        df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheetID}/export?format=csv")
        df["comments"].fillna("None", inplace=True)

        today = date.today()
        yesterday = today - timedelta(days = 1)
        cengg_filename = "cengg_SA" + str(yesterday)
        static_dir_str_charts = "base/static/base/charts/"

        # Rename Value
        df.loc[df['collegeDepartments'] == 'College of Engineering (CENGG)', 'collegeDepartments'] = 'CENGG'

        # Select all CENGG
        dfEngineering = df.loc[df['collegeDepartments'] == 'CENGG']
        dfEngineering["sentiments"] = dfEngineering["comments"].apply(sentiment_score)
        dfEngineering[['sentiments','comments']].to_csv("results/csv/" + str(cengg_filename) + '.csv', index=False)

        df_cengg_SA = pd.read_csv("results/csv/" + str(cengg_filename) + '.csv')
        cengg_count = df_cengg_SA['sentiments'].value_counts()
        cengg_mylabels = df_cengg_SA['sentiments'].unique().tolist()

        cengg_colors = sns.color_palette('bright')[0:5]

        plt.pie(cengg_count, labels=cengg_mylabels, startangle=90, colors=cengg_colors)

        # add a circle at the center to transform it in a donut chart
        my_circle=plt.Circle( (0,0), 0.7, color='white')
        p=plt.gcf()
        p.gca().add_artist(my_circle)

        # Add Legend
        plt.legend(title='Feedback Polarity', loc=10)

        plt.savefig(static_dir_str_charts + cengg_filename + '.png')