def solve():
	from PIL import Image
	import base64
	import pytesseract
	from io import BytesIO
	browser.get("https://ringzer0ctf.com/challenges/17")
	image = browser.find_elements_by_tag_name('img')[1].get_attribute('src')[22:] #[22:] is to remove the beginning of the src, the 'data:image/png;base64,'
	imageStr = BytesIO(base64.b64decode(image))
	image = Image.open(imageStr)
	image.show()
	image.load()
	return pytesseract.image_to_string(image)

solve()
