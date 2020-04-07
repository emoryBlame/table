import random

from django.core.management.base import BaseCommand, CommandError

from booking.models import Table


class Command(BaseCommand):

	help = "Table command management"

	def handle(self, *args, **options):

		self.stdout.write(self.help)

		table = Table.objects.last()
		count = 1
		if table:
			count = table.pk + 1
		stop = count + 8

		while True:
			data = {
				"number": count,
				"places": random.randint(1, 5),
				"shape": random.randint(0, 1),
				"horizontal": random.randint(0, 80),
				"vertical": random.randint(1, 80),
				"width": random.randint(1, 20),
				"length": random.randint(1, 20),
			}
			try:
				Table.objects.create(**data)
			except Exception as exc:
				self.stdout.write(f"{exc}")
			else:
				count += 1

			if count == stop: 
				break

