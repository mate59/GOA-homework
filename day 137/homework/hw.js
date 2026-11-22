// 1
let products = ["Laptop", "Phone", "Tablet", "Monitor", "Keyboard"]

products.unshift("Mouse")

products.push("Headphones", "Speaker")

let removedProduct = products.shift()

let monitorIndex = products.indexOf("Monitor")

let tabletIndex = products.indexOf("Tablet")
products.splice(tabletIndex, 1, "Smartwatch")

let newProducts = products.slice(2, 5)

let productsString = products.join(" | ")

console.log(products)
console.log(removedProduct)
console.log(monitorIndex)
console.log(newProducts)
console.log(productsString)



// // 2 



let text = "HTML,CSS,JavaScript,React,Node.js,Python"

let technologies = text.split(",")

technologies.unshift("Git")

technologies.push("TypeScript")

let reactIndex = technologies.indexOf("React")

technologies.splice(2, 2)

let firstFour = technologies.slice(0, 4)

let newString = firstFour.join(" - ")

let finalArray = newString.split(" - ")

console.log(technologies)
console.log(reactIndex)
console.log(firstFour)
console.log(newString)
console.log(finalArray)

//3




let students = ["Nika","Ana","Gio","Mariam","Luka","Saba","Elene"]

students.unshift("data" , "tako")

students.pop()

students.indexOf("Mariam")

students.splice(2 , 2)

students.splice(4, 0, "Irakli")

let students2 = students.splice(3)

let students3 = ["Giorgi", "Salome"]

let students2And3 = students2.concat(students3)

let joinedStudents = students.join(",")

let joinedStudents2 = students.join(" ")

students.isArray()

console.log(students)
console.log(students2)



//4


let scores = [45, 78, 92, 34, 88, 67, 100, 56]

scores.unshift(50)

scores.push(73 , 85)

let scoresIndex = scores.indexOf(92)

scores.splice(4 , 2)

scores.splice(5 , 0 , 70)

let slicedMasive = scores.slice(Math.floor(scores.length / 2))

let addedScores = [95, 81, 60]

scores.concat(addedScores)

scores.pop()

scores.unshift(99)

let joinedScore = scores.join("/")

let splitedScores = joinedScore.split("/")

console.log(scores)


//5

let groups = [["Nika", "Ana", "Gio"],["Mariam", "Luka"],["Saba", "Elene", "Data"]]

let flattedGroups = groups.flat()

flattedGroups.unshift("tako")

flattedGroups.push("irakli" , "salome")

let indexFind = flattedGroups.indexOf("Luka")

flattedGroups.splice(3 , 2)

let slicedGroup = flattedGroups.slice(0 , 5)

let addedGroup = ["Giorgi", "Sandro"]

flattedGroups.concat(addedGroup)

console.log(slicedGroup)
console.log(flattedGroups)