from django.http import JsonResponse

def hello_world(request):
    data = {
        "message": "Hello from sample app!",
        "status": "success"
    }
    return JsonResponse(data, safe=False)