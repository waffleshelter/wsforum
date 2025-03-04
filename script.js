function serializeForm(formNode) {
    const { elements } = formNode
    const data = Array.from(elements)
      .filter((item) => !!item.name)
      .map((element) => {
        const { name, value } = element
  
        return { name, value }
      })
  
    document.getElementById('main-pub-block').innerHTML += `<div class'main-pub-block-item shadow'> <h1>${data[0]['value']}</h1> <p>${data[1]['value']}</p> </div>`;
  }
  
  

function handleFormSubmit(event) {
    // Просим форму не отправлять данные самостоятельно
    event.preventDefault()
    
    console.log('Отправка!')
    serializeForm(applicantForm)
  }
  
  const applicantForm = document.getElementById('user-form')
  applicantForm.addEventListener('submit', handleFormSubmit)
  
  

// Добавление к HTML обработанного сообщения от пользователя: НЕ РАБОТАЕТ
// if(document.getElementById('submit-btn').onclick) {
//     document.getElementById('main-pub-block').innerHTML += "<div class'main-pub-block-item shadow'> <h1>Никнейм</h1> <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Tempore dolorum vero ex quaerat suscipit aliquid illo magnam hic explicabo ad, at deleniti architecto quas ducimus consequuntur. Voluptatum obcaecati repudiandae reprehenderit.</p> </div>";
// }