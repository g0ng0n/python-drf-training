from rest_framework import serializers
from . import models


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        },
        fields = (
            'id',
            'course',
            'name',
            'email',
            'comment',
            'rating',
            'create_at'
        )
        model = models.Review


class CourseSerializer(serializers.ModelSerializer):
    reviews = serializers.HyperlinkedRelatedField(many=True, read_only=True,
                                                  view_name='apiv2:review-detail')

    class Meta:
        fields = (
            'id',
            'title',
            'url',
            'reviews',
        )
        model = models.Course