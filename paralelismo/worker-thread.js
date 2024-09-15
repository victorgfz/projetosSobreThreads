const { parentPort } = require("node:worker_threads")


parentPort.on('message', ({ data1, data2, resultado, iteracoes }) => {

    for (let ind in data1) {
        let count = 0
        resultado.push(data1[ind] * data2[ind])
        for (let i = 0; i < iteracoes; i++) {
            count++
        }
    }


    parentPort.postMessage('Done')
}) 