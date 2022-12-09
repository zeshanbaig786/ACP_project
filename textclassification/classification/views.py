from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.urls import reverse
from django.views import generic
from .forms import NameForm

def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    form = NameForm()
    context = {"form": form}
    return render(request, "classification/index.html", context=context)
