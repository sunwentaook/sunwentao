# 剔除人名中的空白
famous_person = '         Alber\n\t Einstein\n\t once\n\t said'
message = 'A person who never made a mistake never tried anything new'
name = famous_person + ',"' + message + '."'
print(name)
print(famous_person.lstrip())
print(name.rstrip())
print(name.strip())
