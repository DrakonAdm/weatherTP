from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

UserModel = get_user_model()


def custom_validation(data):
    email = data.get('email', '').strip()
    if 'nickname' in data:
        nickname = data.get('nickname', '').strip()
    password = data.get('password', '').strip()
    ##
    if not email or UserModel.objects.filter(email=email).exists():
        raise ValidationError('choose another email')
    ##
    if not password or len(password) < 8:
        raise ValidationError('choose another password, min 8 characters')
    ##
    # if not nickname:
    #     raise ValidationError('choose another username')
    return data


def validate_email(data):
    email = data.get('email', '').strip()
    if not email:
        raise ValidationError('choose another email')
    return True


def validate_nickname(data):
    nickname = data.get('nickname', '').strip()
    if not nickname:
        raise ValidationError('a nickname is needed')
    return True


def validate_password(data):
    password = data.get('password', '').strip()
    if not password:
        raise ValidationError('a password is needed')
    return True
