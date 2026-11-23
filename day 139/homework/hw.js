//1

let numbers = [12, 25, 8, 40, 17, 30]

for(let i = 0; i < numbers.length; i++){
    console.log(numbers[i])
}

for(let i = 0; i < numbers.length; i++){
    if (numbers[i] % 2 == 0)
        console.log(numbers[i])
}

for(let i = 0; i < numbers.length; i++){
    if(numbers[i] % 2 == 1)
        console.log(numbers[i])
}

for(let i = 0; i < numbers.length; i++){
    console.log(numbers[i] * 2)
}

//2

let names = ["Nika", "Ana", "Giorgi", "Mariam", "Luka"]

for(let i = 0; i < names.length; i++){
    console.log(names[i])
}

for(let i = 0; i < names.length; i++){
    if(names[i].length >= 4){
        console.log(names[i])
    }
}

for(let i = 0; i < names.length; i++){
    if(names[i].startsWith("A")){
        console.log(names[i])
    }
}

for(let i = 0; i < names.length; i++){
    console.log(names[i] + "!")
}

//3

let ages = [12, 17, 20, 15, 25, 16]

for(let i = 0; i < ages.length; i++){
    console.log(ages[i] + 1)
}

for(let i = 0; i < ages.length; i++){
    if(ages[i] < 18){
        ages[i] = 18
    }
}

console.log(ages)


//4

let prices = [100, 250, 80, 400, 150, 50]

let count = 0

for(let i = 0; i < prices.length; i++){
    if(prices[i] < 100){
        console.log(prices[i])
    }

    console.log(prices[i] + 20)

    if(prices[i] < 200){
        console.log(prices[i] - 50)
    }

    if(prices[1] < 100){
        count++
    }
}

//5

let scores = [45, 90, 67, 32, 100, 75, 50]

let count1 = 0

let maxCount = scores[0]

for(let i = 0; i < scores.length; i++){
    console.log(scores[i])

    if(scores[i] < 60){
        console.log(scores[i])
    }

    if(scores[i] < 70){
        count1++
    }

    if(scores[i] > maxCount){
        maxCount = scores[i]
    }
}

//6

let numbers1 = [5, 12, 8, 21, 30, 7, 16]
let evenNumbers = []

for (let i = 0; i < numbers1.length; i++) {
    if (numbers1[i] % 2 == 0) {
        evenNumbers.push(numbers1[i])
    }
}

for (let i = 0; i < evenNumbers.length; i++) {
    evenNumbers[i] *= 3
}

console.log(evenNumbers)


//7

let numbers2 = [12, -5, 8, -20, 0, 15, -3, 7]

let positive = 0
let negative = 0
let sum = 0
let newNumbers = []

for (let i = 0; i < numbers2.length; i++) {
    if (numbers2[i] > 0) {
        positive++
        newNumbers.push(numbers2[i])
    }

    if (numbers2[i] < 0) {
        negative++
    }

    sum += numbers2[i]
}

console.log("Positive:", positive)
console.log("Negative:", negative)
console.log("Sum:", sum)
console.log("New array:", newNumbers)

//8

let numbers3 = [12, -5, 8, -20, 0, 15, -3, 7]

positive = 0
negative = 0
sum = 0
newNumbers = []

for (let i = 0; i < numbers3.length; i++) {
    if (numbers3[i] > 0) {
        positive++
        newNumbers.push(numbers3[i])
    }

    if (numbers3[i] < 0) {
        negative++
        numbers3[i] = 0
    }

    sum += numbers3[i]
}

console.log("Positive:", positive)
console.log("Negative:", negative)
console.log("Sum:", sum)
console.log("New array:", newNumbers)
console.log("Updated array:", numbers3)


//9

let students = ["Nika", "Ana", "Giorgi", "Luka", "Mariam", "Dato"]
let selectedStudents = []

let count2 = 0

for (let i = 0; i < students.length; i++) {
    if (students[i].length > 4) {
        selectedStudents.push(students[i])
    }

    if (students[i][0] == "M") {
        console.log("Special student: " + students[i])
    }

    if (students[i].length >= 5) {
        count2++
    }
}

console.log(selectedStudents)
console.log(count2)

//10

let points = [15, 40, 65, 20, 90, 35, 100]

for (let i = 0; i < points.length; i++) {

    if (points[i] < 50) {
        points[i] += 10
    }
    else if (points[i] <= 80) {
        points[i] += 5
    }
    else {
        points[i] -= 10
    }
}

console.log(points)

let count4 = 0

for (let i = 0; i < points.length; i++) {
    if (points[i] > 50) {
        count4++
    }
}

console.log(count4)