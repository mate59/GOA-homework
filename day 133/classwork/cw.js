let hero = Math.floor(Math.random() * 21) + 20
let monster = Math.floor(Math.random() * 21) + 15

console.log("გმირის ძალა: ", hero)
console.log("მონსტრის ძალა: ", monster)

if (hero === 30){
    hero += 10
}

console.log("საბოლოო გმირის ძალა: ", hero)

if (hero > monster){
    console.log("გმირმა მოიგო!")
} else if (monster > hero) {
    console.log("მონსტრმა მოიგო!")
} else {
    console.log("ბრძოლა ფრედ დასრულდა!")
}
