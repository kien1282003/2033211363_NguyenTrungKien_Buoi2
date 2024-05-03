from ._anvil_designer import Form1Template
from anvil import *

class Form1(Form1Template):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run before the form opens.
        self.text_box_1.visible = False  # Ẩn TextBox1 ban đầu

    def button_1_click(self, **event_args):
        """This method is called when the "Nhập" button is clicked"""
        # Hiển thị TextBox1 khi nhấn nút "Nhập"
        self.text_box_1.visible = True
        # Focus vào TextBox1 để người dùng có thể nhập liệu ngay lập tức
        self.text_box_1.focus()

    def button_2_click(self, **event_args):
        """This method is called when the "Sắp xếp tăng" button is clicked"""
        # Lấy dãy số từ TextBox1 và chuyển thành danh sách các số nguyên
        numbers = [int(num) for num in self.text_box_1.text.split()]
        
        # Thực hiện sắp xếp dãy số bằng thuật toán Insertion Sort
        sorted_numbers = self.insertion_sort(numbers)
        
        # Hiển thị dãy số đã sắp xếp tăng dần trong TextBox2
        self.text_box_2.text = ' '.join(map(str, sorted_numbers))
        # Ẩn TextBox1 sau khi đã nhập và hiển thị kết quả
        self.text_box_1.visible = False

    def button_3_click(self, **event_args):
        """This method is called when the "Sắp xếp giảm" button is clicked"""
        # Lấy dãy số từ TextBox1 và chuyển thành danh sách các số nguyên
        numbers = [int(num) for num in self.text_box_1.text.split()]
        
        # Thực hiện sắp xếp dãy số bằng thuật toán Insertion Sort và đảo ngược
        sorted_numbers = self.insertion_sort(numbers)
        
        # Hiển thị dãy số đã sắp xếp giảm dần trong TextBox3
        self.text_box_3.text = ' '.join(map(str, sorted_numbers[::-1]))
        # Ẩn TextBox1 sau khi đã nhập và hiển thị kết quả
        self.text_box_1.visible = False

    def insertion_sort(self, arr):
        # Thuật toán sắp xếp chèn
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr

    def text_box_1_pressed_enter(self, **event_args):
      """This method is called when the user presses Enter in this text box"""
      pass

    def text_box_2_pressed_enter(self, **event_args):
      """This method is called when the user presses Enter in this text box"""
      pass

    def text_box_3_pressed_enter(self, **event_args):
      """This method is called when the user presses Enter in this text box"""
      pass
