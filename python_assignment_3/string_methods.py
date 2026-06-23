# string methods
from xml.etree.ElementPath import find


name = 'MD ASADUJZAMAN'
print(name.lower()) # md asadujzaman
print(name.upper()) # MD ASADUJZAMAN
print(name.replace('MD', 'Mohammad')) # Mohammad ASADUJZAMAN
print(name.split(' ')) # ['MD', 'ASADUJZAMAN']
print(name.strip()) # MD ASADUJZAMAN
print(name.startswith('MD')) # True
print(name.find('ASADUJZAMAN')) # 3
print(name.count('A')) # 4