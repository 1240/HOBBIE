from django.http import HttpResponse

# Create your views here.
from django.template.loader import get_template


def home(request):
    view = "template"
    template = get_template('main_page.html')
    html = template
    return HttpResponse(html)
