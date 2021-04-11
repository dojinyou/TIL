let todo_item_list = [];
let input_button = document.getElementById('input_button');
input_button.addEventListener('click', addItem);
function addItem() {
	let todo_item = document.getElementById('todo_title').value;
	if (todo_item != null) {
		todo_item_list.push(todo_item);
		document.getElementById('todo_title').value = '';
	}
	let new_li = document.createElement('li');
	new_li.textContent = todo_item_list[i];

	let delete_button = document.createElement('button');
	delete_button.value = 'delete';
	delete_button.click = () => {
		console.log('작동');
		new_div.parentNode.removeChild(new_div);
	};

	let new_div = document.createElement('div');
	new_div.appendChild(new_li);
	new_div.appendChild(delete_button);

	let todo_items = document.getElementById('todo_items');
	todo_items.appendChild(new_div);
}
