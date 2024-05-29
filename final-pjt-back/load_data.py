import json
import os
import django

# Django 프로젝트 설정 파일 로드
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'richbeats.settings')
django.setup()

from django.core.management import call_command

def load_data(file_name):
    if os.path.exists(file_name):
        print(f'Loading data from {file_name}...')
        call_command('loaddata', file_name)
        print(f'Data loaded from {file_name}')
    else:
        print(f'File {file_name} does not exist')

if __name__ == "__main__":
    json_files = [
        'exchangerate_data.json',
        'deposit_products_data.json',
        'deposit_options_data.json',
        'saving_products_data.json',
        'saving_options_data.json'
    ]

    for file_name in json_files:
        load_data(file_name)
