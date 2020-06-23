import  base64


old = base64.b64encode('doctor_web:'.encode('utf-8'))
new=str(old, 'utf-8')
print(new)

