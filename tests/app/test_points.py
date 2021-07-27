from django.urls import reverse
import pytest
from rest_framework import status

class TestPoints:

    @pytest.mark.django_db
    def test_can_successfully_get_closest_pairs(self, client, test_data): 
        """ test get comments list """
        url = reverse('app:get-pairs')
        client.credentials(HTTP_AUTHORIZATION='Bearer ')
        response = client.post(url,test_data)
        assert response.status_code == status.HTTP_200_OK
        # import pdb;pdb.set_trace()

        assert response.data.get('Response') == 'Closest point is [1 1], at a distance of 0.0'
    def test_cannot_get_closest_pairs_with_invalid_relative_point(self, client, test_with_invalid_relative_point): 
            """ test get comments list """
            url = reverse('app:get-pairs')
            client.credentials(HTTP_AUTHORIZATION='Bearer ')
            response = client.post(url,test_with_invalid_relative_point)
            assert response.status_code == status.HTTP_400_BAD_REQUEST

            assert response.data.get('relative_point').get('error') == 'relative should folow this format (x,y)'
    def test_cannot_get_closest_pairs_with_invalid_points_submitted(self, client, test_with_invalid_points_submitted): 
            """ test get comments list """
            url = reverse('app:get-pairs')
            client.credentials(HTTP_AUTHORIZATION='Bearer ')
            response = client.post(url,test_with_invalid_points_submitted)
            assert response.status_code == status.HTTP_400_BAD_REQUEST

            assert response.data.get('error') == "axis 1 is out of bounds for array of dimension 1"
