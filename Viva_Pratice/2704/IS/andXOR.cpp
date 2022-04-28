#include <iostream>

using namespace std;

int main(){
    string x = "Hello World";
    for (int i = 0; i < x.length(); i++)
    {
        cout<< char(x[i] & 127);
    }
    cout <<endl;
    for (int i = 0; i < x.length(); i++)
    {
        cout<< char(x[i] ^ 127);
    }
    cout <<endl;
    
    return 0;
}