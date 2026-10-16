let price = 250;
let age = 22;
let isMember = true;

let discount = 0;

if (price < 0) {
    console.log("Invalid price")
} else if (isMember && price > 200){
    discount = 25
} else if (isMember || age < 18){
    discount = 10
} else if (age >= 60 && price > 100){
    discount = 15
} else{
    discount = 0
}

let finalPrice = price - discount

if (price >= 0){
    console.log("Initial price:", price)
    console.log("Discount:", discount)
    console.log("Final price:", finalPrice)
}