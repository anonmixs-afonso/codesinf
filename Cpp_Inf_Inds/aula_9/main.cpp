#include "mobilerobot.h"
#include <cstdlib>
#include <ctime>

void ExecutaMovimento(MobileRobot *ptr){
    std::srand(std::time(0));
    
    double speed = std::rand() % 201; // % 201 to ensure the number is between 0 and 200
    double xspeed = speed*(1.35);
    double yspeed = speed*(0.15);
    double zspeed = speed*(2.78);
    long int time = (long int)speed/(long int)5;

    cout << "Sorted Speeds: " << endl;
    cout << "Xspe: " << xspeed << endl;
    cout << "Yspe: " << yspeed << endl;
    cout << "Zspe: " << zspeed << endl;
    cout << "Time of path: " << time << " seconds." << endl << endl;

    ptr->Move(xspeed, yspeed, zspeed,(double)time);

    
}

int main (){
    TerrRobot t1;
    Quadtor q1;
    cout << "Moviment of terrestrial vehicles..." << endl;
    ExecutaMovimento(&t1);
    cout << "Moviment of drone..." << endl;
    ExecutaMovimento(&q1);



    // t1.Move(2, 3, 0,2);
    // q1.Move(2, 3, 4, 5);
    return 0;
}