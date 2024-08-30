from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import CustomUser, CompanyProfile, ExpertProfile
from .serializers import (
    UpdateProfileTypeSerializer,
    CompanyProfileSerializer,
    ExpertProfileSerializer,
)
from .services import update_profile_type, create_company_profile, create_expert_profile


class ProfileTypeViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UpdateProfileTypeSerializer

    def update(self, request, *args, **kwargs):
        user = request.user
        serializer = self.get_serializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        # Atualiza o tipo de perfil usando o service
        updated_user = update_profile_type(user, serializer.validated_data)

        # Redireciona para a criação de perfil baseado no tipo de usuário
        if updated_user.is_company:
            return Response(
                {"message": "Create your company profile"}, status=status.HTTP_200_OK
            )
        elif updated_user.is_expert:
            return Response(
                {"message": "Create your expert profile"}, status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"message": "Profile type not set"}, status=status.HTTP_400_BAD_REQUEST
            )


class CompanyProfileViewSet(viewsets.ModelViewSet):
    queryset = CompanyProfile.objects.all()
    serializer_class = CompanyProfileSerializer

    def create(self, request, *args, **kwargs):
        user = request.user
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            profile = create_company_profile(user, serializer.validated_data)
            return Response(
                {
                    "message": "Company profile created",
                    "profile": CompanyProfileSerializer(profile).data,
                },
                status=status.HTTP_201_CREATED,
            )
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class ExpertProfileViewSet(viewsets.ModelViewSet):
    queryset = ExpertProfile.objects.all()
    serializer_class = ExpertProfileSerializer

    def create(self, request, *args, **kwargs):
        user = request.user
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            profile = create_expert_profile(user, serializer.validated_data)
            return Response(
                {
                    "message": "Expert profile created",
                    "profile": ExpertProfileSerializer(profile).data,
                },
                status=status.HTTP_201_CREATED,
            )
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
