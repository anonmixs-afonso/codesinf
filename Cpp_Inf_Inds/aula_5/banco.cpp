#include "banco.h"
#include "conta.h"
#include <iostream>

using namespace std;

Banco::Banco() //O construtor criara 4 contas
{
    this->ptr[0] = Conta(1234, 1, "Joao", "Corrente", 300);
    this->ptr[1] = Conta(4567, 2, "Jose", "Poupanca", 800);
    this->ptr[2] = {7890, 3, "Maria", "Corrente", 1000};
    this->ptr[3] = {8956, 4, "Madalena", "Poupanca", 2000};
}

Banco::~Banco()
{
    cout << "Destruiu Banco." <<endl;
}

void Banco::transferencia (int numc1, int numc2, double valuemandarecebe, int senha1)
{
    Conta* contamanda;
    Conta* contarecebe;

    contamanda = this->buscaConta(numc1);
    contarecebe = this->buscaConta(numc2);

    if (contamanda->saque(senha1, valuemandarecebe) != -2)
    {
        contarecebe->Validasaida(contarecebe->deposito(valuemandarecebe));
    }
    else 
    {
        cout << "Saldo Insuficiente." << endl;
    }
    cout << "A conta de saque tem: " << contamanda->Validasaida(contamanda->getSaldo(senha1)) << endl;
}

Conta *Banco::buscaConta(int numero)//Retorna o endereço da conta que possuir o mesmo numero informado
{
    for (int i = 0; i < NUMCONTAS; i++)
    {
        if (numero == this->ptr[i].numero)
        {
            return &this->ptr[i];
        }
    }

    return nullptr;
}


int Banco::buscaContaPOs(int numero)//Retorna o endereço da conta que possuir o mesmo numero informado
{
    for (int i = 0; i < NUMCONTAS; i++)
    {
        if (numero == this->ptr[i].numero)
        {
            return i;
        }
    }

}

void Banco::excluiConta(int cont, int poscont){
    Conta *paux = new Conta [cont+4];
    for (int i = 0; i < cont + 4; i++){
        if (i == poscont){
            continue;
        }
        paux[i] = ptr[i];
    }
    delete [] ptr;
    ptr = paux;


}

void Banco::excluiContaFixas(int poscont){
    Conta *paux = new Conta [4];
    for (int i = 0; i < 4; i++){
        if (i == poscont){
            continue;
        }
        paux[i] = ptr[i];
    }
    delete [] ptr;
    ptr = paux;
}

void Banco::atendimentoEscolha()
{
    int escolha;
    cout << "Para Acessar Conta Tecle '1' (clientes): " <<endl;
    cout << "Para Cadastrar Clientes tecle '2' (funcionários apenas): " <<endl;
    cin >> escolha;
    if (escolha == 1)
    {
        atendimentoCliente();
    }
    if (escolha == 2)
    {
        atendimentoCadastro();
    }

}

void Banco::atendimentoCadastro()
{
    int cont = 0;
    char contcad;
    char cadex;
    char ec2;
    int senha;
    int numc;
    float saldo;
    std::string nome;
    std::string tipodaconta;
    cout << "Para Cadastrar uma Nova Conta Digite 'c', Para Excluir uma Conta Digite 'e': " << endl;
    cin >> cadex;
    if (cadex == 'c'){
        cout << "Cadastro de Novos Usuários ao Banco **APENAS FUNCIONÁRIOS DO DEP. BANCÁRIO**" << endl;
        while (contcad != 'n'){ 
            cont++;
            cout << "Senha: " << endl;
            cin >> senha;
            cout << "Número da conta: " << endl;
            cin >> numc;
            cout << "Saldo: " << endl;
            cin >> saldo;
            cout << "Nome do Titular: " << endl;
            cin >> nome;
            cout << "Tipo da Conta: " << endl;
            cin >> tipodaconta;
            this->ptr[cont + 3] = Conta(senha, numc, nome, tipodaconta, saldo);
            cout << "Cadastrar Nova Conta? s/n: ";
            cin >> contcad;
        }
        cout << "Deseja Excluir Alguma das Novas Contas Cadastradas?(s/n): " << endl;
        cin >> ec2;
        if (ec2 == 's'){
            int numcont;
            int pos;
            cout << "Digite o Número da Conta a Ser Exluída" << endl;
            cin >> numcont;
            pos = buscaContaPOs(numcont);
            Banco::excluiConta(cont, pos);
            cout << "Pos da conta: " << pos << endl;
            Banco::atendimentoCliente();

        }
        else{
            Banco::atendimentoCliente();
        }
    }
    else{
        int numcont;
        int pos;
        cout << "Digite o Número da Conta a Ser Exluída" << endl;
        cin >> numcont;
        pos = buscaContaPOs(numcont);
        Banco::excluiContaFixas(pos);
        cout << "Pos da conta: " << pos << endl;
        atendimentoCliente();
    }
   
}


void Banco::atendimentoCliente() //Realiza o atendimento ao cliente(Função chamada na main)
{
    Conta *contaCliente;
    int numC = 0;
    int senhain;
    bool atendimento = true;

    cout << "Bem vindo ao sistema de atendimento do banco" << endl;
    cout << "Digite o numero da sua conta: ";
    cin >> numC;

    contaCliente = this->buscaConta(numC); //Chama o Metodo buscaConta() do banco para achar o objeto conta que possui o numero numC

    if (contaCliente == nullptr)//Se não achar nenhuma conta que corresponda entra nesse if
    {
        cout << "Conta invalida" << endl;
    }
    else
    {
        cout << "Digite a sua senha: ";
        cin >> senhain;

        if (contaCliente->validaSenha(senhain))
        {
            cout << "Ola " << contaCliente->titular << endl;
            while (atendimento) //Realiza o atendimento
            {
                int op;
                double valor;
                cout << "Qual operacao deseja fazer? (1 - Saque, 2 - Deposito, 3 - Ver Saldo, 4 - Transferência, 5 - Sair): ";
                cin >> op;
                switch (op)
                {
                case 1:
                    cout << "Digite o valor: ";
                    cin>>valor;
                    contaCliente->Validasaida(contaCliente->saque(senhain,valor));
                    break;
                case 2:
                    cout << "Digite o valor: ";
                    cin>>valor;
                    contaCliente->Validasaida(contaCliente->deposito(valor));
                    break;
                case 3:
                    cout << "Saldo: R$ "<<contaCliente->Validasaida(contaCliente->getSaldo(senhain))<<endl;
                    break;
                case 4:
                    int num1;
                    int num2;
                    float value;
                    cout << "Digite o número da conta de transferência: " <<endl;
                    cin >> num1;
                    cout << "Digite o número da conta de recebimento: " <<endl;
                    cin >> num2;
                    cout << "Digite o valor a ser transferido: " <<endl;
                    cin >> value;
                    transferencia(num1, num2, value, senhain);
                    break;
                case 5:
                    atendimento = false;
                    break;
                }
            }
        }
        else
        {
            cout << "Senha invalida" << endl;
        }
    }
}
