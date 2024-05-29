from django.http import JsonResponse
from django.views import View
from .models import ExchangeRate
import requests
from decimal import Decimal
from django.conf import settings
from rest_framework.decorators import api_view
from .serializers import exchangeSerializer
from rest_framework.response import Response
from rest_framework import status

# class ExchangeRateView(View):
#     def get(self, request):
#         api_key = settings.EXCHANGE_RATE_API_KEY
#         api_url = f'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey={api_key}&searchdate=20180102&data=AP01'

#         response = requests.get(api_url)

#         if response.status_code == 200:
#             data = response.json()
#             for entry in data:
#                 # API에서 가져온 데이터를 DecimalField에 맞게 변환하여 저장
#                 exchange_rate = ExchangeRate.objects.create(
#                     cur_unit=entry['cur_unit'],
#                     cur_nm=entry['cur_nm'],
#                     ttb=Decimal(entry['ttb'].replace(',', '')),  # 쉼표를 제거하고 Decimal 형태로 변환
#                     tts=Decimal(entry['tts'].replace(',', '')),  # 쉼표를 제거하고 Decimal 형태로 변환
#                     deal_bas_r=Decimal(entry['deal_bas_r'].replace(',', '')),  # 쉼표를 제거하고 Decimal 형태로 변환
#                     bkpr=Decimal(entry['bkpr'].replace(',', '')),  # 쉼표를 제거하고 Decimal 형태로 변환
#                     yy_efee_r=Decimal(entry['yy_efee_r'].replace(',', '')),  # 쉼표를 제거하고 Decimal 형태로 변환
#                     ten_dd_efee_r=Decimal(entry['ten_dd_efee_r'].replace(',', '')),  # 쉼표를 제거하고 Decimal 형태로 변환
#                     kftc_deal_bas_r=Decimal(entry['kftc_deal_bas_r'].replace(',', '')),  # 쉼표를 제거하고 Decimal 형태로 변환
#                     kftc_bkpr=Decimal(entry['kftc_bkpr'].replace(',', '')),  # 쉼표를 제거하고 Decimal 형태로 변환
#                 )
#             return JsonResponse({'message': 'Exchange rates saved successfully'})
#         else:
#             return JsonResponse({'error': 'Failed to fetch exchange rates'}, status=500)


api_key = settings.EXCHANGE_RATE_API_KEY
@api_view(['GET'])
def save_exchange_rate(request):
    
    api_url = f'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey={api_key}&searchdate=20180102&data=AP01'

    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        for entry in data:
            if len(ExchangeRate.objects.filter(cur_unit=entry['cur_unit'])) >= 1:
                continue
            # API에서 가져온 데이터를 DecimalField에 맞게 변환하여 저장
            exchange_rate = ExchangeRate.objects.create(
                cur_unit=entry['cur_unit'],
                cur_nm=entry['cur_nm'],
                ttb=Decimal(entry['ttb'].replace(',', '')),  # 쉼표를 제거하고 Decimal 형태로 변환
                tts=Decimal(entry['tts'].replace(',', '')),  # 쉼표를 제거하고 Decimal 형태로 변환
                deal_bas_r=Decimal(entry['deal_bas_r'].replace(',', '')),  # 쉼표를 제거하고 Decimal 형태로 변환
                bkpr=Decimal(entry['bkpr'].replace(',', '')),  # 쉼표를 제거하고 Decimal 형태로 변환
                yy_efee_r=Decimal(entry['yy_efee_r'].replace(',', '')),  # 쉼표를 제거하고 Decimal 형태로 변환
                ten_dd_efee_r=Decimal(entry['ten_dd_efee_r'].replace(',', '')),  # 쉼표를 제거하고 Decimal 형태로 변환
                kftc_deal_bas_r=Decimal(entry['kftc_deal_bas_r'].replace(',', '')),  # 쉼표를 제거하고 Decimal 형태로 변환
                kftc_bkpr=Decimal(entry['kftc_bkpr'].replace(',', '')),  # 쉼표를 제거하고 Decimal 형태로 변환
            )
        return JsonResponse({'message': 'Exchange rates saved successfully'})
    else:
        return JsonResponse({'error': 'Failed to fetch exchange rates'}, status=500)


@api_view(['GET', 'POST'])
def get_exchange_rate(request):
    if request.method == 'GET':
        exchangeRate = ExchangeRate.objects.all()
        serializers = exchangeSerializer(exchangeRate, many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
        serializers = exchangeSerializer(data=request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
