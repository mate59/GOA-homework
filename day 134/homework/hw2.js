let score = 0

for (let i = 1; i <= 5; i++) {
    let d1 = Math.floor(Math.random() * 6) + 1
    let d2 = Math.floor(Math.random() * 6) + 1
    let d3 = Math.floor(Math.random() * 6) + 1

    let sum = d1 + d2 + d3

    console.log("Round " + i)
    console.log(d1, d2, d3)
    console.log("Sum: " + sum)

    if (d1 === d2 && d2 === d3) {
        score += 50
    } else if (d1 === d2 || d1 === d3 || d2 === d3) {
        score += 20
    } else if (sum > 10) {
        score += 10
    }

    if (sum % 2 === 0) {
        score += 5
    } else {
        score -= 3
    }

    console.log("Current score: " + score)
}

console.log("Final score: " + score)