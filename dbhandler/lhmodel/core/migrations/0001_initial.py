# Generated by Django 3.1.5 on 2021-01-14 12:03

import core.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artifact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('price', models.FloatField()),
                ('is_exclusive', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='ArtistInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subdomain', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('shop_page_nosql_id', models.CharField(max_length=100, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='BankDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ifsc_code', models.CharField(max_length=50)),
                ('bank_name', models.CharField(max_length=100)),
                ('account_number', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='BuyerInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('debit_details_nosql_id', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('status', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentStatus',
            fields=[
                ('status', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('role', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('is_phone_verified', models.BooleanField(default=False)),
                ('is_email_verified', models.BooleanField(default=False)),
                ('dp_s3_url', models.CharField(max_length=150, null=True)),
                ('artist_info', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='core.artistinfo')),
                ('buyer_info', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='core.buyerinfo')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=15, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('details', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='core.userdetails')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.role')),
            ],
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s3_url', models.CharField(max_length=150, unique=True)),
                ('artifact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.artifact')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('mode', models.CharField(max_length=50, null=True)),
                ('details', models.JSONField(null=True)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.ForeignKey(default=core.models.PaymentStatus.get_default_pk, on_delete=django.db.models.deletion.PROTECT, to='core.paymentstatus')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('artifact', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.artifact')),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.user')),
                ('payment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.payment')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.orderstatus')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artifact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.artifact')),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.user')),
            ],
        ),
        migrations.AddField(
            model_name='artistinfo',
            name='bank_details',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.bankdetails'),
        ),
        migrations.AddField(
            model_name='artifact',
            name='artist',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.user'),
        ),
    ]
