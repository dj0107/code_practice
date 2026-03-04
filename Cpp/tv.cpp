#include <iostream>
#include <string>
using namespace std;

class TV
{
public:
    TV (int channel, int volume);
    int getchannel() const {return channel;};

private:
    int channel, volume;
};

double& dd() {
    double d = 5.0;
    return d;
}

int main() {
    string a, b;
    getline(cin, a) >> b;
    cout << a << b << endl;
}

TV::TV(int channel, int volume) : channel(channel), volume(volume) {}
// int TV::getchannel() const 
// {
//     return channel;
// }