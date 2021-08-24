import DS from 'ember-data';

// using JSONAPI for everything makes life much easier on the frontend
// but it can look like magic
export default DS.JSONAPISerializer;