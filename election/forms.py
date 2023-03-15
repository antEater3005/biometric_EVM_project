from django.forms import ModelForm

from .models import Election


class ElectionForm(ModelForm):
    class Meta:
        model = Election
        fields = '__all__'
