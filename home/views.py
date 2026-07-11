from django.shortcuts import render

# Create your views here.
def home(request):
    categories = [
        {"name": "Mobiles", "icon": "phone"},
        {"name": "Fashion", "icon": "fashion"},
        {"name": "Electronics", "icon": "headphones"},
        {"name": "Home", "icon": "home"},
        {"name": "Appliances", "icon": "washer"},
        {"name": "Beauty", "icon": "beauty"},
        {"name": "Toys", "icon": "toy"},
        {"name": "Grocery", "icon": "grocery"},
    ]

    products = [
        {
            "name": "Smartphone Pro",
            "price": "From Rs. 12,999",
            "tag": "Best seller",
            "type": "phone",
        },
        {
            "name": "Wireless Headphones",
            "price": "From Rs. 999",
            "tag": "40% off",
            "type": "headphones",
        },
        {
            "name": "Running Shoes",
            "price": "From Rs. 1,499",
            "tag": "Hot deal",
            "type": "shoe",
        },
        {
            "name": "Mixer Grinder",
            "price": "From Rs. 2,199",
            "tag": "Kitchen picks",
            "type": "appliance",
        },
    ]

    deals = [
        "Bank offers",
        "No-cost EMI",
        "Exchange bonus",
        "Free delivery",
    ]

    return render(
        request,
        "home/home.html",
        {"categories": categories, "products": products, "deals": deals},
    )
