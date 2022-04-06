//---DESCRIPTION---//
/*
Stacks are a type of container adaptors with LIFO, where a new element is added at one end (top) and an element is removed from that end only.
Stack uses an encapsulated object of either vector, deque (default), or list.
This is its underlying container, providing a specific set of member functions to access its elements.

To create a stack, must inlcude the stack header
Use this syntax to define the std::stack

    template<class Type, class Container=deque<Type>> class stack;

    Type - the type of element contained in the std::stack
        This can be any valid C++ type or even a user-defined type
    Container - the type of underlying container object

The functions associated with stack are:
    empty() - returns whether stack is empty. Time Complexity: O(1)
    size() - returns stack size. Time Complexity: O(1)
    top() - returns reference to the top stack element. Time Complexity: O(1)
    push(g) - adds element g to top of stack. Time Complexity: O(1)
    pop() - deletes the top stack element. Time Complexity: O(1)

*/

//---CODE EXAMPLE---//
#include <iostream>
#include <stack>

using namespace std;
int main() 
{
    stack<int> stack;
    stack.push(21);
    stack.push(22);
    stack.push(24);
    stack.push(25);

    while (!stack.empty()){
        cout << ' ' << stack.top();
        stack.pop();
    }

}