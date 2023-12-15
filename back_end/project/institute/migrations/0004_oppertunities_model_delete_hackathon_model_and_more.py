# Generated by Django 5.0 on 2023-12-14 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institute', '0003_alter_scholarship_model_amount_given'),
    ]

    operations = [
        migrations.CreateModel(
            name='Oppertunities_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='intern')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('organiser', models.CharField(max_length=100)),
                ('apply', models.URLField()),
                ('amount', models.DecimalField(decimal_places=3, max_digits=10)),
                ('Start_date', models.DateField()),
                ('End_date', models.DateField()),
                ('is_online', models.BooleanField(default=False)),
                ('is_offline', models.BooleanField(default=False)),
                ('openings', models.IntegerField()),
                ('is_scholarship', models.BooleanField(default=False)),
                ('is_hack', models.BooleanField(default=False)),
                ('is_intern', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='Hackathon_model',
        ),
        migrations.DeleteModel(
            name='InternJob_model',
        ),
        migrations.DeleteModel(
            name='Scholarship_model',
        ),
    ]
