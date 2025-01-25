#ifndef CONTA_H
#define CONTA_H
#include <string>


class Conta
{
private:
    double saldo;
    int senha;
public:
    Conta();
    Conta(int senha, int numero, std::string titular, std::string tipo, double saldo);
    ~Conta();
    int numero;
    std::string titular;
    std::string tipo;
    void exibeDados();
    double getSaldo(int senha);
    double setSaldo(double valor);
    void setSenha(int novaSenha);
    double deposito(double valor);
    double saque(int senha, double valor);
    bool validaSenha(int senha);
    double Validasaida(int retorno);


};


#endif