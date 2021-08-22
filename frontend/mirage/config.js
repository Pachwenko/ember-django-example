import faker from 'faker';

export default function () {
  this.get('/rentals', (schema) => {
    return schema.rentals.all();
  });

  this.get('/rentals/:id', (schema, request) => {
    console.log(schema.rentals.all());
    return schema.rentals.find(request.params.id);
  });

  this.get('https://api.mapbox.com/styles/v1/mapbox/streets-v11/static/*', (schema, request) => {
    return faker.image.abstract(600, 600);
  });
}
