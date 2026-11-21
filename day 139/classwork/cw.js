// 1

let numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for (let i = 0; i < numbers.length; i++) {
    if (numbers[i] % 2 === 0) {
        console.log(numbers[i])
    }
}


// 2

let numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for (let i = 0; i < numbers1.length; i++) {
    if (numbers1[i] % 2 !== 0) {
        console.log(numbers1[i])
    }
}

// 3

let names = ["გიორგი", "ნიკა", "გიგა", "ანა", "გელა"]

for (let i = 0; i < names.length; i++) {
    if (names[i].startsWith("გ")) {
        console.log(names[i])
    }
}

// 4

let names1 = ["გიორგი", "გიგა", "გელა", "გურამი", "ანა"]

for (let i = 0; i < names1.length; i++) {
    if (names1[i].startsWith("გ") && names1[i].length > 5) {
        console.log(names1[i])
    }
}

// 5

let items = [10, "გამარჯობა", 25, "JavaScript", true, "სალამი", 50]

for (let i = 0; i < items.length; i++) {
    if (typeof items[i] === "string") {
        console.log(items[i])
    }
}