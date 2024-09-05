from rest_framework import serializers


class ProductSerializer(serializers.Serializer):

    name = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=255)
    price = serializers.FloatField()
    inventory_count = serializers.IntegerField()
    category = serializers.CharField(max_length=100)
    popularity_score = serializers.FloatField(read_only=True)
    sales = serializers.IntegerField(required=False, default=0)
