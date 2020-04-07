from django.db import models

# Create your models here.


shape_choices = (
	(0, 'Прямоугольный'),
	(1, 'Овальный'),
	)


class Table(models.Model):

	number = models.IntegerField(blank=False, null=False)
	places = models.IntegerField(blank=False, null=False)
	shape = models.IntegerField(choices=shape_choices, blank=False, null=False)
	horizontal = models.DecimalField(decimal_places=2, max_digits=4, blank=False, null=False)
	vertical = models.DecimalField(decimal_places=2, max_digits=4, blank=False, null=False)
	width = models.DecimalField(decimal_places=2, max_digits=4, blank=False, null=False)
	length = models.DecimalField(decimal_places=2, max_digits=4, blank=False, null=False)

	def __str__(self):
		return f"Table №{self.number} with {self.places} places"

	# @property
	# def horizontal_ends(self):
	# 	return self.horizontal + self.width

	# @property
	# def vertical_ends(self):
	# 	return self.vertical + self.length

	# @property
	# def size(self):
	# 	result = (
	# 		(self.horizontal, self.horizontal_ends),
	# 		(self.vertical, self.vertical_ends)
	# 		)
	# 	return result

	# def intersaction(self, size1, size2):
	# 	# return True if tables intersactions 

	# 	if ( (size1[0][0] > size2[0][0] and size1[0][0] < size2[0][1]) or 
	# 		 (size1[0][1] > size2[0][0] and size1[0][1] < size2[0][1]) ):
	# 		# first table inside second by horizontal
	# 		if ( (size1[1][0] > size2[1][0] and size1[1][0] < size2[1][1]) or 
	# 			 (size1[1][1] > size2[1][0] and size1[1][1] < size2[1][1]) ):
	# 			# first table inside second by vertical
	# 			return True

	# 	if ( (size2[0][0] > size1[0][0] and size2[0][0] < size1[0][1]) or 
	# 		 (size2[0][1] > size1[0][0] and size2[0][1] < size1[0][1]) ):
	# 		# first table inside second by horizontal
	# 		if ( (size2[1][0] > size1[1][0] and size2[1][0] < size1[1][1]) or 
	# 			 (size2[1][1] > size1[1][0] and size2[1][1] < size1[1][1]) ):
	# 			# first table inside second by vertical
	# 			return True

	# 	return False

	# def check_table_location(self):
	# 	# return True if location is valid

	# 	tables = Table.objects.exclude(pk=self.pk)

	# 	for table in tables:
	# 		if self.intersaction(table.size, self.size):
	# 			return False 

	# 	return True

	@property
	def center(self):
		x = self.horizontal + self.width/2
		y = self.vertical + self.length/2

		return float(x), float(y)

	def intersaction(self, table1, table2):
		# return True if tables intersactions
		x_t1, y_t1 = table1.center
		x_t2, y_t2 = table2.center
		x_length = abs(x_t1-x_t2)
		y_length = abs(y_t1-y_t2)

		width_average = (table1.width+table2.width) / 2
		length_average = (table1.length+table2.length) / 2

		if (x_length <= width_average) and (y_length <= length_average):
			return True

		return False

	def check_table_location(self):
		# return True if location is valid

		tables = Table.objects.exclude(pk=self.pk)

		for table in tables:
			if self.intersaction(table, self):
				return False 

		return True

	def save(self, *args, **kwargs):

		max_width = self.vertical + self.width
		max_lenth = self.horizontal + self.length

		if max_width > 100 or max_lenth > 100:
			raise ValueError("Can not create table with those properties")

		if not self.check_table_location():
			raise ValueError("There are table in this location")

		super().save(*args, **kwargs)


class Booking(models.Model):

	table = models.ForeignKey(Table, on_delete=models.CASCADE, null=True, blank=True)
	date = models.DateField(auto_now_add=True)
	reserved = models.BooleanField(default=False)

	def __str__(self):
		return f"Booking {self.date} of table"