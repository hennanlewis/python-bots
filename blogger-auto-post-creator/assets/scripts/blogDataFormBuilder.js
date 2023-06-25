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

const createInitialPostNumberLabel = (options) => {
	const label = document.createElement("label")
	const span = document.createElement("span")
	span.textContent = "Initial post number"
	label.appendChild(span)

	const input = document.createElement("input")
	input.type = "number"
	input.id = `initial-post${options.position}`
	input.name = `initial-post${options.position}`
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

const createRemoveItemButton = (options) => {
	const button = document.createElement("button")
	button.type = "button"
	button.textContent = "Remove link"
	button.addEventListener("click", (event) => {
		const parent = event.target.parentNode
		const parentPosition = Number(parent.id.replace("position", ""))
		parent.classList.add("height0")
		options.array = options.array.filter(item => item.position != parentPosition)
		setInterval(() => parent.remove(), 1000)
	})

	return button
}

export const builtBlogDataForm = (options) => {
	const div = document.createElement("div")
	div.id = `position${options.position}`

	const urlLabel = createUrlLabel(options.position)
	div.appendChild(urlLabel)

	const initialPostNumberLabel = createInitialPostNumberLabel(options)
	div.appendChild(initialPostNumberLabel)

	const postQuantityLabel = createPostQuantity(options.position)
	div.appendChild(postQuantityLabel)

	const removeItemButton = createRemoveItemButton(options)
	div.appendChild(removeItemButton)

	const container = document.querySelector("form#links-options")
	container.appendChild(div)
}

