from django.shortcuts import render

# Create your views here.
def index(request):
    cont_dict={'name':"keerthan rai",'number':102}
    return render(request,'basic_app/index.html',cont_dict)

def other(request):
    return render(request,'basic_app/other.html')

def basic(request):
    return render(request,'basic_app/basic.html')

def relative(request):
    return render(request,'basic_app/relative_url_template.html')
