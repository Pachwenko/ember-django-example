import { module, test } from 'qunit';
import { setupRenderingTest } from 'ember-qunit';
import { setupMirage } from 'ember-cli-mirage/test-support';
import { render, fillIn } from '@ember/test-helpers';
import { hbs } from 'ember-cli-htmlbars';

module('Integration | Component | rentals', function (hooks) {
  setupRenderingTest(hooks);
  setupMirage(hooks);

  hooks.beforeEach(function () {
    this.rental1 = this.server.create('rental', {
      id: 'grand-old-mansion',
      title: 'Grand Old Mansion',
    });
    this.rental2 = this.server.create('rental', {
      id: 'urban-living',
      title: 'Urban Living',
    });
    this.rental3 = this.server.create('rental', {
      id: 'downtown-charm',
      title: 'Downtown Charm',
    });
    this.store = this.owner.lookup('service:store');
  });

  test('it renders all given rental properties by default', async function (assert) {
    await this.store
      .findAll('rental')
      .then((rentals) => this.set('rentals', rentals));
    await render(hbs`<Rentals @rentals={{this.rentals}} />`);

    assert.dom('.rentals').exists();
    assert.dom('.rentals input').exists();

    assert.dom('.rentals .results').exists();
    assert.dom('.rentals .results li').exists({ count: 3 });

    assert
      .dom('.rentals .results li:nth-of-type(1)')
      .containsText('Grand Old Mansion');

    assert
      .dom('.rentals .results li:nth-of-type(2)')
      .containsText('Urban Living');

    assert
      .dom('.rentals .results li:nth-of-type(3)')
      .containsText('Downtown Charm');
  });

  test('it updates the results according to the search query', async function (assert) {
    await this.store
      .findAll('rental')
      .then((rentals) => this.set('rentals', rentals));
    await render(hbs`<Rentals @rentals={{this.rentals}} />`);

    assert.dom('.rentals').exists();
    assert.dom('.rentals input').exists();

    await fillIn('.rentals input', 'Downtown');

    assert.dom('.rentals .results').exists();
    assert.dom('.rentals .results li').exists({ count: 1 });
    assert.dom('.rentals .results li').containsText('Downtown Charm');

    await fillIn('.rentals input', 'Mansion');

    assert.dom('.rentals .results').exists();
    assert.dom('.rentals .results li').exists({ count: 1 });
    assert.dom('.rentals .results li').containsText('Grand Old Mansion');
  });
});
