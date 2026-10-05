from rest_framework import serializers
from .models import Product
class ProductSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        required = True,
        allow_blank = False,
        error_messages = {
            "blank" :'Product Name cannot be empty',
            "required" :'Product Name is required'
        } 
    )
    
    price = serializers.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    def validate_price(self,price):
            if price<=0:
                raise serializers.ValidationError("Price must be greater than zero !!")
            return price

    stock = serializers.IntegerField()
        
    def validate_stock(self,stock):
         if stock<0:
                raise serializers.ValidationError('Stock cannot be less than zero !!')
         return stock
    class Meta:
        model = Product
        fields = ['id','name','description','price','stock']
