class myclass:
    def _init_(self,x=0):
        print("initiating____.")
        self.counter=x
    def _call_(self,x=1):
        print("updating values___.")
        self.counter+=x
obj=myclass()
myclass._init_(obj,10)
print("Original Value==>",obj.counter)
myclass._call_(obj,10)
print("Updated Value==>",obj.counter)
print("Can we call _call_ method==>",callable(obj._call_))
print("Can we call counter variable==>",callable(obj.counter))

