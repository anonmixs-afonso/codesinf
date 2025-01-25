#include "conta.h"
#include <iostream>

Conta::Conta()
{
    this->numero = 0;
    this->senha = 1111;
    this->titular = "Nenhum";
    this->saldo = 0;
}

Conta::Conta(int senha, int numero, std::string titular, std::string tipo, double saldo)
{
    this->senha = senha;
    this->numero = numero;
    this->titular = titular;
    this->tipo = tipo;
    if(saldo>0)
    {
        this->saldo = saldo;
    }
    else
    {
        std::cout<<"Saldo inicial invalido"<<std::endl;
    }    
}

Conta::~Conta()
{
    std::cout << "Destruiu Conta." << std::endl;
}

void Conta::exibeDados()
{
    std::cout<< "Titular: "<<this->titular<<std::endl;
    std::cout<< "Numero: "<<this->numero<<std::endl;
    std::cout<< "Tipo: "<<this->tipo<<std::endl;
}

double Conta::getSaldo(int senha)
{

    switch ((int)(senha==this->senha)) {
        case 1 :
        return this -> saldo;
        break;
        case 0:
        return -4;
    }
  return 0;
   
}

double Conta::Validasaida(int retorno)
{
    if (retorno == -2)
    {
        std::cout << "Saldo insuficiente!" << std::endl;
    }
    if (retorno == -3)
    {
        std::cout << "Senha Errada!" << std::endl;
    }
    if (retorno == -4)
    {
        std::cout << "Valor Inválido!" << std::endl;
    }
    if (retorno == -5)
    {
        std::cout << "Depósito Efetuado Com Sucesso!" << std::endl;
    }
    if (retorno > 0)
    {
        return retorno;
    }
    return 0;
}

double Conta::setSaldo(double valor)
{
    if(valor>0)
        return this->saldo = valor;
    else
        return -1;
}

void Conta::setSenha(int novaSenha)
{
    this->senha = novaSenha;
}

double Conta::deposito(double valor)
{
    if(valor>0)
    {
        return this->saldo+=valor;
    }
    else
    {
        return -4;
    }
    
}

double Conta::saque(int senha, double valor)
{
    if(senha==this->senha)
    {
        if(this->saldo>=valor)
        {
            this->saldo-=valor;
            return -5;
        }
        else
        {
            return -2;
        }    
    }
    else
    {
        return -3;
    }
    
}

bool Conta::validaSenha(int senha)
{
    return (this->senha == senha);   
}

