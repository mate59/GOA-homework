let player1 = Math.floor(Math.random() * 6) + 1
let player2 = Math.floor(Math.random() * 6) + 1

console.log("player1 results: " + player1)
console.log("player2 results: " + player2)

if (player1 > player2){
    console.log("player1 won!")
} else if (player1 < player2){
    console.log("player2 won!")
} else {
    console.log("tie!")
}