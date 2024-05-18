const PORT = process.env.PORT || 8000;
const express = require("express");
const app = express();

const museums = require("./museums");
const restaurants = require("./restaurants");
const hospitals = require("./hospital");
const hotels = require("./hotels");
const officials = require("./officials");
const pharmacies = require("./pharmacies");

const allPlaces = [
  ...museums,
  ...restaurants,
  ...hospitals,
  ...hotels,
  ...officials,
  ...pharmacies,
];
const events = [
  {
    eventId: 1,
    category: "category",
    eventLocalAddress: "All hotels and restaurants",
    eventName: "New Year's Day",
    Description:
      "January 1st marks the beginning of the year, and like in many other countries, it is celebrated with fireworks, parties, and special events.",
    date_range: {
      start_date: "2025-01-01",
      end_date: "2024-01-01",
    },
    image:
      "https://www.cyprusparadise.com/media/17492/new-years-day-north-cyprus.jpg",
    location: {
      link: "https://bit.ly/4dHHmqL",
      local_range: {
        latitude: "35.32691673875462",
        longitude: "33.30850257065095",
      },
    },
    added_by_user: 1,
  },
  {
    eventId: 2,
    category: "culture",
    eventLocalAddress: "4WGV+X8 Famagusta",
    eventName: "Famagusta Culture and Art Days",
    Description:
      "The Famagusta Culture and Art Days is an annual event that celebrates the rich cultural heritage of Famagusta, a city located in the eastern part of North Cyprus. The event takes place during the months of August to September and features a wide range of cultural and artistic activities.",
    date_range: {
      start_date: "2024-08-01",
      end_date: "2024-09-26",
    },
    image:
      "https://www.cyprusparadise.com/media/17495/art-craft-north-cyprus.jpg",
    location: {
      link: "https://bit.ly/4dHb6UB",
      local_range: {
        latitude: "35.12758664490059",
        longitude: "33.943323224614126",
      },
    },
    added_by_user: 1,
  },
  {
    eventId: 3,
    category: "entertainment",
    eventLocalAddress: "Bellapais Abbey, Kyrenia",
    eventName: "International Bellapais Music Festival",
    Description:
      "Held in June and July, this festival brings together international and local musicians for a series of classical music performances in the beautiful Bellapais Abbey.",
    date_range: {
      start_date: "2024-06-06",
      end_date: "2024-07-09",
    },
    image:
      "https://www.cyprusparadise.com/media/17495/art-craft-north-cyprus.jpg",
    location: {
      link: "https://bit.ly/4bMaWcZ",
      local_range: {
        latitude: "35.30726511896368",
        longitude: "33.355242800000006",
      },
    },
    added_by_user: 1,
  },
  {
    eventId: 4,
    category: "entertainment",
    eventLocalAddress: "Bellapais Abbey, Kyrenia",
    eventName: "Orange Festival",
    Description:
      "Since 1977, this event held by Guzelyurt Municipality, has been the venue for a festival that originally celebrated the orange harvest.",
    date_range: {
      start_date: "2024-06-27",
      end_date: "2024-07-10",
    },
    image:
      "https://www.visitncy.com/wp-content/uploads/2020/02/Orange-Festival-9.jpg",
    location: {
      link: "https://bit.ly/4bMbnE9",
      local_range: {
        latitude: "35.20352364355105",
        longitude: "32.98992623673244",
      },
    },
    added_by_user: 1,
  },
  {
    eventId: 5,
    category: "entertainment",
    eventLocalAddress: "TATLISU4, BOZDAG STR ISKELE",
    eventName: "tatlisu carob festival",
    Description:
      "This annual festival held by the Tatlisu Municipality contributes to promotion of the region and the continuation of carob and molasses production.",
    date_range: {
      start_date: "2024-06-06",
      end_date: "2024-07-07",
    },
    image:
      "https://www.visitncy.com/wp-content/uploads/2020/02/Tatlisu-Carob-Festival-2.jpg",
    location: {
      link: "https://bit.ly/44OLxwJ",
      local_range: {
        latitude: "35.33098707612464",
        longitude: "33.76260637783909",
      },
    },
    added_by_user: 1,
  },
  {
    eventId: 6,
    category: "entertainment",
    eventLocalAddress: "Kyrenia, North Cyprus",
    eventName: "Olive Festival",
    Description:
      "Local farmers and producers showcase their products, and visitors can learn about the history and cultural significance of olives in North Cyprus.",
    date_range: {
      start_date: "2024-10-06",
      end_date: "2024-11-10",
    },
    image:
      "https://www.cyprusparadise.com/media/15827/olive-festival-north-cyprus.jpg",
    location: {
      link: "https://bit.ly/3yswdtN",
      local_range: {
        latitude: "35.333728707512044",
        longitude: "33.31502588926075",
      },
    },
    added_by_user: 1,
  },
  {
    eventId: 7,
    category: "entertainment",
    eventLocalAddress: "Eco Day Fest",
    eventName: "Eco Day Fest",
    Description:
      "North Cyprus is a prime spot for due to its unspoilt nature and prominence local life, and a destination that truly takes you far away from the hum of fast paced western culture.",
    date_range: {
      start_date: "2024-10-08",
      end_date: "2024-10-11",
    },
    image:
      "https://www.visitncy.com/wp-content/uploads/2020/02/join-ecotourismfest.jpg",
    location: {
      link: "https://bit.ly/4bMc3JH",
      local_range: {
        latitude: "35.331904042000964",
        longitude: "33.33069227065104",
      },
    },
    added_by_user: 1,
  },
  {
    eventId: 8,
    category: "entertainment",
    eventLocalAddress: "Kyrenia Centret",
    eventName: "Kyrenia Tour",
    Description:
      "Highlights of this tour include visits to the Kyrenia Harbour, Kyrenia Castle, the Ottoman-era Baldoken Graveyard, and the Bellapais Monastery.",
    date_range: {
      start_date: "2024-08-08",
      end_date: "2024-08-08",
    },
    image:
      "https://media-cdn.tripadvisor.com/media/attractions-splice-spp-720x480/0a/28/a4/bf.jpg",
    location: {
      link: "https://bit.ly/4bMc3JH",
      local_range: {
        latitude: "35.331904042000964",
        longitude: "33.33069227065104",
      },
    },
    added_by_user: 1,
  },
  {
    eventId: 9,
    category: "Religious",
    eventLocalAddress: "All hotels",
    eventName: "Christmas Day",
    Description:
      "December 25th is a religious holiday that commemorates the birth of Jesus Christ. In North Cyprus, it is marked with church services and other events.",
    date_range: {
      start_date: "2024-12-08",
      end_date: "2024-12-25",
    },
    image:
      "https://www.cyprusparadise.com/media/17498/christmas-festival-north-cyprus.jpg",
    location: {
      link: "https://bit.ly/4bFCroq",
      local_range: {
        latitude: "35.33901815654128",
        longitude: "33.33235328229513",
      },
    },
    added_by_user: 1,
    local_range: {
      latitude: "35.4094828",
      longitude: "33.9961463",
    },
  },
  {
    eventId: 10,
    category: "category",
    eventLocalAddress: "Gazimağusa 99450",
    eventName: "Korineum Golf Club Events",
    Description:
      "Kernium Golf Club is a renowned golf club that offers some of the best golfing experiences in the country. The club hosts a wide range of events throughout the year that cater to golfers of all levels.",
    date_range: {
      start_date: "2024-12-12",
      end_date: "2024-12-12",
    },
    image:
      "https://www.cyprusparadise.com/media/17499/korineum-golf-beach-resort.jpg",
    location: {
      link: "https://bit.ly/4dIvFQF",
      local_range: {
        latitude: "35.32582309455396",
        longitude: "33.51650359578765",
      },
    },
    added_by_user: 1,
  },
];

app.get("/", (req, res) => {
  res.json(
    "This is our custom places and Events API for Cyprus to integrate with the expo app. \n\n This is hosted on render. \n\n Go to /places-data \n\n or to /events "
  );
});

app.get("/events", async (req, res) => {
  res.json(events);
});
app.get("/places-data/all", (req, res) => {
  res.json(allPlaces);
});

app.get("/places-data/museums", (req, res) => {
  res.json(museums);
});

app.get("/places-data/restaurants", (req, res) => {
  res.json(restaurants);
});

app.get("/places-data/hospitals", (req, res) => {
  res.json(hospitals);
});

app.get("/places-data/hotels", (req, res) => {
  res.json(hotels);
});

app.get("/places-data/officials", (req, res) => {
  res.json(officials);
});

app.get("/places-data/pharmacies", (req, res) => {
  res.json(pharmacies);
});

app.listen(PORT, () =>
  console.log(`Server running on PORT http://localhost:${PORT}`)
);
