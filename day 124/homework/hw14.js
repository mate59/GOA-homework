let input = "   Hello!!! My name is Goga!!! I love JS!!!   "

console.log(input.trim() .replaceAll("!!!", "!") .slice(0, 21) + "...")