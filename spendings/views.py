from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import SpendingSerializer, SpendingCategorySerializer
from .models import Spending, SpendingCategory


class SpendingsViewSet(viewsets.ModelViewSet):

    permission_classes = (IsAuthenticated, )
    serializer_class = SpendingSerializer

    def get_queryset(self):
        return Spending.objects.filter()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class SpendingCategoryViewSet(viewsets.ModelViewSet):

    permission_classes = (IsAuthenticated, )
    serializer_class = SpendingCategorySerializer

    def get_queryset(self):
        return SpendingCategory.objects.filter()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)