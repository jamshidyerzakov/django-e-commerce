
class BadHTTPMethodError(BaseException):
    __cause__ = "Bad http method was used"
