print("Mai Xuân Huy")
print("MSSV:235752021610062")
def file_read(fname):
    
    with open(fname, "a") as myfile:
        # Nối văn bản vào tệp
        myfile.write("Python Exercises\n")
        myfile.write("Java Exercises\n")
    
    with open(fname, "r") as myfile:
        # Đọc và hiển thị toàn bộ nội dung tệp
        print(myfile.read())

# Gọi hàm để thực hiện chức năng
file_read('xyz.txt')
