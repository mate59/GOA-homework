let age = Number(prompt("შეიყვანე ასაკი:"))

if (age < 0) {
    console.log("არასწორი ასაკი")
} else if (age >= 18) {
    console.log("სრულწლოვანი ხარ")
} else {
    console.log("არასრულწლოვანი ხარ")
}
