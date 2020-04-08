from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'index.html'

class LoginTestView(TemplateView):
    template_name = 'test.html'

class LogoutThanksView(TemplateView):
    template_name = 'thanks.html'
