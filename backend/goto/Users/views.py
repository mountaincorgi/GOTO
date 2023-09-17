from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import TemplateView, View

from .forms import LoginForm, RegistrationForm


class HomeView(TemplateView):
    """Homepage view that all visitors hit if not logged in."""

    template_name = "Users/home.html"

    # TODO: If user is logged in, redirect to the user's homepage
    def get_context_data(self, **kwargs):
        """Add forms to the context."""

        context = super().get_context_data(**kwargs)

        context["login_form"] = LoginForm()
        context["registration_form"] = RegistrationForm()
        # TODO: Add password reset form
        return context
    

class UserLoginView(LoginView):
    # TODO: Custom authentication
    def get_redirect_url(self):
        """Return the user-originating redirect URL if it's safe."""
        if self.request.user:
            redirect_to = f"/{self.request.user.username}"
        else:
            redirect_to = "/"
        return redirect_to


class UserRegistrationView(View):
    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("user-home", args=[user.username]))
        # TODO: Add validation


class UserHomeView(TemplateView):
    template_name = "Users/user-home.html"


# Auth
# if not request.user.is_authenticated:
# @login_required
# LoginRequiredMixin
# https://docs.djangoproject.com/en/4.2/topics/auth/default/
# https://www.django-rest-framework.org/api-guide/authentication/
