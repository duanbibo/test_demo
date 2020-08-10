
class upper(str):

      def __new__(cls, string):
            string=string.upper()
            return str.__new__(cls,string)

a=upper("aaaa")
print(a)