import pytest

# Models


@pytest.fixture(scope='function')
def test_data():
    params = {
        "points_submitted": "(2,3), (1,1), (5, 4)",
        "relative_point": '(1,1)',
    }
    return params
@pytest.fixture(scope='function')
def test_with_invalid_relative_point():
    params = {
        "points_submitted": "(2,3), (1,1), (5, 4)",
        "relative_point": (1,1),
    }
    return params
@pytest.fixture(scope='function')
def test_with_invalid_points_submitted():
    params = {
        "points_submitted": '(2,3)',
        "relative_point": '(1,1)',
    }
    return params
