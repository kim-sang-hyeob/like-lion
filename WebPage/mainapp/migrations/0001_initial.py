# Generated by Django 3.2.8 on 2021-10-23 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company_Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100, verbose_name='회사 이름')),
                ('ceo_of_company', models.CharField(max_length=50, verbose_name='회사 대표')),
                ('year_of_establishment', models.CharField(max_length=15, verbose_name='설립 연도')),
                ('area', models.CharField(max_length=50, verbose_name='지역')),
                ('number', models.CharField(max_length=12, verbose_name='전화번호')),
                ('email_address', models.CharField(max_length=50, verbose_name='이메일 주소')),
                ('homepage', models.CharField(max_length=30, verbose_name='홈페이지')),
                ('introduce_company', models.TextField(verbose_name='회사 소개')),
            ],
        ),
    ]
