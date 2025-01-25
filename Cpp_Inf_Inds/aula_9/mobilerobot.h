#ifndef MOBILEROBOT_H
#define MOBILEROBOT_H

#include <iostream>
using namespace std;

class MobileRobot{
    private:
        double CurrentPosition[3]; //X, Y e Z
    public:
        double getCurrentPosition(char coord); 
        void setCurrentPosition(double x, double y, double z);
        virtual void Move(double xspeed, double yspeed, double zspeed, double vtim){
            xspeed += 0;
            yspeed += 0;
            zspeed += 0;
            vtim += 0;
        }
};

class TerrRobot : public MobileRobot{
    public:
        TerrRobot();
        void Move (double xspeed, double yspeed, double zspeed, double vtim);
};

class Quadtor : public MobileRobot{
    public:
        Quadtor();
        void Move (double xspeed, double yspeed, double zspeed, double vtim);
};

#endif