from rest_framework import serializers

from back_app.models import *


class FinalProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinalProjectModel
        fields = ('name', 'course_1', 'course_2',)
