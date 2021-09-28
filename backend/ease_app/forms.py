from django import forms
from .models import Food, Quotes, Meditate, Post


class FoodForm(forms.ModelForm):
    
    class Meta:
        model = Food
        fields = ('title',' photo_url', 'benefits')


class QuoteForm(forms.ModelForm):
    
    class Meta:
        model = Quotes
        fields = ('title', 'author')
        

class MeditateForm(forms.ModelForm):
    
    class Meta:
        model = Meditate
        fields = ('title',' moderator', 'description','preview_url')


class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ('title',' description')

