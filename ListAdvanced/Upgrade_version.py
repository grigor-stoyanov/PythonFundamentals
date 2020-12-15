current_version = input().split('.')
next_version = int("".join(current_version))+1
next_version = [str(each) for each in str(next_version)]
print('.'.join(next_version))