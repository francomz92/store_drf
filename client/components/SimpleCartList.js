export const SimpleCheckOutList = (items) => {
    const $cartList = document.createElement('ul')
    $cartList.classList.add('cart-list')

    if (items.length <= 0) return $cartList

    const $checkOutButton = document.createElement('button')
    $checkOutButton.setAttribute('id', 'checkout')
    $checkOutButton.setAttribute('type', 'button')
    $checkOutButton.classList.add('button')
    $checkOutButton.textContent = 'Checkout'

    items.forEach(item => {
        const $product = document.createElement('li')
        $product.innerHTML = `
            <details>
                <summary>
                    <img src="${item.product.image_url || '../assets/img/default-no-image.png'}">
                    <div>
                        <span>${item.ammount} ${item.product.name}</span>
                        <span>$${item.price}</span>
                    </div>
                </summary>
                <span>Descripcion: ${item.product.description} ${item.product.offer ? '- En oferta' : ''}</span>
            </details>
            <i class="remove-item" id="${item.id}"></i>
         `
        $cartList.appendChild($product)
    })
    $cartList.appendChild($checkOutButton)

    return $cartList
}