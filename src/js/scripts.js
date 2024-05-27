/*!
* Start Bootstrap - Scrolling Nav v5.0.5 (https://startbootstrap.com/template/scrolling-nav)
* Copyright 2013-2022 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-scrolling-nav/blob/master/LICENSE)
*/
//
// Scripts
// 

// window.addEventListener('DOMContentLoaded', event => {

//     // Activate Bootstrap scrollspy on the main nav element
//     const mainNav = document.body.querySelector('#mainNav');
//     if (mainNav) {
//         new bootstrap.ScrollSpy(document.body, {
//             target: '#mainNav',
//             offset: 74,
//         });
//     };

//     // Collapse responsive navbar when toggler is visible
//     const navbarToggler = document.body.querySelector('.navbar-toggler');
//     const responsiveNavItems = [].slice.call(
//         document.querySelectorAll('#navbarResponsive .nav-link')
//     );
//     responsiveNavItems.map(function (responsiveNavItem) {
//         responsiveNavItem.addEventListener('click', () => {
//             if (window.getComputedStyle(navbarToggler).display !== 'none') {
//                 navbarToggler.click();
//             }
//         });
//     });

// });

// // Minimize the header height on scroll, show surveys
// // Slide control
// var lastScrollTop = 0;

// $(window).scroll(function () {
//   var windowWidth = $(window).width();
//   var siteHeader = $(".mainNav");
//   var searchDrawer = $("#search-drawer");
//   var scrollTop = $(document).scrollTop();
//   var st = $(this).scrollTop();

//   // shrink the logo - legacy effect
//   if (scrollTop > 500 && windowWidth >= 1068) {
//     if (st > lastScrollTop) {
//       siteHeader.css({ top: "-190px", height: "140px" });
//       searchDrawer.collapse("hide");
//     } else {
//       siteHeader.css({ top: "0", height: "140px" });
//     //   addStickyMargin();
//     }
//   } else if (windowWidth >= 1068) {
//     siteLogo.css("width", "100%");
//     siteHeader.css({ top: "0", height: "140px" });
//   } else if (scrollTop > 500 && windowWidth <= 1068) {
//     siteHeader.css({ height: "100px", top: "-100px", opacity: "0" });
//     searchDrawer.collapse("hide");

//     if (st > lastScrollTop) {
//       siteHeader.css({ height: "100px", top: "-100px", opacity: "0" });
//     } else {
//     //   addStickyMargin();
//       siteHeader.css({ height: "100px", top: "0", opacity: "1" });
//     }
//   }

//   lastScrollTop = st;
// });


(() => {
  'use strict'

  const storedTheme = localStorage.getItem('theme')

  const getPreferredTheme = () => {
    if (storedTheme) {
      return storedTheme
    }

    return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'
  }

  const setTheme = function (theme) {
    if (theme === 'auto' && window.matchMedia('(prefers-color-scheme: dark)').matches) {
      document.documentElement.setAttribute('data-bs-theme', 'dark')
    } else {
      document.documentElement.setAttribute('data-bs-theme', theme)
    }
  }

  setTheme(getPreferredTheme())

  const showActiveTheme = theme => {
    const activeThemeIcon = document.querySelector('.theme-icon-active use')
    const btnToActive = document.querySelector(`[data-bs-theme-value="${theme}"]`)
    const svgOfActiveBtn = btnToActive.querySelector('svg use').getAttribute('href')

    document.querySelectorAll('[data-bs-theme-value]').forEach(element => {
      element.classList.remove('active')
    })

    btnToActive.classList.add('active')
    activeThemeIcon.setAttribute('href', svgOfActiveBtn)
  }

  window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', () => {
    if (storedTheme !== 'light' || storedTheme !== 'dark') {
      setTheme(getPreferredTheme())
    }
  })

  window.addEventListener('DOMContentLoaded', () => {
    showActiveTheme(getPreferredTheme())

    document.querySelectorAll('[data-bs-theme-value]')
      .forEach(toggle => {
        toggle.addEventListener('click', () => {
          const theme = toggle.getAttribute('data-bs-theme-value')
          localStorage.setItem('theme', theme)
          setTheme(theme)
          showActiveTheme(theme)
        })
      })
  })
})()