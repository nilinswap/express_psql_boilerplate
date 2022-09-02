from django.db import models
from django.utils import timezone
from django.contrib import admin


class Role(models.Model):
	role = models.CharField(max_length=50, primary_key=True)
	
	def __str__(self):
		"""String for representing the Model object."""
		return f"{self.role}"


class BuyerInfo(models.Model):
	debit_details_nosql_id = models.CharField(max_length=100, unique=True)


class BankDetails(models.Model):
	ifsc_code = models.CharField(max_length=50)
	bank_name = models.CharField(max_length=100)
	account_number = models.CharField(max_length=50)
	
	def __str__(self):
		"""String for representing the Model object."""
		return f"{self.ifsc_code}{self.bank_name}{self.account_number}"


class ArtistInfo(models.Model):
	subdomain = models.CharField(max_length=50)
	bank_details = models.ForeignKey(BankDetails, null=True,
	                                 on_delete=models.SET_NULL)
	description = models.TextField()
	shop_page_nosql_id = models.CharField(max_length=100, unique=True,
	                                      null=True)
	
	def __str__(self):
		"""String for representing the Model object."""
		return f"{self.subdomain}"


class UserDetails(models.Model):
	role = models.ForeignKey(Role, on_delete=models.PROTECT)
	is_phone_verified = models.BooleanField(default=False)
	is_email_verified = models.BooleanField(default=False)
	dp_s3_url = models.CharField(max_length=150, null=True)
	buyer_info = models.ForeignKey(BuyerInfo, null=True,
	                               on_delete=models.PROTECT)
	artist_info = models.ForeignKey(ArtistInfo, null=True,
	                                on_delete=models.PROTECT)
	
	def __str__(self):
		"""String for representing the Model object."""
		return f"{self.first_name}"


class User(models.Model):
	email = models.EmailField(unique=True)
	phone = models.CharField(max_length=15, unique=True)
	password = models.CharField(max_length=100)
	first_name = models.CharField(max_length=50, null=False)
	last_name = models.CharField(max_length=50, null=False)
	details = models.ForeignKey(UserDetails, on_delete=models.PROTECT,
	                              null=True)
	
	def __str__(self):
		"""String for representing the Model object."""
		return f"{self.email}"


class Artifact(models.Model):
	artist = models.ForeignKey(User, null=True,
	                           on_delete=models.SET_NULL)
	title = models.CharField(max_length=200)
	description = models.TextField()
	price = models.FloatField()
	is_exclusive = models.BooleanField()
	
	def __str__(self):
		"""String for representing the Model object."""
		return f"{self.title}"


class Picture(models.Model):
	artifact = models.ForeignKey(Artifact, on_delete=models.CASCADE)
	s3_url = models.CharField(max_length=150, unique=True)
	
	def __str__(self):
		"""String for representing the Model object."""
		return f"{self.s3_url}"


class PaymentStatus(models.Model):
	status = models.CharField(max_length=50, primary_key=True)
	
	@classmethod
	def get_default_pk(self):
		return self.objects.get(status='unassigned').pk
	
	def __str__(self):
		"""String for representing the Model object."""
		return f"{self.status}"


class Payment(models.Model):
	amount = models.FloatField()
	mode = models.CharField(max_length=50, null=True)
	status = models.ForeignKey(PaymentStatus, on_delete=models.PROTECT,
	                           default=PaymentStatus.get_default_pk)
	details = models.JSONField(null=True)
	created_on = models.DateTimeField(default=timezone.now)
	
	def __str__(self):
		"""String for representing the Model object."""
		return f"{self.mode}{self.created_on}"


class OrderStatus(models.Model):
	status = models.CharField(max_length=50, primary_key=True)
	
	def __str__(self):
		"""String for representing the Model object."""
		return f"{self.status}"
	

class Order(models.Model):
	buyer = models.ForeignKey(User, on_delete=models.CASCADE)
	artifact = models.ForeignKey(Artifact, on_delete=models.PROTECT)
	payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
	status = models.ForeignKey(OrderStatus, on_delete=models.PROTECT)
	created_on = models.DateTimeField(default=timezone.now)
	
	def __str__(self):
		"""String for representing the Model object."""
		return f"{self.created_on}"


class Cart(models.Model):
	buyer = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
	artifact = models.ForeignKey(Artifact, null=False, on_delete=models.CASCADE)


admin.site.register(PaymentStatus)
admin.site.register(OrderStatus)
admin.site.register(Role)
admin.site.register(Payment)
admin.site.register(Order)
admin.site.register(User)

'''
NoSql
- ShotState
- state snapshot (containing but not limited to ‘checkoutState’, ‘cartState’ etc)
- LikedArts should be nosql
'''
