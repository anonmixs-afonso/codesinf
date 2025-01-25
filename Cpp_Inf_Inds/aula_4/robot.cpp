#include "iostream"
#include "robot.h"

using namespace std;

void Robot::showPos (char id){

    cout << "ID: " << id << ", POSX: " << this->pos[0] << "m" << endl;
    cout << "ID: " << id << ", POSY: " << this->pos[1] << "m" << endl;

}

void Robot::ChangeSpeed(float vx, float vy, char idty){
    this->speed[0] = vx;
    this->speed[1] = vy;
    cout <<"ID: " << idty << ", New Speeds: vx = " << speed[0] << "m/s, vy = " << speed[1] << "m/s" << endl;
}

void Robot::move (float t){
    float deltadx = 0;
    float deltady = 0;
    deltadx = (this->speed[0])*(t);
    deltady = (this->speed[1])*(t);
    this->pos[0] += deltadx;
    this->pos[1] += deltady;
}