from rest_framework import serializers
from .models import Account
from rest_framework.exceptions import AuthenticationFailed
from django.contrib import auth
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
# import smtplib

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['username', 'password', 'role', 'aid']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=255,  write_only=True)
    username = serializers.CharField(
        max_length=255)

    tokens = serializers.SerializerMethodField()

    def get_tokens(self, obj):
        user = Account.objects.get(username=obj['username']) 
        return {           
            'refresh': user.tokens()['refresh'],
            'access': user.tokens()['access']
        }

    class Meta:
        model = Account
        fields = ['username', 'password', 'role', 'tokens', 'aid']

    def validate(self, attrs):
        username = attrs.get('username', '')
        password = attrs.get('password', '')
        # filtered_user_by_username = Account.objects.filter(username=username)
        user = auth.authenticate(username=username, password=password)
        if not user:
            raise AuthenticationFailed('Invalid credentials, try again')
        return {
            'username': user.username,
            'password': user.password,
            'tokens': user.tokens,
            'role': user.role,
            'aid' : user.aid
        }

        return super().validate(attrs)

# class sendEmail():
#     server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
#     server.login("soliditycpn.g9@gmail.com", "solidity123")
#     server.sendmail("soliditycpn.g9@gmail.com", "quypham1503@gmail.com", "Please comfirm your email!")
#     server.quit()


