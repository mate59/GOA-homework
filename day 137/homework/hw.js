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



// 2 



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

