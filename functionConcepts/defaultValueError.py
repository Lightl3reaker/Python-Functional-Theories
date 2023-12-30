#This kind of using datetime of utcnow method can get default value error
from datetime import datetime
def myfunc(msg,*,dt=datetime.utcnow()):
    print("{}:{}".format(dt,msg))
myfunc("Text Message.")
#This is solution
def newfunc(msg,*,dt=None):
    if not dt:
        dt=datetime.utcnow()
        print("{}:{}".format(dt,msg))
newfunc("This is Message.")