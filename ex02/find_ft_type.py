def all_thing_is_obj(object: any) -> int:
	obj_type = object.__class__
	ret = None

	match object:
		case str():
			if object == "Brian":
				ret = f'{object} is in the kitchen : {obj_type}'
			elif object == "Toto":
				ret = f'{object} is in the kitchen : {obj_type}'
			else:
				ret = "Type not found"
		case list():
			ret = f'List : {obj_type}'
		case tuple():
			ret = f'Tuple : {obj_type}'
		case set():
			ret = f'Set : {obj_type}'
		case dict():
			ret = f'Dict : {obj_type}'
		case _:
			ret = "Type not found"

	print(ret)
	return 42
