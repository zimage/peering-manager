# Generated by Django 2.1.3 on 2018-11-13 20:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('peering', '0020_auto_20181105_0850'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoutingPolicy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=128)),
                ('slug', models.SlugField(unique=True)),
                ('type', models.CharField(choices=[('import-policy', 'Import'), ('export-policy', 'Export')], default='import-policy', max_length=50)),
                ('comment', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'routing policies',
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='directpeeringsession',
            name='export_routing_policy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='directpeeringsession_export_routing_policy', to='peering.RoutingPolicy'),
        ),
        migrations.AddField(
            model_name='directpeeringsession',
            name='import_routing_policy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='directpeeringsession_import_routing_policy', to='peering.RoutingPolicy'),
        ),
        migrations.AddField(
            model_name='internetexchange',
            name='export_routing_policy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='internetexchange_export_routing_policy', to='peering.RoutingPolicy'),
        ),
        migrations.AddField(
            model_name='internetexchange',
            name='import_routing_policy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='internetexchange_import_routing_policy', to='peering.RoutingPolicy'),
        ),
        migrations.AddField(
            model_name='internetexchangepeeringsession',
            name='export_routing_policy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='internetexchangepeeringsession_export_routing_policy', to='peering.RoutingPolicy'),
        ),
        migrations.AddField(
            model_name='internetexchangepeeringsession',
            name='import_routing_policy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='internetexchangepeeringsession_import_routing_policy', to='peering.RoutingPolicy'),
        ),
    ]
