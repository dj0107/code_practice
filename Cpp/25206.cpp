#include <iostream>
#include <string>
using namespace std;

const int N = 20;

double addTotal(const double weight, const string score) 
{
    if (score == "A+") {return (weight * 4.5);}
    else if (score == "A0") {return (weight * 4.0);}
    else if (score == "B+") {return (weight * 3.5);}
    else if (score == "B0") {return (weight * 3.0);}
    else if (score == "C+") {return (weight * 2.5);}
    else if (score == "C0") {return (weight * 2.0);}
    else if (score == "D+") {return (weight * 1.5);}
    else if (score == "D0") {return (weight * 1.0);}
    else {return 0;} // F거나 P일 경우, 총 성적에 더하지 않음

    return 0;
}

double getFinalScore(const double weightSum, const double totalSum)
{
    return (totalSum / weightSum);
}



int main() 
{
    string name, score;
    double weight, weightSum, totalSum = 0;
    
    for (int i = 0; i < N; i++)
    {
        //입력 받기
        cin >> name >> weight >> score;

        //총 이수 학점 더하기(weightSum)
        if (score != "P")
        {
        weightSum += weight;
        }

        //최종 성적 더하기(totalSum)
        totalSum += addTotal(weight, score);
    }

    cout << getFinalScore(weightSum, totalSum) << endl;


    return 0;
}