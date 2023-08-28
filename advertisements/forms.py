from django import forms
from .models import Advertisement
from django.forms import ModelForm

# class AdvertisementForm(forms.Form):
#     title = forms.CharField(max_length=60, widget=forms.TextInput(
#         attrs={'class': 'form-control'}
#     ))
#     description = forms.CharField(widget=forms.Textarea(
#         attrs={'class': 'form-control'}
#     ))
#     price = forms.DecimalField(widget=forms.NumberInput(
#         attrs={'class': 'form-control'}
#     ))
#     auction = forms.BooleanField(required=False, widget=forms.CheckboxInput(
#         attrs={'class': 'form-check-input'}
#     ))
#     image = forms.ImageField(widget=forms.FileInput(
#         attrs={'class': 'form-control'}
#     ))

class AdvertisementForm(ModelForm):
    class Meta:
        model = Advertisement
        fields = ['title', 'description', 'price', 'auction', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'auction': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'})
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if title.startswith('?'):
            raise forms.ValidationError("Заголовок не может начинаться с вопросительного знака.")
        return title
