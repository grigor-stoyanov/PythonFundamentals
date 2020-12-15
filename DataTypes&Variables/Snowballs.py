n = int(input())
max = -1
for i in range(0, n):
    snow = int(input())
    time = int(input())
    quality = int(input())
    calc = int((snow/time)**quality)
    if calc > max:
        max = calc
        maxsnow = snow
        maxtimee = time
        maxquality = quality
print(f'{maxsnow} : {maxtimee} = {max} ({maxquality})')