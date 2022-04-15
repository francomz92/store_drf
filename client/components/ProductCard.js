export const card = (data) => {
   const $card = document.createElement('article');
   $card.setAttribute('id', data.id);
   $card.innerHTML = `
      <img src="${data.image_url || '../assets/img/default-no-image.png'}" alt="${data.name}" />
      <h5>${data.name}</h5>
      `;
   if (data.offer) {
      $card.innerHTML += `
         <span class="on-sale">On Sale</span>
         <span class="discount-rate">${data.discount_rate}%</span>
         <span class="unit-price-on-discount">$${data.unit_price}</span>
         <span class="price-discount">$${data.price_with_discount}</span>
         `;
   } else {
      $card.innerHTML += `
         <span class="unit-price">$${data.unit_price}</span>
         `;
   }
   $card.innerHTML += `
      <span>Quedan ${data.stok}</span>
   `;
   return $card;
};
