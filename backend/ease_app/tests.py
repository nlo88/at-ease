from rest_framework import serializers
from .models import Food, Quote, Meditate

class FoodSerializer(serializers.HyperlinkedModelSerializer):
    food = serializers.HyperlinkedRelatedField(
        view_name='food_detail',
        many=True,
        read_only=True
    )

    class Meta:
        model = Food
        fields = ('id','title', 'photo_url', 'benefits',)


class QuoteSerializer(serializers.HyperlinkedModelSerializer):
    quote = serializers.HyperlinkedRelatedField(
        view_name='quote_detail',
        many=False,
        read_only=True
    )

    class Meta:
        model = Quote
        fields = ('id', 'quote','author',)


class MediateSerializer(serializers.HyperlinkedModelSerializer):
    mediate = serializers.HyperlinkedRelatedField(
        view_name='meditate_detail',
        many=False,
        read_only=True
    )

    class Meta:
        model = Quote
        fields = ('id', 'curator','author','description', 'preview_url')


