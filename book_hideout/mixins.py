from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.shortcuts import redirect, reverse


class SuperUserMixin(LoginRequiredMixin, UserPassesTestMixin):
    """A Mixin for checking if a logged in user is a superuser and
    handling no permission error. If the user is not a superuser they are
    redirected to the home page and a info message is displayed. If the user is
    a superuser, the view is executed normally

    Args:
        LoginRequiredMixin (class): A mixin that redirects a user who isn't
        logged in to the settings.LOGIN_URL. If the user is logged in, execute
        the view normally.
        UserPassesTestMixin (class): A mixin that limits the access based on
        certain permission or test
    """

    def test_func(self):
        return self.request.user.is_superuser

    def handle_no_permission(self):
        messages.info(self.request, 'Ooops! Only an Admin can to that!')
        return redirect(reverse('home'))
