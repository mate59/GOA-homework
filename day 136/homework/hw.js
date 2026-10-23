// 1

let numbers1 = [10, 20, 30, 40, 50]

let removedNumber = numbers.pop()

console.log(removedNumber)
console.log(numbers)

// 2

let colors = ["Red", "Green", "Blue", "Black"]

let removedColor = colors.shift()

console.log(removedColor)
console.log(colors)

colors.unshift("Red")

console.log(colors)

// 3

let animals = ["Dog", "Cat"]

animals.unshift("Lion")
animals.unshift("Tiger", "Bear")

console.log(animals)

// 4

let numbers2 = [5, 10, 15, 20, 25, 30, 35]

let firstArray = numbers.slice(1, 4)
let lastThree1 = numbers.slice(-3)
let withoutFirstTwo = numbers.slice(2)

console.log(firstArray)
console.log(lastThree1)
console.log(withoutFirstTwo)
console.log(numbers)

// 5

let games = ["Minecraft", "GTA", "FIFA", "Roblox", "Fortnite"]

games.splice(1, 1)
console.log(games)

games.splice(1, 1, "eFootball")
console.log(games)

games.splice(1, 0, "Terraria")
console.log(games)

// 6

let cities = ["Tbilisi", "Batumi", "Kutaisi", "Rustavi"]

let withoutBatumi = cities.slice()
withoutBatumi.splice(1, 1)
console.log(withoutBatumi)

let withGori = cities.slice()
withGori.splice(2, 1, "Gori")
console.log(withGori)

let withZugdidi = cities.slice()
withZugdidi.splice(2, 0, "Zugdidi")
console.log(withZugdidi)

console.log(cities)

// 7

let first1 = [1, 2, 3]
let second1 = "JavaScript"
let third = { name: "Goga" }
let fourth = 25
let fifth = ["HTML", "CSS"]

console.log(Array.isArray(first1))
console.log(Array.isArray(second1))
console.log(Array.isArray(third))
console.log(Array.isArray(fourth))
console.log(Array.isArray(fifth))

// 8

let numbers = [1, 2, [3, 4], [5, 6]]

let flatNumbers = numbers.flat()

console.log(flatNumbers)
console.log(numbers)

// 9

let first2 = ["HTML", "CSS"]
let second2 = ["JavaScript", "React"]

let combined = first2.concat(second2)

console.log(combined)

// 10

let fruits = ["Apple", "Banana", "Orange", "Kiwi"]

fruits.push("Mango")
fruits.unshift("Strawberry")
fruits.pop()
fruits.shift()

let newFruits = fruits.slice(0, 2)

console.log(fruits)
console.log(newFruits)

// 11

let toys = ["Car", "Doll", "Ball", "Robot", "Puzzle"]

toys.splice(1, 1, "Teddy Bear")
toys.push("Lego")

let newToys = toys.slice(0, 3)

console.log(toys)
console.log(newToys)

// 12

let teamA = ["Nika", "Ana", "Gio"]
let teamB = ["Mariam", "Luka", "Saba"]

let team = teamA.concat(teamB)

team.unshift("Goga")
team.push("Data")
team.pop()

let newTeam = team.slice(0, 4)

console.log(team)
console.log(newTeam)

// 13

let students = ["Nika", "Ana", "Gio", "Mariam", "Luka"]
let newStudents = ["Saba", "Data"]

let allStudents = students.concat(newStudents)

allStudents.unshift("Goga")
allStudents.splice(2, 1, "Elene")

let lastThree2 = allStudents.slice(-3)

allStudents.pop()

console.log(allStudents)
console.log(lastThree2)