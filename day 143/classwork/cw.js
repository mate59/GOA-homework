let secretNumber = 0

let guess = ""

let count = 0

do{
    guess = Number(prompt("guess the number: "))

    count++

    if(guess !== secretNumber){
        console.log("try again")
    } else{
        console.log("you guessed it!!!!!!!!")
    }

}while(guess != secretNumber)

console.log("attempts: " + count)


