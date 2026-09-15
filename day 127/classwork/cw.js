let number = Number(prompt("enter a number: "))

if (number > 10 && number % 2 === 0){
    console.log("good number")
} else {
    console.log("bad time")
}


let name = prompt("enter your name: ")

if (name.length > 5 || name.startsWith("g")){
    console.log("good name")
} else {
    console.log("bad name")
}

