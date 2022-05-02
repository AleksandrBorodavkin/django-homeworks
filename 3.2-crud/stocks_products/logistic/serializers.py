from rest_framework import serializers

from logistic.models import Product, StockProduct, Stock


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockProduct
        fields = ['product', 'quantity', 'price']


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    class Meta:
        model = Stock
        fields = '__all__'

    def create(self, validated_data):
        """create stock position"""
        positions = validated_data.pop('positions')
        stock = super().create(validated_data)
        for position in positions:
            StockProduct.objects.create(stock=stock, **position)
        return stock

    def update(self, instance, validated_data):
        """update stock position"""
        positions = validated_data.pop('positions')

        stock = super().update(instance, validated_data)
        for position in positions:
            sp, created = StockProduct.objects.get_or_create(
                product_id=position['product'].id,
                stock_id=stock.id, defaults=position)
            sp.quantity = position['quantity']
            sp.price = position['price']
            sp.save()
        return stock
