![Screenshot_20201114-001136](https://user-images.githubusercontent.com/69844284/99106382-5b69f380-260e-11eb-9b97-a8e0e975b2f7.png)
## output:
![Screenshot_20201114-001159](https://user-images.githubusercontent.com/69844284/99106391-5efd7a80-260e-11eb-9100-e74b51f9a86c.png)

## written code bellow:

#Welcome inputer
name=input()
print("Hello "+name)

#-----------------------------------

#get system info
import platform
my_system=platform.uname()

print(f"System:  {my_system.system}")
print(f"Node Name:  {my_system.node}")
print(f"Release:  {my_system.release}")
print(f"Version:  {my_system.version}")
print(f"Machine:  {my_system.machine}")
print(f"System:  {my_system.system}")
print(f"Processor:  {my_system.processor}")
