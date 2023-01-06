from rest_framework import serializers

from .models import User


class RegisterUserSerializers(serializers.ModelSerializer):
    password_confirm = serializers.CharField(min_length=8, required=True)


    class Meta:
        model = User
        fields = ('email', 'password', 'password_confirm')
    

    def validate(self, attrs):
        pass1 = attrs.get('password')
        pass2 = attrs.pop('password_confirm')

        if pass1 != pass2:
            serializers.ValidationError('Password do not match')
        
        return attrs

    
    def validate_email(self, email):
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError('Email is already exists')
        
        return email
    

    def create(self, validated_data):
        return User.objects.create(**validated_data)