from django.shortcuts import render
from django.views.generic import TemplateView

from listings.models import Listing
from realtors.models import Realtor


def index(request):
    listings = Listing.objects.order_by('-list_date') \
                   .filter(is_published=True)[:3]

    context = {
        'listings': listings
    }

    return render(request, 'pages/index.html', context)


class AboutView(TemplateView):
    template_name = 'pages/about.html'

    def get_context_data(self, **kwargs):
        realtors = Realtor.objects.all()
        return {
            'realtors': realtors
        }
