let age = Number(prompt("Enter your age"))
let price = Number(prompt("Enter the ticket price"))

if(age < 7){
    console.log('ticket is free')
} else if(age > 7 || age < 17){
    console.log('you have a 50% discount')
} else if(age > 18 || age < 59){
    console.log('pay the full price')
} else if(age >= 60){
    console.log('you have a 30% discount')
} else(age < 0 || price < 0);{
    console.log('invalid input')
}