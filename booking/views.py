from datetime import datetime

from django.conf import settings
from django.shortcuts import render
from django.views.generic import ListView

from rest_framework import status
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, UpdateAPIView

from booking.models import Table, Booking
from booking.serializers import TableSerializer, BookingSerializer
from booking.utils import send_mail


# Create your views here.


class BookingListView(ListView):

	model = Booking
	template_name = "booking/booking.html"
	context_object_name = "booking"

	def get_queryset(self):
		today = datetime.today()
		return self.model.objects.filter(date=today)


class BookingListAPIView(ListAPIView):

	model = Booking
	serializer_class = BookingSerializer
	renderer_classes = [JSONRenderer]

	def get_queryset(self):
		data = self.request.query_params
		date = datetime.fromisoformat(data['date'])
		return self.model.objects.filter(date=date)


class ReserveTable(APIView):

	model = Booking

	def post(self, request, format=None):
		data = request.data
		date = datetime.fromisoformat(data['date'])
		tables = data['tables']
		queryset = self.model.objects.filter(date=date, table__id__in=tables)
		result = "Creadentials error"
		if queryset:
			queryset.update(**{"reserved": True})
			send_mail(data['name'], data['email'])
			result = "OK"
			return Response({result: result}, status=status.HTTP_200_OK)

		return Response({result: result}, status=status.HTTP_400_BAD_REQUEST)
