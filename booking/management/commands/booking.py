import random
from datetime import datetime, timedelta

from django.core.management.base import BaseCommand, CommandError

from booking.models import Table, Booking


class Command(BaseCommand):

	help = "Booking command management"

	def handle(self, *args, **options):

		self.stdout.write(self.help)

		table = Table.objects.last()
		count = 1
		if table:
			count = table.pk + 1
		stop = count + 8
		
		week = [datetime.today()+timedelta(days=i) for i in range(0, 7)] 
		tables = Table.objects.all()

		for day in week:
			for table in tables:
				print(table, day)
				kwargs = {
					'table': table,
					'date': day,
					'reserved': random.randint(0, 1)
				}
				booking = Booking.objects.filter(table=table,
												 date=day)
				if not booking.last():
					booking = Booking.objects.create(**kwargs)
				else:
					booking.update(**kwargs)
				

