
#include "iostream"
#include "robot.h"

using namespace std;

int main(){
    Robot r1, r2;
    char id1 = '1';
    char id2 = '2';

    //All robots in x=0 e y=0;
    cout << "Inicialization of r1:" << endl;
    r1.pos[0] = 0;
    r1.pos[1] = 0;
    r1.speed[0] = 0;
    r1.speed[1] = 0;
    r1.showPos(id1);
    cout << "Inicialization of r2:" << endl;
    r2.pos[0] = 0;
    r2.pos[1] = 0;
    r2.speed[0] = 0;
    r2.speed[1] = 0;
    r2.showPos(id2);
    //Changing Parameters r1
    cout << "Moving r1: " <<endl;
    r1.ChangeSpeed(3, 4, id1);
    r2.ChangeSpeed(5, 2, id2);
    r1.move(2);
    r1.showPos(id1);
    r1.move(1);
    r1.showPos(id1); 
    cout << "Moving r2: " << endl;
    r2.move(3);
    r2.showPos(id2);
    r2.move(4);
    r2.showPos(id2);





    return 0;
}