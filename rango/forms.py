from django import forms
from django.contrib.auth.models import User
from rango.models import Page, Category, UserProfile
from django.template.defaultfilters import slugify
from django import forms


class CategoryForm(forms.ModelForm):
    name = forms.CharField(
        max_length=128, help_text="Please Enter the Categor Name")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Category
        fields = ('name',)


class PageForm(forms.ModelForm):
    titile = forms.CharField(max_length=128,
                             help_text="Please Enter the title of page")
    url = forms.URLField(
        max_length=200, help_text="pelase Enter the URL of page.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Page
        fields = ('titile', 'url',)
        #exclude = ('category',)


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')


class CategoryEditForm(forms.ModelForm):
    name = forms.CharField(
        max_length=128, help_text='Update the name of Category', initial='name')
    views = forms.IntegerField(
        help_text='Update the views of Category', initial='views')
    likes = forms.IntegerField(
        help_text='Update the likes of Category', initial='likes')
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Category
        fields = ('name', 'views', 'likes')

class UserProfileForm(forms.ModelForm):
    website = forms.URLField(required=False)
    picture = forms.ImageField(required=False)
    class Meta:
        model = UserProfile
        exclude = ('user',)

