import pyAesCrypt
import os


def Encryption(file, password):
    buffer = 512*1024

    pyAesCrypt.encryptFile(
    str(file),
    str(file) + '.crp',
    buffer,
    password
    )

def walking_by_dir(dir, password):
    for name in os.listdir(dir):
        path = os.path.join(dir, name)

        if os.path.isfile(path):
            try:
                 Encryption(path, password)
            except Exception as ex:
                print(ex)
        else:
             walking_by_dir(path, password)

password = input('Enter your password:')
walking_by_dir('!!!!!Write here file directory!!!!!', password)


# Decription



# import pyAesCrypt
# import os
#
# 
# def Encryption(file, password):
#     buffer = 512*1024
#
#     pyAesCrypt.encryptFile(
#     str(file),
#     str(file) + '.crp',
#     buffer,
#     password
#     )
#
# def walking_by_dir(dir, password):
#     for name in os.listdir(dir):
#         path = os.path.join(dir, name)
#
#         if os.path.isfile(path):
#             try:
#                  Encryption(path, password)
#             except Exception as ex:
#                 print(ex)
#         else:
#              walking_by_dir(path, password)
#
# password = input('Enter your password:')
# walking_by_dir('!!!!!Write here file directory!!!!!', password)