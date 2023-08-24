from django.contrib.auth import get_user_model
from django.db import models
from django.contrib import admin
from django.utils.html import format_html


User = get_user_model()


class Advertisement(models.Model):
    title = models.CharField(max_length=80, verbose_name='заголовок')
    description = models.TextField('описание')
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='цена')
    auction = models.BooleanField(help_text='Отметьте, если торг уместен', verbose_name='возможность торга')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/")

    @admin.display(description='Дата создания')
    def created_date(self):
        from django.utils import timezone
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime('%H:%M')
            return format_html("<span style='color: green'> Сегодня в {}</span>", created_time)
        return self.created_at

    @admin.display(description='Дата изменения')
    def updated_date(self):
        from django.utils import timezone
        if self.updated_at.date() == timezone.now().date():
            updated_time = self.updated_at.time().strftime('%H:%M')
            return format_html("<span style='color: red'> Сегодня в {}</span>", updated_time)
        return self.updated_at



    class Meta:
        db_table = 'advertisements'
        verbose_name = 'объявлеине'
        verbose_name_plural = 'объявления'

    def __str__(self):
        return f"Advertisement(id={self.id}, title={self.title}, price={self.price})"

