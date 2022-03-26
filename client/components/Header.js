export const header = (currentUser) => {
   const $header = document.createElement('header');
   const $img = document.createElement('img');
   const $nav = document.createElement('nav');
   const $ul = document.createElement('ul');

   $header.classList.add('header');
   $ul.classList.add('header__nav');
   $img.classList.add('header-logo');

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

   if (currentUser) {
      $ul.innerHTML += `
         <li>
            <p class="user">${currentUser.email}</p>
         </li>
         <li>
            <button id="cart"></button>
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
   $header.appendChild($img);
   $header.appendChild($nav);

   return $header;
};
