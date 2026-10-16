let car1 = Math.floor(Math.random() * 51) + 50
let car2 = Math.floor(Math.random() * 51) + 50

console.log(car1)
console.log(car2)

if (car1 > 90) console.log("🔥 Super fast!")
if (car2 > 90) console.log("🔥 Super fast!")

if (car1 > car2) {
    console.log("Car 1 wins!")
} else if (car2 > car1) {
    console.log("Car 2 wins!")
} else {
    console.log("Draw!")
}