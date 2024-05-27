#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <thread>
#include <mutex>

struct ThreadData
{
    int pInicial;
    int pFinal;
    std::vector<int> caminho;
    int valorAresta;
};

int qtde = 0;
int menorValor = INT_MAX;
std::string caminhoMaisRapido;
std::vector<std::vector<int>> matriz;
std::mutex mtx;
std::vector<std::thread> threads;

void acharCaminho(ThreadData *data)
{
    int pInicial = data->pInicial;
    int pFinal = data->pFinal;
    std::vector<int> caminho = data->caminho;
    int valorAresta = data->valorAresta;
    delete data;

    if (pInicial == pFinal)
    {
        caminho.push_back(pInicial);
        std::string caminhoStr = std::to_string(caminho[0] + 1);
        for (size_t i = 1; i < caminho.size(); i++)
        {
            caminhoStr += " -> " + std::to_string(caminho[i] + 1);
        }

        std::lock_guard<std::mutex> lock(mtx); 
        if (menorValor > valorAresta)
        {
            menorValor = valorAresta;
            caminhoMaisRapido = caminhoStr;
        }
        qtde++;
        std::cout << caminhoStr << ": " << valorAresta << "\n";
        return;
    }

    for (int i = 0; i < matriz.size(); i++)
    {
        int valor = matriz[pInicial][i];
        if (std::find(caminho.begin(), caminho.end(), i) == caminho.end() && valor > 0)
        {
            ThreadData *newData = new ThreadData{i, pFinal, caminho, valorAresta + valor};
            newData->caminho.push_back(pInicial);
            std::thread(acharCaminho, newData).detach();
        }
    }
}

std::vector<std::vector<int>> iniciarMatriz()
{
    int numRange;
    std::cout << "range: ";
    std::cin >> numRange;
    std::vector<std::vector<int>> lista(numRange, std::vector<int>(numRange, 0));
    return lista;
}

int main()
{
    while (true)
    {
        int escolha;
        std::cout << "\n1: Iniciar a Matriz\n2: Mostrar a Matriz\n3: Editar a Matriz\n4: Números Aleatórios\n5: Achar caminho\n6: Excluir a Matriz\n";
        std::cin >> escolha;

        if (escolha == 1)
        {
            matriz = iniciarMatriz();
        }
        else if (escolha == 2 && !matriz.empty())
        {
            for (const auto &row : matriz)
            {
                for (int value : row)
                {
                    std::cout << value << " ";
                }
                std::cout << "\n";
            }
        }
        else if (escolha == 3 && !matriz.empty())
        {
            char orientadoBool;
            std::cout << "É orientado ou não? (Y/N) ";
            std::cin >> orientadoBool;
            int arestas;
            std::cout << "Quantas arestas?\n";
            std::cin >> arestas;
            for (int i = 0; i < arestas; i++)
            {
                int x, y, valor;
                std::cout << "Índices e valor: ";
                std::cin >> x >> y >> valor;
                x--;
                y--;
                if (x == y)
                {
                    std::cout << "Os índice não podem ser iguais\n";
                }
                else
                {
                    matriz[x][y] = valor;
                    if (orientadoBool != 'Y')
                    {
                        matriz[y][x] = valor;
                    }
                }
            }
        }
        else if (escolha == 4 && !matriz.empty())
        {
            int lenght = matriz.size();
            for (int i = 0; i < lenght; i++)
            {
                for (int j = 0; j < lenght; j++)
                {
                    if (i != j)
                    {
                        matriz[j][i] = rand() % 10;
                    }
                }
            }
        }
        else if (escolha == 5 && !matriz.empty())
        {
            int pInicial, pFinal;
            std::cout << "Ponto inicial: ";
            std::cin >> pInicial;
            std::cout << "Ponto final: ";
            std::cin >> pFinal;
            pInicial--;
            pFinal--;
            std::vector<int> caminho = {pInicial};

            ThreadData *data = new ThreadData{pInicial, pFinal, caminho, 0};
            acharCaminho(data);

            std::this_thread::sleep_for(std::chrono::seconds(1));

            std::cout << "De " << qtde << " repetições, o caminho mais rápido é " << caminhoMaisRapido << " com valor " << menorValor << "\n";
        }
        else if (escolha == 6 && !matriz.empty())
        {
            matriz.clear();
            std::cout << "Matriz apagada\n";
        }
        else
        {
            if (matriz.empty())
            {
                std::cout << "Inicialize a matriz\n";
            }
            else
            {
                std::cout << "Escolha uma opção válida\n";
            }
        }
    }

    return 0;
}
