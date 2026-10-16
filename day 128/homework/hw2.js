let username = "Goga";
let password = "Goa2026";
let age = 20;

if (username === '' || password === ''){
    console.log('fill in all fields')
} else if(username === 'Goga' || password === 'Goga2026'){
    console.log('Login successful')
} else if(username === 'Goga'){
    console.log('Incorrect password')
} else{
    console.log('Incorrect username')
}

if (age < 18) {
    console.log("Access denied");
}