from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class SuperUserRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    login_url = 'employee:login'

    def test_func(self):
        return self.request.user.is_superuser


class GroupRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
  login_url = 'employee:login'
  group_names = ["employee"]

  def test_func(self):
    return self.request.user.groups.filter(name__in = self.group_names)

  def get_permission_denied_message(self):
    return "Must be {} to access this page".format(*self.group_names)
