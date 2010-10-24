from django.db import models

class Link(models.Model):
	link = models.TextField()
	desc = models.CharField(max_length=255)
	hash = models.CharField(max_length=10)
	pub_date = models.DateTimeField('date published')
	def __unicode__(self):
		return self.desc

class Statistic(models.Model):
	link = models.ForeignKey(Link)
	ip = models.CharField(max_length=200)
	last_viewed = models.DateTimeField('last viewed')
