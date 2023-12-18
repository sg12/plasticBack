from rest_framework.response import Response
from apps.clinics.models import Rating
from apps.clinics.serializers import RatingSerializer
from rest_framework.views import APIView


__all__ = ['RatingView']


class RatingView(APIView):
    def post(self, request, pk):
        instance = Rating.objects.filter(clinic_id=pk, user=request.user).first()
                
        serializer = RatingSerializer(instance=instance, data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response()