let number = 45

if (number >= 10 && number <= 50) {
    console.log("Inside range")
} else {
    console.log("Outside range")
}

if (number % 2 === 0 && number > 20) {
    console.log("Special even number")
}

if (number % 2 !== 0 && number < 30) {
    console.log("Special odd number")
}

if (number === 25 || number === 50) {
    console.log("Exact match")
}
