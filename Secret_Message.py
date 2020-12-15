import getpass, os

print(f"Hello, {getpass.getuser()}. That's you right?")
cmd = input()

os.system('cls' if os.name == 'nt' else 'clear')