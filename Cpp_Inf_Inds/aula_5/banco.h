#ifndef BANCO_H
#define BANCO_H

#include "conta.h"

#define NUMCONTAS 100 //Define que a palavar NUMCONTAS passa a valer como escrever 100

class Banco
{
private:
    Conta *ptr = new Conta [NUMCONTAS]; //Cria um vetor de objetos do tipo Conta que pode armazenar até 100 contas
public:
    Banco();
    ~Banco();
    Conta* buscaConta(int numero); //Metodo que retorna o endereço do objeto conta que possui o mesmo numero informado
    void transferencia (int numc1, int numc2, double valuemandarecebe, int senha1);
    void atendimentoEscolha();
    void atendimentoCliente();
    void atendimentoCadastro();
    void excluiConta(int count, int poscont);
    void excluiContaFixas(int count);
    int buscaContaPOs(int numero);


};


#endif