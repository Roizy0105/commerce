from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listings(models.Model):
    Categories = (
        ("0", ""),
        ("1", "Antiques"),
        ("2", "Art"),
        ("3", "Baby"),
        ("4", "Books"),
        ("5", "Business & Industrial"),
        ("6", "Cameras & Photo"),
        ("7", "Cell Phones & Accessories"),
        ("8", "Clothing, Shoes & Accessories"),
        ("9", "Coins & Paper Money"),
        ("10", "Collectibles"),
        ("11", "Computers/Tablets & Networking"),
        ("12", "Consumer Electronics"),
        ("13", "Crafts"),
        ("14", "Dolls & Bears"),
        ("15", "DVDs & Movies"),
        ("16", "eBay Motors"),
        ("17", "Entertainment Memorabilia"),
        ("18", "Gift Cards & Coupons"),
        ("19", "Health & Beauty"),
        ("20", "Home & Garden"),
        ("21", "Jewelry & Watches"),
        ("22", "Music"),
        ("23", "Musical Instruments & Gear"),
        ("24", "Pet Supplies"),
        ("25", "Pottery & Glass"),
        ("26", "Real Estate"),
        ("27", "Specialty Services"),
        ("28", "Sporting Goods"),
        ("29", "Sports Mem, Cards & Fan Shop"),
        ("30", "Stamps"),
        ("31", "Tickets & Experiences"),
        ("32", "Toys & Hobbies"),
        ("33", "Travel"),
        ("34", "Video Games & Consoles"),
        ("35", "Everything Else"),
    )
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    starting_bid = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to="images/")
    category = models.CharField(max_length=100, choices=Categories)

class Bids(models.Model):
    listing_id = models.ForeignKey(Listings, on_delete=models.CASCADE, related_name='owner')
    bid = models.DecimalField(max_digits=5, decimal_places=2)
    winner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='winner')

class Watch_list(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    listing_id = models.ForeignKey(Listings, on_delete=models.CASCADE)

class Closed_listings(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='stared_auction')
    title = models.CharField(max_length=100)
    description = models.TextField()
    price_sold = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to="images/")
    winner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='won_auction')

class Comments(models.Model):
    listing_id = models.ForeignKey(Listings, on_delete=models.CASCADE)
    comment = models.TextField()
