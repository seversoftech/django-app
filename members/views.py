from django.http import HttpResponse, HttpResponseRedirect
from django.http import HttpResponse
from django.template import loader
from .models import Member
from django.db.models import Q

def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers' : mymembers,
  }
  return HttpResponse(template.render(context, request))


def details(request, slug):
  mymember = Member.objects.get(slug=slug)
  templates = loader.get_template('details.html')
  context = {
    'mymember':mymember,
  }
  return HttpResponse(templates.render(context,request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def testing(request):
  mydata = Member.objects.values_list('firstname')
  mydata = Member.objects.filter(Q(firstname='Sever') | Q(firstname = 'Dev' )).values()
  template = loader.get_template('template.html')
  context = {
    'mymembers': mydata,
  }
  return HttpResponse(template.render(context, request))