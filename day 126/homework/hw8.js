let age = Number(prompt("შეიყვანე ასაკი:"));

if (age <= 0) {
    console.log("არასწორი ასაკი")
} else {

    let ticketType = prompt("შეიყვანე ბილეთის ტიპი:") .toLowerCase()
        
    let username = prompt("შეიყვანე მომხმარებლის სახელი:") .trim()

    let price

    if (age < 12) {
        price = 5
    } else if (age >= 12 && age <= 17) {
        price = 8
    } else {
        price = 15
    }

    if (ticketType === "vip") {
        price = price + 10
    } else if (ticketType === "standard") {
        price = price
    } else {
        console.log("ბილეთის ტიპი არასწორია")
    }
}