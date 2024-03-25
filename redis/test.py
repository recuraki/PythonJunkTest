import redis
import sys
try:
    r = redis.Redis(host='localhost', port=6379, db=0)
except redis.exceptions.ConnectionError as e:
    print("redis: Connection Error")
    sys.exit(-1)
r.set('hoge', 'moge')
r.set('hoge', 'moge2')
r.set('moge', 'moge2')
r.set('hoge2', 'moge2')
print(r.get('hoge'))
print(r.get("moge"))
t = r.keys("hoge*")
print(t)