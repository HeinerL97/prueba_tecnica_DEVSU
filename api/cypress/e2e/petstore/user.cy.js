describe('Petstore API - CRUD Usuario', () => {

  const username = "qa_user" + Date.now()

  const user = {
    id: Date.now(),
    username: username,
    firstName: "Heiner",
    lastName: "Urrego",
    email: "heiner@test.com",
    password: "123456",
    phone: "3000000000",
    userStatus: 1
  }

  const updatedUser = {
    ...user,
    firstName: "HeinerUpdated",
    email: "updated@test.com"
  }

  it('Crear usuario', () => {

    cy.request({
      method: 'POST',
      url: '/user',
      body: user
    }).then((response) => {

      cy.log("Usuario creado:", JSON.stringify(response.body))

      expect(response.status).to.eq(200)
      expect(response.body.message).to.eq(String(user.id))

    })

  })


  it('Buscar usuario creado', () => {

    cy.request(`/user/${username}`).then((response) => {

      cy.log("Usuario encontrado:", JSON.stringify(response.body))

      expect(response.status).to.eq(200)
      expect(response.body.username).to.eq(username)
      expect(response.body.email).to.eq(user.email)

    })

  })


  it('Actualizar nombre y correo', () => {

    cy.request({
      method: 'PUT',
      url: `/user/${username}`,
      body: updatedUser
    }).then((response) => {

      cy.log("Usuario actualizado:", JSON.stringify(response.body))

      expect(response.status).to.eq(200)

    })

  })


  it('Buscar usuario actualizado', () => {

    cy.request(`/user/${username}`).then((response) => {

      cy.log("Datos actualizados:", JSON.stringify(response.body))

      expect(response.status).to.eq(200)
      expect(response.body.firstName).to.eq(updatedUser.firstName)
      expect(response.body.email).to.eq(updatedUser.email)

    })

  })


  it('Eliminar usuario', () => {

    cy.request({
      method: 'DELETE',
      url: `/user/${username}`
    }).then((response) => {

      cy.log("Usuario eliminado:", JSON.stringify(response.body))

      expect(response.status).to.eq(200)

    })

  })

})