def NULL_not_found(object: any) -> int:
	obj_type = object.__class__
	output = ''

	match object:
		case str() if not object:
			output = 'Empty: '
		case float() if object != object:
			output = 'Cheese: '
		case bool() if object is False:
			output = 'Fake: '
		case int() if object == 0:
			output = 'Zero: '
		case None:
			output = 'Nothing: '
		case _:
			print("Type not found")
			return 1

	print(f"{output}{object} {obj_type}")
	return 0
