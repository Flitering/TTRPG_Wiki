from django.shortcuts import render

def rules_home(request):
    return render(request, 'rules/rules_home.html')
