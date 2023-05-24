const { User } = require('./models')

const express = require('express')
const jwt = require('jsonwebtoken')

const { application } = require('express')

const app = express()
const SECRET = 'asdgsmnfgiow3940tj92j2q43tr'
app.use(express.json())

app.get('/api/users', async(req, res) => {
    const users = await User.find()
    res.send(users)
})

app.post('/api/register', async(req, res) => {
    // console.log(req.body)
    // res.send('register')
    const user = await User.create({
        username: req.body.username,
        password: req.body.password,
    })
    res.send(user)
})

app.post('/api/login', async(req, res) => {
    const user = await User.findOne({
        username: req.body.username
    })
    if (!user) {
        return res.status(422).send({
            message: 'user do not exit'
        })
    }
    const isPasswordValid = require('bcrypt').compareSync(
        req.body.password,
        user.password
    )
    if (!isPasswordValid) {
        return res.status(422).send({
            message: 'password invalid'
        })
    }
    // 生成token
    const jwt = require('jsonwebtoken')
    const token = jwt.sign({
        id: String(user._id),
    }, SECRET)
    
    res.send({
        user,
        token: token
    })
})


const auth = async(req, res, next) => {
    const raw = String(req.headers.authorization).split(' ').pop()
    const { id } = jwt.verify(raw, SECRET)
    req.user = await User.findById(id)
    next()
}

app.get('/api/profile', auth, async(req, res) => {
    // const raw = String(req.headers.authorization).split(' ').pop()
    // const { id } = jwt.verify(raw, SECRET)
    // const user = await User.findById(id)
    res.send(req.user)
})

app.get('/api/orders', auth, async(req, res) => {
    const orders = await Orders.find().where({
        user: req.user
    })
    res.send(orders)
})


app.listen(3001, () => {
    console.log('http://localhost:3001')
})




