from django_countries.serializer_fields import CountryField
from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    email = serializers.EmailField(source='user.email')
    full_name = serializers.SerializerMethodField(read_only=True)
    profile_img = serializers.SerializerMethodField()
    country = CountryField(name_only=True)

    class Meta:
        model = Profile
        fields = ['id', 'first_name', 'last_name', 'full_name', 'email', 'profile_img',
                'phone_number', 'gender', 'country', 'city', 'twitter_handle', 'about_me']


    def get_full_name(self, obj):
        first_name = obj.user.first_name.title()
        last_name = obj.user.last_name.title()
        return f"{first_name} {last_name}"
    
    def get_profile_img(self, obj):
        return obj.profile_img.url
    

class UpdateProfileSerializer(serializers.ModelSerializer):
    country = CountryField(name_only=True)

    class Meta:
        model = Profile
        fields = ['phone_number', 'profile_img', 'about_me', 'gender', 'country', 'city', 'twitter_handle',]


class FollowingSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'profile_img', 'about_me', 'twitter_handle']