from rest_framework import serializers

from booking.models import Table, Booking


class TableSerializer(serializers.ModelSerializer):

	class Meta:
		model = Table
		fields = ('__all__')


class BookingSerializer(serializers.ModelSerializer):

	table = TableSerializer()

	class Meta:
		model = Booking
		fields = (
			'table',
			'date',
			'reserved'
			)