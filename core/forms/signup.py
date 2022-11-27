from django.contrib.auth.forms import UserCreationForm
from core.models.user import CustomUser
class SignUpForm(UserCreationForm):
#profile_year        = blaaa blaa blaaa irrelevant.. You have your own stuff here don't worry about it

   # here is the important part.. add a class Meta-
   class Meta:
      model = CustomUser #this is the "YourCustomUser" that you imported at the top of the file  
      fields = ('email','username', 'password1', 'password2') #etc etc, other fields you want displayed on the form)