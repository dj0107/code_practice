#include <iostream>

using namespace std;

int main()
{
    bool continued = true;
    int n, k;
    cin >> n >> k;
    int as, ae, bs, be, cs, ce;
    cin >> as >> ae >> bs >> be >> cs >> ce;
    int currentTime = ae;
    for(int i = 0; i < n; i++)
    {
        //breakfast check

        if(currentTime + k < as)
        {
            continued = false;
            break;
        }
        else if(currentTime + k >= as)
        {
            currentTime = min(currentTime + k, ae);
        }
        //lunch check
        if(currentTime + k < bs)
        {
            continued = false;
            break;
        }
        else if(currentTime + k >= bs)
        {
            currentTime = min(currentTime + k, be);
        }
        //dinner check
        if(currentTime + k < cs)
        {
            continued = false;
            break;
        }
        else if(currentTime + k >= cs)
        {
            currentTime = min(currentTime + k, ce);
        }
        //time adjust
        currentTime -= 1440;
    }

    if(continued) {cout << "YES";}
    else if(!continued) {cout << "NO";}
}