

document.querySelector('[data-form-create-product]').addEventListener('submit', (e)=>{
const price= document.querySelector('input[name=price]')
  const negative_price_error= document.querySelector('[data-form-error-negative-num]')
  if(price.value<0){
    e.preventDefault()
    negative_price_error.classList.remove('d-none')
  }
})