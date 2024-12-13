from django.conf import settings
from django.shortcuts import render

def home(request):
    return render(request, 'applica/home.html')

def calculate(request):
    if request.method == "POST":
        num1 = float(request.POST['num1'])
        num2 = float(request.POST['num2'])
        operation = request.POST['operation']
        
        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            result = num1 / num2 if num2 != 0 else "Error: Division by zero"
        else:
            result = "Invalid Operation"

        return render(request, 'applica/result.html', {'result': result})
    else:
        return render(request, 'applica/home.html')
