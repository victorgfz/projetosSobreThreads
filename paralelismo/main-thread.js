const { Worker } = require("node:worker_threads")


const vetor1 = Array.from({ length: 500 }, () => Math.floor(Math.random() * 500) * + 1)
const vetor2 = Array.from({ length: 500 }, () => Math.floor(Math.random() * 500) * + 1)
const resultado = []
const iteracoes = 1e7


function dividiVetor(array, n) { // funcao pra dividir o vetor para que as partes sejam executadas paralelamente
    let partes = []
    for (let i = n; i > 0; i--) {
        partes.push(array.splice(0, Math.ceil(array.length / i)))
    }
    return partes
}


function rodar(array1, array2, workers) {
    const partes1 = dividiVetor(array1, workers)
    const partes2 = dividiVetor(array2, workers)

    const tic = performance.now()

    let contador = 0

    partes1.forEach((data1, i) => { // itera sobre cada parte dos arrays criada, cada parte sera realizada por uma thread
        const data2 = partes2[i]

        const worker = new Worker('./worker-thread.js') // instancia um novo worker para cada parte
        worker.postMessage({ data1, data2, resultado, iteracoes }) // envia os dados

        worker.on('message', () => { // recebe os dados de volta
            console.log(`Worker ${i} finalizou!`)
            contador++
            if (contador === workers) {
                const tac = performance.now()
                console.log(`${workers} workers levaram ${tac - tic} ms`)

                process.exit()
            }
        })
        worker.on("error", (err) => { // trata o erro
            console.error(`Worker ${i} encontrou um erro:`, err);
        });
    })




}


rodar(vetor1, vetor2, 2)