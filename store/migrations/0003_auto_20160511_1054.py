# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20160511_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='author_usuario',
            field=models.ForeignKey(unique=True, verbose_name='Usuario', to=settings.AUTH_USER_MODEL),
        ),
    ]
