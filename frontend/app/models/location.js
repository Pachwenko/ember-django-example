import Model, { attr, belongsTo } from '@ember-data/model';

export default class RentalModel extends Model {
  @belongsTo('rental') rental;
  @attr lat;
  @attr lng;
}
