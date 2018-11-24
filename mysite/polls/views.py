from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from.models import Question

def index(request):
    latestQuestion = Question.objects.order_by('-pub_date')[:5]
    context = {'latestQuestion':latestQuestion}
    return render(request,'index.html',context)

def detail(request, questionId):
    return HttpResponse("it is the %s Question detail" %questionId)

def result(request, questionId):
    return HttpResponse("it is the %s Question results" %questionId)

def vote(request, questionId):
    return HttpResponse("it is the %s Question vote" %questionId)