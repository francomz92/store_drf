import { showModal } from "./loaders/modals.js";

export const expiredToken = () => {
    const $body = document.body
    const $errorNotification = document.createElement('div')
    const $errorMessage = document.createElement('span')

    $errorNotification.classList.add('error-notification');
    $errorMessage.classList.add('error-message');

    $errorMessage.textContent = 'Sesion Expirada'

    $errorNotification.appendChild($errorMessage)

    $body.appendChild($errorNotification)

    showModal($errorNotification, [document.body.querySelector('main')])

    setTimeout(() => {
        localStorage.removeItem('user')
        location.reload()
    }, 3000);
}