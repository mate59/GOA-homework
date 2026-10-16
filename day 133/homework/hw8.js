let n1 = Math.floor(Math.random() * 9) + 1
let n2 = Math.floor(Math.random() * 9) + 1
let n3 = Math.floor(Math.random() * 9) + 1

console.log(n1, n2, n3)

let p1 = Number(prompt("Enter first number:"))
let p2 = Number(prompt("Enter second number:"))
let p3 = Number(prompt("Enter third number:"))

let count = 0

if (p1 === n1) count++
if (p2 === n2) count++
if (p3 === n3) count++

if (count === 3) {
    console.log("JACKPOT!")
} else if (count === 2) {
    console.log("დიდი მოგება!")
} else if (count === 1) {
    console.log("პატარა მოგება!")
} else {
    console.log("წააგე!")
}