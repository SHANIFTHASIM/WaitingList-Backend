from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import WaitlistEntrySerializer
from .models import WaitlistEntry
from django.core.exceptions import ValidationError

@api_view(['POST'])
def join_waitlist(request):
    serializer = WaitlistEntrySerializer(data=request.data)
    if serializer.is_valid():
        try:
            serializer.save()
            return Response({"message": "Successfully added to waitlist!"}, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            return Response({"email": "This email is already on the waitlist."}, status=status.HTTP_208_ALREADY_REPORTED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def get_join_count(request):
    count = WaitlistEntry.objects.count()
    return JsonResponse({"count": count})
