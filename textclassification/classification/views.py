from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.urls import reverse
from django.views import generic
from .forms import NameForm
from .huggingface import HuggingFace

def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    form = NameForm()
    context = {"form": form}
    return render(request, "classification/index.html", context=context)


def ajax_posting(request):
    if(request.headers.get('x-requested-with') == 'XMLHttpRequest'):
        inp = request.POST['text_to_classify']
        result = HuggingFace().query(inp)
        #return HttpResponse(F'result of <b>{inp}</b> is <br/>{str(result)}')
        return JsonResponse(result)
    return HttpResponseNotFound("hello")  
