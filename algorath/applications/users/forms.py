from django import forms
#
from .models import User, Connection


class UserRegisterForm(forms.ModelForm):

    class Meta:
        """Meta definition for Userform."""

        model = User
        fields = (
            'name',
        )

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder' : 'Name'
                }
            ),
        }


class ConnectionRegisterForm(forms.ModelForm):

    class Meta:
        """Meta definition for Userform."""

        model = Connection
        fields = (
            'user1',
            'user2',
        )

        
