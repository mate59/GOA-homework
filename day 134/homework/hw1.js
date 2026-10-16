let score1 = 0
let score2 = 0

for (let i = 1; i <= 5; i++) {
    let player1 = Math.floor(Math.random() * 21) + 10
    let player2 = Math.floor(Math.random() * 21) + 10

    if (player1 === 20) player1 += 5
    if (player2 === 20) player2 += 5

    console.log("Player 1: " + player1)
    console.log("Player 2: " + player2)

    if (player1 > 25 && player2 > 25) {
        console.log("ფრეა!")
    } else if (player1 > player2) {
        console.log("Player 1 wins!")
        score1++
    } else if (player2 > player1) {
        console.log("Player 2 wins!")
        score2++
    } else {
        console.log("ფრეა!")
    }
}

console.log("Player 1 score: " + score1)
console.log("Player 2 score: " + score2)

if (score1 > score2) {
    console.log("Player 1 is the winner!")
} else if (score2 > score1) {
    console.log("Player 2 is the winner!")
} else {
    console.log("ფრეა!")
}