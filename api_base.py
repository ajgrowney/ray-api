from django.http import JsonResponse

def StandardResponse(status, results) -> dict:
    responseType = type(results[0]) if len(results) > 0 else None
    if(responseType):
    	response = {"StatusCode": status, "Type": (responseType.__name__), "Results": results }
    else:
        response = {"StatusCode": status, "Type": "None", "Results": []}
    return JsonResponse(response,status=status)
     