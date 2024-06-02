from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')
def form(request):
    n = ""
    n1 = ""
    n2 = ""
    try:
        if request.method == "POST":
            n1 = eval(request.POST.get("Num1"))
            n2 = eval(request.POST.get("Num2"))
            op = request.POST.get("op")
            if op == "+":
                n = n1 + n2
            elif op == "-":
                n = n1 - n2
            elif op == "*":
                n = n1 * n2
            elif op == "/":
                n = n1 / n2
    except:
        n = "invalid input"
        return n
    content = {"n1":n1,"n2":n2,'value': n}
    return render(request,'form.html',content)
