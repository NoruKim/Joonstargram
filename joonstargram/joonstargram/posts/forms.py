from django import forms
from .models import *
from joonstargram.users.models import *

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["caption", "image"]

        labels = {
            "caption": "キャプション",
            "image": "写真",
        }

class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["caption"]

        labels = {
            "caption": "キャプション",
        }

class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea, label="")

    class Meta:
        model = Comment
        fields = ["content"]

class ProfileForm(forms.ModelForm):
    email = forms.EmailField(disabled=True, label='メールアドレス')
    name = forms.CharField(disabled=True, label='氏名')

    class Meta:
        model = User
        fields = [
            'email', 'name', 'username',
            'profile_photo', 'website',
            'intro', 'phone_number', 'gender',
            ]

        labels = {
            "username": "使用者名",
            "profile_photo": "写真",
            "website": "ウェブアドレス",
            "intro": "紹介",
            "phone_number": "電話番号",
            "gender": "性別",
        }
