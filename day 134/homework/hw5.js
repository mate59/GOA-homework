let secret = Math.floor(Math.random() * 50) + 1
let win = false

for (let i = 1; i <= 5; i++) {
    let guess = Number(prompt("გამოიცანი რიცხვი 1-დან 50-მდე"))

    if (guess > secret) {
        console.log("შეამცირე!")
    } else if (guess < secret) {
        console.log("გაზარდე!")
    } else {
        console.log("მოიგე!")
        win = true
        break
    }
}

if (win === false) {
    console.log("საიდუმლო რიცხვი იყო: " + secret)
}