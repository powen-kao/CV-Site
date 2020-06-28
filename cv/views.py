from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.views import generic
from .models import Experience, Education, Skill


# class IndexView(generic.ListView):
#     template_name = 'cv/index.html'
#     context_object_name = 'experience_list'
#
#     def get_queryset(self):
#         return Experience.objects.order_by('-end_date')[:5]

def index(request):
    experience_list = Experience.objects.order_by('-end_date')
    education_list = Education.objects.order_by('-end_date')
    skill_list = Skill.objects.all().order_by('category')
    template = loader.get_template('cv/index.html')
    context = {
        'experience_list': experience_list,
        'education_list': education_list,
        'skill_list': skill_list,
    }
    response = HttpResponse(template.render(context, request))
    # response['Access-Control-Allow-Origin'] = "*"
    return response

    # latest_exp_list = Experience.objects.order_by('-start_date')[:5]
    # output = ', '.join([q.title for q in latest_exp_list])
    # return HttpResponse(output)

    # return HttpResponse("Hello, world. You're at the polls index.")

# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." % question_id)
#
#
# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)
#
#
# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)
