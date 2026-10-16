from rest_framework import serializers
from LeadApp.models import Lead
import re

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model=Lead
        fields="__all__"
        read_only_fields=['id','added_date']
        
    # def validate_phone_no(self,phone):#when is_valid() works,the execution comes here
    #     pattern=r"^[6-9][0-9]{9}$"
    #     if re.search(pattern,str(phone)):
    #         return phone
    #     else:
    #         raise serializers.ValidationError("phone number not validated")