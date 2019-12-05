from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
#from django.template import loader
from .models import Question, Choice
from django.http import Http404
from django.urls import reverse
from django.views import generic

# Create your views here.
class IndexView(generic.ListView):
    #django的通用视图，用于简单一致的信息显示
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
# class ResultsView(generic.DetailView):
#     modle = Question
#     template_name = 'polls/results.html'
#显示问题列表
#def index(request):
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]#只显示最新的5个
        #template = loader.get_template('polls/index.html')
    #context = {
    #    'latest_question_list': latest_question_list
    #}
    #return render(request,'polls/index.html',context)#向html文件传递一个context
        #return HttpResponse(template.render(context, request))

        #output = ', '.join([q.question_text for q in latest_question_list])
        #return HttpResponse(output)
        #return HttpResponse("Hello, world. You're at the polls index.")
#显示问题详情
#def detail(request, question_id):
        # try:
        #     question = Question.objects.get(pk=question_id)
        # except Question.DoesNotExist:
        #     raise Http404("Question does not exist")
    #question = get_object_or_404(Question,pk=question_id)
    #eturn render(request, 'polls/detail.html',{'question':question})
#显示投票结果
def results(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
     #response = "You're looking at the results of question %s."
     #return HttpResponse(response % question_id)

def vote(request, question_id):
    #return HttpResponse("You're voting on question %s." % question_id)
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])#request.post通过关键字choice获取choice的id，request.get用于获取数据
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))#重定向（reverse对命名的url解析并传递参数，再使用redirect进行重定向）

