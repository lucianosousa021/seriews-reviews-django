from rest_framework import serializers
from reviews.models import SeriesReviews

class SeriesReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeriesReviews
        fields = '__all__'