from .models import Program, Application
from .serializers import (StaffRegisterSerializer, ApplicantRegisterSerializer, 
                        ProgramSerializer, ApplicationSerializer, ProgramHistorySerializer)
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class StaffRegister(CreateAPIView):
    serializer_class = StaffRegisterSerializer

class ApplicantRegister(CreateAPIView):
    serializer_class = ApplicantRegisterSerializer

class ProgramList(ListAPIView):
    serializer_class = ProgramSerializer
    queryset = Program.objects.all()

class ProgramCreate(CreateAPIView):
    serializer_class = ProgramSerializer
    permission_classes = [IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(supervisor=self.request.user)

class Apply(CreateAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(applicant = self.request.user, program_id = self.kwargs['program_id'])

class ProgramHistory(RetrieveAPIView):
    serializer_class = ProgramHistorySerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return Application.objects.get(applicant = self.request.user)    

