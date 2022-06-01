def GaussSeidel(matriz):  
        for i in range(len(matriz)):
            try:
                matriz[i] = [elemento/matriz[i][i] for elemento in matriz[i]] ## DIVINDO OS ELEMENTOS DA LINHA PELO SEU NUMERO NA DIAGONAL PRINCIPAL
            except ZeroDivisionError: ## SE ALGUM VALOR DA DIAGONAL PRINCIPAL ZERAR, SIGUINIFICA QUE O MÉTODO GAUSS-SIDEL NÃO É VALIDO NESTE CASO.
                print('Matriz possue equacoes impossiveis e/ou redundantes, logo, não pode ser determinada')
                return "Não existente"
            for j in range(len(matriz)):    
                if i != j and matriz[j][i] != 0: ##CERTIFICANDO QUE NÃO MEXEREMOS NA DIAGONAL PRINCIPAL OU EM UM NUMERO QUE JÁ ESTÁ ZERADO
                    pivo =  [elemento*-matriz[j][i] for elemento in matriz[i]]## MULTIPLICANDO OS ELEMENTOS DA LINHA PELO NEGATIVO DO NUMERO QUE QUEREMOS ZERAR
                    matriz[j] = [matriz[j][k]+pivo[k] for k in range(len(matriz[j]))] ## SOMANDO PIVO COM A LINHA QUE QUEREMOS ZERAR
        return [equacao[-1] for equacao in matriz] ## RETORNANDO LISTA CONTENDO CONJUNTO SOLUÇÃO
                      
GaussSeidel_possivel = True           
           
tam_eq = int(input("Quantas equações o sistema possue? ")) ## CRIANDO A MATRIZ A PARTIR DE INPUTS
matriz = [[] for n in range(tam_eq)]
for linha in range(tam_eq):
        for variavel in range(tam_eq):
            valor = int(input(f'Digite o valor de x{variavel + 1} da {linha + 1}ª equação: '))
            matriz[linha].append(valor)
        equidade = int(input(f"Digite a equidade da {linha + 1}ª equação: "))
        matriz[linha].append(equidade)

print(f'Sistema transformado em matriz: {matriz}')
           
for i in range(len(matriz)): 
    if matriz[i][i] == 0: ## CHECANDO SE EXISTEM ZEROS NA DIAGONAL PRINCIPAL
        GaussSeidel_possivel = False

if GaussSeidel_possivel:
    print(f"Vetor solução: {GaussSeidel(matriz)}")
else:
    print('Método GaussSeidel impossível com a forma da matriz apresentada')




