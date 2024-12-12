from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView

class Signup(CreateView):
    form_class=UserCreationForm
    context_object_name='form'
    template_name='pages/signup.html'
    success_url='/'
