export default function () {
  this.get('http://localhost:8000/api/rentals', (schema) => {
    return schema.rentals.all();
  });

  this.get('http://localhost:8000/api/rentals/:id', (schema, request) => {
    return schema.rentals.find(request.params.id);
  });
}
