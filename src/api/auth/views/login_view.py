from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from api.auth.serializer.login_serializer import LoginSerializer

@method_decorator(csrf_exempt, name='dispatch') 
class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data, context={'request': request})
        
        if serializer.is_valid():
            user = serializer.validated_data['user']
            return Response({
                "message": "Tizimga muvaffaqiyatli kirdingiz!",
                "username": user.username,
                "email": user.email,
                "tokens": user.token() 
            }, status=status.HTTP_200_OK)
        
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)