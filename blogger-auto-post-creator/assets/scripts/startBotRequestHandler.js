import { generateDataToRequest } from "./validation.js"

export const startBot = (event, options) => {
	const dataToRequest = generateDataToRequest(options)

	console.log(dataToRequest)
	if (dataToRequest.filter(item => item).length > 0) {
		fetch("/startbot", {
			method: "POST", body: JSON.stringify(dataToRequest), headers: {
				"Content-Type": "application/json",
			},
		}).then(res => res.json())
			.then(data => {
				changeToResetButton(event.target, options)
				console.log(data)
			})

	}
}

const changeToResetButton = (element, options) => {
	const clone = element.cloneNode(true)
	clone.textContent = "Reset Bot"
	clone.addEventListener("click", event => {
		fetch("/resetbot")
			.then(res => {
				changeToStartBot(event.target, options)
				return res.json()
			})
			.then(data => console.log(data))
	})
	element.parentNode.replaceChild(clone, element)
}

const changeToStartBot = (element, options) => {
	const clone = element.cloneNode(true)
	clone.textContent = "Start Creating Post"
	clone.addEventListener("click", event => startBot(event, options))
	element.parentNode.replaceChild(clone, element)
}
