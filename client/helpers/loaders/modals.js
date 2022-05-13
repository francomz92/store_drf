import { signIn } from "../../apis/authentication.js";

const showModal = (modalNode, extraNodes) => {
    modalNode.classList.add('show');
    if (extraNodes) {
        extraNodes.forEach(node => node.classList.add('blur'))
    }
}

const hiddeModal = (modalNode, extraNodes) => {
    modalNode.classList.remove('show');
    if (extraNodes) {
        extraNodes.forEach(node => node.classList.remove('blur'))
    }
}


export const loadSignUpModal = (headerNode) => {
    const $signInModal = document.getElementById('sign-in-modal');
    const $main = document.body.querySelector('main');

    showModal($signInModal, [$main, headerNode]);

    $signInModal.addEventListener('click', e => {
        if (e.target.matches('.modal-close-button')) {
            hiddeModal($signInModal, [$main, headerNode]);
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