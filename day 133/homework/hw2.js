let diceRoll = Math.floor(Math.random() * 6) + 1

console.log("you rolled: " + diceRoll)

if (diceRoll === 6){
    console.log("🎉 You got the highest number!")
} else if (diceRoll === 1){
    console.log("😢 You got the lowest number!")
} else{
    console.log("normal number")
}