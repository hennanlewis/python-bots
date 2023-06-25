export const isValidURL = (url) => {
	const patronURL1 = /^https?:\/\/www\.blogger\.com\/blog\/posts\/\d+$/
	const patronURL2 = /^https?:\/\/www\.blogger\.com\/u\/\d+\/blog\/posts\/\d+$/
	return patronURL1.test(url) || patronURL2.test(url)
}

export const generateDataToRequest = (options) => (
	options.array.map(item => {
		const { position } = item
		const formsValues = document.querySelector(`div#position${position}`)
		const blog_url = formsValues?.querySelector(`#link-url${position}`)

		if(!blog_url) return null

		if (!isValidURL(blog_url.value)) {
			blog_url.focus()
			return null
		}

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
)
