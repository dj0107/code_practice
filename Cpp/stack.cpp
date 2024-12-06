#include <iostream>
using namespace std;

class Stack
{
public:
    Stack()
    {
        size = 10;

    }
    Stack(int newsize)
    {
        size = newsize;
    }
    int getSize() {return size;}
private:
    int size;
    int* stk = new int(size);
    


};

int main()
{

}