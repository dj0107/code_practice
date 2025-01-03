#include <iostream>
#include <string>
#include <vector>
//#include <cmath>
using namespace std;

int main() 
{
    int n;
    cin >> n;

    vector<string> trash(n);

    for (int i = 0; i < n; i++)
    {
        cin >> trash[i];
    }

    int p, c, v, s, g, f, o;
    cin >> p >> c >> v >> s >> g >> f;
    cin >> o;

    p = min(p, o);
    c = min(c, o);
    v = min(v, o);
    s = min(s, o);
    g = min(g, o);
    f = min(f, o);

    long long total = 0;
    for(int i = 0; i < n; i++)
    {
        bool recycle = true;
        for(int j = 1; j < trash[i].size(); j++) // figure recyclability
        {
            if(trash[i][j] != trash[i][j - 1]) {recycle = false;} //if 2 or more ingredients are mixed
        }
        if(trash[i][0] == 'O') {recycle = false;} // if O, it is non-recyclable

        if(recycle == true)
        {
            if(trash[i][0] == 'P')
            {
                total += trash[i].size() * p;
            }
            else if(trash[i][0] == 'C')
            {
                total += trash[i].size() * c;
            }
            else if(trash[i][0] == 'V')
            {
                total += trash[i].size() * v;
            }
            else if(trash[i][0] == 'S')
            {
                total += trash[i].size() * s;
            }
            else if(trash[i][0] == 'G')
            {
                total += trash[i].size() * g;
            }
            else if(trash[i][0] == 'F')
            {
                total += trash[i].size() * f;
            }
        }
        else if(recycle != true) {total += trash[i].size() * o;}

    }

    cout << total << endl;
}