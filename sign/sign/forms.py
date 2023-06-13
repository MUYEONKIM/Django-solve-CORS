from django import forms
from .models import Image

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image',)
        
# 파일자체를 추가