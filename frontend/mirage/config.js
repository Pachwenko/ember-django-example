export default function () {
  this.get('/rentals', (schema) => {
    return schema.rentals.all();
  });

  this.get('/rentals/:id', (schema, request) => {
    return schema.rentals.find(request.params.id);
  });
}
