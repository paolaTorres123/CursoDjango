from django import forms
from .models import IceCreamStore

class IceCreamStoreUpdateForm(forms.ModelForm):
    
    class Meta:
        model = IceCreamStore

    def __init__(self, *args, **kwargs):
        # Call the original __init__ method before assigning
        # field overloads
        super(IceCreamStoreUpdateForm, self).__init__(*args,
                            **kwargs)
        self.fields['phone'].required = True
        self.fields['description'].required = True


class IceCreamStoreCreateForm(forms.ModelForm):
    class Meta:
        model = IceCreamStore
        fields = ['title', 'block_address', ]