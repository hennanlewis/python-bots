import { startBot } from "./startBotRequestHandler.js"
import { builtBlogDataForm } from "./blogDataFormBuilder.js"

const options = { array: [], position: 0 }

const addLinkButton = document.querySelector("#add-item")
addLinkButton.addEventListener("click", () => {
	options.position += 1
	builtBlogDataForm(options)
	options.array.push({
		url_link: "",
		initial_post: 0,
		post_quantity: 1,
		position: options.position
	})
})

const createPostButton = document.querySelector("#create-post")
createPostButton.addEventListener("click", event => startBot(event, options))