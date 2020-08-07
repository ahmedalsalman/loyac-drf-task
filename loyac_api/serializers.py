from rest_framework import serializers
from .models import CustomUser, Program, StaffUserRequest



class StaffRegisterSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True)

	class Meta:
		model = CustomUser
		fields = ['first_name','last_name','email','date_of_birth','employeeID','password']

	def create(self, validated_data):
		new_user = CustomUser(**validated_data)
		new_user.set_password(validated_data['password'])
		new_user.save()
		return validated_data



class ApplicantRegisterSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True)

	class Meta:
		model = CustomUser
		fields = ['first_name','last_name','email','date_of_birth','password']

	def create(self, validated_data):
		new_user = CustomUser(**validated_data)
		new_user.set_password(validated_data['password'])
		new_user.save()
		return validated_data