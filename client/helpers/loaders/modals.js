import { signIn } from "../../apis/authentication.js";

export const loadSignUpModal = (headerNode) => {
    const $signInModal = document.getElementById('sign-in-modal');
    const $body = document.body.querySelector('main');

    $signInModal.classList.add('show');
    headerNode.classList.add('blur')
    $body.classList.add('blur')

    $signInModal.addEventListener('click', e => {
        if (e.target.matches('.modal-close-button')) {
            $signInModal.classList.remove('show');
            headerNode.classList.remove('blur')
            $body.classList.remove('blur')
        }
    })

    document.addEventListener('submit', async e => {
        e.preventDefault()
        
        $signInModal.querySelectorAll('span').forEach(el => { el.innerHTML = '' })
        
        if (e.target.matches('#login-form')) {
            const formData = {
                email: e.target.email.value,
                password: e.target.password.value
            }
            await signIn(formData, $signInModal)
        }
    })
}