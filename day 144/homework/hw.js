//1

let sum = 0

for(let i = 0; i <= 50; i++){
    if(i % 2 == 1){
        sum += 1
    }

    if(sum < 100){
        break
    }
}

console.log(sum)

//2

let numbers = [5, 12, 18, 7, 25, 30, 9, 40]

for (let i = 0; i < numbers.length; i++){
    if (numbers[i] > 10){
        console.log(numbers[i])
    }
    
    if (numbers[i] === 30){
        break
    }
}

//3

let scores = [45, 67, 82, 91, 38, 75, 100, 55]

for(let i = 0; i < scores.length; i++){
    if(scores[i] < 50){
        console.log("Failed!")
    }

    if(scores[i] >= 90){
        console.log("Excellent!")
    }

    if(scores[i] >= 100){
        break
    }
}

//4

let code = 2026

for(let i = 0; i <= 4; i++){
    let userInput = Number(prompt("enter a code: "))

    if(userInput === code){
        console.log("Access Granted!")
        break
    }

    if(userInput !== code){
        console.log("Access Denied!")
    }

}

//5

let numbers1 = [12, 25, 8, 34, 17, 50, 9, 60]

let found = false

for (let i = 0; i < numbers1.length; i++){
    if (numbers1[i] > 20 && numbers1[i] % 3 === 0){
        console.log(numbers1[i])
        found = true
        break
    }
}

if (found === false){
    console.log("Not Found!")
}

//6

let prices = [15, 25, 10, 40, 30, 50, 20]

let jami = 0

for(let i = 0; i < prices.length; i++){
    jami += prices[i]

    if(jami > 100){
        break
    }
}

//7

let numbers2 = [8, 14, 21, 6, 35, 42, 11, 50]

let countEven = 0

for(let i = 0; i < numbers2.length; i++){
    if(numbers2[i] > 30 && numbers2[i] % 5 == 0){
        break
    }

    if(numbers2[i] % 2 == 0)(
        countEven++
    )
}

console.log(countEven)

//8


for(let i = 0; i <= 5; i++){
    let inputAge = Number(prompt("enter your age: "))

    if(inputAge >= 18 && inputAge <= 60){
        console.log("Valid Age!")
        break
    } else{
        console.log("Invalid Age!")
    }

    if(i === 5){
        console.log("Attempts Finished!")
    }
}