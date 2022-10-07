# Create your views here.
from wiki.models import WikiBase, WikiContent
from wiki.serializer import WikiBaseSerializer, WikiContentSerializer
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
class WikiBaseViewSet(viewsets.ModelViewSet):
    serializer_class = WikiBaseSerializer
    queryset = WikiBase.objects.all()
    pagination_class = StandardResultsSetPagination

    @action(detail=False)
    @method_decorator(cache_page(60*60*24))
    def tags(self, request):
        tags = WikiBase.objects.values_list('tags', flat=True)
        flattag = set([])
        for tag in tags:
            arrtag = tag.split(',')
            for strtag in arrtag:
                flattag.add(strtag.strip())
        return Response(flattag)
    
    @action(detail=True)
    def content(self, request, pk=None):
        content = {}
        if pk is not None:
            content = WikiContent.objects.filter(base_id=pk).filter(is_approved=True).values().last()
        return Response(content)

class WikiContentViewSet(viewsets.ModelViewSet):
    serializer_class = WikiContentSerializer
    queryset = WikiContent.objects.all()
