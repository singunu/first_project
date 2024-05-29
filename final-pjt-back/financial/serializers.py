from rest_framework import serializers
from .models import DepositProducts, DepositOptions, SavingProducts, SavingOptions, FavoriteDepositProduct, FavoriteSavingProduct

class DepositProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositProducts
        fields = '__all__'

class DepositOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositOptions
        fields = '__all__'
        read_only_fields = ('product',)

class SavingProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingProducts
        fields = '__all__'

class SavingOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingOptions
        fields = '__all__'
        read_only_fields = ('product',)

class FavoriteDepositProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteDepositProduct
        fields = ['user', 'deposit_product']  # 사용자와 제품 필드만 포함

    def validate_user(self, value):
        # 유효성 검사를 통해 사용자 필드가 비어 있는지 확인
        if value is None:
            raise serializers.ValidationError("This field is required.")
        return value
    
class FavoriteSavingProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteSavingProduct
        fields = ['user', 'saving_product']  # 사용자와 제품 필드만 포함

    def validate_user(self, value):
        # 유효성 검사를 통해 사용자 필드가 비어 있는지 확인
        if value is None:
            raise serializers.ValidationError("This field is required.")
        return value