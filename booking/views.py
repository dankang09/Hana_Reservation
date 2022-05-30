from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, DeleteView

from braces.views import LoginRequiredMixin, UserPassesTestMixin

# 이메일 인증
# from allauth.account.models import EmailAddress
# from braces.views import UserPassesTestMixin
# from login.functions import confirmation_required_redirect

from django.db.models import Q
from booking.models import Branch, Booking
from booking.forms import BookingForm


# Create your views here.

def booking(request):
    return render(request, 'booking/booking.html')

# 본인이 작성한 booking만 볼 수 있게 바꿔야함
class BookingView(ListView):
    model = Booking
    template_name = "booking/booking.html"
    context_object_name = "bookings"
    paginate_by = 4
    ordering = ["booking_dates"]


class BranchView(ListView):
    model = Branch
    template_name = "booking/branch_list.html"
    context_object_name = "branches"
    paginate_by = 4
    ordering = ["branch_name"]


class SearchView(ListView):
    model = Branch
    context_object_name = 'search_results'
    template_name = 'booking/search_results.html'
    paginate_by = 4

    def get_queryset(self):
        query = self.request.GET.get('query', '')
        return Branch.objects.filter(
            Q(branch_name__icontains=query)
            | Q(branch_tel__icontains=query)
            | Q(branch_address__icontains=query)
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('query', '')
        return context


# 본인이 작성한 booking만 볼 수 있게 바꿔야함
class BookingDetailView(DetailView):
    model = Booking
    template_name = "booking/booking_detail.html"
    pk_url_kwarg = "booking_id"


# 믹스인 로직이 뷰로직보다 먼저기 때문에 믹스인을 왼쪽 파라미터로
# 이메일 인증 추가하려면 LoginRequiredMixin 뒤에 UserPassesTestMixin 추가 
class BookingCreateView(LoginRequiredMixin, CreateView):
    model = Booking
    form_class = BookingForm
    template_name = "booking/booking_form.html"
    pk_url_kwarg = "branch_id"
    context_object_name = 'branch_id'

    # redirect_unauthenticated_users = True
    # raise_exception = confirmation_required_redirect

    def form_valid(self, form):  # 메소드 오버라이팅(현재 로그인된 유저 정보 넘기기)
        form.instance.booking_client = self.request.user
        form.instance.booking_branch = Branch.objects.get(id = 1)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("booking:booking-list")

    # 이메일 인증
    # def test_func(self, user):
    #     return EmailAddress.objects.filter(user=user, verified=True).exists()


# 본인이 작성한 booking만 삭제할 수 있게 바꿔야함
class BookingDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Booking
    template_name = "booking/booking_confirm_delete.html"
    pk_url_kwarg = "booking_id"

    raise_exception = True

    def get_success_url(self):
        return reverse("booking:booking-list")

    def test_func(self, user):
        booking = self.get_object()
        return booking.booking_client == user
