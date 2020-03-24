from django.db import models

import uuid

def get_uuid():
	return str(uuid.uuid4().fields[0])


class Good(models.Model):

	name 				= models.CharField(max_length = 150, verbose_name='Наименование')
	name_full 			= models.CharField(max_length=1024, verbose_name='Наименование полное', blank=True)
	description 		= models.TextField(max_length=1024, verbose_name='Описание', blank=True)

	meta_name 			= models.CharField(max_length=150, verbose_name='meta name', blank=True, null=True, default='')
	meta_description 	= models.TextField(verbose_name='meta description', blank=True, null=True, default='')

	price 				= models.DecimalField(verbose_name='Цена', max_digits=15, decimal_places=0, blank=True, default='0')
	old_price			= models.DecimalField(verbose_name='Старая цена', max_digits=15, decimal_places=0, blank=True, default='0')

	quantity			= models.DecimalField(verbose_name='Остаток', max_digits=15, decimal_places=0, blank=True, default='0')

	vendor_code 		= models.CharField(max_length=150, verbose_name='Артикул', blank=True)
	slug 				= models.SlugField(max_length=10, verbose_name='Url', blank=True, db_index=True)

	is_catalog 			= models.BooleanField(verbose_name='Это каталог', default=False)

	parent_catalog 		= models.ForeignKey('Good', verbose_name='Родительский каталог', on_delete=models.PROTECT,null=True, blank=True, default='')

	def __str__(self):

		return self.name

	def save(self, *args, **kwargs):

		if self.slug == "":
			self.slug = get_uuid()
		super(Good, self).save(*args, **kwargs)
			
	
	class Meta:
		verbose_name = 'Товар'
		verbose_name_plural = 'Товары'
		


def get_image_name_270(instance, filename):
		
	
	return get_image_name(instance, filename, '270')

def get_image_name_570(instance, filename):
		
	
	return get_image_name(instance, filename, '570')

def get_image_name_1200(instance, filename):
		
	
	return get_image_name(instance, filename, '1200')

def get_image_name_90(instance, filename):
		
	
	return get_image_name(instance, filename, '90')		



def get_image_name(instance, filename, param):
		
	new_name = ('%s' + '_' + param + '.'+ filename.split('.')[-1]) % instance.slug
	return new_name



class Picture(models.Model):

	title 					= models.CharField(max_length=150, verbose_name='Наименование', blank=True)
	slug 					= models.SlugField(max_length=10, verbose_name='Url', blank=True, db_index=True)
	good 					= models.ForeignKey('Good', verbose_name='Товар', on_delete=models.CASCADE)

	image270				= models.ImageField(upload_to=get_image_name_270, verbose_name='Изображение 270x301', default=None, null=True, blank=True)
	image570				= models.ImageField(upload_to=get_image_name_570, verbose_name='Изображение 570x570', default=None, null=True, blank=True)
	image1200				= models.ImageField(upload_to=get_image_name_1200, verbose_name='Изображение 1200x1125', default=None, null=True, blank=True)
	image90					= models.ImageField(upload_to=get_image_name_90, verbose_name='Изображение 90x90', default=None, null=True, blank=True)

	main_image				= models.BooleanField(verbose_name='Основная картинка', default=False)

	def __str__(self):
		
		return self.slug


	def save(self, *args, **kwargs):
		
		if self.slug == "":
			self.slug = get_uuid()
			self.title = self.slug

		super(Picture, self).save(*args, **kwargs)


	class Meta:
		
		verbose_name = 'Картинка'
		verbose_name_plural = 'Картинки'		