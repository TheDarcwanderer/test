import sys

f = open('/app/out.txt', 'w')
f.write(f'{sys.version}\nhello world')