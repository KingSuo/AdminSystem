from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.views.generic.base import View


class IndexView(View):
    def get(self, request):
        return render(request, 'BlueMoon/index.html')


class Index2View(View):
    def get(self, request):
        return render(request, 'BlueMoon/index2.html')


class FormsView(View):
    def get(self, request):
        return render(request, 'BlueMoon/forms.html')


class FlotView(View):
    def get(self, request):
        return render(request, 'BlueMoon/flot.html')


class GraphsView(View):
    def get(self, request):
        return render(request, 'BlueMoon/graphs.html')


class VectorMapsView(View):
    def get(self, request):
        return render(request, 'BlueMoon/vector-maps.html')


class UiElementsView(View):
    def get(self, request):
        return render(request, 'BlueMoon/ui-elements.html')


class PanelsView(View):
    def get(self, request):
        return render(request, 'BlueMoon/panels.html')


class NotificationsView(View):
    def get(self, request):
        return render(request, 'BlueMoon/notifications.html')


class IconsView(View):
    def get(self, request):
        return render(request, 'BlueMoon/icons.html')


class BlogView(View):
    def get(self, request):
        return render(request, 'BlueMoon/blog.html')


class BlogFullPageView(View):
    def get(self, request):
        return render(request, 'BlueMoon/blog-full-page.html')


class EditProfileView(View):
    def get(self, request):
        return render(request, 'BlueMoon/edit-profile.html')


class InvoiceView(View):
    def get(self, request):
        return render(request, 'BlueMoon/invoice.html')


class DefaultView(View):
    def get(self, request):
        return render(request, 'BlueMoon/default.html')


class LoginView(View):
    def get(self, request):
        return render(request, 'BlueMoon/login.html')


class HelpView(View):
    def get(self, request):
        return render(request, 'BlueMoon/help.html')


class Err404View(View):
    def get(self, request):
        return render(request, 'BlueMoon/404.html')


class Err500View(View):
    def get(self, request):
        return render(request, 'BlueMoon/500.html')


class TablesView(View):
    def get(self, request):
        return render(request, 'BlueMoon/tables.html')


class PricingView(View):
    def get(self, request):
        return render(request, 'BlueMoon/pricing.html')


class TimelineView(View):
    def get(self, request):
        return render(request, 'BlueMoon/timeline.html')


class MediaView(View):
    def get(self, request):
        return render(request, 'BlueMoon/media.html')


class CalendarView(View):
    def get(self, request):
        return render(request, 'BlueMoon/calendar.html')


class TypographyView(View):
    def get(self, request):
        return render(request, 'BlueMoon/typography.html')