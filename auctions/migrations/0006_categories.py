# Generated by Django 3.2.5 on 2021-07-28 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_comments'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('1', 'Antiques'), ('2', 'Art'), ('3', 'Baby'), ('4', 'Books'), ('5', 'Business & Industrial'), ('6', 'Cameras & Photo'), ('7', 'Cell Phones & Accessories'), ('8', 'Clothing, Shoes & Accessories'), ('9', 'Coins & Paper Money'), ('10', 'Collectibles'), ('11', 'Computers/Tablets & Networking'), ('12', 'Consumer Electronics'), ('13', 'Crafts'), ('14', 'Dolls & Bears'), ('15', 'DVDs & Movies'), ('16', 'eBay Motors'), ('17', 'Entertainment Memorabilia'), ('18', 'Gift Cards & Coupons'), ('19', 'Health & Beauty'), ('20', 'Home & Garden'), ('21', 'Jewelry & Watches'), ('22', 'Music'), ('23', 'Musical Instruments & Gear'), ('24', 'Pet Supplies'), ('25', 'Pottery & Glass'), ('26', 'Real Estate'), ('27', 'Specialty Services'), ('28', 'Sporting Goods'), ('29', 'Sports Mem, Cards & Fan Shop'), ('30', 'Stamps'), ('31', 'Tickets & Experiences'), ('32', 'Toys & Hobbies'), ('33', 'Travel'), ('34', 'Video Games & Consoles'), ('35', 'Everything Else')], max_length=100)),
                ('listing_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctions.listings')),
            ],
        ),
    ]
