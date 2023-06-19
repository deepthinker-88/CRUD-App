from rest_framework import serializers

from .models import Grandparent


class GrandparentSerializer(serializers.ModelSerializer):
    #daughter_name = serializers.StringRelatedField(many=True)
    #grandchildren = serializers.StringRelatedField(many=True)
    first_name = serializers.StringRelatedField(many=False)
    last_name = serializers.StringRelatedField(many=False)
    #first_name = serializers.StringRelatedField(many=False)
    #daughter_name = serializers.CharField(required=True,allow_blank=False,max_length=30)
    daughter_name = serializers.StringRelatedField(many=True)
    son_name = serializers.StringRelatedField(many=True)
    grandchildren = serializers.StringRelatedField(many=True)
    #age = serializers.StringRelatedField(many=False)
    
        
     

    
    
    # class Meta:
    #     model = Grandparent
    #     fields = '__all__'
    class Meta:
        model = Grandparent
       
        fields = [
            "id",
            "age",
            "first_name",
            "last_name",
            "daughter_name",
            "son_name",
            "grandchildren",
            
            
 ]
