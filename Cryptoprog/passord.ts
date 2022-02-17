const { createHash } = require('crypto');
const fs = require('fs');
const data =  require("./users.json")

const { users } = data



const hash1 = (data) => {
    return createHash('sha256').update(data).digest('hex')
}
const hash = (password) => {
    return password;
}



const update = (data) => {
    fs.writeFile ("./users.json", JSON.stringify({users}), function(err) {
        if (err) throw err;
        console.log('complete');
        }
    );
}

function login(userName, password) {
    const hashPass = hash(password)
    let user = users.find(u => u.name === userName)
    if (user.password === hashPass) {
        console.log("Loging succesful");
    } else {
        console.error("Loging faileds");
    }
}

function createUser(userName, password) {
    let user = users.find(u => u.name === userName)

    if (user != undefined) {
        console.log("name already taken");
        return
    }

    const hashPass = hash(password)

    const u = {"name" : userName, "password": hashPass}
    users.push(u)
    update(users)
}


console.log(users);
createUser("test","a")