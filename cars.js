const PORT = process.env.PORT || 8000;
const express = require('express');
const axios = require('axios');
const cheerio = require('cheerio');
const app = express();
const cors = require('cors');

app.use(cors());

const newspapers = [
    {
        name: 'cars',
        address: 'https://cd.coinafrique.com/categorie/voitures',
        base: 'https://cd.coinafrique.com/'
    },
    // {
    //     name: 'cars',
    //     address: 'https://www.motukanayo.com/petites-annonces-voitures?page=2',
    //     base: 'https://www.motukanayo.com/'
    // },
    // {
    //     name: 'cars',
    //     address: 'https://www.motukanayo.com/petites-annonces-voitures?page=3',
    //     base: 'https://www.motukanayo.com/'
    // },
    // {
    //     name: 'cars',
    //     address: 'https://www.motukanayo.com/petites-annonces-voitures?page=4',
    //     base: 'https://www.motukanayo.com/'
    // },
];

let articles = [];

const fetchArticles = async (newspaper) => {
    try {
        const response = await axios.get(newspaper.address);
        const html = response.data;
        const $ = cheerio.load(html);

        $('div.card', html).each(function () {
            const articleElement = $(this);
            extractArticleDetails(articleElement, newspaper.base);
        });
    } catch (error) {
        console.error(`Error fetching cars for ${newspaper.name}: ${error.message}`);
    }
};

const extractArticleDetails = (articleElement) => {
    const price = articleElement.find('p.ad__card-price').text();
    const address = articleElement.find('p.ad__card-location').find('span').text().trim();
    const imageUrl = articleElement.find('img.ad__card-img').attr('src');
    // const category = articleElement.find('li.h-type').find('span').text().trim();
    const shortDescription = articleElement.find('p.ad__card-description').find('a').text().trim();
    // const whatsapp = articleElement.find('a.btn-item').attr('href');
    // const beds = articleElement.find('li.h-beds').find('.hz-figure').text();
    // const garage = articleElement.find('li.h-cars').find('.hz-figure').text();
    // const bathroom = articleElement.find('li.h-baths').find('.hz-figure').text();

    // const details = [];
    // details.push({
    //     beds,
    //     bathroom,
    //     garage
    // });

    articles.push({
        price,
        imageUrl,
        address,
        // category,
        shortDescription,
        // whatsapp,
        // details,
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
    res.json('Welcome to my cars Listings API\n\nGo to \n /cars to see cars listings \n');
});

app.get('/cars', async (req, res) => {
    const page = parseInt(req.query.page) || 1;
    const paginatedArticles = await fetchAllArticles(page);
    res.json(paginatedArticles);
});

app.listen(PORT, () => console.log(`Server running on PORT ${PORT}`));
