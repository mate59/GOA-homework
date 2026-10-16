let score = 0

for (let i = 1; i <= 5; i++) {
    let guess = Number(prompt("0 - გერბი, 1 - საფასური"))
    let coin = Math.floor(Math.random() * 2) + 1

    if (coin === 0) {
        console.log("გერბი")
    } else {
        console.log("საფასური")
    }

    if (guess === coin) {
        console.log("სწორია! +10 ქულა")
        score += 10
    } else {
        console.log("არასწორია!")
    }
}

console.log("საერთო ქულა: " + score)