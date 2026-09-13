let username = prompt("შეიყვანე მომხმარებლის სახელი:").trim()

if (username === "") {
    console.log("სახელი აუცილებელია")
} else if (username.length < 3) {
    console.log("სახელი ძალიან მოკლეა")
} else if (username.length > 12) {
    console.log("სახელი ძალიან გრძელია")
} else if (username.startsWith("admin")) {
    console.log("ადმინისტრატორის სახელის გამოყენება აკრძალულია")
} else {
    console.log("მომხმარებლის სახელი მიღებულია")
}