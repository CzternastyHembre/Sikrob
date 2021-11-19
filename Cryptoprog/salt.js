const { randomBytes, scryptSync, timingSafeEqual } = require("crypto");

users = []

function signUp(email, password) {
    const salt = randomBytes(16).toString('hex');
    const hashedPassword = scryptSync(password, salt, 64);

    const user = {email, password: `${salt}:${hashedPassword}`};

    users.push(user);

    return user;
}

function login(email, password) {

    const user = users.find(v => v.email === email)

    const [salt, key]= user.password.split(':');
    const hashedBuffer = scryptSync(password, salt, 64);

    const keyBuffer = Buffer.from(key, 'hex');
    console.log(hashedBuffer);
    console.log(keyBuffer);
    const math = timingSafeEqual(hashedBuffer, keyBuffer);
/*
    if (math) {
        return 'logib success';
    } else {
        return 'login fail';
    }
*/

    return math ? 'login success' : 'login fail';

}

user = signUp("aaa", "123");
console.log(user)
console.log(login("aaa", "123"))