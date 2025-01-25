#include "mobilerobot.h"
#include <iostream>
using namespace std;

double MobileRobot::getCurrentPosition(char coord){
    if (coord == 'x'){
        return this->CurrentPosition[0];        
    }

    if (coord == 'y'){
        return this->CurrentPosition[1];        
    }

    if (coord == 'z'){
        return this->CurrentPosition[2];        
    }

    return -1;
}

void MobileRobot::setCurrentPosition (double x, double y, double z){
    this->CurrentPosition[0] = x;
    this->CurrentPosition[1] = y;
    this->CurrentPosition[2] = z;
}

TerrRobot::TerrRobot(){
    this->setCurrentPosition(0, 0, 0);
}

void TerrRobot::Move(double xspeed, double yspeed, double zspeed, double vtim){
    cout << "Ativating Whells..." << endl;
    cout << "Position Before Move: " << endl;
    cout << "X: " << this->getCurrentPosition('x') << endl;
    cout << "Y: " << this->getCurrentPosition('y') << endl;
    cout << "Z: " << this->getCurrentPosition('z') << endl << endl;
    cout << "Position After Move: " << endl;
    this->setCurrentPosition(xspeed*vtim, yspeed*vtim, zspeed*0);
    cout << "X: " << this->getCurrentPosition('x') << endl;
    cout << "Y: " << this->getCurrentPosition('y') << endl;
    cout << "Z: " << this->getCurrentPosition('z') << endl;
}

Quadtor::Quadtor(){
    this->setCurrentPosition(0, 0, 0);
}

void Quadtor::Move(double xspeed, double yspeed, double zspeed, double vtim){
    cout << "Ativating Propellers..." << endl;
    cout << "Position Before Move: " << endl;
    cout << "X: " << this->getCurrentPosition('x') << endl;
    cout << "Y: " << this->getCurrentPosition('y') << endl;
    cout << "Z: " << this->getCurrentPosition('z') << endl << endl;
    cout << "Position After Move: " << endl;
    this->setCurrentPosition(xspeed*vtim, yspeed*vtim, zspeed*vtim);
    cout << "X: " << this->getCurrentPosition('x') << endl;
    cout << "Y: " << this->getCurrentPosition('y') << endl;
    cout << "Z: " << this->getCurrentPosition('z') << endl;
}
