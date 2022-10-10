# Create your views here.
from wiki.models import Wiki
from wiki.serializer import WikiSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action
from rest_framework.response import Response

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000

# Create viewset here
class WikiViewSet(viewsets.ModelViewSet):
    serializer_class = WikiSerializer
    queryset = Wiki.objects.all()
    pagination_class = StandardResultsSetPagination

    @action(detail=False)
    @method_decorator(cache_page(60*60*24))
    def tags(self, request):
        tags = Wiki.objects.values_list('tags', flat=True)
        flattag = set([])
        for tag in tags:
            arrtag = tag.split(',')
            for strtag in arrtag:
                flattag.add(strtag.strip())
        return Response(flattag)

