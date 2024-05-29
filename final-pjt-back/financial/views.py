import re
import os
import requests
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.conf import settings
from .models import DepositProducts, DepositOptions, SavingOptions, SavingProducts, FavoriteDepositProduct, FavoriteSavingProduct
from .serializers import DepositProductSerializer, DepositOptionSerializer, SavingProductSerializer, SavingOptionSerializer, FavoriteDepositProductSerializer, FavoriteSavingProductSerializer
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
import pandas as pd
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Max

# Create your views here.
api_key = settings.FINANCIAL_API_KEY
BASE_URL = 'http://finlife.fss.or.kr/finlifeapi/'

@api_view(['GET'])
def save_deposit_products(request):
    URL = BASE_URL + 'depositProductsSearch.json'
    params = {
        'auth': api_key,
        'topFinGrpNo': '020000',
        'pageNo': 1
    }
    response = requests.get(URL, params=params).json()
    for li in response['result']['baseList']:
        if DepositProducts.objects.filter(fin_prdt_cd=li['fin_prdt_cd']).exists():
            continue

        save_data = {
            'fin_prdt_cd': li['fin_prdt_cd'],
            'kor_co_nm': li['kor_co_nm'],
            'fin_prdt_nm': li['fin_prdt_nm'],
            'etc_note': li['etc_note'],
            'join_deny': li['join_deny'],
            'join_member': li['join_member'],
            'join_way': li['join_way'],
            'spcl_cnd': li['spcl_cnd']
        }
        serializer = DepositProductSerializer(data=save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
    for li in response['result']['optionList']:
        if DepositOptions.objects.filter(
                fin_prdt_cd=li['fin_prdt_cd'],
                intr_rate_tpye_nm=li['intr_rate_type_nm'],
                intr_rate=li['intr_rate'],
                intr_rate2=li['intr_rate2'],
                save_trm=li['save_trm']).exists():
            continue

        save_data2 = {
            'fin_prdt_cd': li['fin_prdt_cd'],
            'intr_rate_tpye_nm': li['intr_rate_type_nm'],
            'intr_rate': li['intr_rate'],
            'intr_rate2': li['intr_rate2'],
            'save_trm': li['save_trm'],
        }
        product = DepositProducts.objects.get(fin_prdt_cd=li['fin_prdt_cd'])
        serializer2 = DepositOptionSerializer(data=save_data2)
        if serializer2.is_valid(raise_exception=True):
            serializer2.save(product=product)
    return Response({"message": "성공"})

@api_view(['GET', 'POST'])
def deposit_products(request):
    if request.method == 'GET':
        depositProducts = DepositProducts.objects.all()
        serializers = DepositProductSerializer(depositProducts, many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
        serializers = DepositProductSerializer(data=request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def deposit_product_options(request, fin_prdt_cd):
    optionLists = DepositOptions.objects.filter(fin_prdt_cd=fin_prdt_cd)
    serializer = DepositOptionSerializer(optionLists, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def save_saving_products(request):
    URL = BASE_URL + 'savingProductsSearch.json'
    params = {
        'auth': api_key,
        'topFinGrpNo': '020000',
        'pageNo': 1
    }
    response = requests.get(URL, params=params).json()
    for li in response['result']['baseList']:
        if SavingProducts.objects.filter(fin_prdt_cd=li['fin_prdt_cd']).exists():
            continue

        save_data = {
            'fin_prdt_cd': li['fin_prdt_cd'],
            'kor_co_nm': li['kor_co_nm'],
            'fin_prdt_nm': li['fin_prdt_nm'],
            'etc_note': li['etc_note'],
            'join_deny': li['join_deny'],
            'join_member': li['join_member'],
            'join_way': li['join_way'],
            'spcl_cnd': li['spcl_cnd']
        }
        serializer = SavingProductSerializer(data=save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
    for li in response['result']['optionList']:
        if SavingOptions.objects.filter(
                fin_prdt_cd=li['fin_prdt_cd'],
                intr_rate_tpye_nm=li['intr_rate_type_nm'],
                intr_rate=li['intr_rate'],
                intr_rate2=li['intr_rate2'],
                save_trm=li['save_trm'],
                rsrv_type=li['rsrv_type'],
                rsrv_type_nm=li['rsrv_type_nm']).exists():
            continue

        save_data2 = {
            'fin_prdt_cd': li['fin_prdt_cd'],
            'intr_rate_tpye_nm': li['intr_rate_type_nm'],
            'intr_rate': li['intr_rate'],
            'intr_rate2': li['intr_rate2'],
            'save_trm': li['save_trm'],
            'rsrv_type': li['rsrv_type'],
            'rsrv_type_nm': li['rsrv_type_nm']
        }
        product = SavingProducts.objects.get(fin_prdt_cd=li['fin_prdt_cd'])
        serializer2 = SavingOptionSerializer(data=save_data2)
        if serializer2.is_valid(raise_exception=True):
            serializer2.save(product=product)
    return Response({"message": "성공"})

@api_view(['GET', 'POST'])
def saving_products(request):
    if request.method == 'GET':
        savingProducts = SavingProducts.objects.all()
        serializers = SavingProductSerializer(savingProducts, many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
        serializers = SavingProductSerializer(data=request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def saving_product_options(request, fin_prdt_cd):
    optionLists = SavingOptions.objects.filter(fin_prdt_cd=fin_prdt_cd)
    serializer = SavingOptionSerializer(optionLists, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

def read_excel_file(file_path):
    try:
        print(f"Reading file from: {file_path}")  # 파일 경로 출력
        df = pd.read_excel(file_path)
        print(df.columns)  # 열 이름을 출력하여 확인
        return df
    except Exception as e:
        raise Exception(f"Error reading {file_path}: {str(e)}")
    
def update_deposit_products_from_excel(file_path):
    df = read_excel_file(file_path)

    for _, row in df.iterrows():
        DepositProducts.objects.filter(fin_prdt_cd=row['fin_prdt_cd']).update(
            min_deposit_amount=row['min_deposit_amount'] if pd.notnull(row['min_deposit_amount']) else 0,
            max_deposit_amount=row['max_deposit_amount'] if pd.notnull(row['max_deposit_amount']) else 10000000000000.0,
            min_period=row['min_period'] if pd.notnull(row['min_period']) else 0,
            max_period=row['max_period'] if pd.notnull(row['max_period']) else 9999
        )

def update_saving_products_from_excel(file_path):
    df = read_excel_file(file_path)

    for _, row in df.iterrows():
        SavingProducts.objects.filter(fin_prdt_cd=row['fin_prdt_cd']).update(
            min_deposit_amount=row['min_deposit_amount'] if pd.notnull(row['min_deposit_amount']) else 0,
            max_deposit_amount=row['max_deposit_amount'] if pd.notnull(row['max_deposit_amount']) else 10000000000000.0,
            min_period=row['min_period'] if pd.notnull(row['min_period']) else 0,
            max_period=row['max_period'] if pd.notnull(row['max_period']) else 9999
        )

@csrf_exempt
def update_deposit_products(request):
    file_path = os.path.join(settings.BASE_DIR, 'financial', 'deposit.xlsx')
    try:
        update_deposit_products_from_excel(file_path)
        return JsonResponse({"message": "성공"}, status=200)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

@csrf_exempt
def update_saving_products(request):
    file_path = os.path.join(settings.BASE_DIR, 'financial', 'saving.xlsx')
    try:
        update_saving_products_from_excel(file_path)
        return JsonResponse({"message": "성공"}, status=200)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
    




@api_view(['GET'])
def top_deposit_products(request):
    product_ids = request.GET.get('product_ids')
    if product_ids:
        product_ids = product_ids.split(',')
        product_ids = [int(id.strip()) for id in product_ids]

    products = DepositProducts.objects.filter(id__in=product_ids)

    top_products = []
    for product in products:
        highest_option = DepositOptions.objects.filter(product=product).aggregate(Max('intr_rate2'))
        product_highest_rate = highest_option['intr_rate2__max']
        if product_highest_rate is not None:
            top_products.append((product, product_highest_rate))

    top_products = sorted(top_products, key=lambda x: x[1], reverse=True)[:3]

    response_data = []
    for product, rate in top_products:
        options = DepositOptions.objects.filter(product=product, intr_rate2=rate)
        response_data.append({
            'product': DepositProductSerializer(product).data,
            'options': DepositOptionSerializer(options, many=True).data
        })

    return Response(response_data, status=status.HTTP_200_OK)


@api_view(['GET'])
def top_saving_products(request):
    try:
        product_ids = request.GET.get('product_ids')
        if product_ids:
            product_ids = product_ids.split(',')
            product_ids = [int(id.strip()) for id in product_ids]

        products = SavingProducts.objects.filter(id__in=product_ids)

        top_products = []
        for product in products:
            highest_option = SavingOptions.objects.filter(product=product).aggregate(Max('intr_rate2'))
            product_highest_rate = highest_option['intr_rate2__max']
            if product_highest_rate is not None:
                top_products.append((product, product_highest_rate))

        top_products = sorted(top_products, key=lambda x: x[1], reverse=True)[:3]

        response_data = []
        for product, rate in top_products:
            options = SavingOptions.objects.filter(product=product, intr_rate2=rate)
            response_data.append({
                'product': SavingProductSerializer(product).data,
                'options': SavingOptionSerializer(options, many=True).data
            })

        return Response(response_data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def filtered_deposit_products(request):
    try:
        amount = float(request.GET.get('amount', 0))
        period = int(request.GET.get('period', 0))

        filtered_products = DepositProducts.objects.filter(
            min_deposit_amount__lte=amount,
            max_deposit_amount__gte=amount,
            min_period__lte=period,
            max_period__gte=period
        )

        products_with_options = []
        for product in filtered_products:
            options = DepositOptions.objects.filter(product=product)
            if options.exists():
                product_data = DepositProductSerializer(product).data
                product_data['options'] = DepositOptionSerializer(options, many=True).data
                products_with_options.append(product_data)

        return Response(products_with_options, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def filtered_saving_products(request):
    try:
        amount = float(request.GET.get('amount', 0))
        period = int(request.GET.get('period', 0))

        filtered_products = SavingProducts.objects.filter(
            min_deposit_amount__lte=amount,
            max_deposit_amount__gte=amount,
            min_period__lte=period,
            max_period__gte=period
        )

        products_with_options = []
        for product in filtered_products:
            options = SavingOptions.objects.filter(product=product)
            if options.exists():
                product_data = SavingProductSerializer(product).data
                product_data['options'] = SavingOptionSerializer(options, many=True).data
                products_with_options.append(product_data)

        return Response(products_with_options, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_favorite_deposit_products(request):
    user = request.user
    favorites = FavoriteDepositProduct.objects.filter(user=user)
    serializer = FavoriteDepositProductSerializer(favorites, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_favorite_deposit_product(request):
    user = request.user
    deposit_product_id = request.data.get('deposit_product')

    # 이미 존재하는지 확인
    if FavoriteDepositProduct.objects.filter(user=user, deposit_product_id=deposit_product_id).exists():
        return Response({"detail": "이미 관심 목록에 추가된 상품입니다."}, status=status.HTTP_400_BAD_REQUEST)

    # 새로운 관심 상품 추가
    serializer = FavoriteDepositProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def remove_favorite_deposit_product(request, product_id):
    user = request.user
    try:
        favorite = FavoriteDepositProduct.objects.get(user=user, deposit_product_id=product_id)
        favorite.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except FavoriteDepositProduct.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_favorite_saving_products(request):
    user = request.user
    favorites = FavoriteSavingProduct.objects.filter(user=user)
    serializer = FavoriteSavingProductSerializer(favorites, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_favorite_saving_product(request):
    user = request.user
    saving_product_id = request.data.get('saving_product')

    # 이미 존재하는지 확인
    if FavoriteSavingProduct.objects.filter(user=user, saving_product_id=saving_product_id).exists():
        return Response({"detail": "이미 관심 목록에 추가된 상품입니다."}, status=status.HTTP_400_BAD_REQUEST)

    # 새로운 관심 상품 추가
    serializer = FavoriteSavingProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def remove_favorite_saving_product(request, product_id):
    user = request.user
    try:
        favorite = FavoriteSavingProduct.objects.get(user=user, saving_product_id=product_id)
        favorite.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except FavoriteSavingProduct.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
