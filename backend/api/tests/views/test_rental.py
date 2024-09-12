from api.tests.factories.rental import RentalFactory
from api.tests.factories.location import LocationFactory

from django.test import TestCase

class TestFoo(TestCase):

    # helps clean up JSON:API tests
    # TODO: move this to some kind of test helpers file
    def get_item_from_response(self, response_data, item_type, item_id) -> dict:
        _id = item_id if isinstance(item_id, str) else str(item_id)
        for item in response_data:
            if item['type'] == item_type and item['id'] == _id:
                return item
        return {}

    def test_get_rentals_returns_single_rental(self):
        location1 = LocationFactory()
        rental1 = RentalFactory(location=location1)
        # we aren't using django's reverse utility for urls
        # this is because the frontent is relying on these urls not to change
        # if we used reverse we can easliy pass all our API tests but the frontend will break
        response = self.client.get(f'/api/rentals/{rental1.pk}/')
        # having the first assert for status code is helpful
        # because a 200 != 404 is much clearer than "KeyError" or other such error
        # can make a huge difference tracking down bugs due to a large refactor
        assert 200 == response.status_code

        result_rental1 = response.json()['data']['attributes']
        assert result_rental1['owner'] == rental1.owner
        assert result_rental1['city'] == rental1.city
        assert result_rental1['title'] == rental1.title
        assert result_rental1['category'] == rental1.category
        assert result_rental1['description'] == rental1.description
        assert result_rental1['image'] == rental1.image
        assert result_rental1['bedrooms'] == rental1.bedrooms

    def test_get_rentals_returns_all_rentals(self):
        location1 = LocationFactory()
        location2 = LocationFactory()
        rental1 = RentalFactory(location=location1)
        rental2 = RentalFactory(location=location2)
        response = self.client.get('/api/rentals/')
        assert 200 == response.status_code
        assert 2 == len(response.json()['data'])

        result_rental1 = self.get_item_from_response(response.json()['data'], 'Rental', rental1.pk)['attributes']
        assert result_rental1['owner'] == rental1.owner
        assert result_rental1['city'] == rental1.city
        assert result_rental1['title'] == rental1.title
        assert result_rental1['category'] == rental1.category
        assert result_rental1['description'] == rental1.description
        assert result_rental1['image'] == rental1.image
        assert result_rental1['bedrooms'] == rental1.bedrooms

        result_rental2 = self.get_item_from_response(response.json()['data'], 'Rental', rental2.pk)['attributes']
        assert result_rental2['owner'] == rental2.owner
        assert result_rental2['city'] == rental2.city
        assert result_rental2['title'] == rental2.title
        assert result_rental2['category'] == rental2.category
        assert result_rental2['description'] == rental2.description
        assert result_rental2['image'] == rental2.image
        assert result_rental2['bedrooms'] == rental2.bedrooms

    def test_get_rentals_returns_locations_in_included(self):
        rental = RentalFactory()
        response = self.client.get('/api/rentals/')
        assert 200 == response.status_code
        assert 1 == len(response.json()['included'])

        result_rental1_location1 = self.get_item_from_response(
            response.json()['included'],
            'Location',
            rental.location.pk
        )['attributes']
        assert result_rental1_location1['lat'] == str(round(rental.location.lat, 6))
        assert result_rental1_location1['lng'] == str(round(rental.location.lng, 6))

    def test_minimal_queries_with_many_relations(self):
        for i in range(10):
            RentalFactory()
        with self.assertNumQueries(2):
            response = self.client.get('/api/rentals/')
            assert 200 == response.status_code
