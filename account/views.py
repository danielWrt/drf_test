from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import RegisterUserSerializers


class RegisterUserView(APIView):

    def post(self, request):
        ser = RegisterUserSerializers(data=request.data)
        ser.is_valid(raise_exception=True)
        ser.save()

        return Response('success', 201)
