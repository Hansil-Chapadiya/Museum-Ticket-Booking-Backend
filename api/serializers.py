from rest_framework import serializers
from bson import ObjectId
from backend.models import Museums

class ObjectIdField(serializers.Field):
    """Custom field for handling MongoDB ObjectId"""
    def to_representation(self, value):
        return str(value)

    def to_internal_value(self, data):
        return ObjectId(data)

class MuseumSerializer(serializers.ModelSerializer):
    _id = ObjectIdField(read_only=True)

    class Meta:
        model = Museums
        fields = '__all__'