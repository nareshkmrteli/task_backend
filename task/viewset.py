import datetime

from django.core.exceptions import ObjectDoesNotExist
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.filters import BaseFilterBackend, SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from utility.utility import CsrExemptSessionAuthentiation

from .models import Task
from .serializer import TaskSerializer


class CustomFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        if 'fromTime' in request.query_params:
            queryset = queryset.filter(fromTime__gte=datetime.datetime.fromtimestamp(int(request.query_params['fromTime'])))
        if 'toTime' in request.query_params:
            queryset = queryset.filter(toTime__lte=datetime.datetime.fromtimestamp(int(request.query_params['toTime'])))
        return queryset

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class=TaskSerializer
    pagination_class=PageNumberPagination
    pagination_class.page_size=10
    filter_backends=[SearchFilter,CustomFilter]
    search_fields=['name','detail']
    authentication_classes=[CsrExemptSessionAuthentiation]
    queryset=Task.objects.all()

    @action(methods=['post'],detail=True)
    def updateStatus(self,request,pk):
        if 'status' in request.POST:
            try:
                task=Task.objects.get(pk=pk)
                task.status='true'==request.POST['status']
                task.save()
            except(ObjectDoesNotExist):
                return Response(data={'detail':'Task does not exist'},status=404)
            
            return Response(data={'detail':'Task Status is updated '},status=200)

        else:
            return Response(data={'detail':'bad request'},status=400)
        