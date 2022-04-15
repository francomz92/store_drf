export const header = (userData, cart) => {
   const $header = document.createElement('header');
   const $a = document.createElement('a');
   const $img = document.createElement('img');
   const $nav = document.createElement('nav');
   const $ul = document.createElement('ul');

   $header.classList.add('header');
   $ul.classList.add('header__nav');
   $img.classList.add('header-logo');
   $a.setAttribute('href', '/');

   $img.setAttribute('src', '../assets/img/logo.png');
   $img.setAttribute('alt', 'STORE');

   $ul.innerHTML = `
      <li>
         <a href="/">Home</a>
      </li>
      <li>
         <a href="/#store">Store</a>
      </li>
      <li>
         <a href="/#contact">Contact</a>
      </li>
   `;

   if (userData) {
      $ul.innerHTML += `
         <li>
            <p class="user">${userData.user.email}</p>
         </li>
         <li>
            <button id="cart">${cart.results.items.length > 0 ? cart.results.items.length : ''}</button>
         </li>
         <div class="auth-buttons">
            <a href="/#sign-out">Sign Out</a>
         </div>
      `;
   } else {
      $ul.innerHTML += `
         <li>
            <div class="auth-buttons">
               <a href="/#sign-in">Sign In</a>
               <a href="/#sign-up">Sign Up</a>
            </div>
         </li>
      `;
   }

   $nav.appendChild($ul);
   $a.appendChild($img);
   $header.appendChild($a);
   $header.appendChild($nav);

   return $header;
};
