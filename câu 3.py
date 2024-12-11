print("Mai Xuân Huy")
print("MSSV:235752021610062")
try:
    with open('D:/vohuy.txt', 'r') as file:  
        content = file.read() 
        print(content) 
except FileNotFoundError:
    print("Tệp không tồn tại. Hãy kiểm tra lại đường dẫn.")
