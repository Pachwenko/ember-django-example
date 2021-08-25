from django.db import models

# 
# export default Factory.extend({
#   owner: faker.name.firstName,
#   type: faker.random.word,
#   city: faker.random.word,
#   title: faker.random.word,
#   category: faker.random.word,
#   image: 'https://placeimg.com/600/600/arch', // faker just generates urls to this site, but doesn't have "arch"
#   bedrooms: faker.datatype.number,
#   description() {
#     return faker.lorem.words(8);
#   },
#   location() {
#     return {
#       lat: 45.5175,
#       lng: -122.6801,
#     };
#   },
# });


class Rental(models.Model):
    description = models.TextField(max_length=1024)