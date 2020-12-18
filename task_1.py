import os
def get_files_count(d):
    os.chdir(d)
    cnt = next(os.walk(os.getcwd()))[2]
    print("Количество файлов: ", len(cnt))

get_files_count(r"C:\Users\Asus\PycharmProjects\pe_lab_4")
