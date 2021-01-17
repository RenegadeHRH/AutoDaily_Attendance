def testResultGetBaseInfo_json(func):
    def wrapper(self,*args, **kwargs):
        result = func(self,*args, **kwargs)
        print("Auth:",self.GetAuth())
        print("cookies:",self.cookies)
        print("typeofResult:",type(result))
        print("result:%s" % result)
        return result
    return wrapper
