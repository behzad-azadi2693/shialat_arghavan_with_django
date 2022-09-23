from django.db import models
from uuid import uuid4
from django.core.validators import MaxValueValidator
# Create your models here.

class CategoryModel(models.Model):
    image = models.ImageField(upload_to='category')
    name = models.CharField(max_length=200, unique=True, verbose_name=' نام دسته بندی')

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        try:
            if this.image != self.image:
                this.image.delete()
        except: 
            pass
        
        super(CategoryModel, self).save()


    def delete(self, *args, **kwargs):
        self.image.delete()
        super(CategoryModel, self).delete()


class ProductModel(models.Model):
    name = models.CharField(max_length=200, verbose_name='نام محصول')
    category = models.ForeignKey(CategoryModel, on_delete=models.SET_NULL, null=True, verbose_name='انتخاب دسته بندی')
    slug = models.SlugField(default=uuid4())
    price = models.PositiveIntegerField(verbose_name='قیمت کالا')
    ranking = models.PositiveIntegerField(verbose_name='ستاره ها', validators=[MaxValueValidator(5)], help_text='عددی از ۱ تا ۵')
    color = models.CharField(max_length=200, verbose_name='رنگ های موجود')
    image = models.ImageField(upload_to='products', verbose_name='تصویر اصلی محصول')
    new_product = models.BooleanField(default=False, verbose_name='محصول جدید؟؟')
    public = models.BooleanField(default=True, verbose_name='نمایش محصول؟؟')
    description = models.TextField(verbose_name='توضیحات')
    specification = models.TextField(verbose_name='ویژگی های محصول', help_text='هر ویژگی جداگانه را با علامت , از هم جدا نمایید')
    search = models.TextField(verbose_name='جستجوی بهینه', help_text='هر بخش جداگانه را با علامت , از هم جدا نمایید')

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'
        ordering = ('-id', 'public', 'new_product')
        
    def __str__(self):
        return f'{self.name}-{self.id}'

    def update_method(self):
        slugify = self.name.replace(' ','_').replace('/','_')
        ProductModel.objects.filter(id=self.id).update(slug = f'{slugify}-{self.id}')

    def save(self, *args, **kwargs):
        try:
            this = ProductModel.objects.get(id=self.id)
            if this.image != self.image:
                this.image.delete()
        except: 
            pass
        super(ProductModel, self).save()
        self.update_method()

    def delete(self, *args, **kwargs):
        self.image.delete()
        super(ProductModel, self).delete()

    @property
    def ranking_range(self):
        return range(self.ranking)

class ProductsImagesModel(models.Model):
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product', verbose_name='تصویر محصول')

    def __str__(self):
        return f'{self.product.name}-{self.id}'

    def save(self, *args, **kwargs):
        try:
            this = ProductsImagesModel.objects.get(id=self.id)
            if this.image != self.image:
                this.image.delete()
        except: 
            pass
        super(ProductsImagesModel, self).save()

    def delete(self, *args, **kwargs):
        self.image.delete()
        super(ProductsImagesModel, self).delete()


class ContactModel(models.Model):
    name = models.CharField(max_length=200, verbose_name='نام')
    email = models.EmailField(verbose_name='ایمیل')
    subject = models.CharField(max_length=200, verbose_name='موضوع')
    message = models.TextField(verbose_name='پیغام')
    read = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}-{self.id}'

    class Meta:
        verbose_name = 'ارتباط با ما'
        verbose_name_plural = 'ارتباط با ما'
        ordering = ('-id', '-date', '-read')