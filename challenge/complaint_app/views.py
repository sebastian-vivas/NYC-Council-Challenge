from rest_framework import viewsets
from .models import UserProfile, Complaint
from .serializers import UserSerializer, UserProfileSerializer, ComplaintSerializer
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Count

class ComplaintViewSet(viewsets.ModelViewSet):
    http_method_names = ['get']
    serializer_class = ComplaintSerializer
    
    def list(self, request):
        user_profile = UserProfile.objects.get(user=request.user)
        user_district = user_profile.district
        
        padded_district = user_district.zfill(2)
        district_pattern = f"NYCC{padded_district}"
        
        complaints = Complaint.objects.filter(account=district_pattern)
        serializer = self.serializer_class(complaints, many=True)
        return Response(serializer.data)

class OpenCasesViewSet(viewsets.ModelViewSet):
    http_method_names = ['get']
    serializer_class = ComplaintSerializer
    
    def list(self, request):
        user_profile = UserProfile.objects.get(user=request.user)
        user_district = user_profile.district
        
        padded_district = user_district.zfill(2)
        district_pattern = f"NYCC{padded_district}"
        
        complaints = Complaint.objects.filter(account=district_pattern, closedate__isnull=True)
        serializer = self.serializer_class(complaints, many=True)
        return Response(serializer.data)

class ClosedCasesViewSet(viewsets.ModelViewSet):
    http_method_names = ['get'] 
    serializer_class = ComplaintSerializer
    
    def list(self, request):
        user_profile = UserProfile.objects.get(user=request.user)
        user_district = user_profile.district
        
        padded_district = user_district.zfill(2)
        district_pattern = f"NYCC{padded_district}"
        
        complaints = Complaint.objects.filter(account=district_pattern, closedate__isnull=False)
        serializer = self.serializer_class(complaints, many=True)
        return Response(serializer.data)
    
class TopComplaintTypeViewSet(viewsets.ModelViewSet):
    http_method_names = ['get']
    
    def list(self, request):
        user_profile = UserProfile.objects.get(user=request.user)
        user_district = user_profile.district
        
        padded_district = user_district.zfill(2)
        district_pattern = f"NYCC{padded_district}"
        
        top_complaints = (Complaint.objects
            .filter(account=district_pattern)
            .exclude(complaint_type__isnull=True)
            .exclude(complaint_type='')
            .values('complaint_type')
            .annotate(count=Count('complaint_type'))
            .order_by('-count')[:3])
        
        return Response(top_complaints)

class ConstituentComplaintsViewSet(viewsets.ModelViewSet):
    http_method_names = ['get']
    serializer_class = ComplaintSerializer
    
    def list(self, request):
        user_profile = UserProfile.objects.get(user=request.user)
        user_district = user_profile.district
        
        padded_district = user_district.zfill(2)
        district_pattern = f"NYCC{padded_district}"
        
        complaints = Complaint.objects.filter(council_dist=district_pattern)
        serializer = self.serializer_class(complaints, many=True)
        return Response(serializer.data)