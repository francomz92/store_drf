export const signIn = async (credentials, formNode) => {
    try {
        const response = await fetch('http://localhost:8000/api/login/', {
            method: 'POST',
            body: JSON.stringify(credentials),
            headers: {
                'content-type': 'application/json'
            }
        })
        const data = await response.json()

        if (!response.ok) throw { response, data }

        localStorage.setItem('user', JSON.stringify(data))
        location.reload()

        return data
    } catch (error) {
        if (error.data) {
            if (error.data.email) {
                formNode.querySelector('#email-error').textContent = error.data.email
            }
            if (error.data.password) {
                formNode.querySelector('#password-error').textContent = error.data.password
            }
            if (error.data.detail) {
                formNode.querySelector('#credentials-invalid').textContent = error.data.detail
            }
        }
    }
}

export const signOut = async (userData) => {
    try {
        const response = await fetch('http://localhost:8000/api/logout/', {
            method: 'POST',
            body: JSON.stringify(userData),
            'content-type': 'application/json'
        })
        const data = response.json()
        if (!response.ok) throw response

        localStorage.removeItem('user')
        location.reload()
        
        return data
    } catch (error) {
        alert(error.statusText || 'Error')
    }
}