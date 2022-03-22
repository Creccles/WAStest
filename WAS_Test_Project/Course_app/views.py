from django.shortcuts import render
from Course_app.models import Category


def course(request):
    list_of_courses = Category.objects.all()


    context_dict = {}
    context_dict['courses'] = list_of_courses
    return render(request, 'pages/web_page.html', context=context_dict)

