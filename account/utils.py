from account.models import CustomUser, Profession, ReferalCode, ReferalUser
from rest_framework_simplejwt.tokens import RefreshToken
import re
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

def is_email(input):
    pat = re.compile("[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?")
    m = pat.match(input)
    if m:
        return True
    return False


def is_mobile(input):
    if len(input) == 10:
        return str(input).isdigit()
    return False


def validate_password(password):
    if password is None:
        return False

    if len(password) < 6:
        return False

    return True


def validate_data(data):
    username = data.get("username")
    password = data.get("password")
    email = data.get("email", None)
    refer_code = data.get("refer_code",None)

    if email:
        email = email.strip()

    required_fields = ['email', 'password']
    st = True
    msg = []
    for i in required_fields:
        v = data.get(i, None)
        if v is None or v == '':
            st = False
            msg.append(f'{i} is required!')

    if ReferalUser.objects.filter(refer_code__iexact=refer_code).exists():
        pass
    else:
        st = False
        msg.append("Refer code does not exist!")

    if email and CustomUser.objects.filter(email__iexact=email).exists():
            st = False
            msg.append("Email ID already exist!")
    if CustomUser.objects.filter(username__iexact=username).exists():
        st = False
        msg.append("Username already exists!")
    
    
    if not validate_password(password):
        st = False
        msg.append("Keep your profile safe. Enter a password with at least 6 Characters")

    return st, msg

def register_user(data):
    """
    function to register the user
    """
    from django.contrib.auth import login, authenticate
    try:
        username = data.get("username")
        password = data.get("password")
        email = data.get("email", None)
        refer_code = data.get("refer_code",None)
        profession = data.get("profession")

        if email:
            email = email.strip()
        profession_data = Profession.objects.get(slug=profession)

        user = CustomUser(
            username = username,
            email=email,
            profession=profession_data,
            user_storage = 10000
        )
        user.save()
        if ReferalCode.objects.filter(refer_code=refer_code).exists():
            ReferalUser.objects.filter(refer_by_without_register=email)
        referCode = ReferalCode(
            refer_code = "AD"+user.id
        )
        referCode.save()

        rc = ReferalCode.objects.get(refer_code="AD"+user.id)
        user.referal_code = rc
        user.save()

        user.set_password(password)
        user.save()
        return user
    except Exception as e:
        print(e)
        return None