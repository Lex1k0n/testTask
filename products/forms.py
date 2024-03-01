from django import forms
from .models import ProductModel, LessonModels


class ProductForm(forms.ModelForm):

    class Meta:
        model = ProductModel
        fields = ('title', 'author', 'starttime', 'price', 'group_count', 'min_part', 'max_part')


class LessonForm(forms.ModelForm):

    class Meta:
        model = LessonModels
        fields = ('title', 'ref')
