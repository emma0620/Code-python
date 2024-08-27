#編號：CANDY-021
#程式語言：Python
#題目：實作 Stack 資料結構

class Stack :
  def __init__(data):
    data.num_item = []

  def push(data, item=None):
    if data is not None:
       data.num_item.append(item)

    def pop(data):
      if data.is_empty():
        raise IndexError("pop from empty stack")
      return data.num_item.pop()

    def is_empty(data):
     return len(data.num_item)==0

    def size(data):
      return len(data.num_item)

#測試代碼

if __name__="__main__":
    stack = Stack()
    stack.push(123)
    stack.push(456)
    stack.push(); #試圖推入一個 undefined
    print(stack.size) #應該印出 2

    item = stack.pop(); #取出元素
    print(item); #應該印出 456

    stack.pop(); #繼續取出元素
    print(stack.size); #應該印出 0