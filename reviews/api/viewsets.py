from rest_framework import viewsets
from reviews.api import serializers
from reviews.models import SeriesReviews

class SeriesReviewsSets(viewsets.ModelViewSet):
    serializer_class = serializers.SeriesReviewsSerializer
    queryset = SeriesReviews.objects.all()