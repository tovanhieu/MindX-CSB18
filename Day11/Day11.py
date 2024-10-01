#=================STACK===============================
stack = [1,5,6,3,7]
# Them phan tu vao stack ~ push() ~ O(1)
stack.append(9)
# Xem phan tu o dinh stack ~ top()
print(stack[-1])
# Lay phan tu o dinh stack ~ pop() ~ O(1)
top = stack.pop()
# Kiem tra danh sach co rong hay khong
def is_empty(stack):
    if len(stack) == 0:
        return True
    else:
        return False
#In ra do dai cua stack
print(len(stack))
#==========================Thuc hanh===================

class Browser:
    def __init__(self) -> None:
        self.back_stack = []
        self.forward_stack = []
    
    def visit_page(self, url):
        self.back_stack.append(url)
        self.forward_stack.clear()
        print(f"Visiting: {url}")
    
    def back(self):
        if len(self.back_stack) > 1:
            current_page = self.back_stack.pop()
            self.forward_stack.append(current_page)
            previous_page = self.back_stack[-1]
            print(f"Going back to: {previous_page}")
        else:
            print("Cannot go back")

    def forward(self):
        if self.forward_stack:
            next_page = self.forward_stack.pop()
            self.back_stack.append(next_page)
            print(f"Going forward to: {next_page}")
        else:
            print("Cannot go forward")

browser = Browser()
browser.visit_page("google.com")
browser.visit_page("dantri.com")
browser.visit_page("facebook.com")

browser.back()
browser.back()
browser.back()

browser.forward()
browser.forward()
browser.forward()



    
