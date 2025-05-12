// Ciclos
/* 

for(iterador; condicion; incremento){
    codigo
}

for(indice in coleccion){
    codigo
}

for(valor of coleccion){
    codigo
}

while(condicion){
    codigo
}

do {
    codigo
} while (condicion)


*/
let nombres = ["Hugo", "Paco", "Luis"]

for(let i = 1; i <= 10; i++){
    console.log(i)
}

for(let i = 0; i < nombres.length; i++){
    console.log(nombres[i])
}

for(let indice in nombres){
    console.log(indice) // 0 1 2
}

for(let valor of nombres){
    console.log(valor) // Hugo Paco Luis
}