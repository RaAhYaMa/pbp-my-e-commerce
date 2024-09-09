from django.shortcuts import render

# Create your views here.
def index(request):
    item = {
        "name": "Purcel - Calculus",
        "price": "Rp500.000,00",
        "description": "Buku sakti kalkulus untuk anak computer science"
    }
    return render(request, "index.html", item)