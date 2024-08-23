from rest_framework import serializers

from homepage.models import Service, Ideas, ProcessStep


class ServiceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"

class IdeasSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ideas
        fields = "__all__"


class ProcessStepSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProcessStep
        fields = "__all__"
