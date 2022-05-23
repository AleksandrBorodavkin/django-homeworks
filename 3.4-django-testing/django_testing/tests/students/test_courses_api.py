import pytest
from rest_framework.test import APIClient
from model_bakery import baker

from students.models import Course, Student


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)

    return factory


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, make_m2m=True, *args, **kwargs)

    return factory


@pytest.mark.django_db
def test_retrieve_course(client, course_factory):
    # Arrange
    courses = course_factory(_quantity=10)

    # Act
    response = client.get('/api/v1/courses/1/')

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert data['id'] == 1


@pytest.mark.django_db
def test_list_courses(client, course_factory):
    # Arrange
    courses = course_factory(_quantity=10)

    # Act
    response = client.get('/api/v1/courses/')

    # Assert
    data = response.json()
    assert len(data) == 10
    assert response.status_code == 200


@pytest.mark.django_db
def test_filter_id(client, course_factory):
    # Arrange
    courses = course_factory(_quantity=10)

    # Act
    response = client.get('/api/v1/courses/?id=3')
    # Assert
    data = response.json()
    print(data[0])
    assert data[0]['id'] == 3
    assert response.status_code == 200


@pytest.mark.django_db
def test_filter_name(client, course_factory):
    # Arrange
    courses = course_factory(_quantity=10)

    # Act
    response = client.get(f'/api/v1/courses/?name={courses[0].name}')

    # Assert
    data = response.json()

    assert data[0]['name'] == courses[0].name
    assert response.status_code == 200


@pytest.mark.django_db
def test_created_course(client):
    # Act
    response = client.post('/api/v1/courses/', data={'name': 'course #1'})

    # Assert
    assert response.status_code == 201


@pytest.mark.django_db
def test_update_course(client, course_factory):
    # Arrange
    courses = course_factory(_quantity=10)

    # Act
    response = client.patch('/api/v1/courses/1/', data={'name': 'course #1'})
    new_entry = client.get('/api/v1/courses/1/')
    new_entry = new_entry.json()

    # Assert
    assert response.status_code == 200
    assert new_entry['name'] == 'course #1'


@pytest.mark.django_db
def test_delete_course(client, course_factory):
    # Arrange
    courses = course_factory(_quantity=10)

    # Act
    response = client.delete('/api/v1/courses/1/')

    # Assert
    assert response.status_code == 204
