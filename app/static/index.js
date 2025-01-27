function request_deletion(product_id) {
  const main_node= document.querySelector('[data-popup]')
  const close_button= document.querySelector('[data-popup-close]')
  const url= document.querySelector('[data-delete-request-url]')
  main_node.classList.add('active')

  close_button.addEventListener('click', ()=>{
    main_node.classList.remove('active')
  })
  url.attributes.href.value= '/product-delete?product-id='+product_id
}

