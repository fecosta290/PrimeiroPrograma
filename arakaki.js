const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

function criarArvoresDeNatal(N) {
  if (N < 3 || N > 26) {
    console.log("O valor de N deve estar entre 3 e 26.");
    rl.close();
    return;
  }

  const alfabeto = "abcdefghijklmnopqrstuvwxyz";

  for (let i = 0; i < N; i++) {
    if(i === 0){
        let a = " ".repeat(N - 1) + "a";
        console.log(a);
    } else{
            let espacos = " ".repeat(N - i - 1);
            let asteriscos = "*".repeat(i * 2 - 1);
            let linha = espacos + alfabeto[i] + asteriscos + alfabeto[i];
            console.log(linha);
    };

    }

  // Tronco da árvore
  let tronco = " ".repeat(N - 1) + "|";
  console.log(tronco);

  rl.close();
}

rl.question("Digite um valor entre 3 e 26 para a altura da árvore de Natal: ", (inputN) => {
  const N = parseInt(inputN);

  if (!isNaN(N)) {
    criarArvoresDeNatal(N);
  } else {
    console.log("Por favor, insira um número válido.");
    rl.close();
  }
});
