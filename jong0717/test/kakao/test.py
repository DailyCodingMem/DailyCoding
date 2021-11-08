   
# import copy

# # 구분 비트 선언
# STBIT = '0x530x54'
# ENBIT = '0x450x4e'


# def createDataArr(arr, line, data):
#     print(len(line))
#     if len(line) != 80:
#         line.append(int(data, 16))
#     else:
#         arr.append(line)
#         line = []
#         print(len(line))


# #  데이터 읽어오기(USB or file)
# print(createDataArr())

# # datacheck = False
# # fileSize = 8
# arr = []
# line = []
# # while True:
# #     data = f.read(fileSize)
# #     if not data: break

# #     if datacheck:
# #         createDataArr(arr, line, data)

# #     if data == STBIT :
# #         datacheck = True
# #         fileSize = 4

# #     if data == ENBIT :
# #         datacheck = False
# #         fileSize = 8

# print(arr)



import tkinter as tk


root = tk.Tk()
root.geometry("400x240")

textExample=tk.Text(root, height=10)
textExample.pack()

textExample.configure(font=("Blackadder ITC", 16,))

root.mainloop()



