from shutil import unregister_unpack_format
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView, 
    UpdateView,
    DeleteView,
    View
    )
from django.contrib.contenttypes.models import ContentType

from braces.views import LoginRequiredMixin

from django.db.models import Q
from booking.models import Branch, Booking, Comment, Like
from booking.forms import BookingForm, CommentForm, BranchForm

# 프로필 구현
from login.models import User

# 리팩터링된 접근제어
from .mixins import LoginAndVerificationRequiredMixin, LoginAndOwnershipRequiredMixin, LoginAndOwnershipRequiredMixin2

# Create your views here.

class ProfileView(DetailView):
    model = User
    template_name = "booking/profile.html"
    pk_url_kwarg = "user_id"
    # user_id에 해당하는 유저는 "profile_user"라는 이름으로 템플릿에게 전달됨
    context_object_name = "profile_user"  # 안 쓰면 default는 User가 됨

    # 템플릿으로 전달되는 context에 추가해주기 (오버라이드)
    def get_context_data(self, **kwargs):
        # 기존의 context 가져오기
        context = super().get_context_data(**kwargs)
        # url에 있는 <int:user_id>에서 유저아이디를 가져오기
        user_id = self.kwargs.get("user_id")
        # 현재 로그인 되어있는 유저 가져오기
        user = self.request.user
        
        if user.employee:
            # 소속 브랜치 가져오기
            employee_branch = user.employee.employee_branch
            # 우리 지점의 최신 예약 10개 가져오기
            context["branch_bookings"] = Booking.objects.filter(booking_branch=employee_branch).order_by("-booking_dates")[:10]
        else:
            # 유저의 최신 예약 4개 가져오기
            context["user_bookings"] = Booking.objects.filter(booking_client=user_id).order_by("-booking_dates")[:4]
        return context
    


class BranchView(ListView):
    model = Branch
    template_name = "booking/branch_list.html"
    context_object_name = "branches"
    paginate_by = 4
    ordering = ["branch_name"]


class BranchDetailView(DetailView):
    model = Branch
    template_name = "booking/branch_detail.html"
    pk_url_kwarg = "branch_id"

    def get_context_data(self, **kwargs):
        branch_id = self.kwargs.get('branch_id')
        user = self.request.user

        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        context['branch_ctype_id'] = ContentType.objects.get(model='branch').id
        context['comment_ctype_id'] = ContentType.objects.get(model='comment').id

        # 현재 유저가 branch, comment를 like하는지 판단하기
        if user.is_authenticated:
            branch = self.object
            context['likes_branch'] = Like.objects.filter(user=user, branch=branch).exists()
            context['liked_comments'] = Comment.objects.filter(comment_branch=branch).filter(likes__user=user)
            # branch를 follow하는지 판단하기
            context['is_following'] = user.following.filter(id=branch_id).exists()
        return context


# 우리지점 수정
class BranchUpdateView(UpdateView):
    model = Branch
    form_class = BranchForm
    template_name = 'booking/branch_update_form.html'
    pk_url_kwarg = 'branch_id'

    # 업데이트 해야할 오브젝트(유저)가 뭔지 UpdateView에게 알려주기(오버라이드)
    # 하나의 오브젝트를 다루는 DetailView, DeleteView, CreateView 는 get_object를 오버라이드 할 수 있음
    # 그 외에 여러개의 오브젝트를 다루는 뷰에서는 get_queryset을 오버라이드 해야함
    def get_object(self):
        # 현재 유저로부터 브랜치정보 가져오기
        user_branch = self.request.user.employee.employee_branch
        print("안녕1")
        return user_branch

    def get_success_url(self):
        print("안녕2")
        return reverse('booking:branch-detail', kwargs={'branch_id': self.object.id})


class CommentCreateView(LoginAndVerificationRequiredMixin, CreateView):
    http_method_names = ['post']
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.comment_branch = Branch.objects.get(id=self.kwargs.get('branch_id'))
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('booking:branch-detail', kwargs={'branch_id': self.kwargs.get('branch_id')})


class CommentUpdateView(LoginAndOwnershipRequiredMixin2, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'booking/comment_update_form.html'
    pk_url_kwarg = 'comment_id'

    def get_success_url(self):
        return reverse('booking:branch-detail', kwargs={'branch_id': self.object.comment_branch.id})


class CommentDeleteView(LoginAndOwnershipRequiredMixin2, DeleteView):
    model = Comment
    template_name = 'booking/comment_confirm_delete.html'
    pk_url_kwarg = 'comment_id'

    def get_success_url(self):
        return reverse('booking:branch-detail', kwargs={'branch_id': self.object.comment_branch.id})

    
class ProcessLikeView(LoginAndVerificationRequiredMixin, View):
    http_method_names = ['post']  # POST method만 처리해주는 뷰이기 때문

    def post(self, request, *args, **kwargs):
        # 유저가 오브젝트에 좋아요를 눌렀는지 판단하기
        # 밑의 조건을 충족하면 get -> like에 저장
        # 조건을 충족하지 못하면 created가 false -> like에 저장 -> 다시 created가 true
        like, created = Like.objects.get_or_create(
            user = self.request.user,  # 현재유저
            content_type_id = self.kwargs.get('content_type_id'), # url로 넘어온 content_type_id 가져오기
            object_id = self.kwargs.get('object_id'),  # url로 넘어온 object_id 가져오기
        )
        if not created:
            like.delete()
        
        return redirect(self.request.META['HTTP_REFERER'])


class ProcessFollowView(LoginAndVerificationRequiredMixin, View):
    http_method_names = ['post']  # POST method만 처리해주는 뷰이기 때문

    def post(self, request, *args, **kwargs):
        user = self.request.user
        branch_id = self.kwargs.get('branch_id')
        if user.following.filter(id=branch_id).exists():
            user.following.remove(branch_id)
        else:
            user.following.add(branch_id)
        return redirect('booking:branch-detail', branch_id = branch_id)


# 유저가 필로잉하는 브랜치들 보여주기
class FollowingListView(ListView):
    model = Branch
    template_name = 'booking/following_list.html'
    context_object_name = 'following'
    paginate_by = 10

    #유저가 팔로우하는 브랜치들 쿼리셋
    def get_queryset(self):
        user = get_object_or_404(User, pk=self.kwargs.get('user_id'))
        return user.following.all()

    # '프로필로 돌아가기' url태그를 위해 템플릿으로 전달
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile_user_id'] = self.kwargs.get('user_id')
        return context


# 브랜치를 팔로잉하는 유저들 보여주기
class FollowerListView(ListView):
    model = User
    template_name = 'booking/follower_list.html'
    context_object_name = 'followers'
    paginate_by = 10

    # 브랜치를 팔로우하는 유저들 쿼리셋
    def get_queryset(self):
        branch = get_object_or_404(Branch, pk=self.kwargs.get('branch_id'))
        return branch.followers.all()

    # '지점 상세보기로 돌아가기' url태그를 위해 템플릿으로 전달
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['branch_id'] = self.kwargs.get('branch_id')
        return context


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


### 본인이 작성한 booking만 볼 수 있게 바꿔야함 ###
class BookingDetailView(DetailView):
    model = Booking
    template_name = "booking/booking_detail.html"
    pk_url_kwarg = "booking_id"


# 믹스인 로직이 뷰로직보다 먼저기 때문에 믹스인을 왼쪽 파라미터로
# 이메일 인증 추가하려면 LoginRequiredMixin 뒤에 UserPassesTestMixin 추가 
class BookingCreateView(LoginAndVerificationRequiredMixin, CreateView):
    model = Booking
    form_class = BookingForm
    template_name = "booking/booking_form.html"
    pk_url_kwarg = "branch_id"
    context_object_name = 'branch_id'

    def form_valid(self, form):  # 메소드 오버라이팅
        # 현재 로그인된 유저 정보를 폼에 넣기
        form.instance.booking_client = self.request.user
        # url에서 branch_id 가져오기
        branch_id = self.kwargs.get("branch_id")
        # 가져온 branch_id로 브랜치 객체 찾아서 폼에 넣기
        form.instance.booking_branch = Branch.objects.get(id = branch_id)
        return super().form_valid(form)

    def get_success_url(self):
        user = self.request.user
        return reverse("booking:profile", args=[user.id])


# 본인이 작성한 booking만 삭제가능함
class BookingDeleteView(LoginAndOwnershipRequiredMixin, DeleteView):
    model = Booking
    template_name = "booking/booking_confirm_delete.html"
    pk_url_kwarg = "booking_id"

    def get_success_url(self):
        user = self.request.user
        return reverse("booking:profile", args=[user.id])
