from django.http import HttpResponse
from django.template import loader
from .models import Member

def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers' : mymembers,
  }
  return HttpResponse(template.render(context, request))


def details(request, id):
  mymember = Member.objects.get(id=id)
  templates = loader.get_template('details.html')
  context = {
    'mymember':mymember,
  }
  return HttpResponse(templates.render(context,request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def testing(request):
  templates = loader.get_template('template.html')
  context={
    'fruits':['Apple', 'Banana', 'Cherry'],
    
  }
  return HttpResponse(templates.render(context, request))