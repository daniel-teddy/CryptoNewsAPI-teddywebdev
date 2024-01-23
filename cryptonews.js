const PORT = process.env.PORT || 8000;
const express = require('express');
const axios = require('axios');
const cheerio = require('cheerio');
const app = express();

const newspapers = [
    {
        name: 'cryptonews',
        address: 'https://cryptonews.com/news/',
        base: 'https://cryptonews.com'
    },
    {
        name: 'cryptonews',
        address: 'https://cryptonews.com/news/page/2/',
        base: 'https://cryptonews.com'
    },
    {
        name: 'cryptonews',
        address: 'https://cryptonews.com/news/page/3/',
        base: 'https://cryptonews.com'
    },
    {
        name: 'cryptonews',
        address: 'https://cryptonews.com/news/page/4/',
        base: 'https://cryptonews.com'
    },
];

const articles = [];

const fetchArticles = async (newspaper) => {
    try {
        const response = await axios.get(newspaper.address);
        const html = response.data;
        const $ = cheerio.load(html);

        // Handle articles within <article> tags
        $('article', html).each(function () {
            const articleElement = $(this);
            extractArticleDetails(articleElement, newspaper.base);
        });

        // Handle articles within <div class="news-one"> tags
        $('div.news-one', html).each(function () {
            const articleElement = $(this);
            extractNewsOneDetails(articleElement, newspaper.base);
        });
    } catch (error) {
        console.error(`Error fetching articles for ${newspaper.name}: ${error.message}`);
    }
};

const extractArticleDetails = (articleElement, base) => {
    const title = articleElement.find('a.article__title').text();
    const url = articleElement.find('a.article__title').attr('href');
    const imageUrl = articleElement.find('img.img-fluid').attr('src');
    const category = articleElement.find('a.article__badge--md').text().trim();
    const date = articleElement.find('.article__badge-date').attr('data-utctime');
    const shortDescription = articleElement.find('.short-description').text().trim();

    articles.push({
        title,
        url: base + url,
        imageUrl,
        category,
        date,
        shortDescription,
        source: newspapers[0].name // Assuming there is only one newspaper in the array
    });
};

const extractNewsOneDetails = (articleElement, base) => {
    const title = articleElement.find('div.news-one-title a').text();
    const url = articleElement.find('a').attr('href');
    const imageUrl = articleElement.find('img').attr('src');
    const category = articleElement.find('a.news-one-category').text().trim();
    const date = articleElement.find('.article__badge-date').attr('data-utctime');
    
    articles.push({
        title,
        url: base + url,
        imageUrl,
        category,
        date,
        shortDescription: '', // No short description in the news-one structure
        source: newspapers[0].name // Assuming there is only one newspaper in the array
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

app.get('/news', async (req, res) => {
    await fetchAllArticles();
    res.json(articles);
});

app.listen(PORT, () => console.log(`Server running on PORT ${PORT}`));
