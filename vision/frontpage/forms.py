from django import forms
from .models import Image

class ImageForm(forms.ModelForm):
    name = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={
            "placeholder": "사용자 이름을 입력해주세요",
            "aria-label":"Large",
            "class":"form-control-lg",
            
        })
    )
    class Meta:
        model = Image
        fields = ('name', 'image', )

