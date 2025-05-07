nums = [1, 2, 3, 4]

response = list(map(str, nums))

obj = " ".join(response)

# for i in response:
#    obj = i.join(obj)
#     
print(obj)


def hola():
    return "hola"

print(hola())    

holas = lambda: 'hola'

print(holas())