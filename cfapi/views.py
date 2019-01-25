from django.core.serializers import serialize
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.generic import View
from btre.mixins import JsonResponseMixin

from .models import Update

def json_example_view(request):
    data = {
        "warrior": "Elon",
        "Intellegence": 100
    }
    return JsonResponse(data)

class JsonCBV(View):
    def get(self, request, *args, **kwargs):
        data = {
            "warrior": "Elon",
            "Intellegence": 100
        }
        return JsonResponse(data)

class JsonCBV2(JsonResponseMixin, View):
    def get(self, request, *args, **kwargs):
        data = {
            "warrior": "Elon",
            "Intellegence": 100
        }
        return self.render_to_json_response(data)

class SerializedListView(View):
    def get(self, request, *args, **kwargs):
        qs = Update.objects.all()
        data = serialize("json", qs, fields=('user', 'content', 'updated'))
        return HttpResponse(data, content_type='application/json')