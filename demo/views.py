from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, ModelViewSet

from .models import Weapon, Comment, Adv
from .serializers import WeaponSerializer, CommentSerializer, AdvSerializer

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import LimitOffsetPagination

from .permissions import IsOwnerOrReadOnly


# Create your views here.
# @api_view(['GET', 'POST'])
# def demo(request):
#     if request.method == 'GET':
#         weapons = Weapon.objects.all()
#         ser = WeaponSerializer(weapons, many=True)
#         return Response(ser.data)
#     if request.method == 'POST':
#         return Response({'status': 'OK'})

class DemoView(ListAPIView):
    queryset = Weapon.objects.all()
    serializer_class = WeaponSerializer

    def post(self, request):
        return Response({'status': 'OK'})


class WeaponView(RetrieveAPIView):
    queryset = Weapon.objects.all()
    serializer_class = WeaponSerializer


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    # Фильтрация данных - 3 типа фильтров
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['user', ]  # Искать по user
    search_fields = ['text', ]  # Искать по тексту * сокращение s
    ordering_fields = ['id', 'user', 'text', 'created_at']  # Упорядочивание данных * сокращение о
    # Пагинация для конкретного вьюсета
    pagination_class = LimitOffsetPagination  # Limit например 2 c offset 5 (показать 2 с 5)


class AdvViewSet(ModelViewSet):
    queryset = Adv.objects.all()
    serializer_class = AdvSerializer
    # Создаем свой permissions
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
