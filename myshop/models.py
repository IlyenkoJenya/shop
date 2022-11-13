from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        # ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('myshop:product_list_by_category', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category,
                                 related_name='products',
                                 on_delete=models.CASCADE)

    name = models.CharField(max_length=150, db_index=True)
    slug = models.CharField(max_length=150, db_index=True, unique=True)
    image = models.ImageField(upload_to='product/%Y/%m/%d', blank=True)
    image1 = models.ImageField(upload_to='product/%Y/%m/%d', blank=True)
    image2 = models.ImageField(upload_to='product/%Y/%m/%d', blank=True)
    image3 = models.ImageField(upload_to='product/%Y/%m/%d', blank=True)
    image4 = models.ImageField(upload_to='product/%Y/%m/%d', blank=True)
    image5 = models.ImageField(upload_to='product/%Y/%m/%d', blank=True)
    image7 = models.ImageField(upload_to='product/%Y/%m/%d', blank=True)
    image8 = models.ImageField(upload_to='product/%Y/%m/%d', blank=True)
    description = models.TextField(max_length=1000, blank=True)
    artikul = models.TextField(max_length=1000, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    uploaded = models.DateTimeField(auto_now=True)
    k_short_description = models.TextField(max_length=1000, blank=True)
    k_proizvoditel = models.TextField(max_length=1000, blank=True)
    k_max_mosch = models.TextField(max_length=1000, blank=True)
    k_min_mosch = models.TextField(max_length=1000, blank=True)
    k_norma_prirod_gas = models.TextField(max_length=1000, blank=True)
    k_norma_jj_gas = models.TextField(max_length=1000, blank=True)
    k_obem_baka = models.TextField(max_length=1000, blank=True)
    k_nomimal_podacha_gaza = models.TextField(max_length=1000, blank=True)
    k_max_temp_contura = models.TextField(max_length=1000, blank=True)
    k_max_temp_gvs = models.TextField(max_length=1000, blank=True)
    k_min_temp_gvs = models.TextField(max_length=1000, blank=True)
    k_pritok_pri_at25 = models.TextField(max_length=1000, blank=True)
    k_trebuemaya_mosch = models.TextField(max_length=1000, blank=True)
    k_garantiya = models.TextField(max_length=1000, blank=True)

    f_short_description = models.TextField(max_length=1000, blank=True)
    f_chislo_stupeney = models.TextField(max_length=1000, blank=True)
    f_proizviditelnost = models.TextField(max_length=1000, blank=True)
    f_resurs = models.TextField(max_length=1000, blank=True)
    f_min_bar = models.TextField(max_length=1000, blank=True)
    f_max_bar = models.TextField(max_length=1000, blank=True)
    f_nasos = models.TextField(max_length=1000, blank=True)
    f_krav_v_korobke = models.TextField(max_length=1000, blank=True)
    f_type_voda = models.TextField(max_length=1000, blank=True)
    f_razmer = models.TextField(max_length=1000, blank=True)
    f_garantiya = models.TextField(max_length=1000, blank=True)




    class Meta:
        ordering = ('name',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('myshop:product_detail', args=[self.id, self.slug])


class Fb(models.Model):
    name = models.CharField(max_length=30, blank=True, verbose_name='Имя заявителя')
    phone = models.CharField(max_length=12, default='+7', verbose_name='Телефон заявителя',
                             help_text='Ввод номера в формате 8 999 999 99 99')
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата заявки')
