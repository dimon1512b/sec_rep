"""

Якщо ви хочете створити CRUD (Create, Read, Update, Delete) методи для вашої
моделі у Django з використанням Django Rest Framework і мати можливість
очікувати та повертати різні колонки для кожного методу, ви можете
використовувати різні серіалізатори для кожного методу в вашому ViewSet.

from rest_framework import serializers, viewsets
from .models import YourModel

class YourModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = YourModel
        fields = ('id', 'field_a', 'field_b', 'field_c', 'field_d')

class YourModelCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = YourModel
        fields = ('field_a', 'field_b', 'field_c', 'field_d')
        extra_kwargs = {
            'field_c': {'required': False},
            'field_d': {'required': False}
        }

class YourModelUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = YourModel
        fields = ('field_b', 'field_c', 'field_d')

class YourModelViewSet(viewsets.ModelViewSet):
    queryset = YourModel.objects.all()
    serializer_class = YourModelSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return YourModelCreateSerializer
        elif self.action == 'update':
            return YourModelUpdateSerializer
        else:
            return YourModelSerializer

"""