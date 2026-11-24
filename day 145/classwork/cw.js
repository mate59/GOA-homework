// let names = ["mate", "saba", "gela", "mayvala", "goga"]

// names.forEach((name, index) =>{
//     if(name[0] === "g"){
//         console.log(name, index)
//     }
// }
// )





// let numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

// names.forEach((num) =>{
//     if(num % 2 == 0){
//         console.log(num)
//     }
// }
// )




// let randomMonacemebi = ["mate", 22, 14.2, true, 94, "gela"]

// randomMonacemebi.forEach((monac)=>{
//     if(typeof monac === "string"){
//         console.log(item)
//     }
// }
// )



let names = ["mate", "saba", "gela", "mayvala", "goga"]

let newArray = names.map((saxeli, index)=>{
    if(saxeli.length > 5){
        return saxeli + " გრძელი სახელია"
    } else{
        return saxeli + "mokle saxelia"
    }
}
)

console.log(newNames)





let numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

let nums = numbers.map(ricxvi=>{
    if(ricxvi % 2 == 0){
        return ricxvi * 200
    } else{
        return ricxvi * 100
    }
}
)

console.log(newNumbers)







