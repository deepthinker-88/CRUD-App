from rest_framework import serializers
from .models import Cousin



class CousinSerializer(serializers.ModelSerializer):
    first_name = serializers.StringRelatedField(many=False)
    last_name = serializers.StringRelatedField(many=False)
    age = serializers.StringRelatedField(many=False)
    mother = serializers.StringRelatedField(many=False)
    father = serializers.StringRelatedField(many=False)
    grandfathers = serializers.CharField
    grandmothers = serializers.StringRelatedField(many=True)

    class Meta:
        model = Cousin
        #fields = '__all__'
        fields = [
            "id",
            "first_name",
            "last_name",
            "age",
            "father",
            "mother",
            "grandfathers",
            "grandmothers",
        ]
      
