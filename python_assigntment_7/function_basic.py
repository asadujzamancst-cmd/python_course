#function basic def keyword , required parameter and default parameter
#def keyword
def my_name():
    print("md asadujzaman")

my_name()

# required parameter
def name(my_name):
    print(f'Hello,{my_name}')


name("asadujzaman")

# default parameter
def defaul_parameter(name="asda"):
    print(name)

defaul_parameter()
defaul_parameter('asadujzaman')