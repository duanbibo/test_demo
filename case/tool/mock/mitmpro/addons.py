
import sys

sys.path.append(r"C:\Users\87842\PycharmProjects\test_demo")
print(sys.path)

from  case.tool.mock.mitmpro import P02_update   as Update
#from  case.tool.mock.mitmpro import P01_Counter   as Counter

addons=[
     # Counter.Counter(),
      Update.Joker()

]