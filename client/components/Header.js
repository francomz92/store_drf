export const Header = (userData, cart) => {
   const $header = document.createElement('header');
   const $a = document.createElement('a');
   const $img = document.createElement('img');
   const $nav = document.createElement('nav');
   const $ul = document.createElement('ul');
   const $button = document.createElement('button')

   $header.classList.add('header');
   $button.classList.add('burgger');
   $ul.classList.add('header__nav');
   $img.classList.add('header-logo');
   $a.setAttribute('href', '/');

   $img.setAttribute('src', '../assets/img/logo.png');
   $img.setAttribute('alt', 'STORE');

   $ul.innerHTML = `
      <li>
         <a href="/#home">Home</a>
      </li>
      <li>
         <a href="/#store">Store</a>
      </li>
      <li>
         <a href="/#contact">Contact</a>
      </li>
   `;

   if (userData && cart) {
      $ul.innerHTML += `
         <li>
            <p class="user">${userData.user.email}</p>
         </li>
         <li>
            <button id="cart">${cart.results.items.length > 0 ? cart.results.items.length : ''}</button>
         </li>
         <div class="auth-buttons">
            <button id="sign-out">Sign Out</button>
         </div>
      `;
   } else {
      $ul.innerHTML += `
         <li>
            <div class="auth-buttons">
               <button id="sign-in">Sign In</button>
               <button id="sign-up">Sign Up</button>
            </div>
         </li>
      `;
   }

   $nav.appendChild($ul);
   $a.appendChild($img);
   $header.appendChild($button)
   $header.appendChild($a);
   $header.appendChild($nav);

   return $header;
};
