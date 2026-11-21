let i = 0

while (i < 20) {
    console.log("mate")
    i++
}


let n = 0

while (n <= 20) {
    console.log(n)
    n++
}


let m = 40

while (m <= 60) {
    console.log(m)
    m++
}


let w = 20

while (w <= 50) {
    console.log(w)
    w += 2
}


let l = 20

while (l <= 50) {
    console.log(l)
    l += 3
}




let names = ["gio", "nika", "ana", "sandro"]

let g = 0

while (g < names.length){
    if (names[g].length > 5){
        console.log(names[g])
    }
    g++
}


let numbers = [1, 2, 3, 4, 5, 6]

let evenNumbers = []

let h = 0

while (h < numbers.length){
    if (numbers[h] % 2 === 0){
        evenNumbers.push(numbers[h])
    }
    h++
}

console.log(evenNumbers)


let data = ["world", 25, true]

let c = 0

while (c < data.length){
    if (typeof data[c] === "string"){
        console.log(data[c])
    }
    c++
}