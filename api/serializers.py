from rest_framework.serializers import ModelSerializer
from .models import AccountCreationDetails, ProductDetails

class AccountSerializer(ModelSerializer):
    class Meta:
        model=AccountCreationDetails
        fields='__all__'


class ProductDetailSerializer(ModelSerializer):
    class Meta:
        model=ProductDetails
        fields='__all__'