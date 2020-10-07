import redis

age_field = redis.Redis()
age_field.set_response_callback('HGET', int)
age_field.hget('foo', 'age')
# OUT: 40
a =age_field.hget('foo', 'age')
type(a)
# OUT: <type 'int'>

gpa_field = redis.Redis()
gpa_field.set_response_callback('HGET', float)
gpa_field.hget('foo', 'gpa')
# OUT: 2.5
b = gpa_field.hget('foo', 'gpa')
type(b)
# OUT: <type 'float'>
