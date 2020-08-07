from .models import CustomUser, Program, StaffUserRequest
from .serializers import StaffRegisterSerializer, ApplicantRegisterSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView


class StaffRegister(CreateAPIView):
    serializer_class = StaffRegisterSerializer

class ApplicantRegister(CreateAPIView):
    serializer_class = ApplicantRegisterSerializer

