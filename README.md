# Simulação Epidemiológica com Autômatos Celulares

## Descrição

Este projeto implementa um modelo de simulação epidemiológica baseado no modelo SIR (Susceptíveis, Infectados, Recuperados) utilizando autômatos celulares. O objetivo é capturar a dinâmica espacial da propagação de doenças infecciosas, permitindo análises visuais e quantitativas do comportamento de epidemias.

## Motivação

Os modelos epidemiológicos tradicionais, como o SIR clássico, assumem uma mistura homogênea da população, o que pode ser uma simplificação excessiva. Este projeto utiliza autômatos celulares para introduzir interações locais, permitindo uma representação mais realista da disseminação da infecção em um ambiente espacialmente estruturado.

## Funcionalidades

- Implementação do modelo SIR com dinâmica baseada em autômatos celulares;
- Simulação de epidemias em uma grade bidimensional;
- Parâmetros configuráveis para taxa de infecção, taxa de recuperação e tamanho da população;
- Animação da evolução da epidemia ao longo do tempo.

## Requisitos

- Python 3.x
- Bibliotecas necessárias:
  - numpy
  - matplotlib

Para instalar as dependências, execute:

```bash
pip install numpy matplotlib
```

## Como Executar

1. Clone o repositório ou baixe os arquivos.
2. Execute o script principal com:

```bash
python epidemic_simulation.py
```

3. A simulação será exibida como uma animação mostrando a propagação da infecção na população.

## Parâmetros Configuráveis

Dentro do código, os seguintes parâmetros podem ser ajustados para modificar a simulação:

- `GRID_SIZE`: Define o tamanho da grade da população;
- `INFECTION_RATE`: Probabilidade de um indivíduo suscetível ser infectado por um vizinho infectado;
- `RECOVERY_RATE`: Probabilidade de recuperação de um indivíduo infectado;
- `INITIAL_INFECTED`: Número inicial de indivíduos infectados;
- `STEPS`: Número total de iterações da simulação.

## Resultados Esperados

A simulação apresenta ondas de infecção, demonstrando como a doença se espalha, atinge um pico e eventualmente regride à medida que os indivíduos se recuperam. A interação local entre os indivíduos gera padrões emergentes que podem ser analisados para entender a dinâmica da propagação.

## Contribuições

Contribuições são bem-vindas! Caso tenha sugestões ou melhorias, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto é distribuído sob a licença MIT. Sinta-se livre para utilizá-lo e modificá-lo conforme necessário.

## Contato

Para dúvidas ou sugestões, entre em contato pelo e-mail: jurupoc222@gmail.com

