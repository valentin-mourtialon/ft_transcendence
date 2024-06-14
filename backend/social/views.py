from rest_framework import generics
from .models import CustomUserProfile
from .serializers import CustomUserProfileSerializer

class UserProfileDetailView(generics.RetrieveUpdateAPIView):
    queryset = CustomUserProfile.objects.all()
    serializer_class = CustomUserProfileSerializer

    def get_object(self):
        return self.request.user.profile
