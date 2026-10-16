let age = 19;
let hasTicket = true;
let isVip = false;

console.log(age < 18 ? 'too young' : age >= 18 && !hasTicket ? 'no ticket' : isVip && hasTicket ? 'vip enterance' : 'normal enerance')