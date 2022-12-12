from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView,ListCreateAPIView,RetrieveAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView
from .serializers  import ThingSerializer
# Create your views here.
from .models import Thing


class ThingListView(ListCreateAPIView):
    queryset=Thing.objects.all()
    serializer_class= ThingSerializer


class ThingDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Thing.objects.all()
    serializer_class= ThingSerializer