from django import forms
from .models import Food, Quotes, Meditate


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

