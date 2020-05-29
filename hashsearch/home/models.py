from django.db import models

class FeedElement(models.Model):
    width = models.IntegerField()
    height = models.IntegerField()
    imageurl=models.URLField(max_length=200, primary_key=True)
    fullimage=models.URLField(max_length=200, unique=True, default='https://cdn.pixabay.com/photo/2017/03/09/12/31/error-2129569_1280.jpg')
    views = models.BigIntegerField()
    def __str__(self):
    	return self.imageurl
    class meta:
    	ordering=['-views']

class SearchTag(models.Model):
	tag = models.CharField(max_length=200, primary_key=True)
	frequency = models.BigIntegerField()
	def __str__(self):
		return self.tag

class ImageTags(models.Model):
	image = models.ForeignKey(FeedElement, on_delete=models.CASCADE)
	imgtag = models.ForeignKey(SearchTag,on_delete=models.CASCADE)
	
	class meta:
		constraints=[
			models.UniqueConstraint(fields=['image', 'imgtag'], name='unique imagetag')
			]
	def __str__(self):
		return "IMAGE=> "+self.image.imageurl+ "TAG=> " + self.imgtag.tag + "\n"
	
	