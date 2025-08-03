from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Customer, Room, Booking
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.dateparse import parse_datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, "coar/home.html")

# def info(request):
#     if request.method=="POST":
#         first_name = request.POST.get("first_name")
#         last_name = request.POST.get("last_name")
#         gmail = request.POST.get("gmail")
#         phone = request.POST.get("phone")
#         if first_name and last_name and gmail and phone:
#             Customer.objects.create(first_name=first_name, last_name=last_name,gmail=gmail,phone=phone)
#             return redirect("Дякуем")
#     return render(request, "coar/info.html")



@login_required
def info(request):
    room_id = request.GET.get("room_id") or request.POST.get("room_id")
    room = get_object_or_404(Room, id=room_id) if room_id else None


    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        gmail = request.POST.get("gmail")
        phone = request.POST.get("phone")
        starttime = request.POST.get("starttime")
        endtime = request.POST.get("endtime")

        if all([first_name, last_name, gmail, phone, starttime, endtime, room]):

            start = parse_datetime(starttime)
            end = parse_datetime(endtime)

            if Booking.objects.filter(room=room, start_time__lt=end, end_time__gt=start).exists():
                return render(request, "coar/room_closed.html")
            
            customer = Customer.objects.create(
                first_name=first_name,
                last_name=last_name,
                gmail=gmail,
                phone=phone
            )
            Booking.objects.create(
                customer=customer,
                room=room,
                start_time=start,
                end_time=end
            )
            return redirect("home")

    return render(request, "coar/info.html", {"room": room})


def search_info(request):
    results = None
    first_name = ""
    last_name = ""

    if request.method == "POST":
        first_name = request.POST.get('first_name', "").strip()
        last_name = request.POST.get('last_name', "").strip()

        if first_name or last_name:
            results = Booking.objects.filter(
                customer__first_name__icontains=first_name,
                customer__last_name__icontains=last_name
            )

    return render(request, 'coar/search_info.html', {
        'results': results,
        'first_name': first_name,
        'last_name': last_name
    })





# def forma(request):
#     if request.method=="POST":
#         first_name = request.POST.get("first_name")
#         last_name = request.POST.get("last_name")
#         gmail = request.POST.get("gmail")
#         phone = request.POST.get("phone")
#         if first_name and last_name and gmail and phone:
#             Customer.objects.create(first_name=first_name, last_name=last_name,gmail=gmail,phone=phone)
#             return redirect("Дякуем")
#     return render(request,"coar/home.html")
    


# def forma(request):
#     if request.method=="POST":
#         form = BookingForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("Дякуем")
#     else:
#         form = BookingForm()
#     return render(request,"coar/home.html",{"form":form})