from django.http import HttpResponse, Http404
from django.shortcuts import render # inserted this line
def index(request):
  context = {
      'questions': [
           {'firstname': 'Alan', 'lastname': 'Schambers', 'activity': 'Basketball', 'language': 'Python'}
       ]
  }
  return render(request, 'landing/index.html', context)
