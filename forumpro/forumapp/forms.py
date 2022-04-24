from .models import forum , discussion
from django.forms import ModelForm

class CreateInForum(ModelForm):
    class Meta:
        model=forum 
        fields="__all__"

class CreateInDiscussion(ModelForm):
    class Meta:
        model=discussion 
        fields="__all__"