from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .forms import CustomSignupForm
from django.contrib.auth import logout


class SignUp(CreateView):
    model = User
    form_class = CustomSignupForm
    success_url = '/accounts/login'
    template_name = 'registration/signup.html'

    # def logout_view(request):
    #     logout(request)
    #     # Redirect to a success page.