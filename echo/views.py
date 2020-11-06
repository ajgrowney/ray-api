from api_base import StandardResponse
# Create your views here.
def healthCheck(request):
    return StandardResponse(200, ["Healthy"])

