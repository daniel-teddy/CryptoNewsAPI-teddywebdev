const PORT = process.env.PORT || 8000
const express = require('express')
const axios = require('axios')
const cheerio = require('cheerio')
const app = express()

const newspapers = [
    {
        name: 'coinmarketcap',
        address: 'https://coinmarketcap.com/community/articles/',
        base: 'https://coinmarketcap.com'
    },
    // {
    //     name: 'coingecko',
    //     address: 'https://www.coingecko.com/en/news',
    //     base: ''
    // },
    {
        name: 'cryptonews',
        address: 'https://cryptonews.com/news/',
        base: 'https://cryptonews.com'
    },
]


const articles = []

newspapers.forEach(newspaper => {
    axios.get(newspaper.address)
        .then(response => {
            const html = response.data
            const $ = cheerio.load(html)

            $('a:contains("coin")' || 'a:contains("crypto")' || 'a:contains("web")' || 'a:contains("token")', html).each(function () {
                const title = $(this).text()
                const url = $(this).attr('href')

                articles.push({
                    title,
                    url: newspaper.base + url,
                    source: newspaper.name
                })
            })

        })
})

app.get('/', (req, res) => {
    res.json('Welcome to my Crypto News API\n\nGo to \n /news to see news articles \n');
  });
  

app.get('/news', (req, res) => {
    res.json(articles)
})

app.get('/news/:newspaperId', (req, res) => {
    const newspaperId = req.params.newspaperId

    const newspaperAddress = newspapers.filter(newspaper => newspaper.name == newspaperId)[0].address
    const newspaperBase = newspapers.filter(newspaper => newspaper.name == newspaperId)[0].base


    axios.get(newspaperAddress)
        .then(response => {
            const html = response.data
            const $ = cheerio.load(html)
            const specificArticles = []

            $('a:contains("coin")' || 'a:contains("crypto")' || 'a:contains("web")' || 'a:contains("token")', html).each(function () {
                const title = $(this).text()
                const url = $(this).attr('href')
                specificArticles.push({
                    title,
                    url: newspaperBase + url,
                    source: newspaperId
                })
            })
            res.json(specificArticles)
        }).catch(err => console.log(err))
})

app.listen(PORT, () => console.log(`server running on PORT ${PORT}`))
