from django.shortcuts import render, get_object_or_404

from .models import Tour


def tour_detail(request, pk):
    tour = get_object_or_404(Tour, pk=pk)
    
    return render(request, 'tours/detail.html', {
        'tour': tour
    })
