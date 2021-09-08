import pytest

from fastapi.testclient import TestClient
from main import app
from core.testbase import init_test_db, drob_test_db, get_test_session
from core.database import get_db
from models.user import User
from services.auth_mixin import check_and_return_user_to_token
from core.testbase import Session

client = TestClient(app)

app.dependency_overrides[get_db] = get_test_session


@pytest.fixture()
def test_db():
    init_test_db()
    yield
    drob_test_db()


@pytest.fixture()
def init_data_to_db():
    user: User = User(
        name='Goga',
        email='test@mail.com',
        password='testtest'
    )
    session = next(get_test_session())
    session.add(user)
    session.commit()


@pytest.fixture()
def auth_client(init_data_to_db):
    def fake_check_token():
        pass

    app.dependency_overrides[check_and_return_user_to_token] = fake_check_token


def test_get_list_users_without_auth(test_db, init_data_to_db):
    response = client.get('/users/')
    assert response.status_code == 401
    assert response.json() == {'detail': 'Not authenticated'}


def test_get_list_users_with_auth(test_db, auth_client):
    response = client.get('/users/')
    assert response.status_code == 200
    assert response.json() == [{'email': 'test@mail.com', 'name': 'Goga', 'is_active': True, 'id': 1}]


def test_get_user_by_wrong_id(test_db):
    response = client.get('/users/1')
    assert response.status_code == 404
    assert response.json() == {'detail': 'User does not exists'}


def test_get_user_by_id(test_db, init_data_to_db):
    response = client.get('/users/1')
    assert response.status_code == 200
    assert response.json() == {'email': 'test@mail.com', 'id': 1, 'is_active': True, 'name': 'Goga'}


def test_delete_user_by_wrong_id(test_db, init_data_to_db):
    response = client.delete('/users/2/delete')
    assert response.status_code == 404
    assert response.json() == {'detail': 'User does not exists'}
    try:
        db = Session()
        assert db.query(User).count() == 1
    finally:
        db.close()


def test_delete_user_by_id(test_db, init_data_to_db):
    try:
        db = Session()
        assert db.query(User).count() == 1
        response = client.delete('/users/1/delete')
        assert db.query(User).count() == 0
        assert response.status_code == 204
        assert response.text == ''
    finally:
        db.close()


def test_create_user_with_valid_data(test_db, init_data_to_db):
    try:
        db = Session()
        assert db.query(User).count() == 1
        response = client.post(
            '/users/create',
            json={
                'name': 'Goga2',
                'email': 'test2@mail.com',
                'password': 'testtest2'
            })
        assert db.query(User).count() == 2
        assert response.status_code == 200
    finally:
        db.close()


def test_create_user_with_invalid_data(test_db, init_data_to_db):
    try:
        db = Session()
        assert db.query(User).count() == 1
        response = client.post(
            '/users/create',
            json={
                'name': 'Goga2',
                'email': 'test2@mail.com',
            })
        assert db.query(User).count() == 1
        assert response.status_code == 422
    finally:
        db.close()


def test_update_user_with_valid_data(test_db, init_data_to_db):
    try:
        db = Session()
        user = db.query(User).all()[0]
        assert user.name != 'Vova'
        response = client.put(
            f'/users/{user.id}/update',
            json={
                'name': 'Vova',
                'email':'test@mail.com',
            }
        )
        assert response.status_code == 200
        db.refresh(user)
        assert user.name == 'Vova'
    finally:
        db.close()

def test_update_user_with_invalid_data(test_db, init_data_to_db):
    try:
        db = Session()
        user = db.query(User).all()[0]
        assert user.name == 'Goga'
        response = client.put(
            f'/users/{user.id}/update',
            json={
                'name': 'Vova',
            }
        )
        assert response.status_code == 422
        db.refresh(user)
        assert user.name == 'Goga'
    finally:
        db.close()