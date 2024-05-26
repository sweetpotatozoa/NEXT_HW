const username = document.querySelector('.username');
const usernameWrapper = document.querySelector('.usernameWrapper');
const header = document.querySelector('#header');

function checkUsername() {
    const checkName = window.localStorage.getItem('username');
    if (checkName) {
        header.innerHTML = `<h1>${checkName}의 투두리스트!</h1><button onclick="setUsername()">초기화하기</button>`;
        usernameWrapper.classList.add('hidden');
    } else {
        usernameWrapper.classList.remove('hidden');
        header.innerHTML = '';
    }
}

checkUsername();

function setUsername() {
    const name = username.value;
    window.localStorage.setItem('username', name);
    username.value = '';
    checkUsername();
}

function resetUsername() {
    window.localStorage.removeItem('username');
    checkUsername();
}

const todoForm = document.getElementById('todo-form');
const todoList = document.getElementById('todo-list');
const submitBtn = document.querySelector('.submitBtn');
const deleteBtn = document.getElementById('deleteBtn');

function addTodo(event) {
    event.preventDefault();
    let todoInput = todoForm.querySelector('#content');
    console.log(todoInput.value);
    let LocalTodoList = JSON.parse(window.localStorage.getItem('todo')) || [];
    //|| []는 방어로직이에요. 이렇게 하는게 맞는지는 모르겠지만~
    //근데 솔직히 방어로직 신경쓰지 힘들어요. ?.도 다들 안 쓰자나!
    console.log(LocalTodoList);
    LocalTodoList.push(todoInput.value);
    todoInput.value = '';
    window.localStorage.setItem('todo', JSON.stringify(LocalTodoList));
    checkTodoList();
}
todoForm.addEventListener('submit', addTodo);

function checkTodoList() {
    const checkTodo = window.localStorage.getItem('todo') || [];
    console.log(checkTodo);
    if (checkTodo) {
        const todoArray = JSON.parse(checkTodo);
        console.log(todoArray);
        const todoLists = todoArray.map(
            (todo, index) => `<li>${todo}<button onclick="deleteTodo(${index})" id="deleteBtn">삭제</button></li>`
        );
        //허헣 혹시라도 제 코드를 참고하시는 누군가가 있다면 index를 파라미터로 쓰는 건 따라하지 마세요 ㅎ...
        //코드에 레거시를 남기는 짓 입니다.
        todoList.innerHTML = '';
        todoList.innerHTML = todoLists.join('');
    }
}

checkTodoList();

function deleteTodo(index) {
    console.log('delete');
    const checkTodo = window.localStorage.getItem('todo') || [];
    const todoArray = JSON.parse(checkTodo);
    todoArray.splice(index, 1);
    window.localStorage.setItem('todo', JSON.stringify(todoArray));
    checkTodoList();
}
