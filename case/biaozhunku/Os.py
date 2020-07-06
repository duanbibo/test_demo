#encoding=utf-8
import os

'''
OS库：主要是python与操作系统之间的交互
 操作系统主要的功能就是读、写、执行一些文件和程序
             
            主要就是获取文件的一些基础信息：如路径、时间、属性、大小、判断时=是目录还是文件
             判断文件路径是否存在，

'''

print( os.getcwd(),"获取当前工作目录")

os.mkdir("mk")
os.rmdir("mk")
print("执行创建目录，删除目录")
print(os.path.curdir  ,".号 可与join进行拼接 代表当前目录 ,可以用在join内做第二个参数")
print(os.path.pardir," ..  返回上级目录")

'''  os.path.join( dirpath,  basename  )
     os.path.join(  dirpath, ..)
      os.path.join(  filepath, ..)
     os.path.join  第一个可以是文件目录，也可以是文件名
         如果是文件目录的话，第二个参数可以是文件名 或者 .. 拼接，实现file的路径或者返回上级目录
         如果第文件名的话，第二个参数必须为  .. 返回上级目录
         如果 使用路径拼接时，后面那个使用了 ..的话，os.path.join外层必须淘一个os.path.abspath()进行解析。
'''
print(os.path.join(os.getcwd(),'Os.py')
      ,"os.path.join 主要用于字符串拼接路径，第一个是目录 ，第二个参数可以是文件名 basename")
print(os.path.abspath(os.path.join(os.path.dirname(__file__),os.path.pardir)),
      "第一个参数是文件名，第二个是 .. 返回上级目录")
print(os.path.abspath(os.path.join(os.path.dirname(__file__),os.path.pardir)),
      "第一个是目录，第二个是.. 返回上上级目录")

''' os.path  主要获取文件路径'''
print(os.path.basename(__file__),"获取文件的base文件名，即文件名称和后缀")
print(os.path.dirname(__file__),"获取父类的目录")
print(os.path.split(__file__),"将当前路径进行分割返回一个元祖，"
                              "第一个是当前文件路径的父目录，第二个元素是文件名称")
print(os.path.splitext(__file__),"拆分路径，第二个是文件类型")
print(os.path.abspath("source.txt"),"只需输入一个当前执行文件下的一个文件名，"
                                    "返回此文件的绝对路径")








''' os这部分需要利用操作系统执行命令，执行window和shell脚本，以及启动线程
  os.system(  "填入cmd命令") 返回值是指令运行结束后返回的状态码 0代表执行成功  256代表未找到

'''

print(os.name, "获取操作系统类型： 输出字符串指示当前使用平台。win->'nt'; Linux->'posix'")
#print(os.environ ,"获取操作系统的环境变量")
ip=os.system("ipconfig")
print(ip,"ipppppppppppppppppppppppppppp")
#print(os.system("ping  www.baidu.com") ,"直接执行命令 ,返回结果为0代表执行成功，返回结果为1代表执行失败")
print(os.system(' echo   “你好”'),"执行echo输出：发出声音")
print(os.system('dir')," 查看当前文件均价下所有的目录和文件")
# print(os.system(" mkdir   mk"),"通过os.system命令创建文件夹")
# print(os.system("rmdir  mk"))




'''
通过popen 可以执行操作系统的一些命令
os.popen(cmd,mode) 打开一个与command进程之间的管道。
返回值是一个文件对象，可以读或者写(由mode决定，默认是’r')。
如果mode为’r'，可以使用此函数的返回值调用read()来获取command命令的执行结果。
'''

shell=os.popen(" ipconfig ","r")
result=shell.read()
print(result,type(shell),type(result),
      "使用popen执行shell命令返回的是一个类似文件，调用read()方法获取执行后的结果为字符串")

'''
使用第三方库 command模块
（1）commands.getstatusoutput(cmd)，其以字符串的形式返回的是输出结果和状态码，即（status,output）。
（2）commands.getoutput(cmd)，返回cmd的输出结果。
（3）commands.getstatus(file)，返回ls -l file的执行结果字符串，调用了getoutput，不建议使用此方法
'''
#import commands




''''
使用subprocess模块
允许创建很多子进程，创建的时候能指定子进程和子进程的输入、输出、错误输出管道，执行后能获取输出结果和执行状态。
subproess.run()
subprocess.run(args[, stdout, stderr, shell ...])：执行args命令，返回值为CompletedProcess类； 
若未指定stdout，则命令执行后的结果输出到屏幕上，函数返回值CompletedProcess中包含有args和returncode；
 若指定有stdout，则命令执行后的结果输出到stdout中，函数返回值CompletedProcess中包含有args、returncode和stdout；
  若执行成功，则returncode为0；若执行失败，则returncode为1； 
  若想获取args命令执行后的输出结果，命令为：output = subprocess.run(args, stdout=subprocess.PIPE).stdout
 
 subprocess的其他方法，都是建立在run方法的执行结果上，比如call方法返回执行状态
                  check_output 方法 获取执行命令的输出结果
 




'''
import subprocess

commadnadb=["adb","devices"]
file='mylog.txt'
print("默认在输出执行结果后，会额外输出一个完成的进程类，包含执行的参数，以及执行的结果code 0代表成功")
adb=subprocess.run(commadnadb)
print(adb)


#List of devices attached
#241da18	device
#CompletedProcess(args=['adb', 'devices'], returncode=0)

print("======直接输出结果")
run_output = subprocess.run("adb  shell ps ", stdout=subprocess.PIPE,encoding='utf-8').stdout
print(run_output)




'''
subprocess.Popen类用于在一个新进程中执行一个子程序，上述subprocess函数均是基于subprocess.Popen类；
 使用Popen执行后返回的是一个内存对象。 通过这个内存对象可以获取当前子进程的Pid
 利用获取的popen对象还可以调用communicate()方法，执行完子进程后继续与当前子进程交互，执行输入的内容shell

'''

pop=subprocess.Popen(["python"],shell=True,universal_newlines=True,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#通过创建popen对象实例化打开的管道file对象，操作这个file对象。对其写入命令

''' 方法一：多个shell执行打开管道输入流，'''
pop.stdin.write("print('hello world')")
pop.stdin.close()
pout=pop.stdout.read()
pop.stdout.close()
peer=pop.stderr.read()
pop.stderr.close()


print("使用Popen对象的构造函数内打开的标准输入流，以及对象的标准输出流获取结果",pout,peer)
print(pop.pid,"popen对象的属性： 查看创建进程的pid")

'''  方法二：多个shell 打开管道传送communicate方法，阻塞父进程。子进程执行结束后返回'''
#通过popen核心的方法communicate执行传输的命令，返回是一个元祖。标准输出流和标准错误流字节流
# pop.stdin.write('print(1)')
#out,er=pop.communicate()
#print(out,er,"使用communicate方法输出会阻塞父进程。待子进程执行完毕后才交给父进程控制器")

print(pop.returncode)


'''场景二： 利用管道将多个shell 一起执行
   实现方式一： 直接利用 管道 将shell输入
    二：通过Popen类创建2个实例，将第一个shell的输出流当做第二个构造函数的参数
     
   
  
  '''


print("=================开始popen")
def subprocess_Popen1():
    print("***通过communicate函数分别输出PopenObject对象的输出流和错误流***")
    args = [["adb", "devices"], ["adb", "devices11"]]
    for arg in args:
        popen_object = subprocess.Popen(arg, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        object_stdout, object_stderr = popen_object.communicate()
        output = {"popen_object": popen_object,
                  "object_stdout": object_stdout,
                  "object_stderr": object_stderr}
        print(output)
    """
    {'popen_object': <subprocess.Popen object at 0x0000000002212400>, 'object_stdout': b'List of devices attached \r\n106D111805005938\tdevice\r\n\r\n', 'object_stderr': b''}
    {'popen_object': <subprocess.Popen object at 0x0000000002577C18>, 'object_stdout': b'', 'object_stderr': b'Android Debug Bridge version 1.0.31\r\n\r\n -a .....}
    """

    print("***通过stdout和stderr方法输出PopenObject对象输出流和错误流***")
    p0 = subprocess.Popen(["adb", "devices"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    object_stdout = p0.stdout.read()
    p0.stdout.close()
    object_stderr = p0.stderr.read()
    p0.stderr.close()
    print(object_stdout)        # 结果：b'List of devices attached \r\n338b123f0504\tdevice\r\n\r\n'
    print(object_stderr)        # 结果：b''

    print("***Popen对象stdin写入功能：使用stdout和stderr输出")
    args = ["python", "python1"]
    for arg in args:
        p4 = subprocess.Popen([arg], shell=True, stdout=subprocess.PIPE,
                              stdin=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        p4.stdin.write("print('hello')")
        p4.stdin.close()
        out = p4.stdout.read()
        p4.stdout.close()
        err = p4.stderr.read()
        p4.stderr.close()
        print("out：%s err：%s" % (out, err))
    """
    ***Popen对象stdin写入功能
    out：hello
    err：
    out： err：'python1' 不是内部或外部命令，也不是可运行的程序或批处理文件。
    """

    print("***Popen对象stdin写入功能：使用communicate输出")
    p4 = subprocess.Popen(["python"], stdout=subprocess.PIPE,
                          stdin=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    p4.stdin.write("print('hello')")
    output = p4.communicate()
    print(output)       # 结果：('hello\n', '')

    print("***不含encoding参数***")
    p1 = subprocess.Popen("adb devices", shell=True, stdout=subprocess.PIPE)
    out1 = p1.stdout.readlines()
    print(out1)         # 结果: [b'List of devices attached \r\n', b'106D111805005938\tdevice\r\n', b'\r\n']

    print("***含encoding参数***")
    p2 = subprocess.Popen("adb devices", shell=True, stdout=subprocess.PIPE, encoding="utf-8")
    out2 = p2.stdout.readlines()
    print(out2)         # 结果: ['List of devices attached \n', '106D111805005938\tdevice\n', '\n']

    print("***Popen对象检查命令是否结束，等待进程结束")
    print(p2.poll())    # 结果: None
    print(p2.wait())    # 结果: 0
    print(p2.poll())    # 结果: 0

    print("***Popen对象communicate函数，它会阻塞父进程直至子进程完成")
    p3 = subprocess.Popen("adb devices", shell=True, stdout=subprocess.PIPE)
    out = p3.communicate()[0]
    print(out)          # 结果：b'List of devices attached \r\n338b123f0504\tdevice\r\n\r\n'
    print(p3.poll())    # 结果：0
subprocess_Popen1()



def subprocess_Popen2():
    """
    1. 通过管道功能，实现adb shell ps | findstr top功能
    2. 直接为args赋值为一个字符串，实现adb shell ps | findstr top功能
    :return:
    """
    print("***通过管道方式***")
    p1 = subprocess.Popen(["adb", "shell", "ps"], stdout=subprocess.PIPE)
    p2 = subprocess.Popen(["findstr", "top"], stdin=p1.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p2.communicate()
    print(out, err)         # 结果：b'shell     8508  8504  2600   1044  c004e5f8 b6f40938 S top\r\r\n' b''
    print("***通过传一个字符串方式***")
    p3 = subprocess.Popen("adb shell ps | findstr top", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p3.communicate()
    print(out, err)         # 结果：b'shell     8508  8504  2600   1044  c004e5f8 b6f40938 S top\r\r\n' b''
subprocess_Popen2()
