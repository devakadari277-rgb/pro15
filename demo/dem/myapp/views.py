from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def student(request):
    data = {
        'name': 'Abhijit',
        'age': 21,
        'phone': '9876543210'
    }
    return render(request, 'student.html', data)