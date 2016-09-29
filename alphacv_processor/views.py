from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request, 'alphacv_processor/index.html', {},
        content_type="text/html")


def process(request):
	return 200