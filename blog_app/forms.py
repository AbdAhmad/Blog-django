from django import forms 
from .models import Post, Profile
from crispy_forms.helper import FormHelper

class PostForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_show_labels = False

    title = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Title'})
    )
    content = forms.CharField( 
        widget=forms.Textarea(attrs={'placeholder': 'Content'})
    )

    class Meta:
        model = Post
        fields = ['title', 'content']

class EditProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['location', 'bio']
         