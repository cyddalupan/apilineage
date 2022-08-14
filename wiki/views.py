# Create your views here.
from wiki.models import WikiBase, WikiContent, WikiFolder
from wiki.serializer import WikiBaseSerializer, WikiContentSerializer, WikiFolderSerializer
from rest_framework import viewsets

# Create viewset here
class WikiFolderViewSet(viewsets.ModelViewSet):
    serializer_class = WikiFolderSerializer
    queryset = WikiFolder.objects.all()

class WikiBaseViewSet(viewsets.ModelViewSet):
    serializer_class = WikiBaseSerializer
    queryset = WikiBase.objects.all()
    

class WikiContentViewSet(viewsets.ModelViewSet):
    serializer_class = WikiContentSerializer
    queryset = WikiContent.objects.all()