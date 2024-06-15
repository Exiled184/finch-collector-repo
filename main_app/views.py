from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    return render(request, 'finches/index.html', {'finches': finches})





finches = [
    {'name': 'Alpha', 'breed': 'Red-eared Firetail', 'description':'trying to be Charizard with my eyebrows on fleek', 'age': 1},
    {'name': 'Beta', 'breed': 'Gouldian', 'description':'jaundice faced with purple honkers', 'age': 2},
    {'name': 'Gamma', 'breed': 'Double-barred', 'description':'I am the owl, sir hold my cloak', 'age': 3},
    {'name': 'Delta', 'breed': 'Zebra', 'description':'Oh, Sugar Honey Ice Tea', 'age': 4},
    {'name': 'Epsilon', 'breed': 'Beautiful Firetail', 'description':'glamourous charizard, no eyeshadow', 'age': 5},
]