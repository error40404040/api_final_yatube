import pytest


@pytest.fixture
def password():
    return '1234567'
# ----------------------------------------

@pytest.fixture
def user(django_user_model, password):
    return django_user_model.objects.create_user(
        username='TestUser', 
        password=password  
    )

@pytest.fixture
def user_2(django_user_model, password):
    return django_user_model.objects.create_user(
        username='TestUser2', 
        password=password
    )

@pytest.fixture
def another_user(django_user_model, password):
    return django_user_model.objects.create_user(
        username='TestUserAnother', 
        password=password
    )


@pytest.fixture
def token(user):
    from rest_framework_simplejwt.tokens import RefreshToken
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


@pytest.fixture
def user_client(token):
    from rest_framework.test import APIClient

    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {token["access"]}')
    return client
