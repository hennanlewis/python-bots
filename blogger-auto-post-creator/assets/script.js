function addLinkForm(position) {
	const formulario = document.createElement("form")

	const label1 = document.createElement("label")
	const span1 = document.createElement("span")
	span1.textContent = "Link url"
	const input1 = document.createElement("input")
	input1.type = "url"
	input1.name = `link-url${position}`
	label1.appendChild(span1)
	label1.appendChild(input1)

	const label2 = document.createElement("label")
	const span2 = document.createElement("span")
	span2.textContent = "Initial post number"
	const input2 = document.createElement("input")
	input2.type = "number"
	input2.name = `initial_post${position}`
	input2.min = "1"
	input2.value = "1"
	label2.appendChild(span2)
	label2.appendChild(input2)

	const label3 = document.createElement("label")
	const span3 = document.createElement("span")
	span2.textContent = "Quantity for insertion"
	const input3Range = document.createElement("input")
	input3Range.type = "range"
	input3Range.name = `quantity_range${position}`
	input3Range.min = "1"
	input3Range.max = "100"
	input3Range.value = "1"
	const input3Number = document.createElement("input")
	input3Number.type = "number"
	input3Number.name = `quantity_number${position}`
	input3Number.min = "1"
	input3Number.max = "100"
	input3Number.value = "1"
	label3.appendChild(span3)
	label3.appendChild(input3Range)
	label3.appendChild(input3Number)

	const button = document.createElement("button")
	button.type = "button"
	button.textContent = "Remove item"

	formulario.appendChild(label1)
	formulario.appendChild(label2)
	formulario.appendChild(label3)
	formulario.appendChild(button)


	const container = document.querySelector("main")
	container.appendChild(formulario)
}

function validateURL(url) {
	const patronURL1 = /^https?:\/\/www\.blogger\.com\/blog\/posts\/\d+$/
	const patronURL2 = /^https?:\/\/www\.blogger\.com\/u\/\d+\/blog\/posts\/\d+$/
	return patronURL1.test(url) || patronURL2.test(url)
}

const optionsArray = []

const addLink = document.querySelector("#add-item")

addLink.addEventListener("click", () => {
	addLinkForm(optionsArray.length + 1)
	optionsArray.push({
		url_link: "",
		initial_post: 0,
		final_post: 1
	})
	console.log(optionsArray)
})