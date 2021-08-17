# Generated by Django 3.2.5 on 2021-07-28 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_alter_categories_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='listings',
            name='category',
            field=models.CharField(blank=True, choices=[('0', ''), ('1', 'Antiques'), ('2', 'Art'), ('3', 'Baby'), ('4', 'Books'), ('5', 'Business & Industrial'), ('6', 'Cameras & Photo'), ('7', 'Cell Phones & Accessories'), ('8', 'Clothing, Shoes & Accessories'), ('9', 'Coins & Paper Money'), ('10', 'Collectibles'), ('11', 'Computers/Tablets & Networking'), ('12', 'Consumer Electronics'), ('13', 'Crafts'), ('14', 'Dolls & Bears'), ('15', 'DVDs & Movies'), ('16', 'eBay Motors'), ('17', 'Entertainment Memorabilia'), ('18', 'Gift Cards & Coupons'), ('19', 'Health & Beauty'), ('20', 'Home & Garden'), ('21', 'Jewelry & Watches'), ('22', 'Music'), ('23', 'Musical Instruments & Gear'), ('24', 'Pet Supplies'), ('25', 'Pottery & Glass'), ('26', 'Real Estate'), ('27', 'Specialty Services'), ('28', 'Sporting Goods'), ('29', 'Sports Mem, Cards & Fan Shop'), ('30', 'Stamps'), ('31', 'Tickets & Experiences'), ('32', 'Toys & Hobbies'), ('33', 'Travel'), ('34', 'Video Games & Consoles'), ('35', 'Everything Else')], max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='Categories',
        ),
    ]