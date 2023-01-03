import time as tm
tm.sleep(1)
print("\n"*130)
print("abc prototype [0.001 alpha test]\nRenato Soft (2023)\n")
vars_name = []
vars_content = []
code = []
current_line = 0
not_error = 0
def write(current_line):
 line = input(str(current_line + 1) + ":")
 if line == "run":
    execute(current_line)
 elif line == "list":
   print("\n"*130)
   for i in range(current_line):
    print(str(i+1)+":"+code[i])
    i = i + 1
 elif line == "cls":
   print("\n"*130)
 elif line == "quit":
   quit()
 else:
  current_line = current_line + 1
  code.append(line)
 write(current_line)
def execute(current_line):
    for i in range(current_line):
     strl = code[i]
     if strl[:3] == "var":
         instances = strl.split()
         vars_name.append(instances[1])
         vars_content.append(instances[3])
     elif strl[:9] == 'print var':
        instances = strl.split()
        index = vars_name.index(instances[2])
        txt = vars_content[index]
        print(txt)
     elif strl[:5] == 'print':
        instances = strl.split()
        txt = instances[1]
        print(txt)
     elif strl[:2] == "//":
         not_error = 0
     else:
      if strl == "" or strl == " " or strl == "   ":
         not_error = 1
      else:
         print("syntax error, line: "+str(i + 1)) 
write(current_line)
