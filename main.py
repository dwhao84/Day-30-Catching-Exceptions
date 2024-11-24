# FileNotFound
from sys import modules
from typing import reveal_type
from zipfile import error

try:
    file = open("a_file.txt")
    a_dictionary = {"key":"value"}
    print(a_dictionary["sdfsdf"])

# 在FileNotFoundError機制處理找不到a_file.txt，因此用except建立處理機制，建立一個file。
except FileNotFoundError:
    print("File Not Found Error")
    file = open("a_file.txt", mode='w')

# 在這個地方找到KeyError的地方，並印出結果。
except KeyError as error_message:
    print(f"The key { error_message } does not exist.")

else:
    content = file.read()
    print(content)

finally:
    file.close() # 檔案關閉，讓記憶體釋放。
    print("File was closed")
    raise  TypeError # 提出一個例外
