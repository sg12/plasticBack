from rest_framework.response import Response
from apps.surgeons.models import Rating
from apps.surgeons.serializers import RatingSerializer
from rest_framework.views import APIView


class SurgeonAddRatingView(APIView):
    def post(self, request, pk):
        instance = Rating.objects.filter(surgeon_id=pk, user=request.user).first()
                
        serializer = RatingSerializer(instance=instance, data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response()