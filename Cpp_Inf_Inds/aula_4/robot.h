#ifndef CONTA_H
#define CONTA_H

class Robot{
    public:

        float pos[2];
        float speed[2];
        void showPos(char id);
        void move(float t);
        void ChangeSpeed(float vx, float vy, char idty);

};

#endif