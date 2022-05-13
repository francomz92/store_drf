export const expiredToken = () => {
    alert('Session expirada')
    localStorage.removeItem('user')
    location.reload()
}