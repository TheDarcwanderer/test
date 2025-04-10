import sys

f = open('/app/out.txt', 'w')
f.write(f'{sys.version}\nhello world')
f.close()
print(f'{sys.version}\nhello world')