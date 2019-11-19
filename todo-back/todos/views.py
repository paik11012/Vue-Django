from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from .serializers import TodoSerializer, UserDetailSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Todo
# 특정 method의 요청만 허용하겠다
User = get_user_model()
# Create your views here.
@api_view(['POST'])
def todo_create(request):
    # request.data는 axios의 body로 전달한 데이터
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid(aise_exception=True):
        serializer.save()
        return Response(serializer.data) # 사용자가 새로 작성한 데이터 응답

@api_view(['PUT', 'DELETE'])
def todo_update_delete(request, todo_id):
    # 수정하거나 삭제할 todo instance 호출
    todo = get_object_or_404(Todo, pk=todo_id)
    if request.method == "PUT":
        # instance todo를 request.data로 넘어온 값으로 수정
        serializer = TodoSerializer(instance=todo, data=request.data)  # 수정 시도
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    if request.method == "DELETE":
        todo.delete()
        return Response(status=204)  # 삭제한 status code 204


@api_view(['GET'])
def user_detail(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    serializer = UserDetailSerializer(instance=user)
    return Response(serializer.data)