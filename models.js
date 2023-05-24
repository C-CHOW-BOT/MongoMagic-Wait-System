const mongoose = require('mongoose')

mongoose.connect('mongodb+srv://YuhangZhou:123564571...@cluster0.nwuuj7i.mongodb.net/?retryWrites=true&w=majority', {
    useNewUrlParser: true
})

const UserSchema = new mongoose.Schema({
    username: { type: String, unique: true },
    password: { 
        type: String,
        set(val) {
            return require('bcrypt').hashSync(val, 10)
        }
    }, 
})

const User = mongoose.model('User', UserSchema)
// User.db.dropCollection('users')
module.exports = { User }