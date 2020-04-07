from datetime import datetime

from django.conf import settings
from django.shortcuts import render
from django.views.generic import ListView

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from booking.models import Table, Booking
from booking.serializers import TableSerializer, BookingSerializer


# Create your views here.


class BookingListView(ListView):

	model = Booking
	template_name = "booking/booking.html"
	context_object_name = "booking"

	def get_queryset(self):
		today = datetime.today()
		return self.model.objects.filter(date=today)


class ReserveTable(APIView):

	model = Booking
	serializer_class = BookingSerializer

	def get(self, request, format=None):
		data = request.query_params
		date = datetime.fromisoformat(data['date'])
		booking = self.model.objects.filter(date=date)
		print(booking)
		serializer = self.serializer_class(booking, many=True)
		print(serializer.data)
		return Response(serializer.data, status=status.HTTP_200_OK)

	def post(self, request, format=None):
		return Response(status=status.HTTP_200_OK)

