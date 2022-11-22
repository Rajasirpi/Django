from rest_framework import serializers
from .models import Restaurant
from django.core.validators import RegexValidator,re


# Created Serializer with custom field vaildation using regual expression
class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    def validate_rname(self, value):
        # if not value.isdigit() and value.isalpha():
        if not re.match(r'^[A-Za-z0-9-_ ]+$', value): 
            raise serializers.ValidationError("Enter proper vlaues for name")
        return value

    def validate_info(self, value):
        if not re.match(r'^[A-Za-z0-9-_  ]+$', value):
            raise serializers.ValidationError("Entered vlaues is not in correct format")
        return value

    def validate_min_ord(self, value):
        if not re.match(r'^[0-9-_]+$', value):
            raise serializers.ValidationError("Enter proper number of order")
        return value
    
    def validate_location(self, value):
        if not re.match(r'^[A-Za-z-_]+$', value):
            raise serializers.ValidationError("Enter the proper location name")
        return value

    class Meta:
        model = Restaurant
        fields = ('id','rname', 'info','min_ord','location','status')
        # validators=[]
   
  
        