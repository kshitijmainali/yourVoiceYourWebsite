const express = require('express')
Router = express.Router()

const listenTo = (req, res) => {
    console.log('abc')
    res.send('request received')
}


Router.route('/').get(listenTo);

module.exports = Router;