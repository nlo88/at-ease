from rest_framework import serializers
from .models import Food, Quotes , Meditate, Post

class FoodSerializer(serializers.HyperlinkedModelSerializer):
    # food = serializers.HyperlinkedRelatedField(
    #     view_name='food_detail',
    #     many=True,
    #     read_only=True
    # )
    class Meta:
        model = Food
        fields = ('id', 'title', 'photo_url','benefits', )


class QuoteSerializer(serializers.HyperlinkedModelSerializer):
    # quotes = serializers.HyperlinkedRelatedField(
    #     view_name='quote_detail',
    #     many=False,
    #     read_only=True
    # )

    class Meta:
        model = Quotes
        fields = ('id', 'quote','author',)


class MeditateSerializer(serializers.HyperlinkedModelSerializer):
    # quotes = serializers.HyperlinkedRelatedField(
    #     view_name='meditate_detail',
    #     many=False,
    #     read_only=True
    # )

    class Meta:
        model = Meditate
        fields = ('id', 'title','moderator','preview_url',)


class PostSerializer(serializers.HyperlinkedModelSerializer):
    # quotes = serializers.HyperlinkedRelatedField(
    #     view_name='post_detail',
    #     many=False,
    #     read_only=True
    # )

    class Meta:
        model = Post
        fields = ('id', 'title','message','author',)