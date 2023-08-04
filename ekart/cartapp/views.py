from django.shortcuts import get_object_or_404,render,redirect


# Create your views here.
def cart(request):
    return render(request,'cart.html')

def insertData(request):
    if request.method=="POST":
        name=request.POST.get('name')
        dis=request.POST.get('dis')
        rate=request.POST.get('rate')
    return render(request,'crud.html')