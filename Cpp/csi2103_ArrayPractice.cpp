//not completed

#include <iostream>
#include <vector>
#include <string>
using namespace std;

class ScoreBoard
{
public:
    ScoreBoard() {} // sorted by score from high to low
    void addEntry(string name, int score)
    {
        scoreBoardArr.push_back(GameEntry(name, score));
        int n = scoreBoardArr.size() - 1;
        while(scoreBoardArr[n].getScore() >
        scoreBoardArr[n - 1].getScore())
        {
            GameEntry temp = scoreBoardArr[n];
            scoreBoardArr[n] = scoreBoardArr[n - 1];
            scoreBoardArr[n - 1] = temp;
            if(n >= 1) {n--;}
        }
    }
    void removeEntry(int index)
    {

    }
private:
    vector<GameEntry> scoreBoardArr;
    
};

class GameEntry
{
public:
    GameEntry(string name, int score)
    {
        this->name = name;
        this->score = score;
    }
    string getName() {return name;}
    int getScore() {return score;}
    //소멸자는 다음에 추가해보기
private:
    string name;
    int score;
};