from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import json
from django.http import StreamingHttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

data = []
@csrf_exempt
def index(request):
    if request.method=='POST':
        
        #print('it was post request: '+str(received_json_data))
        #print('HHHHHHHHHHHHHHHHHHHHHHHHHHHHH')
        #received_json_data=json.loads(request.body)
        #return StreamingHttpResponse('it was post request: '+str(received_json_data))
        #data = json.loads(json.dumps((request.POST['data'])))
        data1 = request.POST['data']
        data.append(data1)
        
        #return render(request,"index.html",{'value':data})
        return JsonResponse(data,safe = False)
    if request.method == 'GET':
        #data = request.GET['temperature']
        return JsonResponse(data,safe = False)

    return HttpResponse(request,data)
    
    #return StreamingHttpResponse('it was GET request')
    #print(request.method)
    #return HttpResponse(request.method)
    