describe('Rentals Tests', () => {
  it('can search and view a rental', () => {
    // visit the app
    cy.visit('http://localhost:4200')
    cy.get('#rentals-search')
      .type('Downtown Charm')
      .should('have.value', 'Downtown Charm')

    // Go to downtown charm page
    cy.get('a:contains(Downtown Charm)').click()
    cy.url().should('include', '/rentals/3')
    cy.contains('About Downtown Charm')

    // Ensure links are correct
    cy.get('h1')
        .should('have.text', 'SuperRentals')
        .parent()
        .should('have.attr', 'href', '/')
    cy.get('.links > a:first')
        .should('have.text', '\n      About\n    ')
        .and('have.attr', 'href', '/about')
    cy.get('.links')
        .children()
        .next()
        .should('have.text', '\n      Contact\n    ')
        .and('have.attr', 'href', '/getting-in-touch')
    cy.get('a:contains(Share on Twitter)').should('have.attr', 'href', 'https://twitter.com/intent/tweet?url=http%3A%2F%2Flocalhost%3A4200%2Frentals%2F3&text=Check+out+Downtown+Charm+on+Super+Rentals%21&hashtags=vacation%2Ctravel%2Cauthentic%2Cblessed%2Csuperrentals&via=emberjs');
  })

  it('tries to work but fails', () => {
    cy.visit('http://localhost:4200')
    cy.get('.results > li')
        .first()
        .find('h3')
        .should('have.text', 'Downtown Farm')
  })
})
