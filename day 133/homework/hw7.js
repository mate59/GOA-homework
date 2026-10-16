let player = Math.floor(Math.random() * 21) + 10
let monster = Math.floor(Math.random() * 21) + 10

if (player === 25) {
    player += 10
}

console.log("Player: " + player)
console.log("Monster: " + monster)

if (player > monster) {
    console.log("Player wins!")
} else if (monster > player) {
    console.log("Monster wins!")
} else {
    console.log("Draw!")
}