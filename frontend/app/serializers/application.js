import JSONAPISerializer from '@ember-data/serializer/json-api';

// using JSONAPI for everything makes life much easier on the frontend
// but it can look like magic as we don't make any API calls directly
export default JSONAPISerializer;
