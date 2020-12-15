n = int(input())
total_free_chairs = 0
isReady = True
for i in range(n):
    chairs, positions = input().split()
    free_chairs = len(chairs) - int(positions)
    if free_chairs < 0:
        print(f'{-free_chairs} more chairs needed in room {i + 1}')
        total_free_chairs += free_chairs
        isReady = False
    else:
        total_free_chairs += free_chairs
if isReady:
    print(f'Game On, {total_free_chairs} free chairs left')
