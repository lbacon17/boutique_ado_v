from django.shortcuts import render


def view_bag(request):
    """A view that render's the bag's contents page"""
    return render(request, "bag/bag.html")