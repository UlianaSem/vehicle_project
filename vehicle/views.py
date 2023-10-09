from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from vehicle.models import Car, Moto, Milage
from vehicle.permissions import IsOwnerOrStaff
from vehicle.serializers import CarSerializer, MotoSerializer, MilageSerializer, MotoMilageSerializer, \
    MotoCreateSerializer


class CarAPIViewSet(ModelViewSet):
    serializer_class = CarSerializer
    queryset = Car.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrStaff]

    def perform_create(self, serializer):
        new_car = serializer.save()
        new_car.owner = self.request.user
        new_car.save()


class MotoCreateAPIView(CreateAPIView):
    serializer_class = MotoCreateSerializer
    queryset = Moto.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_moto = serializer.save()
        new_moto.owner = self.request.user
        new_moto.save()


class MotoListAPIView(ListAPIView):
    serializer_class = MotoSerializer
    queryset = Moto.objects.all()
    permission_classes = [IsAuthenticated]


class MotoDetailAPIView(RetrieveAPIView):
    serializer_class = MotoSerializer
    queryset = Moto.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrStaff]


class MotoUpdateAPIView(UpdateAPIView):
    serializer_class = MotoSerializer
    queryset = Moto.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrStaff]


class MotoDeleteAPIView(DestroyAPIView):
    serializer_class = MotoSerializer
    queryset = Moto.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrStaff]


class MilageAPIViewSet(ModelViewSet):
    serializer_class = MilageSerializer
    queryset = Milage.objects.all()
    permission_classes = [IsAuthenticated]

    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ('car', 'moto', )
    ordering_fields = ('year', )


class MotoMilageListAPIView(ListAPIView):
    queryset = Milage.objects.filter(moto__isnull=False)
    serializer_class = MotoMilageSerializer
    permission_classes = [IsAuthenticated]
