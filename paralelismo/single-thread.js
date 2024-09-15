const vetor1 = Array.from({ length: 500 }, () => Math.floor(Math.random() * 500) * + 1)
const vetor2 = Array.from({ length: 500 }, () => Math.floor(Math.random() * 500) * + 1)
const resultado = []
const iteracoes = 1e7

const tic = performance.now()

for (let ind in vetor1) {
    let count = 0
    resultado.push(vetor1[ind] * vetor2[ind])
    for (let i = 0; i < iteracoes; i++) {
        count++
    }
}



const tac = performance.now()

console.log(`O processo levou ${tac - tic} ms`)