hello  = 'Hello World'
name ='Maxim'
last_name = 'Bortnik'
age = 16

print(hello)
print(name)
print(last_name)
print(age)

print(type(hello))
print(type(name))
print(type(last_name))
print(type(age))

types = [type(hello), type(name), type(last_name), type(age)]
print("Типи даних:", types)

if all(x == types[0] for x in types):
    print("Усі типи однакові")
else:
    print("Є різні типи")