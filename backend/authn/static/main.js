async function fetchAuthCredentials(username, password) {
	const res = await fetch('/api/login', {
		method: 'POST',
		headers: { 'Content-Type': 'application/json' },
		body: JSON.stringify({
			username_or_email: username,
			password: password
		})
	});
	if (res.ok) return res.json();
	throw new Error("Authentication failed");
}

async function fetchRegister(username, email, password) {
	const res = await fetch('/api/register', {
		method: 'POST',
		headers: { 'Content-Type': 'application/json' },
		body: JSON.stringify({
			username: username,
			email: email,
			password: password
		})
	});
	if (res.ok) return res.json();
	throw new Error("Authentication failed");
}

async function authUser(event) {
	event.preventDefault();
	const username = document.getElementById('loginUsernameField').value;
	const password = document.getElementById('loginPasswordField').value;

	try {
		const creds = await fetchAuthCredentials(username, password);
		console.log(creds);
		// Do smthing with auth creds (redirect)
	} catch (error) {
		console.error(error.message);
		// Display infos for user to understand
	}
}

async function registerUser(event) {
	event.preventDefault();
	const username = document.getElementById('registerUsernameField').value;
	const email = document.getElementById('registerEmailField').value;
	const password = document.getElementById('registerPasswordField').value;

	try {
		const res = await fetchRegister(username, email, password);
		console.log(res);
		// Do smthing with auth creds (redirect)
	} catch (error) {
		console.error(error.message);
		// Display infos for user to understand
	}
}

document.getElementById('login').addEventListener('submit', authUser);
document.getElementById('createAccount').addEventListener('submit', registerUser);

/*
	Toggle Create account / login form logic without redirection.
	Add additional logic to maintain state after refreshes.
 */
document.addEventListener('DOMContentLoaded', () => {
	const loginForm = document.querySelector('#login');
	const createAccountForm = document.querySelector('#createAccount');

	// Check localStorage to see which form should be visible
	const activeForm = localStorage.getItem('activeForm');
	if (activeForm === null) {
		loginForm.classList.add('form--hidden');
		createAccountForm.classList.remove('form--hidden');
	} else if (activeForm === 'createAccount') {
		loginForm.classList.add('form--hidden');
		createAccountForm.classList.remove('form--hidden');
	} else if (activeForm === 'login') {
		loginForm.classList.remove('form--hidden');
		createAccountForm.classList.add('form--hidden');
	}

	// Add event listeners: toggle form--hidden state
	document.querySelector('#linkCreateAccount').addEventListener('click', e => {
		e.preventDefault();
		loginForm.classList.add('form--hidden');
		createAccountForm.classList.remove('form--hidden');
		localStorage.setItem('activeForm', 'createAccount');
	});
	document.querySelector('#linkLogin').addEventListener('click', e => {
		e.preventDefault();
		loginForm.classList.remove('form--hidden');
		createAccountForm.classList.add('form--hidden');
		localStorage.setItem('activeForm', 'login');

	});
})