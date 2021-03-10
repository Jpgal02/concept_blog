from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic


from .models import Choice, Question

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def example(request):
    return render(request, 'polls/example.html', {'title': 'example'})

def product(request):
    return render(request, 'polls/product.html', {'title':'product'})

def rank(request):
    return render(request, 'polls/rank.html', {'title':'rank'})

def eln_result(request):
    return render(request, 'polls/eln_result.html', {'title':'eln_result'})

def link(request):
    return render(request, 'polls/link.html', {'title':'link'})

def popup(request):
    return render(request, 'polls/popup.html',{'title':'popup'})

def save(request):
    subject= request.POST['subject']
    body=request.POST['body']
    e=Entry(subject=subject, body=body, pub_date=timezone.now())
    e.save
    return redirect('view')

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))