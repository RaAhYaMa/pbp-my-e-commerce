from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        "title": "T-Shop",
        "name": "Raden Ahmad Yasin Mahendra",
        "class": "PBP-F",
    }
    return render(request, "index.html", context)