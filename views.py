from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# In-memory session storage
sessions = {}

@csrf_exempt
def receive_dlr(request):
    if request.method == 'POST':
            
            #Receiving DLR data from request
            
            dlr_data = request.body.decode(utf-8)
            logging.info(dlr_data)
            channel_layer = get_channel_layer()
            dlr_data = json.loads(dlr_data)
            async_to_sync(channel_layer.group_send)(
                        "dlr_updates",
                        {
                                    "type": "dlr_message",
                                    "message": dlr_data,
                        }
            )
            return httpResponse("DLR received", status=200)

       