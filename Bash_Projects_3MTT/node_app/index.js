const express = require('express')
const app = express()
const port = 3000

app.get('/', (req, res) => {
  res.send('Hello World! from Bashman 3MTT Programe Dev')
})

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
})

