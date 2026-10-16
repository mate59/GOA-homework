let score = 0

let shot = Math.floor(Math.random() * 100) + 1

console.log("Shot: " + shot)

if (shot > 80) {
    score += 20
} else if (shot > 50) {
    score += 10
}

console.log("საერთო ქულა: " + score)