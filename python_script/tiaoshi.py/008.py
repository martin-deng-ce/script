def file_write():
    context = input("请输入你的内容:")
    f = open('010.text', 'w')
    f.write(context)
    f.close()
def file_read():
    f = open('010.text', 'r')
    line = f.readline()
    print(line)
    f.close()
if __name__ == '__main__':
     file_write()
     file_read()