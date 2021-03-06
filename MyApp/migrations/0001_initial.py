# Generated by Django 3.2.6 on 2021-10-15 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('addressID', models.AutoField(primary_key=True, serialize=False)),
                ('zipcode', models.CharField(max_length=10)),
                ('current_address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('cityId', models.AutoField(primary_key=True, serialize=False)),
                ('cityName', models.CharField(max_length=100)),
                ('stateName', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='FoodCategory',
            fields=[
                ('foodCategoryID', models.AutoField(primary_key=True, serialize=False)),
                ('categoryName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('orderId', models.AutoField(primary_key=True, serialize=False)),
                ('orderstatus', models.CharField(max_length=100)),
                ('orderTime', models.DateTimeField(auto_now_add=True)),
                ('addressID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyApp.address')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('userId', models.AutoField(primary_key=True, serialize=False)),
                ('userName', models.CharField(max_length=100, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=1500)),
                ('contactNo', models.CharField(max_length=15)),
                ('emailId', models.EmailField(max_length=50)),
                ('type_of_user', models.CharField(choices=[('customer', 'customer'), ('restaurant_owner', 'restaurant_owner')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='RestaurantOwner',
            fields=[
                ('ownerId', models.AutoField(primary_key=True, serialize=False)),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyApp.users')),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('restaurantId', models.AutoField(primary_key=True, serialize=False)),
                ('Address', models.CharField(max_length=100)),
                ('rating', models.IntegerField()),
                ('cityId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyApp.city')),
                ('ownerId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyApp.restaurantowner')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('paymentId', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.IntegerField()),
                ('paymentStatus', models.CharField(max_length=100)),
                ('orderId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyApp.order')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyApp.users')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='restaurantId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyApp.restaurant'),
        ),
        migrations.AddField(
            model_name='order',
            name='userId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyApp.users'),
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('menuID', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.TextField()),
                ('price', models.IntegerField(default=0)),
                ('foodCategoryId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyApp.foodcategory')),
                ('restaurantId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyApp.restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='ItemsOrdered',
            fields=[
                ('itemOrderId', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField(default=0)),
                ('price', models.IntegerField()),
                ('menuID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyApp.menu')),
                ('orderId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyApp.order')),
            ],
        ),
        migrations.AddField(
            model_name='foodcategory',
            name='restaurentID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyApp.restaurant'),
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customerId', models.AutoField(primary_key=True, serialize=False)),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyApp.users')),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='userId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyApp.users'),
        ),
        migrations.AddField(
            model_name='address',
            name='cityId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyApp.city'),
        ),
        migrations.AddField(
            model_name='address',
            name='userId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyApp.users'),
        ),
    ]
