const createUrlLabel = (position) => {
	const label = document.createElement("label")
	const span = document.createElement("span")
	span.textContent = "Link url"
	label.appendChild(span)

	const input = document.createElement("input")
	input.type = "url"
	input.id = `link-url${position}`
	input.name = `link-url${position}`
	input.placeholder = "Blogger user link"
	input.addEventListener("blur", event => event.target.required = true)
	label.appendChild(input)

	return label
}

const createInitialPostNumberLabel = (position) => {
	const label = document.createElement("label")
	const span = document.createElement("span")
	span.textContent = "Initial post number"
	label.appendChild(span)

	const input = document.createElement("input")
	input.type = "number"
	input.id = `initial-post${position}`
	input.name = `initial-post${position}`
	input.min = "1"
	input.value = "1"
	label.appendChild(input)

	return label
}

const createPostQuantity = (position) => {
	const label = document.createElement("label")
	const span = document.createElement("span")
	span.textContent = "Quantity for insertion: "
	const quantity = document.createElement("b")
	quantity.id = `quantity-value${position}`
	quantity.textContent = "100"
	span.appendChild(quantity)
	label.appendChild(span)

	const inputRange = document.createElement("input")
	inputRange.type = "range"
	inputRange.id = `post-quantity${position}`
	inputRange.name = `post-quantity${position}`
	inputRange.min = "1"
	inputRange.max = "100"
	inputRange.value = "100"
	inputRange.addEventListener("change", () => {
		const quantityValue = document.querySelector(`#quantity-value${position}`)
		quantityValue.textContent = Math.min(Math.max(inputRange.value, 0), 100)
	})
	label.appendChild(inputRange)

	return label
}

const createRemoveItemButton = (position) => {
	const button = document.createElement("button")
	button.type = "button"
	button.textContent = "Remove link"
	button.addEventListener("click", () => {
		const formToRemove = document.querySelector(`div#position${position}`)
		formToRemove.classList.add("height0")
		optionsArray = optionsArray.filter(item => item.position != position)
		setInterval(() => formToRemove.remove(), 1000)
	})

	return button
}

const addLinkForm = (position) => {
	const div = document.createElement("div")
	div.id = `position${position}`

	const urlLabel = createUrlLabel(position)
	div.appendChild(urlLabel)

	const initialPostNumberLabel = createInitialPostNumberLabel(position)
	div.appendChild(initialPostNumberLabel)

	const postQuantityLabel = createPostQuantity(position)
	div.appendChild(postQuantityLabel)

	const removeItemButton = createRemoveItemButton(position)
	div.appendChild(removeItemButton)

	const container = document.querySelector("form#links-options")
	container.appendChild(div)
}

const isValidURL = (url) => {
	const patronURL1 = /^https?:\/\/www\.blogger\.com\/blog\/posts\/\d+$/
	const patronURL2 = /^https?:\/\/www\.blogger\.com\/u\/\d+\/blog\/posts\/\d+$/
	return patronURL1.test(url) || patronURL2.test(url)
}

let optionsArray = []
let optionPosition = 0

const addLinkButton = document.querySelector("#add-item")
addLinkButton.addEventListener("click", () => {
	optionPosition += 1
	addLinkForm(optionPosition)
	optionsArray.push({
		url_link: "",
		initial_post: 0,
		post_quantity: 1,
		position: optionPosition
	})
})

const createPostButton = document.querySelector("#create-post")
createPostButton.addEventListener("click", () => {
	const bot_options = optionsArray.map(item => {
		const { position } = item
		const formsValues = document.querySelector(`div#position${position}`)
		const blog_url = formsValues.querySelector(`#link-url${position}`)
		if (!isValidURL(blog_url.value)) return blog_url.focus()

		const initial_post = formsValues.querySelector(`#initial-post${position}`).value
		const post_quantity = formsValues.querySelector(`#post-quantity${position}`).value
		const browser = document.querySelector("input[name='browser']:checked").value

		return {
			blog_url: blog_url.value,
			initial_post: Number(initial_post),
			post_quantity: Number(post_quantity),
			browser
		}
	})

	console.log(bot_options)
})