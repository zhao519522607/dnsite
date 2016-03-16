from django.db import models

# Create your models here.
class dns_records(models.Model):
	zone = models.CharField(max_length=15,default='wecash.net')
	host = models.CharField(max_length=15,default='www')
	type = models.CharField(max_length=5,default='A')
	data = models.IPAddressField(default='192.168.240.23')
	ttl = models.IntegerField(default=86400)
	mx_priority = models.IntegerField(blank=True,null=True)
	refresh = models.IntegerField(default=3600)
	retry = models.IntegerField(default=15)
	expire = models.IntegerField(default=86400)
	minimum = models.IntegerField(default=3600)
	serial = models.IntegerField(default=2008082700)
	resp_person = models.CharField(max_length=30,default='root.domain.com.')
	primary_ns = models.CharField(max_length=30,default='ns1.domain.com.')
	class Meta:
         	db_table = 'dns_records'
