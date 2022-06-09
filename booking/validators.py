import string
from django.core.exceptions import ValidationError

def validate_branch_link(value):
    if "place.naver.com" not in value and "place.map.kakao.com" not in value:
        raise ValidationError("place.naver.com 또는 place.map.kakao.com이 들어가야 합니다.")