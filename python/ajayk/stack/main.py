# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import stackFromLinkList;

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    mystack = stackFromLinkList.StackLinker();
    mystack.push(10);
    mystack.push(20);
    mystack.push(30);
    print(mystack.pop());
    print(mystack.pop());
    print(mystack.pop());
    print(mystack.pop());
    mystack.push(50);
    mystack.push(70);
    mystack.push(100);
    print(mystack.pop());
    mystack.push(-10);
    print(mystack.pop());
    print(mystack.pop());
    print(mystack.pop());




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
