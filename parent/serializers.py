from rest_framework import serializers
from .models import Parent



class ParentSerializer(serializers.ModelSerializer):
    #first_name = serializers.StringRelatedField(many=False)
    # first_name = serializers.CharField(required=True,allow_blank=False,max_length=30)
    # last_name = serializers.CharField(required=True,allow_blank=False,max_length=30)
    #father_name = serializers.CharField(required=True,allow_blank=True,max_length=30)
    #mother_name = serializers.CharField(required=True,allow_blank=True,max_length=30)
    #son_name = serializers.StringRelatedField(required=True,max_length=30)
    #son_names = serializers.SlugRelatedField(many=True,slug_field ='son_name',read_only=True)
    father_name = serializers.StringRelatedField(many=False)
    mother_name = serializers.StringRelatedField(many=False)
    son_name = serializers.StringRelatedField(many=True)
    #daughter_name= serializers.CharField(required=False,allow_blank=True,max_length=30)
    daughter_name = serializers.StringRelatedField(many=True)
    
    
    class Meta:
        model = Parent
        fields = ['id',
                  'first_name',
                  'last_name',
                  'father_name',
                  'mother_name',
                  'son_name',
                  'daughter_name']
        
      
