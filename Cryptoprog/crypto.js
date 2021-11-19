const { createHash } = require('crypto');

function hash(input) {
    return createHash('sha256').update(input).digest('base64')
}

let passord = "Mattis";

const hash1 = hash(passord);
console.log(hash1);

