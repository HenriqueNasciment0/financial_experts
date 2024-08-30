from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.password_validation import validate_password


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )

    class Meta:
        model = CustomUser
        fields = (
            "id",
            "email",
            "username",
            "first_name",
            "last_name",
            "is_company",
            "is_expert",
            "password",
            "date_joined",
        )
        read_only_fields = (
            "id",
            "date_joined",
            "is_superuser",
            "is_staff",
            "is_active",
            "last_login",
        )

    def create(self, validated_data):
        user = CustomUser.objects.create(
            email=validated_data["email"],
            username=validated_data["username"],
            first_name=validated_data.get("first_name", ""),
            last_name=validated_data.get("last_name", ""),
            is_company=validated_data.get("is_company", False),
            is_expert=validated_data.get("is_expert", False),
        )
        user.set_password(validated_data["password"])
        user.save()
        return user


class UpadateProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ["is_company", "is_expert"]

    def update(self, instance, validated_data):
        if validated_data.get("is_company"):
            instance.is_company = True
            instance.is_expert = False
        elif validated_data.get("is_expert"):
            instance.is_expert = True
            instance.is_company = False
        instance.save()
        return instance
