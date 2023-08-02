from django.shortcuts import render
from .models import Movie
from django.shortcuts import render
from .models import Movie
from .serializers import MovieSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
# Create your views here.
from .permissions import OwnerOnly

class MovielistView(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes =[OwnerOnly]