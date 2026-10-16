let number = Number(prompt("შეიყვანე რიცხვი:"))

if (number > 0) {
    if (number > 100) {
        console.log("Large positive number")
    } else {
        console.log("Small positive number")
    }
} else if (number < 0) {
    if (number % 2 === 0) {
        console.log("Negative even number")
    } else {
        console.log("Negative odd number")
    }
} else {
    console.log("Zero")
}

if (number >= 10 && number <= 20) {
    console.log("Special range")
}
