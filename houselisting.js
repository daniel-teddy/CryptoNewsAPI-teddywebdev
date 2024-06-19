const PORT = process.env.PORT || 8000;
const express = require('express');
const axios = require('axios');
const cheerio = require('cheerio');
const app = express();

const newspapers = [
    {
        name: 'houses',
        address: 'https://zwandako.com/en/properties',
        base: 'https://zwandako.com/'
    },
    // {
    //     name: 'houses',
    //     address: 'https://zwandako.com/en/properties/page/2/',
    //     base: 'https://zwandako.com/'
    // },
    // {
    //     name: 'houses',
    //     address: 'https://zwandako.com/en/properties/page/3/',
    //     base: 'https://zwandako.com/'
    // },
    // {
    //     name: 'houses',
    //     address: 'https://zwandako.com/en/properties/page/4/',
    //     base: 'https://zwandako.com/'
    // },
];

const articles = [];

const fetchArticles = async (newspaper) => {
    try {
        const response = await axios.get(newspaper.address);
        const html = response.data;
        const $ = cheerio.load(html);

        // Handle articles within <article> tags
        $('div.item-wrap', html).each(function () {
            const articleElement = $(this);
            extractArticleDetails(articleElement, newspaper.base);
        });
    } catch (error) {
        console.error(`Error fetching houeses for ${newspaper.name}: ${error.message}`);
    }
};

const extractArticleDetails = (articleElement) => {
    const title = articleElement.find('li.item-price').text();
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
        title,
        imageUrl,
        address,
        category,
        shortDescription,
        whatsapp,
        details,
    });
};

const fetchAllArticles = async () => {
    for (const newspaper of newspapers) {
        await fetchArticles(newspaper);
    }
};

app.get('/', (req, res) => {
    res.json('Welcome to my Crypto News API\n\nGo to \n /news to see news articles \n');
});

app.get('/houses', async (req, res) => {
    await fetchAllArticles();
    res.json(articles);
    console.log(articles, 'zsfdsd')
});

app.listen(PORT, () => console.log(`Server running on PORT ${PORT}`));
