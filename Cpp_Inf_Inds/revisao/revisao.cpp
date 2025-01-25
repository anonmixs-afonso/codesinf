#include <iostream>
#include <string.h>  

using namespace std;
/*
struct pessoa{
    char nome[100];
    int idade;
};
*/
// struct pessoa p1; Em c++ pode-se usar pessoa p1 em ambos os casos


typedef struct{
    char nome[100];
    int idade;
}pessoa;

//pessoa p1;

int main (){
    /////////////////////////Ponteiros///////////////////////////////
    int vet [] = {1,2,3,4,5};
    //vet (nome apenas) é o ponteiro para a 
    //primeira posição do bloco de memória associado ao vetor
    cout << "Antes da mudança do valor vet[0]: " << vet[0] << endl;
    *vet = 2;// == *(vet + 0) = 2; 
    cout << "Depois da mudança 1: " << *vet << endl;
    *(vet + 1) = 3;
    cout << "Depois da mudança 2: " << *(vet+1) << endl;
    /////////////////////////////////////////////////////////////////

    ///////////////////////Struct////////////////////////////////////
    pessoa p1 = {"Anon", 20};
    cout << "Nome: " << p1.nome << "\nIdade: " << p1.idade << endl;
    strcpy(p1.nome, "Anonmixs Amaro Afonso");
    p1.idade = 23;
    cout << "Nome: " << p1.nome << "\nIdade: " << p1.idade << endl;

    return 0;
}