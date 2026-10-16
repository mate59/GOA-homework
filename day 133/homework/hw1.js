let secretNumber = Math.floor(Math.random() * 10) + 1
let playerGuess = Number(prompt("შეიყვანეთ რიცხვი 1-დან 10-მდე: "))

if (playerGuess === secretNumber){
    console.log("🎉 გამოიცანი!")
} else{
    console.log("❌ ვერ გამოიცანი")
}