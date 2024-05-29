import json
import os
import django

# Django 프로젝트 설정 파일 로드
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'richbeats.settings')
django.setup()

from financial.models import DepositOptions
from django.core.serializers import serialize

# 데이터 덤프
data = serialize('json', DepositOptions.objects.all(), indent=4)

# UTF-8 인코딩으로 파일 저장
with open('deposit_options_data.json', 'w', encoding='utf-8') as f:
    f.write(data)

print("Data dumped successfully.")
