// 1

let numbers = [12, 25, 8, 40, 17, 30]

for (let i = 0; i < numbers.length; i++){
    console.log(numbers[i])
    if (numbers[i] % 2 === 0) console.log(numbers[i])
    if (numbers[i] % 2 !== 0) console.log(numbers[i])
    console.log(numbers[i] * 2)
}

// 2

let names = ["Nika", "Ana", "Giorgi", "Mariam", "Luka"]

for (let i = 0; i < names.length; i++){

    console.log(names[i])

    if (names[i].length > 4)
         console.log(names[i])
    if (names[i][0] === "A")
         console.log(names[i])

    console.log(names[i] + "!")
}

// 3

let ages = [12, 17, 20, 15, 25, 16]

for (let i = 0; i < ages.length; i++){
    ages[i]++

    if (ages[i] < 18)
        ages[i] = 18
}

console.log(ages)

// 4

let prices = [100, 250, 80, 400, 150, 50]
let count = 0

for (let i = 0; i < prices.length; i++){
    if (prices[i] > 100){
        console.log(prices[i])
    }
    
    if (prices[i] > 200){
        prices[i] -= 50
    }

    if (prices[i] < 100){
        count++
    }

    prices[i] += 20
}

console.log(count)

// 5

let scores = [45, 90, 67, 32, 100, 75, 50]
let count1 = 0
let max = scores[0]

for (let i = 0; i < scores.length; i++){

    console.log(scores[i])

    if (scores[i] > 60)
        console.log(scores[i])

    if (scores[i] < 50) 
        scores[i] = 50

    if (scores[i] >= 70) 
        count1++

    if (scores[i] > max) 
        max = scores[i]
}

console.log(count1)
console.log(max)

// 6

let numbers1 = [5, 12, 8, 21, 30, 7, 16]
let newNumbers = []

for (let i = 0; i < numbers.length; i++){

    if (numbers1[i] % 2 === 0){
        newNumbers.push(numbers1[i] * 3)
    }
}

console.log(newNumbers)

// 7

let numbers2 = [12, -5, 8, -20, 0, 15, -3, 7]
let positiveCount = 0
let negativeCount = 0
let sum = 0
let positiveNumbers = []

for (let i = 0; i < numbers.length; i++){
    if (numbers2[i] > 0){
        positiveCount++
        positiveNumbers.push(numbers[i])
    }
    
    if (numbers2[i] < 0){
        negativeCount++
        numbers2[i] = 0
    }

    sum += numbers2[i] < 0 ? numbers2[i] : 0

}

console.log(positiveCount, negativeCount, positiveNumbers, numbers2)