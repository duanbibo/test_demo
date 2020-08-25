class  weituo:

      def __init__(self,object):
            self.warrped=object

      def __getattr__(self, attr):
            #print('trace',attr)
            return  getattr(self.warrped,attr)


if __name__ == '__main__':
    w=weituo([1,2,3,4])
    w.append(5)
    print(w.warrped)