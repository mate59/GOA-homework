//1

let i = 1

do {
    console.log(i)
    i++
} while (i <= 10)


//2

let d = 10

do {
    console.log(d)
    d--
} while (d >= 1)


//3 

let c = 2

do {
    console.log(c)
    c += 2
} while (c <= 20)


//4

let l = Number(prompt("Enter number:"))
let e = 1
let f = 0

do {
    f += e
    e++
} while (e <= l)

console.log(f)


//5


let g = 1
let h = 1

do {
    g *= h
    h++
} while (h <= 10)

console.log(g)


//6

let j

do {
    j = prompt("Enter password:")
} while (j !== "javascript123")

console.log("Access Granted!")


//7



let k = 7
let p

do {
    p = Number(prompt("Guess the number:"))
} while (p !== k)

console.log("You Win!")


//8


let m

do {
    m = Number(prompt("Enter number:"))
} while (m <= 0)

console.log("Valid Number!")


//9

let num1 = 0

do{
    num1 = Number(prompt("enter a number "))
}while(num1 = "0")


//10


for(let i = 0; i <= 50; i++){
    if(i % 3 === 0){
        console.log(i)
    }
}





