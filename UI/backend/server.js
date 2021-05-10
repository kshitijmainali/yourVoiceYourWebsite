let express = require('express')
let cors = require('cors')
const app = express();

app.use(cors())
app.use(express.json())

//we ony work on one route and give display in one route
const listningRouter = require('./listningController');

app.use('/listen', listningRouter)

app.listen(5000, () => {
    console.log('app is started in port 5000')
})