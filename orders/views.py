from django.shortcuts import render, get_object_or_404, redirect

from tours.models import Tour
from .models import Order

def create_order(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)

    if request.method == 'POST':
        Order.objects.create(
            tour=tour,
            name=request.POST['name'],
            phone=request.POST['phone'],
            email=request.POST.get('email', ''),
            people=request.POST.get('people', 1)
        )
        return redirect('home')

    return redirect(request, 'orders/create.html', {
        'tour': tour
    })