# 접근제어 리팩터링
from braces.views import LoginRequiredMixin, UserPassesTestMixin
from allauth.account.models import EmailAddress
from login.functions import confirmation_required_redirect

# 로그인만 필요 -> LoginRequiredMixin

# 로그인 + 이메일 인증 필요(예약하기, 댓글 작성, 좋아요)
class LoginAndVerificationRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    redirect_unauthenticated_users = True
    raise_exception = confirmation_required_redirect

    def test_func(self, user):
        return EmailAddress.objects.filter(user=user, verified=True).exists()


# 로그인 + 오브젝트 소유 필요(예약 삭제)
class LoginAndOwnershipRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):

    # 본인이 한 예약이 아니면 403 forbidden error 발생
    raise_exception = True

    # 본인이 한 예약인지 확인
    def test_func(self, user):
        obj = self.get_object()
        return obj.booking_client == user


# 로그인 + 오브젝트 소유 필요(댓글 수정, 댓글 삭제)
