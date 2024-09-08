from django .forms import ModelForm,widgets
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Blog
class Creatform(ModelForm):
    class Meta:
        model=Blog
        fields=['name','body']
    def __init__(self,*args,**kwargs):
        super(Creatform,self).__init__(*args,**kwargs)

        for name , field in self.fields.items():

                field.widget.attrs.update({'class':'input'})