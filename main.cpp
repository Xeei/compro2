
#include <iostream>

using namespace std;

class TestClass
{
public:
    string p1;

private:
    string pp;
};

int main()
{
    TestClass obj1;
    obj1.p1 = "Helloooo";
    cout << obj1.p1 << endl;
    cout << "Hiiiiiiiiiii" << endl;
    return 0;
}