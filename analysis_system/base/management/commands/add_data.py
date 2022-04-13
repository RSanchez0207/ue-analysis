import pandas as pd
from django.core.management.base import BaseCommand
from base.models import SurveyResponse
from sqlalchemy import create_engine
from datetime import date, timedelta

class Command(BaseCommand):
    help = "A command to add data from Spreadsheet to DB"

    def handle(self, *args, **options):
        today = date.today()
        yesterday = today - timedelta(days = 1)        
        filename_SR = "SR" + str(yesterday)

        sheetID = '1i73xYnbaWpPsx6RjaUljmC3zIo8VP0muRzls8-lP8MY'
        df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheetID}/export?format=csv")
        
        engine = create_engine("mysql+pymysql://ueadmin@ue-analysis-mysqlserver:jhT))M=n)g'N26E)@ue-analysis-mysqlserver.mysql.database.azure.com/analysis_system")
        engine.connect()
        df.to_csv("results/csv/" + str(filename_SR) + '.csv')
        df.to_sql(SurveyResponse._meta.db_table, if_exists='replace', con=engine, index=False)