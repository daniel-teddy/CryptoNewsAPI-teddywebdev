// fetching from vape nations


const PORT = process.env.PORT || 4005
const express = require('express')
const axios = require('axios')
const cheerio = require('cheerio')
const app = express()



const links = [
    /* disposable vapes */
    {
        type: 'disposable-vapes',
        address: 'https://vapenationcyprus.com/urun-kategori/disposable-vape-puffbar'
    },
    {
        type: 'disposable-vapes',
        address: 'https://vapenationcyprus.com/urun-kategori-disposable-vape-puffbar/2'
    },
    {
        type: 'disposable-vapes',
        address: 'https://vapenationcyprus.com/urun-kategori-disposable-vape-puffbar/3'
    },
    {
        type: 'disposable-vapes',
        address: 'https://vapenationcyprus.com/urun-kategori-disposable-vape-puffbar/4'
    },
    {
        type: 'disposable-vapes',
        address: 'https://vapenationcyprus.com/urun-kategori-disposable-vape-puffbar/5'
    },
    {
        type: 'disposable-vapes',
        address: 'https://vapenationcyprus.com/urun-kategori-disposable-vape-puffbar/6'
    },
    {
        type: 'disposable-vapes',
        address: 'https://vapenationcyprus.com/urun-kategori-disposable-vape-puffbar/7'
    },
    {
        type: 'disposable-vapes',
        address: 'https://vapenationcyprus.com/urun-kategori-disposable-vape-puffbar/8'
    },
    {
        type: 'disposable-vapes',
        address: 'https://vapenationcyprus.com/urun-kategori-disposable-vape-puffbar/9'
    },
    {
        type: 'disposable-vapes',
        address: 'https://vapenationcyprus.com/urun-kategori-disposable-vape-puffbar/10'
    },
    {
        type: 'disposable-vapes',
        address: 'https://vapenationcyprus.com/urun-kategori-disposable-vape-puffbar/11'
    },
    {
        type: 'disposable-vapes',
        address: 'https://vapenationcyprus.com/urun-kategori-disposable-vape-puffbar/12'
    },
    {
        type: 'disposable-vapes',
        address: 'https://vapenationcyprus.com/urun-kategori-disposable-vape-puffbar/13'
    },
    {
        type: 'disposable-vapes',
        address: 'https://vapenationcyprus.com/urun-kategori-disposable-vape-puffbar/14'
    },
    /* rechrageables */
    {
        type: 'rechargeable-vapes',
        address: 'https://vapenationcyprus.com/urun-kategori/vape-cihazlari',
    },
    {
        type: 'rechargeable-vapes',
        address: 'https://vapenationcyprus.com/urun-kategori-vape-cihazlari/2',
    },
    {
        type: 'rechargeable-vapes',
        address: 'https://vapenationcyprus.com/urun-kategori-vape-cihazlari/3',
    },
    {
        type: 'rechargeable-vapes',
        address: 'https://vapenationcyprus.com/urun-kategori-vape-cihazlari/4',
    },
    {
        type: 'rechargeable-vapes',
        address: 'https://vapenationcyprus.com/urun-kategori-vape-cihazlari/5',
    },
    /* free base liquids */
    {
        type: 'free-base-liquids',
        address: 'https://vapenationcyprus.com/urun-kategori/freebase-likitler-60-120ml',
    },
    {
        type: 'free-base-liquids',
        address: 'https://vapenationcyprus.com/urun-kategori-freebase-likitler-60-120ml/2',
    },
    /* salt liquids */
    {
        type: 'salt-liquid',
        address: 'https://vapenationcyprus.com/urun-kategori/salt-likitler-30-50-mg',
    },
    {
        type: 'salt-liquid',
        address: 'https://vapenationcyprus.com/urun-kategori-salt-likitler-30-50-mg/2',
    },
    /* coil and pods */
    {
        type: 'coils-pods',
        address: 'https://vapenationcyprus.com/urun-kategori/coil-ve-pod',
    },
    {
        type: 'coils-pods',
        address: 'https://vapenationcyprus.com/urun-kategori-coil-ve-pod/2',
    },
    {
        type: 'coils-pods',
        address: 'https://vapenationcyprus.com/urun-kategori-coil-ve-pod/3',
    },
    {
        type: 'coils-pods',
        address: 'https://vapenationcyprus.com/urun-kategori-coil-ve-pod/4',
    },
    {
        type: 'coils-pods',
        address: 'https://vapenationcyprus.com/urun-kategori-coil-ve-pod/5',
    }
]
const base = 'https://vapenationcyprus.com/'

const products = []

links.forEach(link => {
    axios.get(link.address)
        .then(response => {
            const html = response.data
            const $ = cheerio.load(html);
            
            $('div[class*=shop-item]').each((index, element) => {
                const href = $(element).find('a').attr('href');
                const img_link = $(element).find('img').attr('src')
                const item_name = $(element).find('div[class*=features]').find('span').text()
                const item_price = $(element).find('div[class*=price]').find('span').text()
                products.push(
                    {
                        item: item_name,
                        price: item_price,
                        type: link.type,
                        item_url: base+href,
                        item_image: base + img_link
                    }
                );    
              });
            
        })
})

app.get('/', (req, res) => {
    res.json('Welcome to my API')
    
})

app.get('/items', (req, res) => {
    res.json(products)
})
// console.log(links.length)

const newproducts = [
    {
    item: "SMOK NOVO 4",
    price: 40.00 + 2.5,
    type: "rechargeable-vapes",
    item_url: "https://vapenationcyprus.com/urun/smok-novo-4",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-15-at-15.53.38.jpeg"
  },
  {
    item: "VAPORESSO XROS 2 1000Mah 2 ML",
    price: 35.00 + 2.5,
    type: "rechargeable-vapes",
    item_url: "https://vapenationcyprus.com/urun/vaporesso-xros-2-1000mah-2-ml",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/Vape-kits-1-_Страница_01.jpg"
  },
  {
    item: "WENAX Stylus",
    price: 35.00 + 2.5,
    type: "rechargeable-vapes",
    item_url: "https://vapenationcyprus.com/urun/wenax-stylus",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/Vape-kits-1-_Страница_05.jpg"
  },
  {
    item: "MINIFIT MAX",
    price: 35.00 + 2.5,
    type: "rechargeable-vapes",
    item_url: "https://vapenationcyprus.com/urun/minifit-max",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/Vape-kits-1-_Страница_06.jpg"
  },
  {
    item: "Drag TPPX ",
    price: 95.00 + 2.5,
    type: "rechargeable-vapes",
    item_url: "https://vapenationcyprus.com/urun/drag-tppx",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/Vape-kits-1-_Страница_07.jpg"
  },
  {
    item: "Caliburn A2 POD SYSTEM",
    price: 35.00 + 2.5,
    type: "rechargeable-vapes",
    item_url: "https://vapenationcyprus.com/urun/caliburn-a2-pod-system",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/Vape-kits-1-_Страница_13.jpg"
  },
  {
    item: "JUSTFOG MINIFIT MAX",
    price: 30.00 + 2.5,
    type: "rechargeable-vapes",
    item_url: "https://vapenationcyprus.com/urun/justfog-minifit-max",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-15-at-15.53.38-2.jpeg"
  },
  {
    item: "VOOPOO DRAG X",
    price: 75.00 + 2.5,
    type: "rechargeable-vapes",
    item_url: "https://vapenationcyprus.com/urun/voopoo-drag-x",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-15-at-15.53.39-1.jpeg"
  },
  {
    item: "CALIBURN G",
    price: 35.00 + 2.5,
    type: "rechargeable-vapes",
    item_url: "https://vapenationcyprus.com/urun/caliburn-g",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-15-at-15.53.39-2.jpeg"
  },
  {
    item: "VOOPOO DRAG 3",
    price: 95.00 + 2.5,
    type: "rechargeable-vapes",
    item_url: "https://vapenationcyprus.com/urun/voopoo-drag-3",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-15-at-15.53.39.jpeg"
  },
  {
    item: "DRAG X PLUS",
    price: 85.00 + 2.5,
    type: "rechargeable-vapes",
    item_url: "https://vapenationcyprus.com/urun/drag-x-plus",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-15-at-15.53.40-1.jpeg"
  },
  {
    item: "VAPE PEN v2",
    price: 35.00 + 2.5,
    type: "rechargeable-vapes",
    item_url: "https://vapenationcyprus.com/urun/vape-pen-v2",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-15-at-15.53.40-2.jpeg"
  },
  {
    item: "Liberty Busted",
    price: 13.00 + 2.5,
    type: "free-base-liquids",
    item_url: "https://vapenationcyprus.com/urun/liberty-busted",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/IMG-20230111-WA0006.jpg"
  },
  {
    item: "Liberty Amnesia",
    price: 13.00 + 2.5,
    type: "free-base-liquids",
    item_url: "https://vapenationcyprus.com/urun/liberty-amnesia",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/IMG-20230111-WA0001.jpg"
  },
  {
    item: "Liberty Fusion Cream",
    price: 13.00 + 2.5,
    type: "free-base-liquids",
    item_url: "https://vapenationcyprus.com/urun/liberty-fusion-cream",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/IMG-20230111-WA0007.jpg"
  },
  {
    item: "Liberty Fizzy Crusher",
    price: 13.00 + 2.5,
    type: "free-base-liquids",
    item_url: "https://vapenationcyprus.com/urun/liberty-fizzy-crusher",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/IMG-20230111-WA0002.jpg"
  },
  {
    item: "Liberty Tropical Oasis",
    price: 13.00 + 2.5,
    type: "free-base-liquids",
    item_url: "https://vapenationcyprus.com/urun/liberty-tropical-oasis",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/IMG-20230111-WA0008.jpg"
  },
  {
    item: "Liberty Woo Woo",
    price: 13.00 + 2.5,
    type: "free-base-liquids",
    item_url: "https://vapenationcyprus.com/urun/liberty-woo-woo",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/IMG-20230111-WA0003.jpg"
  },
  {
    item: "Strawberry Raspberyy Cherry Ice 600",
    price: 8.00 + 2.5,
    type: "disposable-vapes",
    item_url: "https://vapenationcyprus.com/urun/strawberry-raspberyy-cherry-ice-600",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/283404841_4849448295184234_918331073210867008_n.jpg"
  },
  {
    item: "Elfbar Apple Peach 1500 Puffs",
    price: 14.00 + 2.5,
    type: "disposable-vapes",
    item_url: "https://vapenationcyprus.com/urun/elfbar-apple-peach-1500-puffs",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-15-at-15.51.39-1.jpeg"
  },
  {
    item: "Elfbar Blue Raspberry Lemonade 1500 Puffs",
    price: 14.00 + 2.5,
    type: "disposable-vapes",
    item_url: "https://vapenationcyprus.com/urun/elfbar-blue-raspberry-lemonade-1500-puffs",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-15-at-15.51.39.jpeg"
  },
  {
    item: "Dragbar Grape Ice 5000",
    price: 17.00 + 2.5,
    type: "disposable-vapes",
    item_url: "https://vapenationcyprus.com/urun/dragbar-grape-ice-5000",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-17-at-19.04.41-1.jpeg"
  },
  {
    item: "Dragbar Watermelon Ice 5000",
    price: 17.00 + 2.5,
    type: "disposable-vapes",
    item_url: "https://vapenationcyprus.com/urun/dragbar-watermelon-ice-5000",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-17-at-19.04.41.jpeg"
  },
  {
    item: "Dragbar Banana Ice 5000",
    price: 17.00 + 2.5,
    type: "disposable-vapes",
    item_url: "https://vapenationcyprus.com/urun/dragbar-banana-ice-5000",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-17-at-19.04.42-1.jpeg"
  },
  {
    item: "Dragbar Mango Guava 5000 ",
    price: 17.00 + 2.5,
    type: "disposable-vapes",
    item_url: "https://vapenationcyprus.com/urun/dragbar-mango-guava-5000",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-17-at-19.04.42.jpeg"
  },
  {
    item: "Elfbar Pink Lemonade 1500 Puffs",
    price: 14.00 + 2.5,
    type: "disposable-vapes",
    item_url: "https://vapenationcyprus.com/urun/elfbar-pink-lemonade-1500-puffs",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/IMG-20220908-WA0008.jpg"
  },
  {
    item: "Elfbar Blueberry Sour Raspberry 1500 Puffs",
    price: 14.00 + 2.5,
    type: "disposable-vapes",
    item_url: "https://vapenationcyprus.com/urun/elfbar-blueberry-sour-raspberry-1500-puffs",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/IMG-20220908-WA0007.jpg"
  },
  {
    item: "Elfbar Pineapple Peach Mango 1500 Puffs",
    price: 14.00 + 2.5,
    type: "disposable-vapes",
    item_url: "https://vapenationcyprus.com/urun/elfbar-pineapple-peach-mango-1500-puffs",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/IMG-20220908-WA0006.jpg"
  },
  {
    item: "Elfbar Cherry Lemon Peach 1500 Puffs",
    price: 14.00 + 2.5,
    type: "disposable-vapes",
    item_url: "https://vapenationcyprus.com/urun/elfbar-cherry-lemon-peach-1500-puffs",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/IMG-20220908-WA0005.jpg"
  },
  {
    item: "Elfbar Strawberry Ice Cream 1500 Puffs",
    price: 14.00 + 2.5,
    type: "disposable-vapes",
    item_url: "https://vapenationcyprus.com/urun/elfbar-strawberry-ice-cream-1500-puffs",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/IMG-20220908-WA0011.jpg"
  },
  {
    item: "Elfbar 2500 Banana Milk 50 MG Nicotine",
    price: 16.00 + 2.5,
    type: "disposable-vapes",
    item_url: "https://vapenationcyprus.com/urun/elfbar-2500-banana-milk-50-mg-nicotine",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/IMG-20230322-WA0009.jpg"
  },
  {
    item: "Elfbar Grape 1500 Puffs",
    price: 14.00 + 2.5,
    type: "disposable-vapes",
    item_url: "https://vapenationcyprus.com/urun/elfbar-grape-1500-puffs",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-15-at-15.51.36-2.jpeg"
  },
  {
    item: "Elfbar Mango 1500 Puffs",
    price: 14.00 + 2.5,
    type: "disposable-vapes",
    item_url: "https://vapenationcyprus.com/urun/elfbar-mango-1500-puffs",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-15-at-15.51.36.jpeg"
  },
  {
    item: "Elfbar Banana Ice 1500 Puffs",
    price: 14.00 + 2.5,
    type: "disposable-vapes",
    item_url: "https://vapenationcyprus.com/urun/elfbar-banana-ice-1500-puffs",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-15-at-15.51.37-1.jpeg"
  },
  {
    item: "Elfbar Blueberry 1500 Puffs",
    price: 14.00 + 2.5,
    type: "disposable-vapes",
    item_url: "https://vapenationcyprus.com/urun/elfbar-blueberry-1500-puffs",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-15-at-15.51.37-2.jpeg"
  },
  {
    item: "Elfbar Strawberry Ice Cream 1500 Puffs",
    price: 14.00 + 2.5,
    type: "disposable-vapes",
    item_url: "https://vapenationcyprus.com/urun/elfbar-strawberry-ice-cream-1500-puffs",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-15-at-15.51.37.jpeg"
  },
  {
    item: "Elfbar Strawberry Grape 1500 Puffs",
    price: 14.00 + 2.5,
    type: "disposable-vapes",
    item_url: "https://vapenationcyprus.com/urun/elfbar-strawberry-grape-1500-puffs",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-15-at-15.51.38.jpeg"
  },
  {
    item: "Elfbar Kivi Passion Fruit Guava 600",
    price: 8.00 + 2.5,
    type: "disposable-vapes",
    item_url: "https://vapenationcyprus.com/urun/elfbar-kivi-passion-fruit-guava-600",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-15-at-15.50.56.jpeg"
  },
  {
    item: "Elfbar Mango 600",
    price: 8.00 + 2.5,
    type: "disposable-vapes",
    item_url: "https://vapenationcyprus.com/urun/elfbar-mango-600",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-15-at-15.50.57-1.jpeg"
  },
  {
    item: "Elfbar Blueberry Sour Raspberry 600",
    price: 8.00 + 2.5,
    type: "disposable-vapes",
    item_url: "https://vapenationcyprus.com/urun/elfbar-blueberry-sour-raspberry-600",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-15-at-15.50.57.jpeg"
  },
  {
    item: "Elfbar Watermelon 600",
    price: 8.00 + 2.5,
    type: "disposable-vapes",
    item_url: "https://vapenationcyprus.com/urun/elfbar-watermelon-600",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-15-at-15.50.58-1.jpeg"
  },
  {
    item: "Elfbar Blueberry 600",
    price: 8.00 + 2.5,
    type: "disposable-vapes",
    item_url: "https://vapenationcyprus.com/urun/elfbar-blueberry-600",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-15-at-15.50.58.jpeg"
  },
  {
    item: "Elfbar Energy Ice 600",
    price: 8.00 + 2.5,
    type: "disposable-vapes",
    item_url: "https://vapenationcyprus.com/urun/elfbar-energy-ice-600",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-15-at-15.50.59-1.jpeg"
  },
  {
    item: "Elfbar Strawberry Kiwi 600",
    price: 8.00 + 2.5,
    type: "disposable-vapes",
    item_url: "https://vapenationcyprus.com/urun/elfbar-strawberry-kiwi-600",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-15-at-15.51.02-1.jpeg"
  },
  {
    item: "Elfbar Apple Peach 600",
    price: 8.00 + 2.5,
    type: "disposable-vapes",
    item_url: "https://vapenationcyprus.com/urun/elfbar-apple-peach-600",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-15-at-15.51.02.jpeg"
  },
  {
    item: "Elfbar Lyche Ice 600",
    price: 8.00 + 2.5,
    type: "disposable-vapes",
    item_url: "https://vapenationcyprus.com/urun/elfbar-lyche-ice-600",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-15-at-15.50.50.jpeg"
  },
  {
    item: "Elfbar Cola 1500 Puffs",
    price: 14.00 + 2.5,
    type: "disposable-vapes",
    item_url: "https://vapenationcyprus.com/urun/elfbar-cola-1500-puffs",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-15-at-15.51.34-1.jpeg"
  },
  {
    item: "Elfbar Kiwi Passion Fruit Guaba 1500 Puffs",
    price: 14.00 + 2.5,
    type: "disposable-vapes",
    item_url: "https://vapenationcyprus.com/urun/elfbar-kiwi-passion-fruit-guaba-1500-puffs",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-15-at-15.51.34.jpeg"
  },
  {
    item: "Elfbar Watermelon 1500 Puffs",
    price: 14.00 + 2.5,
    type: "disposable-vapes",
    item_url: "https://vapenationcyprus.com/urun/elfbar-watermelon-1500-puffs",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-15-at-15.51.36-1.jpeg"
  },
  {
    item: "Elfbar Strawberry Ice Cream 1500 Puffs",
    price: 14.00 + 2.5,
    type: "disposable-vapes",
    item_url: "https://vapenationcyprus.com/urun/elfbar-strawberry-ice-cream-1500-puffs",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/IMG-20220908-WA0011.jpg"
  },
  {
    item: "Elfbar 2500 Banana Milk 50 MG Nicotine",
    price: 16.00 + 2.5,
    type: "disposable-vapes",
    item_url: "https://vapenationcyprus.com/urun/elfbar-2500-banana-milk-50-mg-nicotine",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/IMG-20230322-WA0009.jpg"
  },
  {
    item: "ElfBar Lost Mary 600 Pink Lemonade",
    price: 8.00 + 2.5,
    type: "disposable-vapes",
    item_url: "https://vapenationcyprus.com/urun/elfbar-lost-mary-600-pink-lemonade",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/Elfbar-lost-600-20mg-170₺-1-_Страница_09.jpg"
  },
  {
    item: "MegaPuff 9000 Puffs Nicotinli 20 Mg",
    price: 16.00 + 2.5,
    type: "disposable-vapes",
    item_url: "https://vapenationcyprus.com/urun/megapuff-9000-puffs-nicotinli-20-mg",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/Изображение-WhatsApp-2022-10-21-в-14.56.58.jpg"
  },
  {
    item: "Elfbar Grape 1500 Puffs",
    price: 14.00 + 2.5,
    type: "disposable-vapes",
    item_url: "https://vapenationcyprus.com/urun/elfbar-grape-1500-puffs",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/IMG-20220908-WA0014.jpg"
  },
  {
    item: "ElfBar Lost Mary 600 Blueberry Sour Raspberry",
    price: 8.00 + 2.5,
    type: "disposable-vapes",
    item_url: "https://vapenationcyprus.com/urun/elfbar-lost-mary-600-blueberry-sour-raspberry",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/Elfbar-lost-600-20mg-170₺-1-_Страница_04.jpg"
  },
  {
    item: "Elfbar Grape 600",
    price: 8.00 + 2.5,
    type: "disposable-vapes",
    item_url: "https://vapenationcyprus.com/urun/elfbar-grape-600",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-15-at-15.50.59-2.jpeg"
  },
  {
    item: "Elfbar Strawberry Banana 600",
    price: 8.00 + 2.5,
    type: "disposable-vapes",
    item_url: "https://vapenationcyprus.com/urun/elfbar-strawberry-banana-600",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-15-at-15.50.59.jpeg"
  },
  {
    item: "Elfbar Peach Ice 600",
    price: 8.00 + 2.5,
    type: "disposable-vapes",
    item_url: "https://vapenationcyprus.com/urun/elfbar-peach-ice-600",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-15-at-15.51.00-1.jpeg"
  },
  {
    item: "Elfbar Banana Ice 600",
    price: 8.00 + 2.5,
    type: "disposable-vapes",
    item_url: "https://vapenationcyprus.com/urun/elfbar-banana-ice-600",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-15-at-15.51.00.jpeg"
  },
  {
    item: "Elfbar Cola 600",
    price: 8.00 + 2.5,
    type: "disposable-vapes",
    item_url: "https://vapenationcyprus.com/urun/elfbar-cola-600",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-15-at-15.51.01-1.jpeg"
  },
  {
    item: "Elfbar Pink Lemonade 600",
    price: 8.00 + 2.5,
    type: "disposable-vapes",
    item_url: "https://vapenationcyprus.com/urun/elfbar-pink-lemonade-600",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-15-at-15.51.01.jpeg"
  },
  {
    item: "Dragbar Peach Ice 5000",
    price: 17.00 + 2.5,
    type: "disposable-vapes",
    item_url: "https://vapenationcyprus.com/urun/dragbar-peach-ice-5000",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-17-at-19.04.44.jpeg"
  },
  {
    item: "Mango Milk Ice 600 ",
    price: 8.00 + 2.5,
    type: "disposable-vapes",
    item_url: "https://vapenationcyprus.com/urun/mango-milk-ice-600",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-08-10-at-14.24.27.jpeg"
  },
  {
    item: "Spearmint 600",
    price: 8.00 + 2.5,
    type: "disposable-vapes",
    item_url: "https://vapenationcyprus.com/urun/spearmint-600",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-08-10-at-14.24.28-1.jpeg"
  },
  {
    item: "Cherry 600",
    price: 8.00 + 2.5,
    type: "disposable-vapes",
    item_url: "https://vapenationcyprus.com/urun/cherry-600",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-08-10-at-14.24.28.jpeg"
  },
  {
    item: "Strawberry Ice Cream 600",
    price: 8.00 + 2.5,
    type: "disposable-vapes",
    item_url: "https://vapenationcyprus.com/urun/strawberry-ice-cream-600",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-08-10-at-14.24.29.jpeg"
  },
  {
    item: "Cotton Candy Ice 600",
    price: 8.00 + 2.5,
    type: "disposable-vapes",
    item_url: "https://vapenationcyprus.com/urun/cotton-candy-ice-600",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-08-10-at-14.24.30.jpeg"
  },
  {
    item: "Liberty Salt Ice Grape",
    price: 11.00 + 2.5,
    type: "salt-liquid",
    item_url: "https://vapenationcyprus.com/urun/liberty-salt-ice-grape",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-15-at-15.56.54-1.jpeg"
  },
  {
    item: "Liberty Salt Grape Peach",
    price: 11.00 + 2.5,
    type: "salt-liquid",
    item_url: "https://vapenationcyprus.com/urun/liberty-salt-grape-peach",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-15-at-15.56.54.jpeg"
  },
  {
    item: "Liberty Salt Caramel Tobacco",
    price: 11.00 + 2.5,
    type: "salt-liquid",
    item_url: "https://vapenationcyprus.com/urun/liberty-salt-caramel-tobacco",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-15-at-15.56.57.jpeg"
  },
  {
    item: "Liberty Salt Strawberry Cheesecake",
    price: 11.00 + 2.5,
    type: "salt-liquid",
    item_url: "https://vapenationcyprus.com/urun/liberty-salt-strawberry-cheesecake",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-15-at-15.56.59-1.jpeg"
  },
  {
    item: "Liberty Salt Blue Slash",
    price: 11.00 + 2.5,
    type: "salt-liquid",
    item_url: "https://vapenationcyprus.com/urun/liberty-salt-blue-slash",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-15-at-15.56.59.jpeg"
  },
  {
    item: "Liberty Salt Fusion Cream",
    price: 11.00 + 2.5,
    type: "salt-liquid",
    item_url: "https://vapenationcyprus.com/urun/liberty-salt-fusion-cream",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-15-at-15.57.00-1.jpeg"
  },
  {
    item: "Liberty Salt Mango Ice",
    price: 11.00 + 2.5,
    type: "salt-liquid",
    item_url: "https://vapenationcyprus.com/urun/liberty-salt-mango-ice",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-15-at-15.57.00-2.jpeg"
  },
  {
    item: "Liberty Salt Woo Woo",
    price: 11.00 + 2.5,
    type: "salt-liquid",
    item_url: "https://vapenationcyprus.com/urun/liberty-salt-woo-woo",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-15-at-15.57.00.jpeg"
  },
  {
    item: "Liberty Salt Lemonberry Breeze",
    price: 11.00 + 2.5,
    type: "salt-liquid",
    item_url: "https://vapenationcyprus.com/urun/liberty-salt-lemonberry-breeze",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-15-at-15.57.01-1.jpeg"
  },
  {
    item: "Liberty Salt Strawberry Ice Dream",
    price: 11.00 + 2.5,
    type: "salt-liquid",
    item_url: "https://vapenationcyprus.com/urun/liberty-salt-strawberry-ice-dream",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-15-at-15.57.01-2.jpeg"
  },
  {
    item: "Liberty Salt Coffee Tobacco",
    price: 11.00 + 2.5,
    type: "salt-liquid",
    item_url: "https://vapenationcyprus.com/urun/liberty-salt-coffee-tobacco",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-15-at-15.57.01.jpeg"
  },
  {
    item: "Liberty Salt Mentos Mint",
    price: 11.00 + 2.5,
    type: "salt-liquid",
    item_url: "https://vapenationcyprus.com/urun/liberty-salt-mentos-mint",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-15-at-15.57.02.jpeg"
  },
  {
    item: "Vaporesso XROS MINI",
    price: 35.00 + 2.5,
    type: "rechargeable-vapes",
    item_url: "https://vapenationcyprus.com/urun/vaporesso-xros-mini",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-15-at-15.53.35-1.jpeg"
  },
  {
    item: "NFIX Pro Kit",
    price: 40.00 + 2.5,
    type: "rechargeable-vapes",
    item_url: "https://vapenationcyprus.com/urun/nfix-pro-kit",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-15-at-15.53.35.jpeg"
  },
  {
    item: "WENAX K-1",
    price: 35.00 + 2.5,
    type: "rechargeable-vapes",
    item_url: "https://vapenationcyprus.com/urun/wenax-k-1",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-15-at-15.53.36.jpeg"
  },
  {
    item: "Liquideo",
    price: 45.00 + 2.5,
    type: "rechargeable-vapes",
    item_url: "https://vapenationcyprus.com/urun/liquideo",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-15-at-15.53.37-1.jpeg"
  },
  {
    item: "SMOK NORD",
    price: 50.00 + 2.5,
    type: "rechargeable-vapes",
    item_url: "https://vapenationcyprus.com/urun/smok-nord",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-15-at-15.53.37.jpeg"
  },
  {
    item: "ZERO",
    price: 35.00 + 2.5,
    type: "rechargeable-vapes",
    item_url: "https://vapenationcyprus.com/urun/zero",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-15-at-15.53.38-1.jpeg"
  },
  {
    item: "Elfbar Blue Razz Lemonade 1500 Puffs",
    price: 14.00 + 2.5,
    type: "disposable-vapes",
    item_url: "https://vapenationcyprus.com/urun/elfbar-blue-razz-lemonade-1500-puffs",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/IMG-20220908-WA0001.jpg"
  },
  {
    item: "Elfbar Spearmint 1500 Puffs",
    price: 14.00 + 2.5,
    type: "disposable-vapes",
    item_url: "https://vapenationcyprus.com/urun/elfbar-spearmint-1500-puffs",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/IMG-20220908-WA0003.jpg"
  },
  {
    item: "Elfbar Watermelon 1500 Puffs",
    price: 14.00 + 2.5,
    type: "disposable-vapes",
    item_url: "https://vapenationcyprus.com/urun/elfbar-watermelon-1500-puffs",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/IMG-20220908-WA0004.jpg"
  },
  {
    item: "Elfbar 2500 Pink Lemonade 50 MG Nicotine",
    price: 16.00 + 2.5,
    type: "disposable-vapes",
    item_url: "https://vapenationcyprus.com/urun/elfbar-2500-pink-lemonade-50-mg-nicotine",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/IMG-20230322-WA0002.jpg"
  },
  {
    item: "Elfbar 5000 Puffs 50 MG",
    price: 16.00 + 2.5,
    type: "disposable-vapes",
    item_url: "https://vapenationcyprus.com/urun/elfbar-5000-puffs-50-mg",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/Изображение-WhatsApp-2023-03-07-в-13.42.54.jpg"
  },
  {
    item: "ElfBar Lost Mary 600 Blueberry Sour Raspberry",
    price: 8.00 + 2.5,
    type: "disposable-vapes",
    item_url: "https://vapenationcyprus.com/urun/elfbar-lost-mary-600-blueberry-sour-raspberry",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/Elfbar-lost-600-20mg-170₺-1-_Страница_04.jpg"
  },
  {
    item: "Novo 4, NFixPro, XpoZPro Coils ",
    price: 18.00 + 2.5,
    type: "coils-pods",
    item_url: "https://vapenationcyprus.com/urun/novo-4-nfixpro-xpozpro-coils",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-28-at-18.10.05.jpeg"
  },
  {
    item: "Caliburn 1.4 Pods",
    price: 15.00 + 2.5,
    type: "coils-pods",
    item_url: "https://vapenationcyprus.com/urun/caliburn-1-4-pods",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-28-at-18.10.06-1.jpeg"
  },
  {
    item: "Baby Coils ",
    price: 13.00 + 2.5,
    type: "coils-pods",
    item_url: "https://vapenationcyprus.com/urun/baby-coils",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-28-at-18.10.06-2.jpeg"
  },
  {
    item: "Wenax K1 Coils 5 Pieces",
    price: 15.00 + 2.5,
    type: "coils-pods",
    item_url: "https://vapenationcyprus.com/urun/wenax-k1-coils-5-pieces",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-28-at-18.10.06.jpeg"
  },
  {
    item: "Smok Nucig Mini V2 S1 ",
    price: 14.00 + 2.5,
    type: "coils-pods",
    item_url: "https://vapenationcyprus.com/urun/smok-nucig-mini-v2-s1",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-28-at-18.10.07-1.jpeg"
  },
  {
    item: "Smok Tfv12 Prince Coils",
    price: 13.00 + 2.5,
    type: "coils-pods",
    item_url: "https://vapenationcyprus.com/urun/smok-tfv12-prince-coils",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-28-at-18.10.07.jpeg"
  },
  {
    item: "Liberty Kamikaze",
    price: 13.00 + 2.5,
    type: "free-base-liquids",
    item_url: "https://vapenationcyprus.com/urun/liberty-kamikaze",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/IMG-20230111-WA0004.jpg"
  },
  {
    item: "Liberty Sixty 9",
    price: 13.00 + 2.5,
    type: "free-base-liquids",
    item_url: "https://vapenationcyprus.com/urun/liberty-sixty-9",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/IMG-20230111-WA0005.jpg"
  },
  {
    item: "Liberty Blue Slash",
    price: 13.00 + 2.5,
    type: "free-base-liquids",
    item_url: "https://vapenationcyprus.com/urun/liberty-blue-slash",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/IMG-20230111-WA0009.jpg"
  },
  {
    item: "Liberty Watermelon",
    price: 13.00 + 2.5,
    type: "free-base-liquids",
    item_url: "https://vapenationcyprus.com/urun/liberty-watermelon",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/IMG-20230111-WA0010.jpg"
  },
  {
    item: "Caliburn G2 POD SYSTEM",
    price: 40.00 + 2.5,
    type: "rechargeable-vapes",
    item_url: "https://vapenationcyprus.com/urun/caliburn-g2-pod-system",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/Vape-kits-1-_Страница_15.jpg"
  },
  {
    item: "SMOK NFIX KIT PRO",
    price: 40.00 + 2.5,
    type: "rechargeable-vapes",
    item_url: "https://vapenationcyprus.com/urun/smok-nfix-kit-pro",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/Vape-kits-1-_Страница_16.jpg"
  },
  {
    item: "Voopoo ARGUS PRO",
    price: 50.00 + 2.5,
    type: "rechargeable-vapes",
    item_url: "https://vapenationcyprus.com/urun/voopoo-argus-pro",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/Vape-kits-1-_Страница_17.jpg"
  },
  {
    item: "Caliburn TENET ",
    price: 40.00 + 2.5,
    type: "rechargeable-vapes",
    item_url: "https://vapenationcyprus.com/urun/caliburn-tenet",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/Изображение-WhatsApp-2023-03-07-в-13.43.14.jpg"
  },
  {
    item: "Caliburn TENET KOKO",
    price: 40.00 + 2.5,
    type: "rechargeable-vapes",
    item_url: "https://vapenationcyprus.com/urun/caliburn-tenet-koko",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/Изображение-WhatsApp-2023-03-07-в-13.43.12.jpg"
  },
  {
    item: "CALIBURN GK2",
    price: 40.00 + 2.5,
    type: "rechargeable-vapes",
    item_url: "https://vapenationcyprus.com/urun/caliburn-gk2",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-15-at-15.53.29.jpeg"
  },
  {
    item: "Elfbar Watermelon 1500 Puffs",
    price: 14.00 + 2.5,
    type: "disposable-vapes",
    item_url: "https://vapenationcyprus.com/urun/elfbar-watermelon-1500-puffs",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/IMG-20220908-WA0004.jpg"
  },
  {
    item: "Elfbar 5000 Puffs ",
    price: 16.00 + 2.5,
    type: "disposable-vapes",
    item_url: "https://vapenationcyprus.com/urun/elfbar-5000-puffs",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/Изображение-WhatsApp-2023-01-03-в-14.54.50.jpg"
  },
  {
    item: "Elfbar Strawberry Kiwi 1500 Puffs",
    price: 14.00 + 2.5,
    type: "disposable-vapes",
    item_url: "https://vapenationcyprus.com/urun/elfbar-strawberry-kiwi-1500-puffs",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/IMG-20220908-WA0002.jpg"
  },
  {
    item: "Elfbar Cherry Lemon Peach 1500 Puffs",
    price: 14.00 + 2.5,
    type: "disposable-vapes",
    item_url: "https://vapenationcyprus.com/urun/elfbar-cherry-lemon-peach-1500-puffs",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/IMG-20220908-WA0005.jpg"
  },
  {
    item: "Elfbar 2500 Banana Milk 50 MG Nicotine",
    price: 16.00 + 2.5,
    type: "disposable-vapes",
    item_url: "https://vapenationcyprus.com/urun/elfbar-2500-banana-milk-50-mg-nicotine",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/IMG-20230322-WA0009.jpg"
  },
  {
    item: "Elfbar Spearmint 1500 Puffs",
    price: 14.00 + 2.5,
    type: "disposable-vapes",
    item_url: "https://vapenationcyprus.com/urun/elfbar-spearmint-1500-puffs",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/IMG-20220908-WA0003.jpg"
  },
  {
    item: "Elfbar Strawberry Ice Cream 1500 Puffs",
    price: 14.00 + 2.5,
    type: "disposable-vapes",
    item_url: "https://vapenationcyprus.com/urun/elfbar-strawberry-ice-cream-1500-puffs",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/IMG-20220908-WA0011.jpg"
  },
  {
    item: "Elfbar Strawberry Grape 1500 Puffs",
    price: 14.00 + 2.5,
    type: "disposable-vapes",
    item_url: "https://vapenationcyprus.com/urun/elfbar-strawberry-grape-1500-puffs",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/IMG-20220908-WA0010.jpg"
  },
  {
    item: "Elfbar Peach Ice 1500 Puffs",
    price: 14.00 + 2.5,
    type: "disposable-vapes",
    item_url: "https://vapenationcyprus.com/urun/elfbar-peach-ice-1500-puffs",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/IMG-20220908-WA0009.jpg"
  },
  {
    item: "MegaPuff 9000 Puffs Nicotinli 20 Mg",
    price: 16.00 + 2.5,
    type: "disposable-vapes",
    item_url: "https://vapenationcyprus.com/urun/megapuff-9000-puffs-nicotinli-20-mg",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/Изображение-WhatsApp-2022-10-21-в-14.56.58.jpg"
  },
  {
    item: "Elfbar Grape 1500 Puffs",
    price: 14.00 + 2.5,
    type: "disposable-vapes",
    item_url: "https://vapenationcyprus.com/urun/elfbar-grape-1500-puffs",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/IMG-20220908-WA0014.jpg"
  },
  {
    item: "Elfbar Pineapple Peach Mango 1500 Puffs",
    price: 14.00 + 2.5,
    type: "disposable-vapes",
    item_url: "https://vapenationcyprus.com/urun/elfbar-pineapple-peach-mango-1500-puffs",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/IMG-20220908-WA0006.jpg"
  },
  {
    item: "XRos Pods ",
    price: 10.00 + 2.5,
    type: "coils-pods",
    item_url: "https://vapenationcyprus.com/urun/xros-pods",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-28-at-18.10.13-1.jpeg"
  },
  {
    item: "Cotton Bacon",
    price: 8.00 + 2.5,
    type: "coils-pods",
    item_url: "https://vapenationcyprus.com/urun/cotton-bacon",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-28-at-18.10.13.jpeg"
  },
  {
    item: "RPM 1.0 Coils ",
    price: 18.00 + 2.5,
    type: "coils-pods",
    item_url: "https://vapenationcyprus.com/urun/rpm-1-0-coils",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-28-at-18.10.14-1.jpeg"
  },
  {
    item: "NFix Pods ",
    price: 14.00 + 2.5,
    type: "coils-pods",
    item_url: "https://vapenationcyprus.com/urun/nfix-pods",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-28-at-18.10.14.jpeg"
  },
  {
    item: "Smok Nord Coil",
    price: 18.00 + 2.5,
    type: "coils-pods",
    item_url: "https://vapenationcyprus.com/urun/smok-nord-coil",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-28-at-18.10.07-2.jpeg"
  },
  {
    item: "Zero Pods ",
    price: 10.00 + 2.5,
    type: "coils-pods",
    item_url: "https://vapenationcyprus.com/urun/zero-pods",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-28-at-18.10.08-1.jpeg"
  },
  {
    item: "1.2 PnP Metal Coils",
    price: 18.00 + 2.5,
    type: "coils-pods",
    item_url: "https://vapenationcyprus.com/urun/1-2-pnp-metal-coils",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-28-at-18.10.08-2.jpeg"
  },
  {
    item: "Minifit Pods",
    price: 13.00 + 2.5,
    type: "coils-pods",
    item_url: "https://vapenationcyprus.com/urun/minifit-pods",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-28-at-18.10.08.jpeg"
  },
  {
    item: "0.3 PnP Coils ",
    price: 18.00 + 2.5,
    type: "coils-pods",
    item_url: "https://vapenationcyprus.com/urun/0-3-pnp-coils",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-28-at-18.10.09-1.jpeg"
  },
  {
    item: "0.15 PnP Coils",
    price: 18.00 + 2.5,
    type: "coils-pods",
    item_url: "https://vapenationcyprus.com/urun/0-15-pnp-coils",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-28-at-18.10.09.jpeg"
  },
  {
    item: "ElfBar Lost Mary 600 Tripple Mango",
    price: 8.00 + 2.5,
    type: "disposable-vapes",
    item_url: "https://vapenationcyprus.com/urun/elfbar-lost-mary-600-tripple-mango",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/Elfbar-lost-600-20mg-170₺-1-_Страница_07.jpg"
  },
  {
    item: "Elfbar Spearmint 600 ",
    price: 8.00 + 2.5,
    type: "disposable-vapes",
    item_url: "https://vapenationcyprus.com/urun/elfbar-spearmint-600",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-15-at-15.50.53-1.jpeg"
  },
  {
    item: "Elfbar Pineapple Peach Mango 600 ",
    price: 8.00 + 2.5,
    type: "disposable-vapes",
    item_url: "https://vapenationcyprus.com/urun/elfbar-pineapple-peach-mango-600",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-15-at-15.50.53.jpeg"
  },
  {
    item: "Elfbar Strawberry Ice 600",
    price: 8.00 + 2.5,
    type: "disposable-vapes",
    item_url: "https://vapenationcyprus.com/urun/elfbar-strawberry-ice-600",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-15-at-15.50.54.jpeg"
  },
  {
    item: "Elfbar Strawberry Energy 600",
    price: 8.00 + 2.5,
    type: "disposable-vapes",
    item_url: "https://vapenationcyprus.com/urun/elfbar-strawberry-energy-600",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-15-at-15.50.55-1.jpeg"
  },
  {
    item: "Elfbar Cream Tobacco 600",
    price: 8.00 + 2.5,
    type: "disposable-vapes",
    item_url: "https://vapenationcyprus.com/urun/elfbar-cream-tobacco-600",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-15-at-15.50.55.jpeg"
  },
  {
    item: "ElfBar Lost Mary 600 Tripple Mango",
    price: 8.00 + 2.5,
    type: "disposable-vapes",
    item_url: "https://vapenationcyprus.com/urun/elfbar-lost-mary-600-tripple-mango",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/Elfbar-lost-600-20mg-170₺-1-_Страница_07.jpg"
  },
  {
    item: "ElfBar Lost Mary 600 Cotton Candy Ice",
    price: 8.00 + 2.5,
    type: "disposable-vapes",
    item_url: "https://vapenationcyprus.com/urun/elfbar-lost-mary-600-cotton-candy-ice",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/Elfbar-lost-600-20mg-170₺-1-_Страница_06.jpg"
  },
  {
    item: "ElfBar Lost Mary 600 Blue Razz Ice",
    price: 8.00 + 2.5,
    type: "disposable-vapes",
    item_url: "https://vapenationcyprus.com/urun/elfbar-lost-mary-600-blue-razz-ice",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/Elfbar-lost-600-20mg-170₺-1-_Страница_05.jpg"
  },
  {
    item: "ElfBar Lost Mary 600 Blueberry Sour Raspberry",
    price: 8.00 + 2.5,
    type: "disposable-vapes",
    item_url: "https://vapenationcyprus.com/urun/elfbar-lost-mary-600-blueberry-sour-raspberry",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/Elfbar-lost-600-20mg-170₺-1-_Страница_04.jpg"
  },
  {
    item: "ElfBar Lost Mary 600 KIWI PASSION FRUIT GUAVA",
    price: 8.00 + 2.5,
    type: "disposable-vapes",
    item_url: "https://vapenationcyprus.com/urun/elfbar-lost-mary-600-kiwi-passion-fruit-guava",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/Elfbar-lost-600-20mg-170₺-1-_Страница_03.jpg"
  },
  {
    item: "ElfBar Lost Mary 600 Blueberry",
    price: 8.00 + 2.5,
    type: "disposable-vapes",
    item_url: "https://vapenationcyprus.com/urun/elfbar-lost-mary-600-blueberry",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/Elfbar-lost-600-20mg-170₺-1-_Страница_02.jpg"
  },
  {
    item: "Caliburn A2 Pods",
    price: 15.00 + 2.5,
    type: "coils-pods",
    item_url: "https://vapenationcyprus.com/urun/caliburn-a2-pods",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-28-at-18.10.00.jpeg"
  },
  {
    item: "Caliburn G Coils",
    price: 15.00 + 2.5,
    type: "coils-pods",
    item_url: "https://vapenationcyprus.com/urun/caliburn-g-coils",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-28-at-18.10.03-1.jpeg"
  },
  {
    item: "GTX Go Coils 5 Pieces",
    price: 18.00 + 2.5,
    type: "coils-pods",
    item_url: "https://vapenationcyprus.com/urun/gtx-go-coils-5-pieces",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-28-at-18.10.03.jpeg"
  },
  {
    item: "Drag 3 Coils ",
    price: 13.00 + 2.5,
    type: "coils-pods",
    item_url: "https://vapenationcyprus.com/urun/drag-3-coils",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-28-at-18.10.04-1.jpeg"
  },
  {
    item: "Caliburn G Pod ",
    price: 12.00 + 2.5,
    type: "coils-pods",
    item_url: "https://vapenationcyprus.com/urun/caliburn-g-pod",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-28-at-18.10.04.jpeg"
  },
  {
    item: "Wenax K1 Pods ",
    price: 14.00 + 2.5,
    type: "coils-pods",
    item_url: "https://vapenationcyprus.com/urun/wenax-k1-pods",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-28-at-18.10.05-1.jpeg"
  },
  {
    item: "SMOK NFIX KIT",
    price: 35.00 + 2.5,
    type: "rechargeable-vapes",
    item_url: "https://vapenationcyprus.com/urun/smok-nfix-kit",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-15-at-15.53.40.jpeg"
  },
  {
    item: "SMOK NORD 4 KIT",
    price: 55.00 + 2.5,
    type: "rechargeable-vapes",
    item_url: "https://vapenationcyprus.com/urun/smok-nord-4-kit",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-15-at-15.53.41-1.jpeg"
  },
  {
    item: "SMOK NORD 2",
    price: 35.00 + 2.5,
    type: "rechargeable-vapes",
    item_url: "https://vapenationcyprus.com/urun/smok-nord-2",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-15-at-15.53.41-2.jpeg"
  },
  {
    item: "VAPORESSO OSMALL",
    price: 35.00 + 2.5,
    type: "rechargeable-vapes",
    item_url: "https://vapenationcyprus.com/urun/vaporesso-osmall",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-15-at-15.53.41.jpeg"
  },
  {
    item: "Uwell Caliburn A2 Pod Kit",
    price: 35.00 + 2.5,
    type: "rechargeable-vapes",
    item_url: "https://vapenationcyprus.com/urun/uwell-caliburn-a2-pod-kit",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-15-at-15.53.42-1.jpeg"
  },
  {
    item: "VAPORESSO GTX GO",
    price: 35.00 + 2.5,
    type: "rechargeable-vapes",
    item_url: "https://vapenationcyprus.com/urun/vaporesso-gtx-go",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-15-at-15.53.42.jpeg"
  },
  {
    item: "Smok Novo X Pods ",
    price: 13.00 + 2.5,
    type: "coils-pods",
    item_url: "https://vapenationcyprus.com/urun/smok-novo-x-pods",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-28-at-18.10.11-1.jpeg"
  },
  {
    item: "RPM 2 Coils",
    price: 15.00 + 2.5,
    type: "coils-pods",
    item_url: "https://vapenationcyprus.com/urun/rpm-2-coils",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-28-at-18.10.11-2.jpeg"
  },
  {
    item: "Vaporesso OSmall Pods",
    price: 10.00 + 2.5,
    type: "coils-pods",
    item_url: "https://vapenationcyprus.com/urun/vaporesso-osmall-pods",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-28-at-18.10.11-3.jpeg"
  },
  {
    item: "RPM Mesh 0.4 Coil",
    price: 18.00 + 2.5,
    type: "coils-pods",
    item_url: "https://vapenationcyprus.com/urun/rpm-mesh-0-4-coil",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-28-at-18.10.11.jpeg"
  },
  {
    item: "Vape Pen Coils ",
    price: 18.00 + 2.5,
    type: "coils-pods",
    item_url: "https://vapenationcyprus.com/urun/vape-pen-coils",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-28-at-18.10.12-1.jpeg"
  },
  {
    item: "Samsung Battery",
    price: 10.00 + 2.5,
    type: "coils-pods",
    item_url: "https://vapenationcyprus.com/urun/samsung-battery",
    item_image: "https://vapenationcyprus.com/tema/genel/uploads/urunler/WhatsApp-Image-2022-06-28-at-18.10.12-2.jpeg"
  }
]
app.get('/items/new', (req, res) => {
    res.json(newproducts)
})

app.listen(PORT, () => console.log(`server running on PORT http://localhost:${PORT}`))
