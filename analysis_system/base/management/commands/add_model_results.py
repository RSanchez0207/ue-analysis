from django.core.management.base import BaseCommand
from base.models import EmotionOutput, SentimentOutput
from sqlalchemy import create_engine
from datetime import date, timedelta

import pandas as pd

class Command(BaseCommand):
    help = "Add SA and ER Results to Database"

    def handle(self, *args, **options):
        today = date.today()
        yesterday = today - timedelta(days = 1)

        # Create Filename
        filename_ER = "ER" + str(yesterday)
        filename_SA = "SA" + str(yesterday)
        df_ER = pd.read_csv("results/csv/" + str(filename_ER) + '.csv')
        df_SA = pd.read_csv("results/csv/" + str(filename_SA) + '.csv')
        
        # Connect to database
        engine = create_engine("mysql+pymysql://ueadmin@ue-analysis-mysqlserver:jhT))M=n)g'N26E)@ue-analysis-mysqlserver.mysql.database.azure.com/analysis_system")
        engine.connect()

        # Add Data
        df_ER.to_sql(EmotionOutput._meta.db_table, if_exists='replace', con=engine, index=False)
        df_SA.to_sql(SentimentOutput._meta.db_table, if_exists='replace', con=engine, index=False)
        