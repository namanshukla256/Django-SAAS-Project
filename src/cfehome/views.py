import pathlib
from django.shortcuts import render
from django.http import HttpResponse

from visits.models import PageVisit

this_dir = pathlib.Path(__file__).resolve().parent

def home_page_view(request, *args, **kwargs):
    queryset = PageVisit.objects.all()
    my_title = "My Page"
    my_context = {
        "page_title": my_title,
        "page_visit_count": queryset.count()
    }

    path = request.path
    print("path", path)
    html_template = "home.html"
    PageVisit.objects.create()
    return render(request, html_template, my_context)