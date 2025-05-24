from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Customer  # Make sure this imports the correct model
from .serializers import CustomerSerializer, Customergetserializer
from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.decorators import action


class CustomerAPIView(APIView):

    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            validated_data = serializer.validated_data
            
            user = User.objects.create(
                username=validated_data['name'], 
                email=validated_data['email']
            )
            user.set_password(request.data.get('password'))
            user.save()

            customer_obj = Customer.objects.create(user=user, **validated_data)
        
        return Response({"message": "Customer created", "customer_id": customer_obj.id})


class Customerget(APIView):

    def get(self,request, pk):
        customer = Customer.objects.get(id=pk)
        customer_serializer = Customergetserializer(customer)
        

        return Response({"message":customer_serializer.data})

class CustomerUpdate(APIView):

    def patch(self, request, pk):
        customer = Customer.objects.get(id= pk)
        customer_serializer = CustomerSerializer(customer, data = request.data, partial = True)
        if customer_serializer.is_valid(raise_exception=True):
            customer_serializer.save()
        return Response({"message":customer_serializer.data})


class Customergetall(APIView):

    def get(self, request):
        cust = Customer.objects.all()
        cust_ser = CustomerSerializer(cust, many= True).data
        return Response({"message":cust_ser})
    


class UserViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    @action(detail=True, methods=['get'])
    def deactivate(self, request, pk=None):
        """Deactivate a user"""
        user = self.get_object()
        user.is_active = True
        user.save()
        return Response({'status': 'User deactivated'}, status=status.HTTP_200_OK)
    


class UserCustomView(viewsets.ViewSet):

    @action(detail= True, methods=['get'])
    def activate(self, request, pk=None):
        customer  = Customer.objects.get(id = pk)
        serializer = CustomerSerializer(customer).data
        return Response({"message": serializer})
    
