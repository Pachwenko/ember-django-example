describe('My First Test', () => {
  // Given a user visits https://example.cypress.io
  // When they click the link labeled type
  // And they type "fake@email.com" into the .action-email input
  // Then the URL should include /commands/actions
  // And the .action-email input has "fake@email.com" as its value


  it('finds the content "type"', () => {
    cy.visit('https://example.cypress.io')

    cy.contains('type').click()

    // Should be on a new URL which includes '/commands/actions'
    cy.url().should('include', '/commands/actions')

    // Get an input, type into it and verify that the value has been updated
    cy.get('.action-email')
      .type('fake@email.com')
      .should('have.value', 'fake@email.com').debug()
  })
})
