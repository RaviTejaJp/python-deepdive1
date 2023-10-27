import time
def immutable_object(string):
    print(f"{hex(id(string))} -- content --- {string}")
    string = string + ' world'
    print(f"{hex(id(string))} -- content --- {string}")
    return string

def mutable_object(string_list: list[str]) -> list[str]:
    print(f"{hex(id(string_list))} -- content --- {string_list}")
    print_content_and_id(string_list)
    string_list.append("world")
    print(f"{hex(id(string_list))} -- content --- {string_list}")
    print_content_and_id(string_list)
    return string_list

def print_content_and_id(variable:any) -> None:
    for item in variable:
        print(f"{hex(id(item))} -- content --- {item}")
    


print(("ImMutable object Call").center(80))
global_string = "Hello"
print(f"{hex(id(global_string))} -- content --- {global_string}")
immutable_object(global_string)
print(f"{hex(id(global_string))} -- content --- {global_string}")

print(("Mutable object Call").center(80))
global_string_list = ["Hello"]
print(f"{hex(id(global_string_list))} -- content --- {global_string_list}")
print_content_and_id(global_string_list)
mutable_object(global_string_list)
print(f"{hex(id(global_string_list))} -- content --- {global_string_list}")
print_content_and_id(global_string_list)


print(dir(mutable_object))

print(mutable_object.__annotations__)
print((mutable_object.__closure__))