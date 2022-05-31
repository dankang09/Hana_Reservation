from django.urls import reverse
from django.shortcuts import redirect

class ProfileSetupMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    # 프로필 설정 페이지로 가게되는 조건
    def __call__(self, request):
        if (
            request.user.is_authenticated and  # 유저가 로그인 되어있는지 확인
            not request.user.name and  # 이름이 등록되어있는지(프로필이 설정되어있는지) 확인
            request.path_info != reverse('login:profile-set')  # 유저가 프로필설정 페이지가 아닌 다른 페이지로 request를 보내는지 확인
        ):
            return redirect("login:profile-set")

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response