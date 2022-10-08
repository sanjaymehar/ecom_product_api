from rest_framework import serializers
from .models import Product

#product serilizer
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'