from django.http import HttpResponse, Http404
from django.shortcuts import render # inserted this line
def index(request):
  context = {
      'questions': [
           {'firstname': 'Michael', 'lastname': 'Choi', 'activity': 'basketball', 'language': 'Python'}
       ]
  }
  return render(request, 'landing/index.html', context)