import csv
import os
import django
import sys

os.chdir(".")
print("Current dir=", end=""), print(os.getcwd())

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print("BASE_DIR=", end=""), print(BASE_DIR)

sys.path.append(BASE_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")	# 1. 여기서 프로젝트명.settings입력
django.setup()
 
 # 위의 과정까지가 python manage.py shell을 키는 것과 비슷한 효과

from app.models import *	# 2. App이름.models

CSV_PATH = './거래내용_7월.csv'	# 3. csv 파일 경로


def insert_trading_month():

        
def insert_trading(): 
    with open(CSV_PATH, newline='', encoding='utf-8-sig') as csvfile:	# 4. newline =''
        data_reader = csv.DictReader(csvfile)

        for row in data_reader:
            print(row)

            Trading.objects.create(GU_CODE=row['지역코드'],
                                   DONG_NAME=row['법정동'],
                                   TRADE_DATE=row['거래일'],
                                   APT_NAME=row['아파트'],
                                   JI_NUM=row['지번'],
                                   AREA_SIZE=row['전용면적'],
                                   FLOOR=row['층'],
                                   BUILT_YEAR=row['건축년도'],
                                   TRADE_PRICE=row['거래금액'],
                                   TRADE_MONTH=row['거래일'].split("-")[1],)
