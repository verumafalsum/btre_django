from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View
from btre.mixins import JsonResponseMixin

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