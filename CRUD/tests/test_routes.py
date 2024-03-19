'''import pytest
from website import create_app, db

@pytest.fixture
def app():
    app = create_app()
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

def test_add_product(client):
    response = client.post('/product', json={"name": "Test Product", "description": "Test Description", "price": 10.99})
    data = response.get_json()

    assert response.status_code == 200
    assert data['name'] == 'Test Product'
    assert data['description'] == 'Test Description'
    assert data['price'] == 10.99

def test_get_all_products(client):
    client.post('/product', json={"name": "Test Product", "description": "Test Description", "price": 10.99})

    response = client.get('/getallproducts')
    data = response.get_json()

    assert response.status_code == 200
    assert len(data) == 1

def test_get_product(client):
    client.post('/product', json={"name": "Test Product", "description": "Test Description", "price": 10.99})

    response = client.get('/getproduct/1')
    data = response.get_json()

    assert response.status_code == 200
    assert data['name'] == 'Test Product'
    assert data['description'] == 'Test Description'
    assert data['price'] == 10.99

def test_update_product(client):
    client.post('/product', json={"name": "Test Product", "description": "Test Description", "price": 10.99})

    response = client.put('/update/1', json={"name": "Updated Product", "description": "Updated Description", "price": 19.99})
    data = response.get_json()

    assert response.status_code == 200
    assert data['name'] == 'Updated Product'
    assert data['description'] == 'Updated Description'
    assert data['price'] == 19.99

def test_delete_product(client):
    client.post('/product', json={"name": "Test Product", "description": "Test Description", "price": 10.99})

    response = client.delete('/delete/1')
    data = response.get_json()

    assert response.status_code == 200
    assert data['name'] == 'Test Product'
    assert data['description'] == 'Test Description'
    assert data['price'] == 10.99
    '''
