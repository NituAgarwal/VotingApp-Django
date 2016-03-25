from django.shortcuts import render
from django.template import loader
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.conf import settings


from django.http import HttpResponse
from .models import Question,Choice

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('voteapp/index.html')
    context = {'latest_question_list': latest_question_list,}
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.session.get('question_id')==question.question_text and request.session.get('has_voted', False):
        selected_option = request.session.get('selected_choice')
        return HttpResponse("You've already voted %s"%selected_option)
    return render(request,'voteapp/detail.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request,'voteapp/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        request.session['has_voted'] = True
        request.session['selected_choice'] = selected_choice.choice_text
        request.session['question_id']=question.question_text
        return HttpResponseRedirect(
            reverse('confirm'))

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request,'voteapp/results.html', {'question': question})

def confirm(request):
    return render(request,'voteapp/confirm.html')