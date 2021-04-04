from rest_framework import serializers
from .models import User
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
      class Meta:
         model = User
         fields = ('last_login','email', 'name', 'password')
        #  extra_kwargs = {'password': {'write_only': True}}

      def create(self, validated_data):

        user = User(
        email=validated_data['email'],
        name=validated_data['name']
    )
        user.set_password(validated_data['password'])
        user.save()
        return user