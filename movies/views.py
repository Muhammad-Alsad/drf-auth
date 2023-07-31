from django.shortcuts import render
from .models import Movie
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView

from .serializers import MovieSerializer
# from rest_framework.permissions import AllowAny,IsAuthenticated
# from .permissions import IsOwnerOrReadOnly,IsAnAdminOrStaffUser

# Create your views here.
class MovieListView(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    


class MovieDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


