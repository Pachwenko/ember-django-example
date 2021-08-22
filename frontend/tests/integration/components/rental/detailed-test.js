import { module, test } from 'qunit';
import { setupRenderingTest } from 'ember-qunit';
import { setupMirage } from 'ember-cli-mirage/test-support';
import { render } from '@ember/test-helpers';
import { hbs } from 'ember-cli-htmlbars';

module('Integration | Component | rental/detailed', function (hooks) {
  setupRenderingTest(hooks);
  setupMirage(hooks);

  hooks.beforeEach(function () {
    this.rental = this.server.create('rental');
  });

  test('it renders a header with a share button', async function (assert) {
    await render(hbs`<Rental::Detailed @rental={{this.rental}} />`);
    assert.dom('.jumbo').exists();
    assert.dom('.jumbo h2').containsText(this.rental.title);
    assert
      .dom('.jumbo p')
      .containsText(`a nice place to stay near ${this.rental.city}`);
    assert.dom('.jumbo a.button').containsText('Share on Twitter');
  });

  test('it renders detailed information about a rental property', async function (assert) {
    await render(hbs`<Rental::Detailed @rental={{this.rental}} />`);
    assert.dom('article').hasClass('rental');
    assert.dom('article h3').containsText(`About ${this.rental.title}`);
    assert.dom('article .detail.owner').containsText(this.rental.owner);
    assert
      .dom('article .detail.type')
      .containsText(`${this.rental.type} – ${this.rental.category}`);
    assert.dom('article .detail.location').containsText(this.rental.city);
    assert
      .dom('article .detail.description')
      .containsText(this.rental.description);
    assert.dom('article .detail.bedrooms').containsText(this.rental.bedrooms);
    assert.dom('article .image').exists();
    assert.dom('article .map').exists();
  });
});
