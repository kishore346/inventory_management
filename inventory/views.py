from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Item
from .serializers import ItemSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.core.cache import cache
from rest_framework.response import Response

class ItemCreateView(generics.CreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

class ItemListCreate(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]



class ItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request, *args, **kwargs):
        item_id = kwargs.get('pk')
        cached_item = cache.get(f'item_{item_id}')
        if cached_item:
            return Response(cached_item)

        response = super().get(request, *args, **kwargs)
        cache.set(f'item_{item_id}', response.data, timeout=60*5)  # Cache for 5 minutes
        return response
