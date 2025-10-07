ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

# modif list
ft_list[1] = "World!"

# modif tuple
ft_tuple = (ft_tuple[0], "France!")

# modif set
ft_set = {x if x != "tutu!" else "Paris!" for x in ft_set}

# modif dict
ft_dict["Hello"] = "42Paris!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
