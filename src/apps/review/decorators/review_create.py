from pkg.response import ErrorResponse
from apps.review.models import Review


def self_review_prevention(func):
    def wrapper(cls, request, *args, **kwargs):
        account_id = request.data.get('account_id')

        if request.user.id == account_id:
            return ErrorResponse(data="Ошибка операции", status=400)

        return func(cls, request, *args, **kwargs)

    return wrapper


def has_review(func):
    def wrapper(cls, request, *args, **kwargs):
        account_id = request.data.get('account_id')

        if Review.objects.filter(account_id=account_id).first():
            return ErrorResponse(data='Вы уже оставили отзыв', status=400)

        return func(cls, request, *args, **kwargs)

    return wrapper
