from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from django import forms

from .models import User, Listings, Bids, Watch_list, Closed_listings, Comments

def index(request):
    return render(request, "auctions/index.html", {
        "listings": Listings.objects.all(),
        "Categories": Listings.Categories
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


# created a form class to display when user wants to add a new listing
class NewListing(forms.Form):
    title = forms.CharField(label="Title", widget=forms.TextInput(attrs={'class': "form-control"}))
    description = forms.CharField(label="Description", widget=forms.Textarea(attrs={'class': "form-control"}))
    starting_bid = forms.DecimalField(max_digits=8, decimal_places=2, label="starting_bid", widget=forms.NumberInput(attrs={'class': "form-control"}))
    image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': "form-control"}))
    category = forms.CharField(label="Categories", widget=forms.Select(choices=Listings.Categories, attrs={'class': "form-control"}))

@login_required
def new_listing(request):
    if request.method == "POST":
        form = NewListing(request.POST, request.FILES)
        # Check if form data is valid (server-side)
        if form.is_valid():

            # add info to the database
            listing = Listings(user_id=User.objects.get(id=request.user.id), title=form.cleaned_data["title"], description=form.cleaned_data["description"], starting_bid=form.cleaned_data["starting_bid"],image=form.cleaned_data["image"], category=form.cleaned_data["category"])
            # save to the database
            listing.save()
            # save the starting bid to a diffrent table
            bid = Bids(listing_id=Listings.objects.get(id=listing.id), bid=form.cleaned_data["starting_bid"], winner=User.objects.get(id=request.user.id))
            bid.save()
            # return the info of the item that was just added
            listing = Listings.objects.get(id=listing.id)
            return render(request, "auctions/listing.html", {
                # retun the listing
                "listing": listing,
                # category
                "item_category": listing.Categories[int(listing.category)][1],
                # retun the current bid on this listing
                "bid": Bids.objects.get(listing_id=listing.id),
                # return the id of the user that is currently logged in
                "winner": request.user.id,
                "comments": Comments.objects.filter(listing_id=listing.id)
            })
    # render a new form
    return render(request, "auctions/new_listing.html",{
    "form": NewListing()
    })

def listing(request, id):
    listing = Listings.objects.get(id=id)
    return render(request, "auctions/listing.html", {
        # retun the listing
        "listing": listing,
        # category
        "item_category": listing.Categories[int(listing.category)][1],
        # retun the current bid on this listing
        "bid": Bids.objects.get(listing_id=id),
        # return the id of the user that is currently logged in
        "winner": request.user.id,
        "comments": Comments.objects.filter(listing_id=id)
    })

@login_required
def bid(request):
    # if the user submits the popup form then collect the data
    if request.method == "POST":
        listing_id = request.POST["listing_id"]
        id = request.POST["id"]
        winner = request.POST["winner"]
        bid = request.POST['bid']

        # get the starging bid price
        starting_bid = Listings.objects.get(id=listing_id)
        # get the current bid from the database
        updated_bid = Bids.objects.get(id=id)

        if float(bid) < float(updated_bid.bid) or float(bid) == float(updated_bid.bid):
            return render(request, "auctions/bid.html",{
            "message": "Bid must be greater then curent bid"
            })


        # update the database with the new information
        updated_bid = Bids.objects.get(id=id)
        updated_bid.winner = User.objects.get(id=winner)
        updated_bid.bid = bid
        updated_bid.save()

        return render(request, "auctions/bid.html",{
        "message": "Thank you for bidding"
        })
    return render(request, "auctions/bid.html",{
    "message": "Place your bid"
    })

@login_required
def watch_list(request):
    # if user wants to add item to watch list
    if request.method == "POST":
        # get the id of the current user and the id of the item the user wants to add
        user_id = request.POST["user_id"]
        listing_id = request.POST["listing_id"]

        # add the information to the watch list table
        watch_item = Watch_list(user_id=User.objects.get(id=user_id), listing_id=Listings.objects.get(id=listing_id))
        watch_item.save()
    # return the watch list
    return render(request, "auctions/Watch_list.html", {
        "listings": Watch_list.objects.filter(user_id=request.user.id)
    })

@login_required
def remove_from_watch_list(request):
    # if user sumites request to remove item from list
    if request.method == "POST":
        # get the id of the item user wants to delete
        id = request.POST["id"]

        # delete item
        item = Watch_list.objects.get(id=id)
        item.delete()
        # retun the users updated watch list
        return render(request, "auctions/Watch_list.html", {
            "listings": Watch_list.objects.filter(user_id=request.user.id)
        })

@login_required
def end_auction(request):
    # if user closes the listing
    if request.method == "POST":
        # pull the listing id and the winner
        listing_id = request.POST["listing_id"]
        bid_id = request.POST["bid_id"]

        # pull information from the database and save it in these varubals
        listing = Listings.objects.get(id=listing_id)
        bid = Bids.objects.get(id=bid_id)

        # add the inform to closed auctions
        close_listing = Closed_listings(user_id=User.objects.get(id=listing.user_id.id), title=listing.title, description=listing.description, price_sold=bid.bid, image=listing.image, winner=bid.winner)
        close_listing.save()

        # delete the listing
        listing.delete()
        bid.delete()
    return render(request, "auctions/index.html",{
        "listings": Closed_listings.objects.all()
    })

def closed_listings(request):
    return render(request, "auctions/closed_listings.html",{
        "listings": Closed_listings.objects.all()
    })

def closed(request, id):
    return render(request, "auctions/closed.html",{
        "listing": Closed_listings.objects.get(id=id)
    })

def comment(request):
    if request.method == "POST":
        id = request.POST["listing_id"]
        comment = Comments(listing_id=Listings.objects.get(id=request.POST["listing_id"]), comment=request.POST["comment"])
        comment.save()
    # return this listing
    return render(request, "auctions/listing.html", {
        # retun the listing
        "listing": Listings.objects.get(id=id),
        # retun the current bid on this listing
        "bid": Bids.objects.get(listing_id=id),
        # return the id of the user that is currently logged in
        "winner": request.user.id,
        "comments": Comments.objects.filter(listing_id=id)
    })


def Categories(request):
    if request.method == "POST":
        return render(request, "auctions/index.html", {
            "listings": Listings.objects.filter(category=request.POST["myselect"]),
            "Categories": Listings.Categories
        })

    return render(request, "auctions/index.html", {
        "listings": Listings.objects.all(),
        "Categories": Listings.Categories
    })
