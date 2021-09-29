from rest_framework import generics
from .models import Food, Quotes, Meditate, Post
from .serializers import FoodSerializer, QuoteSerializer, MeditateSerializer, PostSerializer

# Create your views here.
class FoodList(generics.ListCreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

class FoodDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

class QuoteList(generics.ListCreateAPIView):
    queryset = Quotes.objects.all()
    serializer_class = QuoteSerializer

class QuoteDetail(generics.RetrieveDestroyAPIView):
    queryset = Quotes.objects.all()
    serializer_class = QuoteSerializer

class MeditateList(generics.ListCreateAPIView):
    queryset = Meditate.objects.all()
    serializer_class = MeditateSerializer

class MeditateDetail(generics.RetrieveDestroyAPIView):
    queryset = Meditate.objects.all()
    serializer_class = MeditateSerializer

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer