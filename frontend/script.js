const menuBtn = document.querySelector('#menu-btn');
const closeBtn = document.querySelector('.close');
const sideMenu = document.querySelector('.nav');
const authBlock = document.querySelector('.auth__block');

// Прослушиваем форму авторизации на отправку данных и предотвращаем перезагрузку страницы
document.querySelector('.form__auth').addEventListener('submit', e => {
  e.preventDefault();

  // Записываем данные из формы авторизации
  const data = {
    password: document.getElementById('auth__password').value,
    username: document.getElementById('auth__username').value
    
  }
  
  sendForm(data);


  // Тут пока костыльное закрытие формы
  authBlock.style.display = "none";
  document.querySelector('.auth-bg').style.display = "none";  
})

async function sendForm(data) {
  // тут пока хз че указывать как аргумент для fetch, должен быть адрес куда отправляю данные из формы
  const res = await fetch('/add', {
    method: 'POST',
    headers: {'Content-type': 'application/json'},
    body: JSON.stringify(data)
  })

  const result = await res.json();

  console.log(result);
  // if(res.status === 201) {
  //   alert(`Thanks! ${result.message}`)

  // }
}




// Функции для работы меню в адаптивном режиме со смартфона
menuBtn.addEventListener('click', () => {
    menuBtn.style.display = "none"
    sideMenu.style.display = "block";
})

closeBtn.addEventListener('click', () => {
    sideMenu.style.display = "none";
    menuBtn.style.display = "inline-block";
})