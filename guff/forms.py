from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post 

class CustomuserCreationForms(UserCreationForm):
    email= forms.EmailField(required=True)
    
    class Meta:
        model= User
        fields =('username','email','password1','password2')
        
        def save(self,commit=True):
            user = super().save(commit=False)
            user.email = self.cleaned_data['email']
            if commit :
                user.save()
                return user 

class PostForm(forms.ModelForm):
    caption=forms.CharField(
        max_length=200,
        widget=forms.Textarea(attrs={'row':3, 'placeholder':'Write some caption here'}),
        help_text= 'Max is 200 characters'
    )
    
    class Meta:
      model= Post 
      fields = ['photo','caption']
      widget = {
         'photo': forms.FileInput(attrs={'accept':'image/*'}),
        }
    
    def clean_photo(self):
        photo = self.cleaned_data.get('photo')
        if photo:
            if not photo.content_type.startswith('image/'):
                raise forms.ValidationError('please upload a valid image')
            
            if photo.size>5 *1024*1024:
                raise forms.ValidationError("Image size is greater than 5 MB")
            return photo
     
  


            
    
      
   
        
                                           