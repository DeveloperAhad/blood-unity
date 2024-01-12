from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image', 'blood_group', 'division', 'district', 'upazila', 'union', 'post_type']