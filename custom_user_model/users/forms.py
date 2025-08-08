from .models import CustomUser
from django.contrib.auth.forms import UserChangeForm, UserCreationForm




class UserCustomCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('age',)

class UserCustomChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields