import go_dfz

while True:
	text = input('go-dfz > ')
	if text.strip() == "": continue
	result, error = go_dfz.run('<stdin>', text)

	if error:
		print(error.as_string())
	elif result:
		if len(result.elements) == 1:
			print(repr(result.elements[0]))
		else:
			print(repr(result))
