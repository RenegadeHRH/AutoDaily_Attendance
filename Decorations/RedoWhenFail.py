def RedoWhenFail(func):
    def wrapper(self,*args,**kwargs):
        while True:
            try:
                result=func(self,*args,**kwargs)
                break
            except Exception:
                continue
        return result
    return wrapper