from django.shortcuts import (render, get_object_or_404)
from django.http import (Http404, HttpResponse)
from django.template import loader

from .models import Question


def index(request):
    list_of_questions = Question.objects.order_by('-pub_date')[:5]
    context = {'list_of_questions': list_of_questions}
    return render(request, 'polls/index-new.html', context)


def details(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/details.html', {'question': question})


def results(request, question_id):
    response = 'You are looking at the results for question %s'
    return HttpResponse(response % question_id)


def votes(request, question_id):
    voting = 'You are looking at the votes on question %s'
    return HttpResponse(voting % question_id)
