const PORT = process.env.PORT || 8000;
const express = require('express');
const axios = require('axios');
const cheerio = require('cheerio');
const app = express();
const cors = require('cors');

app.use(cors());

const newspapers = [
    {
        name: 'houses',
        address: 'https://zwandako.com/en/properties/   ',
        base: 'https://zwandako.com/'
    },
    {
        name: 'houses',
        address: 'https://zwandako.com/en/properties/page/2/',
        base: 'https://zwandako.com/'
    },
    {
        name: 'houses',
        address: 'https://zwandako.com/en/properties/page/3/',
        base: 'https://zwandako.com/'
    },
    {
        name: 'houses',
        address: 'https://zwandako.com/en/properties/page/4/',
        base: 'https://zwandako.com/'
    },
];

let articles = [];

const fetchArticles = async (newspaper) => {
    try {
        const response = await axios.get(newspaper.address);
        const html = response.data;
        const $ = cheerio.load(html);

        $('div.item-wrap', html).each(function () {
            const articleElement = $(this);
            extractArticleDetails(articleElement, newspaper.base);
        });
    } catch (error) {
        console.error(`Error fetching houses for ${newspaper.name}: ${error.message}`);
    }
};

const extractArticleDetails = (articleElement) => {
    const price = articleElement.find('li.item-price').text();
    const address = articleElement.find('address.item-address').text();
    const imageUrl = articleElement.find('img.img-fluid').attr('data-src');
    const category = articleElement.find('li.h-type').find('span').text().trim();
    const shortDescription = articleElement.find('h2.item-title').find('a').text().trim();
    const whatsapp = articleElement.find('a.btn-item').attr('href');
    const beds = articleElement.find('li.h-beds').find('.hz-figure').text();
    const garage = articleElement.find('li.h-cars').find('.hz-figure').text();
    const bathroom = articleElement.find('li.h-baths').find('.hz-figure').text();

    const details = [];
    details.push({
        beds,
        bathroom,
        garage
    });

    articles.push({
        price,
        imageUrl,
        address,
        category,
        shortDescription,
        whatsapp,
        details,
    });
};

const fetchAllArticles = async (page) => {
    articles = [];
    const startIndex = (page - 1) * 10;
    const endIndex = page * 10;

    for (let i = 0; i < newspapers.length; i++) {
        await fetchArticles(newspapers[i]);
    }

    return articles.slice(startIndex, endIndex);
};

app.get('/', (req, res) => {
    res.json('Welcome to my House Listings API\n\nGo to \n /houses to see house listings \n');
});

app.get('/houses', async (req, res) => {
    const page = parseInt(req.query.page) || 1;
    const paginatedArticles = await fetchAllArticles(page);
    res.json(paginatedArticles);
});

app.listen(PORT, () => console.log(`Server running on PORT ${PORT}`));
