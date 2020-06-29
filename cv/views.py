# Create your views here.
from django.http import HttpResponse
from django.template import loader

from .models import Experience, Education, Skill


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
    return HttpResponse(template.render(context, request))