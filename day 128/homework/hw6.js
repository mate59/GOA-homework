let age = Number(prompt("შეიყვანე ასაკი:"))
let height = Number(prompt("შეიყვანე სიმაღლე სანტიმეტრებში:"))

if (age < 0 || height < 0) {
    console.log("Invalid data")
} else if (age >= 12 && height >= 140) {
    console.log("You can ride")

    if (age >= 18 && height >= 180) {
        console.log("VIP access")
    }
} else {
    console.log("You cannot ride")
}
