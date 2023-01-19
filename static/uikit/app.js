// Invoke Functions Call on Document Loaded
document.addEventListener('DOMContentLoaded', function () {
  hljs.highlightAll();
});


let msgWrapper = document.querySelector('.message-box')
let alertClose = document.querySelector('.alert__close')

if(msgWrapper){
    alertClose.addEventListener('click',function(){
        msgWrapper.style.display = 'none'
    })
}