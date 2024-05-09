const restaurants = [
  {
    name: "Carpenters Restaurant & Bar",
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipPsluD8e1aekmlYP_DaQRwszuDZlsRA5jzTIRti=w122-h92-k-no",
    href: "https://www.google.com/maps/place/Carpenters+Restaurant+%26+Bar/data=!4m7!3m6!1s0x14de12abdfc7b19b:0x9fc1c1756b652f3d!8m2!3d35.3448152!4d33.2629269!16s%2Fg%2F1hg4qqf8c!19sChIJm7HH36sS3hQRPS9la3XBwZ8?authuser=0&hl=en&rclk=1",
    latitude: "35.3448152",
    longitude: "33.2629269",
  },
  {
    name: "Driftwood - Restaurant, Bar & Beach",
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipMU5iX4Hxa0Cv2arbkSe037PF61UqEyq8a9CMJ2=w138-h92-k-no",
    href: "https://www.google.com/maps/place/Driftwood+-+Restaurant,+Bar+%26+Beach/data=!4m7!3m6!1s0x14de0dde047ce93f:0xcf2e7bd02e247964!8m2!3d35.3513107!4d33.1697273!16s%2Fg%2F11rc7wy920!19sChIJP-l8BN4N3hQRZHkkLtB7Ls8?authuser=0&hl=en&rclk=1",
    latitude: "35.3513107",
    longitude: "33.1697273",
  },
  {
    name: "Archway Restaurant",
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipMnIS7y-qYpFqiQp-lVLcFmraxsW_y43_gqV6TW=w122-h92-k-no",
    href: "https://www.google.com/maps/place/Archway+Restaurant/data=!4m7!3m6!1s0x14de12d061804199:0x36ee819a4ed26808!8m2!3d35.3303798!4d33.2962293!16s%2Fg%2F12hqr4p0s!19sChIJmUGAYdAS3hQRCGjSTpqB7jY?authuser=0&hl=en&rclk=1",
    latitude: "35.3303798",
    longitude: "33.2962293",
  },
  {
    name: "Peri's Fish Restaurant",
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipMUqJ5B18a4I5BSRMsBzaIiG15ghl_hJ7paXC7u=w122-h92-k-no",
    href: "https://www.google.com/maps/place/Peri%27s+Fish+Restaurant/data=!4m7!3m6!1s0x14de0d8712ed0a89:0xca0599b4158a6d61!8m2!3d35.3471602!4d33.2562326!16s%2Fg%2F11h8jbtj8c!19sChIJiQrtEocN3hQRYW2KFbSZBco?authuser=0&hl=en&rclk=1",
    latitude: "35.3471602",
    longitude: "33.2562326",
  },
  {
    name: "ZemZem Arabic Restaurant",
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipO7oLzfJUhpakNwUkK8o3VFB3zUy9k40B6QWReP=w122-h92-k-no",
    href: "https://www.google.com/maps/place/ZemZem+Arabic+Restaurant/data=!4m7!3m6!1s0x14de17704d275f0d:0x1911ceb6cfad457!8m2!3d35.3370798!4d33.3091265!16s%2Fg%2F11mvv2xqw9!19sChIJDV8nTXAX3hQRV9T6bOsckQE?authuser=0&hl=en&rclk=1",
    latitude: "35.3370798",
    longitude: "33.3091265",
  },
  {
    name: 'Best Burger "Alsancak"',
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipOoeWxNLHnCXyCUtvzjx6A8O3RXm8HRt0Je4a5u=w80-h106-k-no",
    href: "https://www.google.com/maps/place/Best+Burger+%22Alsancak%22/data=!4m7!3m6!1s0x14de0d93b60e0f53:0x9a09c37040bb8226!8m2!3d35.3477276!4d33.2097151!16s%2Fg%2F11sdz9sps2!19sChIJUw8OtpMN3hQRJoK7QHDDCZo?authuser=0&hl=en&rclk=1",
    latitude: "35.3477276",
    longitude: "33.2097151",
  },
  {
    name: "Ezi\u00e7 Lapta",
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipP07fxHYdW-aRCDUH_WqYInHvcPC6OiV5ZqurVS=w122-h92-k-no",
    href: "https://www.google.com/maps/place/Ezi%C3%A7+Lapta/data=!4m7!3m6!1s0x14de0d9a20cab451:0x40c2f3071fb3e165!8m2!3d35.3514514!4d33.1690609!16s%2Fg%2F11jylldlr1!19sChIJUbTKIJoN3hQRZeGzHwfzwkA?authuser=0&hl=en&rclk=1",
    latitude: "35.3514514",
    longitude: "33.1690609",
  },
  {
    name: "Rock Island Cafe",
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipOhIXm_gFehqyIQWJtXDJbiLDyANcSMNSfDNkAt=w80-h106-k-no",
    href: "https://www.google.com/maps/place/Rock+Island+Cafe/data=!4m7!3m6!1s0x14de1328d0d9954d:0x6786f5679a9fe181!8m2!3d35.327799!4d33.3087966!16s%2Fg%2F11c5bmxw5c!19sChIJTZXZ0CgT3hQRgeGfmmf1hmc?authuser=0&hl=en&rclk=1",
    latitude: "35.327799",
    longitude: "33.3087966",
  },
  {
    name: "Kluky's Chicken & Burgers",
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipMqicN919Yw4hOvFQOeq2v2hV0i9hbNRvZqfJia=w122-h92-k-no",
    href: "https://www.google.com/maps/place/Kluky%27s+Chicken+%26+Burgers/data=!4m7!3m6!1s0x14de138aa34a36ab:0x6b8aac804621c443!8m2!3d35.3425367!4d33.2689833!16s%2Fg%2F11fnvrb8_b!19sChIJqzZKo4oT3hQRQ8QhRoCsims?authuser=0&hl=en&rclk=1",
    latitude: "35.3425367",
    longitude: "33.2689833",
  },
  {
    name: "Frankies American Chicken & Pizza",
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipNjqRCu84_O3lW4rHfPm-YS7_2bqj7TTZZcYxvi=w122-h92-k-no",
    href: "https://www.google.com/maps/place/Frankies+American+Chicken+%26+Pizza/data=!4m7!3m6!1s0x14de0d2411e95ad9:0x6111a11057d184e7!8m2!3d35.3487155!4d33.2204795!16s%2Fg%2F11r98hj2t!19sChIJ2VrpESQN3hQR54TRVxChEWE?authuser=0&hl=en&rclk=1",
    latitude: "35.3487155",
    longitude: "33.2204795",
  },
  {
    name: "Kervan Restaurant & Cafe",
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipPaNzQsTaW9WB7GhIqf05SXRn2WF-O2iQYGG4Kf=w194-h92-k-no",
    href: "https://www.google.com/maps/place/Kervan+Restaurant+%26+Cafe/data=!4m7!3m6!1s0x14de0d55cb9cdc51:0x11cba7d71f199118!8m2!3d35.3477556!4d33.2561731!16s%2Fg%2F11b5z1gjnl!19sChIJUdycy1UN3hQRGJEZH9enyxE?authuser=0&hl=en&rclk=1",
    latitude: "35.3477556",
    longitude: "33.2561731",
  },
  {
    name: "Calamari Restaurant",
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipPvun9zwFLERGMpgtcYzg1lhjAnYEM3przH9Qj5=w163-h92-k-no",
    href: "https://www.google.com/maps/place/Calamari+Restaurant/data=!4m7!3m6!1s0x14de0c9bbfc404f1:0x250b62102f5d16a8!8m2!3d35.350717!4d33.1759791!16s%2Fg%2F11gd09hbq4!19sChIJ8QTEv5sM3hQRqBZdLxBiCyU?authuser=0&hl=en&rclk=1",
    latitude: "35.350717",
    longitude: "33.1759791",
  },
  {
    name: "Zeenee Italian & American Restaurant",
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipPtUhQyuR1s08bHkmyP64JetuOuU5qfWWK6athn=w137-h92-k-no",
    href: "https://www.google.com/maps/place/Zeenee+Italian+%26+American+Restaurant/data=!4m7!3m6!1s0x14de138025bb404d:0xe2c6e9727fe2c8ab!8m2!3d35.3281094!4d33.3094404!16s%2Fg%2F11fylw8rkk!19sChIJTUC7JYAT3hQRq8jif3LpxuI?authuser=0&hl=en&rclk=1",
    latitude: "35.3281094",
    longitude: "33.3094404",
  },
  {
    name: "Blue Song Restaurant",
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipPuyTshgnuntnYpJz2MB1zbe2pomQO_2shZ0MAZ=w138-h92-k-no",
    href: "https://www.google.com/maps/place/Blue+Song+Restaurant/data=!4m7!3m6!1s0x14de0c9b8b1db2e9:0x1c16d4b5bd16d87!8m2!3d35.3511094!4d33.1746831!16s%2Fg%2F11c44k4pjt!19sChIJ6bIdi5sM3hQRh23RW0ttwQE?authuser=0&hl=en&rclk=1",
    latitude: "35.3511094",
    longitude: "33.1746831",
  },
  {
    name: "The Taj Indian Restaurant & Bar",
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipMssTvy3mG2t3ZYOYkPL7Rt7VQAI_27eEU5vAI=w122-h92-k-no",
    href: "https://www.google.com/maps/place/The+Taj+Indian+Restaurant+%26+Bar/data=!4m7!3m6!1s0x14de0de2d8ecf0c7:0x9ceb276fdddc3584!8m2!3d35.3473909!4d33.2052248!16s%2Fg%2F11g4lcwgc0!19sChIJx_Ds2OIN3hQRhDXc3W8n65w?authuser=0&hl=en&rclk=1",
    latitude: "35.3473909",
    longitude: "33.2052248",
  },
  {
    name: "Hill Side Restaurant",
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipO-eVu4i16okxqHxYgrI3uRqd-T2gFX9mcumHc6=w163-h92-k-no",
    href: "https://www.google.com/maps/place/Hill+Side+Restaurant/data=!4m7!3m6!1s0x14de0ce7a093bf51:0x45be50573e78a9c!8m2!3d35.3464103!4d33.2053539!16s%2Fg%2F12hx2bws4!19sChIJUb-ToOcM3hQRnIrncwXlWwQ?authuser=0&hl=en&rclk=1",
    latitude: "35.3464103",
    longitude: "33.2053539",
  },
  {
    name: "Dogus Adres Restaurant",
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipM_jzR339dtTu3OYfggjVoR-X3gN0a_GmMBJqRT=w163-h92-k-no",
    href: "https://www.google.com/maps/place/Dogus+Adres+Restaurant/data=!4m7!3m6!1s0x14de12ad5cc3d26d:0x3d8fe8dc72f71623!8m2!3d35.3465742!4d33.2693991!16s%2Fg%2F11cn941whz!19sChIJbdLDXK0S3hQRIxb3ctzojz0?authuser=0&hl=en&rclk=1",
    latitude: "35.3465742",
    longitude: "33.2693991",
  },
  {
    name: "Sea Point Restaurant",
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipOKvTjH_N-34NAZrbBxL3G9mEAKwVPwgSuz3yXD=w122-h92-k-no",
    href: "https://www.google.com/maps/place/Sea+Point+Restaurant/data=!4m7!3m6!1s0x14de0c9b946e8fb5:0xbee0b9f2bb8646d1!8m2!3d35.3506888!4d33.1755198!16s%2Fg%2F12hlr3pjj!19sChIJtY9ulJsM3hQR0UaGu_K54L4?authuser=0&hl=en&rclk=1",
    latitude: "35.3506888",
    longitude: "33.1755198",
  },
  {
    name: "Jashan Indian Restaurant Kyrenia Cyprus",
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipNm4xcpuKuTcsj822FKN6HIZ3AH6js__KnmMx0F=w211-h92-k-no",
    href: "https://www.google.com/maps/place/Jashan+Indian+Restaurant+Kyrenia+Cyprus/data=!4m7!3m6!1s0x14de12b5b17254cf:0x978ad307ebbe8839!8m2!3d35.3415184!4d33.2805824!16s%2Fg%2F11g_3kv0q!19sChIJz1RysbUS3hQROYi-6wfTipc?authuser=0&hl=en&rclk=1",
    latitude: "35.3415184",
    longitude: "33.2805824",
  },
  {
    name: "Royal Moon Restaurant and Bar",
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipMVCt8ScPWO6awhW0BFalQL-7ulWlfoNHkhnHMX=w122-h92-k-no",
    href: "https://www.google.com/maps/place/Royal+Moon+Restaurant+and+Bar/data=!4m7!3m6!1s0x14de0d4547e8534d:0x8792541a96b7f9a2!8m2!3d35.3476233!4d33.2026182!16s%2Fg%2F11t9cjkv7l!19sChIJTVPoR0UN3hQRovm3lhpUkoc?authuser=0&hl=en&rclk=1",
    latitude: "35.3476233",
    longitude: "33.2026182",
  },
  {
    name: "Farinelli Cafe Bar & Ristorante",
    category: "restaurant",
    image_url: "//maps.gstatic.com/tactile/pane/result-no-thumbnail-2x.png",
    href: "https://www.google.com/maps/place/Farinelli+Cafe+Bar+%26+Ristorante/data=!4m7!3m6!1s0x14de1351a5ca27cb:0xe4d1fb7d174b8d42!8m2!3d35.3302719!4d33.3014565!16s%2Fg%2F11np2th8h6!19sChIJyyfKpVET3hQRQo1LF3370eQ?authuser=0&hl=en&rclk=1",
    latitude: "35.3302719",
    longitude: "33.3014565",
  },
  {
    name: "Basilic",
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipP7cCDQBWu0K-V34SylK9GCRIZWYYPr8vLElJs3=w80-h106-k-no",
    href: "https://www.google.com/maps/place/Basilic/data=!4m7!3m6!1s0x14de0ddf5f24a50b:0xefb7e2582efcdef8!8m2!3d35.3487883!4d33.2111184!16s%2Fg%2F11h74rr32q!19sChIJC6UkX98N3hQR-N78Lljit-8?authuser=0&hl=en&rclk=1",
    latitude: "35.3487883",
    longitude: "33.2111184",
  },
  {
    name: "Han\u0131meller Restaurant Cafe and Bar",
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipNmE2l3oy7zdpVOmTrVF4vEQlvZ97APsLJluRe9=w122-h92-k-no",
    href: "https://www.google.com/maps/place/Han%C4%B1meller+Restaurant+Cafe+and+Bar/data=!4m7!3m6!1s0x14de0c9c6635acef:0x796774b21e9befca!8m2!3d35.3510888!4d33.1732897!16s%2Fg%2F11h05d91t!19sChIJ76w1ZpwM3hQRyu-bHrJ0Z3k?authuser=0&hl=en&rclk=1",
    latitude: "35.3510888",
    longitude: "33.1732897",
  },
  {
    name: "Mamma Africa Restaurant",
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipN_mQZHkCtLNEMSCI14UflRBIGXQIF_XcLSpvE=w100-h92-k-no",
    href: "https://www.google.com/maps/place/Mamma+Africa+Restaurant/data=!4m7!3m6!1s0x14de6db1a9e01621:0xeddb24433423fa8d!8m2!3d35.3369168!4d33.3092876!16s%2Fg%2F11r2g3gqwg!19sChIJIRbgqbFt3hQRjfojNEMk2-0?authuser=0&hl=en&rclk=1",
    latitude: "35.3369168",
    longitude: "33.3092876",
  },
  {
    name: "Food Republic",
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipPsT-XcieXLdzNXYNAafv6witsJAjHvQZydUyRu=w80-h106-k-no",
    href: "https://www.google.com/maps/place/Food+Republic/data=!4m7!3m6!1s0x14de12bbc293d61b:0x4555e61fd07f641a!8m2!3d35.3325362!4d33.2748199!16s%2Fg%2F1hdyyrjgg!19sChIJG9aTwrsS3hQRGmR_0B_mVUU?authuser=0&hl=en&rclk=1",
    latitude: "35.3325362",
    longitude: "33.2748199",
  },
  {
    name: "The Meyhane",
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipOoBNbOvW5TY5uUYzEDFA1VWp-JnURCjKAAWhJI=w122-h92-k-no",
    href: "https://www.google.com/maps/place/The+Meyhane/data=!4m7!3m6!1s0x14de12cbfc1228f3:0x6940c87b7c5233f4!8m2!3d35.3371914!4d33.2870066!16s%2Fg%2F1tzt35k7!19sChIJ8ygS_MsS3hQR9DNSfHvIQGk?authuser=0&hl=en&rclk=1",
    latitude: "35.3371914",
    longitude: "33.2870066",
  },
  {
    name: "Yong Chow Asian Food",
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipMlOrSt3iRZWgPwdTIFXOz_NUdvsywdXvS7LhM=w122-h92-k-no",
    href: "https://www.google.com/maps/place/Yong+Chow+Asian+Food/data=!4m7!3m6!1s0x14de0d7de7a1756b:0x71881f4dd4d96f13!8m2!3d35.3481914!4d33.1940888!16s%2Fg%2F11sj2j27wm!19sChIJa3Wh530N3hQRE2_Z1E0fiHE?authuser=0&hl=en&rclk=1",
    latitude: "35.3481914",
    longitude: "33.1940888",
  },
  {
    name: "Balcony Restaurant",
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipNF1cxEluRzK5mpFGfT1DBSMkBHSBm4Guvt1QSg=w122-h92-k-no",
    href: "https://www.google.com/maps/place/Balcony+Restaurant/data=!4m7!3m6!1s0x14de6dfdf1e8206d:0xda8f08f1fc2490dc!8m2!3d35.3435593!4d33.3027506!16s%2Fg%2F11szbx0fxd!19sChIJbSDo8f1t3hQR3JAk_PEIj9o?authuser=0&hl=en&rclk=1",
    latitude: "35.3435593",
    longitude: "33.3027506",
  },
  {
    name: "Reyhun Restaurant (Iranian Restaurant)",
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipP_tQ3VIq_mPFS9LTFlsSihj8Rhql-HfyYwe_if=w80-h106-k-no",
    href: "https://www.google.com/maps/place/Reyhun+Restaurant+%28Iranian+Restaurant%29/data=!4m7!3m6!1s0x14de13535d2f5179:0xe63280adf5eb82a0!8m2!3d35.3422753!4d33.2792634!16s%2Fg%2F11kqr_4lq7!19sChIJeVEvXVMT3hQRoILr9a2AMuY?authuser=0&hl=en&rclk=1",
    latitude: "35.3422753",
    longitude: "33.2792634",
  },
  {
    name: "Speakeasy restaurant and bar",
    category: "restaurant",
    image_url: "//maps.gstatic.com/tactile/pane/result-no-thumbnail-2x.png",
    href: "https://www.google.com/maps/place/Speakeasy+restaurant+and+bar/data=!4m7!3m6!1s0x14de0d23d2d7325f:0x458f65ebc3d41c9e!8m2!3d35.3483223!4d33.1958055!16s%2Fg%2F11sr6knzdz!19sChIJXzLX0iMN3hQRnhzUw-tlj0U?authuser=0&hl=en&rclk=1",
    latitude: "35.3483223",
    longitude: "33.1958055",
  },
  {
    name: "Carlitos Lebanese Tapas&Bar",
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipO1Yh3t80pbvVRWwQbt3p2jN_P7mvTYok7uYpNC=w163-h92-k-no",
    href: "https://www.google.com/maps/place/Carlitos+Lebanese+Tapas%26Bar/data=!4m7!3m6!1s0x14de0d262b07b333:0x74ece5e2c165868f!8m2!3d35.3483221!4d33.1957104!16s%2Fg%2F11tdgmmqcy!19sChIJM7MHKyYN3hQRj4ZlweLl7HQ?authuser=0&hl=en&rclk=1",
    latitude: "35.3483221",
    longitude: "33.1957104",
  },
  {
    name: "De Niro\u2019s Bistro Cafe",
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipM2N65v-dijdrHmibT_OSrzpEs0hTuD4KtOF31z=w163-h92-k-no",
    href: "https://www.google.com/maps/place/De+Niro%E2%80%99s+Bistro+Cafe/data=!4m7!3m6!1s0x14de6d2b36f0e4cb:0x5e05b4ee2b4dbd3!8m2!3d35.3368003!4d33.3098144!16s%2Fg%2F11p73dg75t!19sChIJy-TwNitt3hQR09u04k5b4AU?authuser=0&hl=en&rclk=1",
    latitude: "35.3368003",
    longitude: "33.3098144",
  },
  {
    name: "ThreeB Cyprus - Burger, Beer, Bar",
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipNoqKjZb2s7B58bQlQMh7PPd9fZdLMKtFLhBPcp=w122-h92-k-no",
    href: "https://www.google.com/maps/place/ThreeB+Cyprus+-+Burger,+Beer,+Bar/data=!4m7!3m6!1s0x14de6d042c15402d:0x8bb53321028318ec!8m2!3d35.3369862!4d33.3066878!16s%2Fg%2F11h26bgg0_!19sChIJLUAVLARt3hQR7BiDAiEztYs?authuser=0&hl=en&rclk=1",
    latitude: "35.3369862",
    longitude: "33.3066878",
  },
  {
    name: "Chill Beach Bar & Restaurant",
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipP4ubB_2FszJnS7V7Lt0qVXL12_KPGPvnPGe9gS=w80-h106-k-no",
    href: "https://www.google.com/maps/place/Chill+Beach+Bar+%26+Restaurant/data=!4m7!3m6!1s0x14de0de40591aad9:0xce963625f3066d46!8m2!3d35.3508125!4d33.1731875!16s%2Fg%2F11pyc4n089!19sChIJ2aqRBeQN3hQRRm0G8yU2ls4?authuser=0&hl=en&rclk=1",
    latitude: "35.3508125",
    longitude: "33.1731875",
  },
  {
    name: "Bogaz Restaurant",
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipPmPKQ3uvW1JTVsdJyICWk-fwJbPrk7PrvanqAc=w122-h92-k-no",
    href: "https://www.google.com/maps/place/Bogaz+Restaurant/data=!4m7!3m6!1s0x14de1215cb2df0a3:0x4019c6a49d7e597b!8m2!3d35.2824974!4d33.2766456!16s%2Fg%2F1thj77_p!19sChIJo_AtyxUS3hQRe1l-naTGGUA?authuser=0&hl=en&rclk=1",
    latitude: "35.2824974",
    longitude: "33.2766456",
  },
  {
    name: "Silver Rocks Restaurant",
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipN9GsPrpEqlh6iVGJECeYgMNAvFpp_qOYhTKMq4=w92-h92-k-no",
    href: "https://www.google.com/maps/place/Silver+Rocks+Restaurant/data=!4m7!3m6!1s0x14de0b39bdb46b91:0x1b75bf06a8c54b8d!8m2!3d35.3519976!4d33.1642699!16s%2Fg%2F11j4kz050k!19sChIJkWu0vTkL3hQRjUvFqAa_dRs?authuser=0&hl=en&rclk=1",
    latitude: "35.3519976",
    longitude: "33.1642699",
  },
  {
    name: "Bandir Corba Restaurant",
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipPShsPxR8NwPx9FgNxd9okkwzoDcAE7PPw-qRZq=w80-h106-k-no",
    href: "https://www.google.com/maps/place/Bandir+Corba+Restaurant/data=!4m7!3m6!1s0x14de12cb134caa89:0x916240f829a9b526!8m2!3d35.3410283!4d33.2854669!16s%2Fg%2F11bz005q4s!19sChIJiapME8sS3hQRJrWpKfhAYpE?authuser=0&hl=en&rclk=1",
    latitude: "35.3410283",
    longitude: "33.2854669",
  },
  {
    name: "Beach Bar 88",
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipN79GK-M2j6R8FxmuCPks_-kGTIEfIG_4KyP1g9=w122-h92-k-no",
    href: "https://www.google.com/maps/place/Beach+Bar+88/data=!4m7!3m6!1s0x14de0c9c5d1908d5:0x84f9b592efb2c3af!8m2!3d35.351043!4d33.1729475!16s%2Fg%2F12qfzfmgh!19sChIJ1QgZXZwM3hQRr8Oy75K1-YQ?authuser=0&hl=en&rclk=1",
    latitude: "35.351043",
    longitude: "33.1729475",
  },
  {
    name: "Dolce \u0130talian Restaurant & Bar",
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipM5Ghq3PditHlk3J5NYcP_-pJOUTg1AQ088Q3x-=w80-h106-k-no",
    href: "https://www.google.com/maps/place/Dolce+%C4%B0talian+Restaurant+%26+Bar/data=!4m7!3m6!1s0x14de13e37573da77:0x406d9cdc84cb2e48!8m2!3d35.3409834!4d33.2849842!16s%2Fg%2F11t1rhmg5r!19sChIJd9pzdeMT3hQRSC7LhNycbUA?authuser=0&hl=en&rclk=1",
    latitude: "35.3409834",
    longitude: "33.2849842",
  },
  {
    name: "The Lodge",
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipOnKAfoeXvQkr87A4Jipx2yeZ_0A5zd6m1XxtXI=w122-h92-k-no",
    href: "https://www.google.com/maps/place/The+Lodge/data=!4m7!3m6!1s0x14de0c9b97eff441:0x694cb6d5e79fa28b!8m2!3d35.350262!4d33.1758686!16s%2Fg%2F11bz08jgjk!19sChIJQfTvl5sM3hQRi6Kf59W2TGk?authuser=0&hl=en&rclk=1",
    latitude: "35.350262",
    longitude: "33.1758686",
  },
  {
    name: "Derfish Seafood Restaurant",
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipMBKjaOId1K3Pk89sHVAnX_9cGlMgPSqqBiTDBN=w122-h92-k-no",
    href: "https://www.google.com/maps/place/Derfish+Seafood+Restaurant/data=!4m7!3m6!1s0x14de12a971e21a13:0xfd4404a6cf68367d!8m2!3d35.3441486!4d33.2626972!16s%2Fg%2F11c1xm8jfx!19sChIJExricakS3hQRfTZoz6YERP0?authuser=0&hl=en&rclk=1",
    latitude: "35.3441486",
    longitude: "33.2626972",
  },
  {
    name: "Mozzarella Pizza Cafe & Restaurant",
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipMaLRTA-fNZtuj7D1GpV0RhRn4TZW_Zgiv3XhDR=w122-h92-k-no",
    href: "https://www.google.com/maps/place/Mozzarella+Pizza+Cafe+%26+Restaurant/data=!4m7!3m6!1s0x14de6cd4d8517d2b:0xa8e3262a3692700c!8m2!3d35.3367555!4d33.3066578!16s%2Fg%2F11hbkf_ft2!19sChIJK31R2NRs3hQRDHCSNiom46g?authuser=0&hl=en&rclk=1",
    latitude: "35.3367555",
    longitude: "33.3066578",
  },
  {
    name: "Royal Marina Restaurant",
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipPqQPhlq9H2j6CNGcZD1HyTFjF40rvVxhVHZoIj=w138-h92-k-no",
    href: "https://www.google.com/maps/place/Royal+Marina+Restaurant/data=!4m7!3m6!1s0x14de6d68f128a41d:0x5b8b574d01d946c8!8m2!3d35.343765!4d33.3032224!16s%2Fg%2F11rc7qn994!19sChIJHaQo8Wht3hQRyEbZAU1Xi1s?authuser=0&hl=en&rclk=1",
    latitude: "35.343765",
    longitude: "33.3032224",
  },
  {
    name: "THE TASTE",
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipNA-tuQe77-d4h7t8LFvRxlepVnv_fk_dnNysuZ=w122-h92-k-no",
    href: "https://www.google.com/maps/place/THE+TASTE/data=!4m7!3m6!1s0x14de6d184f82e593:0x23736d1d0d11de56!8m2!3d35.3419872!4d33.3048776!16s%2Fg%2F11mvk_bwhm!19sChIJk-WCTxht3hQRVt4RDR1tcyM?authuser=0&hl=en&rclk=1",
    latitude: "35.3419872",
    longitude: "33.3048776",
  },
  {
    name: "North Kyrenia Cafe & Restaurant",
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipOkVete6k-dSrP6hDNW4BFIFGtFcYkUKrjQXEE1=w80-h106-k-no",
    href: "https://www.google.com/maps/place/North+Kyrenia+Cafe+%26+Restaurant/data=!4m7!3m6!1s0x14dfcba9796961f7:0x3ca5777941530255!8m2!3d35.3283367!4d33.2925299!16s%2Fg%2F11gh9599c3!19sChIJ92FpeanL3xQRVQJTQXl3pTw?authuser=0&hl=en&rclk=1",
    latitude: "35.3283367",
    longitude: "33.2925299",
  },
  {
    name: "Charcos",
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipOFyNIguYAaaSM0pPf2RTd5JeNe82J-JACrLxDN=w122-h92-k-no",
    href: "https://www.google.com/maps/place/Charcos/data=!4m7!3m6!1s0x14de0d3f953b440d:0x946998a4e06d32ac!8m2!3d35.3388871!4d33.1721623!16s%2Fg%2F11s_z3l1_t!19sChIJDUQ7lT8N3hQRrDJt4KSYaZQ?authuser=0&hl=en&rclk=1",
    latitude: "35.3388871",
    longitude: "33.1721623",
  },
  {
    name: "\u015eevket's Bar & Restaurant",
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipO7tJatON9Mpl-CtqJR62B-XGTD7h4P2hxIV0P_=w94-h92-k-no",
    href: "https://www.google.com/maps/place/%C5%9Eevket%27s+Bar+%26+Restaurant/data=!4m7!3m6!1s0x14de0b0b53483075:0x9dafbaa2cf07450c!8m2!3d35.3500084!4d33.1558585!16s%2Fg%2F12hs17qh3!19sChIJdTBIUwsL3hQRDEUHz6K6r50?authuser=0&hl=en&rclk=1",
    latitude: "35.3500084",
    longitude: "33.1558585",
  },
  {
    name: "Alt\u0131n \u0130nci Restaurant",
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipPB44C1gTtEH6iZNFmMiOSa2lcDXP0BYaC1cVMb=w138-h92-k-no",
    href: "https://www.google.com/maps/place/Alt%C4%B1n+%C4%B0nci+Restaurant/data=!4m7!3m6!1s0x14de0d0d173cac61:0xb59dbd5b17aefaed!8m2!3d35.3382252!4d33.1727983!16s%2Fg%2F11h_svlzdb!19sChIJYaw8Fw0N3hQR7fquF1u9nbU?authuser=0&hl=en&rclk=1",
    latitude: "35.3382252",
    longitude: "33.1727983",
  },
  {
    name: "Sevener Restaurant",
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipPY2Wt4LehJERVLNjCI3b9t5zXovE6MqnaTi_4=w122-h92-k-no",
    href: "https://www.google.com/maps/place/Sevener+Restaurant/data=!4m7!3m6!1s0x14de0cde042391bf:0x3166f003a4556dbd!8m2!3d35.3470573!4d33.208683!16s%2Fg%2F1hdzh0hpt!19sChIJv5EjBN4M3hQRvW1VpAPwZjE?authuser=0&hl=en&rclk=1",
    latitude: "35.3470573",
    longitude: "33.208683",
  },
  {
    name: "Shell Wi",
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipPi8BjhEF_6vnb4JsaQWzkL8y6DV7r9t4pcNJLS=w80-h106-k-no",
    href: "https://www.google.com/maps/place/Shell+Wi/data=!4m7!3m6!1s0x14de6d54b4d8440f:0x4f43a9b8a78a42f0!8m2!3d35.341948!4d33.3049202!16s%2Fg%2F11llkjg83p!19sChIJD0TYtFRt3hQR8EKKp7ipQ08?authuser=0&hl=en&rclk=1",
    latitude: "35.341948",
    longitude: "33.3049202",
  },
  {
    name: "Saint Tropez Restaurant",
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipPgQRKJNYCvztpAr1aTuVTIU_V4sH1cvsEDQ4yD=w122-h92-k-no",
    href: "https://www.google.com/maps/place/Saint+Tropez+Restaurant/data=!4m7!3m6!1s0x14de0d3b0d69332b:0xb3fbd05c5272c8e4!8m2!3d35.3472625!4d33.2272098!16s%2Fg%2F11g_v2h4r!19sChIJKzNpDTsN3hQR5MhyUlzQ-7M?authuser=0&hl=en&rclk=1",
    latitude: "35.3472625",
    longitude: "33.2272098",
  },
  {
    name: "Big BOSS",
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipMMK_7QpsPkIC8wMOrx-0IfZVFm8q6bSzALvR1r=w163-h92-k-no",
    href: "https://www.google.com/maps/place/Big+BOSS/data=!4m7!3m6!1s0x14de6db18ea2d5b7:0x2a5e0c99b15a2fa7!8m2!3d35.3365984!4d33.3093258!16s%2Fg%2F11gvzdd6rk!19sChIJt9WijrFt3hQRpy9asZkMXio?authuser=0&hl=en&rclk=1",
    latitude: "35.3365984",
    longitude: "33.3093258",
  },
  {
    name: "Ezic Restaurant",
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipNjhUSstRFP4M1jpqyNXkQx3LylFD2ajyKKKTzF=w163-h92-k-no",
    href: "https://www.google.com/maps/place/Ezic+Restaurant/data=!4m7!3m6!1s0x14de1328b8feec91:0x60d0953be0f0e32d!8m2!3d35.3267417!4d33.3083631!16s%2Fg%2F1td1ylqq!19sChIJkez-uCgT3hQRLePw4DuV0GA?authuser=0&hl=en&rclk=1",
    latitude: "35.3267417",
    longitude: "33.3083631",
  },
  {
    name: "K\u00f6fteci Ramiz Alsancak",
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipPkfWMS4OYNHjR57ZLWTP86hjXUv4DhF8HBysYj=w122-h92-k-no",
    href: "https://www.google.com/maps/place/K%C3%B6fteci+Ramiz+Alsancak/data=!4m7!3m6!1s0x14de0d5cde27c41f:0x14b47e0c952901e4!8m2!3d35.3483773!4d33.1908568!16s%2Fg%2F11v1001w__!19sChIJH8Qn3lwN3hQR5AEplQx-tBQ?authuser=0&hl=en&rclk=1",
    latitude: "35.3483773",
    longitude: "33.1908568",
  },
  {
    name: "Teo's Restoran",
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipOl7b9RWVtzRbXLUZOpmmSNMiFv0VUPWhcuWEj8=w122-h92-k-no",
    href: "https://www.google.com/maps/place/Teo%27s+Restoran/data=!4m7!3m6!1s0x14de0c88ed865fe9:0xc5363a682d6d9137!8m2!3d35.338665!4d33.181745!16s%2Fg%2F11bych4gp8!19sChIJ6V-G7YgM3hQRN5FtLWg6NsU?authuser=0&hl=en&rclk=1",
    latitude: "35.338665",
    longitude: "33.181745",
  },
  {
    name: "Bella Merit Italian Restaurant",
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipPk7BIZI0m31JrQnc3MlfXnsIoiwrRczMtwinmg=w122-h92-k-no",
    href: "https://www.google.com/maps/place/Bella+Merit+Italian+Restaurant/data=!4m7!3m6!1s0x14de0dd4593b14cb:0xd732bd9abb53db67!8m2!3d35.3550791!4d33.2103452!16s%2Fg%2F11qb4n507z!19sChIJyxQ7WdQN3hQRZ9tTu5q9Mtc?authuser=0&hl=en&rclk=1",
    latitude: "35.3550791",
    longitude: "33.2103452",
  },
  {
    name: "Alsancak restaurant heaven",
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipNqd5Q7i8rrMsbFFkfU6v6WnGxDKw2lS-QjvwHD=w122-h92-k-no",
    href: "https://www.google.com/maps/place/Alsancak+restaurant+heaven/data=!4m7!3m6!1s0x14de0d9d604d19cd:0x724c9323cd877392!8m2!3d35.3460208!4d33.2315921!16s%2Fg%2F11qbh21bcq!19sChIJzRlNYJ0N3hQRknOHzSOTTHI?authuser=0&hl=en&rclk=1",
    latitude: "35.3460208",
    longitude: "33.2315921",
  },
  {
    name: "Paradissa Restaurant",
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipP4FDAcwCNyfwvV4cq0KYBEPKbB4zxs0cBoW9Af=w163-h92-k-no",
    href: "https://www.google.com/maps/place/Paradissa+Restaurant/data=!4m7!3m6!1s0x14de0d03bc7593e7:0x67b16cb926425f53!8m2!3d35.3465198!4d33.2552256!16s%2Fg%2F11j7vp60vs!19sChIJ55N1vAMN3hQRU19CJrlssWc?authuser=0&hl=en&rclk=1",
    latitude: "35.3465198",
    longitude: "33.2552256",
  },
  {
    name: "Ezi\u00e7 Point Restaurant",
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipPV2DwwF6o_pdp4wQ3aTDBLrxfBG0b3tYrWulps=w189-h92-k-no",
    href: "https://www.google.com/maps/place/Ezi%C3%A7+Point+Restaurant/data=!4m7!3m6!1s0x14de13528be10d93:0x27152218fe94b67f!8m2!3d35.285244!4d33.2791112!16s%2Fg%2F11h51b62qy!19sChIJkw3hi1IT3hQRf7aU_hgiFSc?authuser=0&hl=en&rclk=1",
    latitude: "35.285244",
    longitude: "33.2791112",
  },
  {
    name: "Fullet restaurant",
    category: "restaurant",
    image_url: "//maps.gstatic.com/tactile/pane/result-no-thumbnail-2x.png",
    href: "https://www.google.com/maps/place/Fullet+restaurant/data=!4m7!3m6!1s0x14de6d6276a6179d:0x89f368aeb07176c8!8m2!3d35.3387435!4d33.305506!16s%2Fg%2F11sc8bdzkq!19sChIJnRemdmJt3hQRyHZxsK5o84k?authuser=0&hl=en&rclk=1",
    latitude: "35.3387435",
    longitude: "33.305506",
  },
  {
    name: "Mezzo Fish Restaurant",
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipMUGSA9u-qyg2F7oWAc-YW2G61ubzkDjSOrLfqU=w138-h92-k-no",
    href: "https://www.google.com/maps/place/Mezzo+Fish+Restaurant/data=!4m7!3m6!1s0x14de1308db2dd2bd:0xe2d2124090f87db8!8m2!3d35.3474993!4d33.2653311!16s%2Fg%2F11h682z6s1!19sChIJvdIt2wgT3hQRuH34kEAS0uI?authuser=0&hl=en&rclk=1",
    latitude: "35.3474993",
    longitude: "33.2653311",
  },
  {
    name: "Ammadi Beach Club Restaurant & Bar",
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipMSjdssEGTScpmoUYyqEwPPcDzXaz05ebRWficm=w122-h92-k-no",
    href: "https://www.google.com/maps/place/Ammadi+Beach+Club+Restaurant+%26+Bar/data=!4m7!3m6!1s0x14de0d7e7bb2eccd:0x190a2008842382e2!8m2!3d35.3512724!4d33.1692494!16s%2Fg%2F11s4x4jhjx!19sChIJzeyye34N3hQR4oIjhAggChk?authuser=0&hl=en&rclk=1",
    latitude: "35.3512724",
    longitude: "33.1692494",
  },
  {
    name: "Fly Inn: Beach, Bar, Restaurant & Caf\u00e9",
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipNHXw4yUGhLt69jC6Ysql61kKK4P1xmxzyjdMcv=w164-h92-k-no",
    href: "https://www.google.com/maps/place/Fly+Inn:+Beach,+Bar,+Restaurant+%26+Caf%C3%A9/data=!4m7!3m6!1s0x14de0c9c67615c7f:0x54dd193080478b2!8m2!3d35.3508914!4d33.1731235!16s%2Fg%2F11c54f3zff!19sChIJf1xhZ5wM3hQRsngECJPRTQU?authuser=0&hl=en&rclk=1",
    latitude: "35.3508914",
    longitude: "33.1731235",
  },
  {
    name: "Guler Fish Restaurant",
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipMoEphBT-ny5n1Pc05DygiwJb8WvVbeU67ih2YQ=w122-h92-k-no",
    href: "https://www.google.com/maps/place/Guler+Fish+Restaurant/data=!4m7!3m6!1s0x14de0d5678f21223:0xfb8c05dd31b3a90c!8m2!3d35.3468561!4d33.257027!16s%2Fg%2F11cn9lrh1p!19sChIJIxLyeFYN3hQRDKmzMd0FjPs?authuser=0&hl=en&rclk=1",
    latitude: "35.3468561",
    longitude: "33.257027",
  },
  {
    name: "Agabey Restaurant",
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipOE85e_tgjfMpXoajQtP8eC_qgqmkvgaaNIjp39=w122-h92-k-no",
    href: "https://www.google.com/maps/place/Agabey+Restaurant/data=!4m7!3m6!1s0x14de13cc4181b4b3:0xd5a7d1e27adf03bf!8m2!3d35.3419562!4d33.2813502!16s%2Fg%2F11qk516bcy!19sChIJs7SBQcwT3hQRvwPfeuLRp9U?authuser=0&hl=en&rclk=1",
    latitude: "35.3419562",
    longitude: "33.2813502",
  },
  {
    name: "ALTA MAREA Restaurant & Lounge",
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipOKpiyWpR61HLw1DZrUvO9B81tXxD8VDCEsFvvs=w137-h92-k-no",
    href: "https://www.google.com/maps/place/ALTA+MAREA+Restaurant+%26+Lounge/data=!4m7!3m6!1s0x14de13e3e13300f9:0xb47fcddbdb37b4e7!8m2!3d35.3443611!4d33.2780972!16s%2Fg%2F11kq29f2sv!19sChIJ-QAz4eMT3hQR57Q329vNf7Q?authuser=0&hl=en&rclk=1",
    latitude: "35.3443611",
    longitude: "33.2780972",
  },
  {
    name: "Alt\u0131n Koy Restaurant.",
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipPR9XveaMyEUlAO8YfkQjIPJOrIBVUiBAvxP4CW=w80-h106-k-no",
    href: "https://www.google.com/maps/place/Alt%C4%B1n+Koy+Restaurant./data=!4m7!3m6!1s0x14de0df4730823db:0x10452893b8d69937!8m2!3d35.3497596!4d33.2267255!16s%2Fg%2F11ghp2pcr0!19sChIJ2yMIc_QN3hQRN5nWuJMoRRA?authuser=0&hl=en&rclk=1",
    latitude: "35.3497596",
    longitude: "33.2267255",
  },
  {
    name: "A\u00e7menya Restaurant",
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipO-oO0fBWLTdwFSVo_VhLDdDuCyuK7xoCndNcAH=w122-h92-k-no",
    href: "https://www.google.com/maps/place/A%C3%A7menya+Restaurant/data=!4m7!3m6!1s0x14de0ce6ee9f016b:0x27b29514e95d7b5c!8m2!3d35.3439876!4d33.2066464!16s%2Fg%2F1hc8n6n9w!19sChIJawGf7uYM3hQRXHtd6RSVsic?authuser=0&hl=en&rclk=1",
    latitude: "35.3439876",
    longitude: "33.2066464",
  },
  {
    name: "Ulfet Restaurant",
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipPukA0K1huqzuZL21zHrSrBuEzJoD0808ft-UD0=w122-h92-k-no",
    href: "https://www.google.com/maps/place/Ulfet+Restaurant/data=!4m7!3m6!1s0x14de6d3baf1db88d:0x4c1ef813527b5e97!8m2!3d35.3472488!4d33.2666554!16s%2Fg%2F11sczr0dg9!19sChIJjbgdrztt3hQRl157UhP4Hkw?authuser=0&hl=en&rclk=1",
    latitude: "35.3472488",
    longitude: "33.2666554",
  },
  {
    name: "Treasure Restaurant",
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipOZ89dTsALUOTG2mVLG2gAsipJcRl4znB73t9Vp=w122-h92-k-no",
    href: "https://www.google.com/maps/place/Treasure+Restaurant/data=!4m7!3m6!1s0x14de12815555555d:0xfe327d9d94ef6da7!8m2!3d35.3179525!4d33.2610187!16s%2Fg%2F11gdrdvmvw!19sChIJXVVVVYES3hQRp23vlJ19Mv4?authuser=0&hl=en&rclk=1",
    latitude: "35.3179525",
    longitude: "33.2610187",
  },
  {
    name: "West End Burger and Kebab House",
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipMOQXz1XhSN7YPn7rNRfis-Lo4TfePCMVdX5FRd=w189-h92-k-no",
    href: "https://www.google.com/maps/place/West+End+Burger+and+Kebab+House/data=!4m7!3m6!1s0x14de0df514662ac1:0xa29aa40cee3dbfad!8m2!3d35.3484575!4d33.2217584!16s%2Fg%2F11hg2qd9f1!19sChIJwSpmFPUN3hQRrb897gykmqI?authuser=0&hl=en&rclk=1",
    latitude: "35.3484575",
    longitude: "33.2217584",
  },
  {
    name: "G\u00fczel Restaurant",
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipPWmp7HnpBn-EXi8WQiUpUCNmrR1Ejsbl1BhqX1=w163-h92-k-no",
    href: "https://www.google.com/maps/place/G%C3%BCzel+Restaurant/data=!4m7!3m6!1s0x14de6d983f16d357:0x6cff1f49e2fbcfa1!8m2!3d35.3368776!4d33.3066583!16s%2Fg%2F11j0zpxhjh!19sChIJV9MWP5ht3hQRoc_74kkf_2w?authuser=0&hl=en&rclk=1",
    latitude: "35.3368776",
    longitude: "33.3066583",
  },
  {
    name: "Alt\u0131nba\u015fak RESTAURANT",
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipMNU0ukE9s3YxObL3Q57Cgd4SEJCsReJYH0ITsV=w163-h92-k-no",
    href: "https://www.google.com/maps/place/Alt%C4%B1nba%C5%9Fak+RESTAURANT/data=!4m7!3m6!1s0x14de0c86fa008057:0x50572908388a3c7a!8m2!3d35.3401231!4d33.1772434!16s%2Fg%2F11cs2h5rj3!19sChIJV4AA-oYM3hQRejyKOAgpV1A?authuser=0&hl=en&rclk=1",
    latitude: "35.3401231",
    longitude: "33.1772434",
  },
  {
    name: "Hilltop Restaurant Meyhane",
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipNPH2g05Tut740Wnddv-niUvcNkD58kbSDMvAlh=w80-h106-k-no",
    href: "https://www.google.com/maps/place/Hilltop+Restaurant+Meyhane/data=!4m7!3m6!1s0x14de0d7660fdf57d:0x7cda958b211038cc!8m2!3d35.3371063!4d33.1754309!16s%2Fg%2F11pqn5qzgk!19sChIJffX9YHYN3hQRzDgQIYuV2nw?authuser=0&hl=en&rclk=1",
    latitude: "35.3371063",
    longitude: "33.1754309",
  },
  {
    name: "Levant Restoran",
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipNGqsM5Z7C3WEwGT0dSgJtsx8AgWTp6Wjvbbpj7=w122-h92-k-no",
    href: "https://www.google.com/maps/place/Levant+Restoran/data=!4m7!3m6!1s0x14de0d7c2a7c831f:0x494beab2752058be!8m2!3d35.317639!4d33.255788!16s%2Fg%2F11b7q4w7wb!19sChIJH4N8KnwN3hQRvlggdbLqS0k?authuser=0&hl=en&rclk=1",
    latitude: "35.317639",
    longitude: "33.255788",
  },
  {
    name: "Eyva brodi",
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipMHnliwnfTyV9j1IILUaprex66dQbzOvYIJp2-y=w163-h92-k-no",
    href: "https://www.google.com/maps/place/Eyva+brodi/data=!4m7!3m6!1s0x14de13a211733afd:0xdad767af559880dc!8m2!3d35.3450417!4d33.2728694!16s%2Fg%2F11j7fc2b65!19sChIJ_TpzEaIT3hQR3ICYVa9n19o?authuser=0&hl=en&rclk=1",
    latitude: "35.3450417",
    longitude: "33.2728694",
  },
  {
    name: "Jashan Indian Restaurant Lapta",
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipM3N_re-nxcj2bvKXOIdklk9tZZqSiKr48niXnu=w122-h92-k-no",
    href: "https://www.google.com/maps/place/Jashan+Indian+Restaurant+Lapta/data=!4m7!3m6!1s0x14de0d4d265d696d:0x1632e89702837e6!8m2!3d35.3487036!4d33.1795055!16s%2Fg%2F11kynm2ct6!19sChIJbWldJk0N3hQR5jcocIkuYwE?authuser=0&hl=en&rclk=1",
    latitude: "35.3487036",
    longitude: "33.1795055",
  },
  {
    name: "\u00c7\u0131nar Restaurant",
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipPtI-8MUrCeq01kXSIwj_Swywc2afxq4JooUxGG=w80-h106-k-no",
    href: "https://www.google.com/maps/place/%C3%87%C4%B1nar+Restaurant/data=!4m7!3m6!1s0x14de0de8f6c5eb39:0x7883d202333c9bd5!8m2!3d35.2900848!4d33.2394361!16s%2Fg%2F12hq9r8tm!19sChIJOevF9ugN3hQR1Zs8MwLSg3g?authuser=0&hl=en&rclk=1",
    latitude: "35.2900848",
    longitude: "33.2394361",
  },
  {
    name: "Day\u0131 Restaurant",
    category: "restaurant",
    image_url: "//maps.gstatic.com/tactile/pane/result-no-thumbnail-2x.png",
    href: "https://www.google.com/maps/place/Day%C4%B1+Restaurant/data=!4m7!3m6!1s0x14de12443a1135d1:0xf0c5e8dc9cac0e99!8m2!3d35.2886781!4d33.2889122!16s%2Fg%2F12hr0mqb1!19sChIJ0TUROkQS3hQRmQ6snNzoxfA?authuser=0&hl=en&rclk=1",
    latitude: "35.2886781",
    longitude: "33.2889122",
  },
  {
    name: "Trattoria Vineyard restaurant",
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipO6wsM3J14NMAxFktJGWUdlz5G3JM3uvnj4uSH6=w80-h106-k-no",
    href: "https://www.google.com/maps/place/Trattoria+Vineyard+restaurant/data=!4m7!3m6!1s0x14de0d60e40e5f19:0x5203b91d2d6a2fb5!8m2!3d35.3242989!4d33.2219433!16s%2Fg%2F11l34kh3z4!19sChIJGV8O5GAN3hQRtS9qLR25A1I?authuser=0&hl=en&rclk=1",
    latitude: "35.3242989",
    longitude: "33.2219433",
  },
  {
    name: "Doren Cafe & Restaurant",
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipOMCaLz0_mhTGwDud5WAwGSSqq6ng_KaDgODcko=w142-h92-k-no",
    href: "https://www.google.com/maps/place/Doren+Cafe+%26+Restaurant/data=!4m7!3m6!1s0x14de6d6e4fe35e65:0x34053806069af6aa!8m2!3d35.3377316!4d33.3039917!16s%2Fg%2F11jpx5skd7!19sChIJZV7jT25t3hQRqvaaBgY4BTQ?authuser=0&hl=en&rclk=1",
    latitude: "35.3377316",
    longitude: "33.3039917",
  },
  {
    name: "Fika Ocakba\u015f\u0131 Meyhane",
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipMKKF1_JE2lKSQTMWEW011fuJXfQl3ImXPhAPcF=w80-h106-k-no",
    href: "https://www.google.com/maps/place/Fika+Ocakba%C5%9F%C4%B1+Meyhane/data=!4m7!3m6!1s0x14de13e39c963009:0x567e375e09af69!8m2!3d35.328559!4d33.3100022!16s%2Fg%2F11trw1f4d3!19sChIJCTCWnOMT3hQRaa8JXjd-VgA?authuser=0&hl=en&rclk=1",
    latitude: "35.328559",
    longitude: "33.3100022",
  },
  {
    name: "Miss K\u00f6fte",
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipOfbNwHNigcGN9FmrvnJKh3Izsk3Spv9ZcrzM2u=w122-h92-k-no",
    href: "https://www.google.com/maps/place/Miss+K%C3%B6fte/data=!4m7!3m6!1s0x14de6d03009da0b1:0x1c05f42c31edf185!8m2!3d35.2966835!4d33.2366496!16s%2Fg%2F11g1nrcrgq!19sChIJsaCdAANt3hQRhfHtMSz0BRw?authuser=0&hl=en&rclk=1",
    latitude: "35.2966835",
    longitude: "33.2366496",
  },
  {
    name: "Kahiye Ate\u015f Kebap Girne",
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipOOvi1WkQBMkfuFTQP_6mvYUq9gj2yJBVLBB2J9=w204-h92-k-no",
    href: "https://www.google.com/maps/place/Kahiye+Ate%C5%9F+Kebap+Girne/data=!4m7!3m6!1s0x14de13ee213764b5:0x94d4be03b48eb65d!8m2!3d35.3317089!4d33.308874!16s%2Fg%2F11j01rgdxh!19sChIJtWQ3Ie4T3hQRXbaOtAO-1JQ?authuser=0&hl=en&rclk=1",
    latitude: "35.3317089",
    longitude: "33.308874",
  },
  {
    name: "Tervetuloa Restaurant",
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipO8b1KGdU6TkiakTIaITmTYjEXuqK9A09GcUfWI=w122-h92-k-no",
    href: "https://www.google.com/maps/place/Tervetuloa+Restaurant/data=!4m7!3m6!1s0x14de0cd8aa4527bd:0x474b64051dd3c8e1!8m2!3d35.3486832!4d33.2104254!16s%2Fg%2F12mkw90dd!19sChIJvSdFqtgM3hQR4cjTHQVkS0c?authuser=0&hl=en&rclk=1",
    latitude: "35.3486832",
    longitude: "33.2104254",
  },
  {
    name: "Afiyetler \u00c7orba Kebap Pide",
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipNzUK37FHCLAeYNCAx41Kz9IHK-S_CookWNX28k=w122-h92-k-no",
    href: "https://www.google.com/maps/place/Afiyetler+%C3%87orba+Kebap+Pide/data=!4m7!3m6!1s0x14de1397fcc3f17b:0x74cd9ca394c5777c!8m2!3d35.3415825!4d33.2839508!16s%2Fg%2F11sszj1qdh!19sChIJe_HD_JcT3hQRfHfFlKOczXQ?authuser=0&hl=en&rclk=1",
    latitude: "35.3415825",
    longitude: "33.2839508",
  },
  {
    name: "Develi",
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipMqZoBLt0pIVk_y9M66FPdvjxJSikSybCdZrSgL=w122-h92-k-no",
    href: "https://www.google.com/maps/place/Develi/data=!4m7!3m6!1s0x14de13649f832ae9:0x548b25f2023eae86!8m2!3d35.3480001!4d33.264831!16s%2Fg%2F11h036dfj4!19sChIJ6SqDn2QT3hQRhq4-AvIli1Q?authuser=0&hl=en&rclk=1",
    latitude: "35.3480001",
    longitude: "33.264831",
  },
  {
    name: "Dragon \u00c7in Restaurant",
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipNRN-J4_P4mqIFci1NbxWyPlot_3FpK2LChajOn=w122-h92-k-no",
    href: "https://www.google.com/maps/place/Dragon+%C3%87in+Restaurant/data=!4m7!3m6!1s0x14de6d0418892315:0xa78c881a00323db5!8m2!3d35.3422688!4d33.3047265!16s%2Fg%2F11s57fk5vp!19sChIJFSOJGARt3hQRtT0yABqIjKc?authuser=0&hl=en&rclk=1",
    latitude: "35.3422688",
    longitude: "33.3047265",
  },
  {
    name: "Green Lotus chinese restaurant",
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipMiKnSLCwAqYsWSIFFvXTVk1MKgDE9N9Yc2Fk3p=w80-h106-k-no",
    href: "https://www.google.com/maps/place/Green+Lotus+chinese+restaurant/data=!4m7!3m6!1s0x14de0d29966d44c9:0xb8762da38692fd9b!8m2!3d35.3482966!4d33.1881252!16s%2Fg%2F11lh51r5v6!19sChIJyURtlikN3hQRm_2ShqMtdrg?authuser=0&hl=en&rclk=1",
    latitude: "35.3482966",
    longitude: "33.1881252",
  },
  {
    name: "Heliconia Cafe",
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipMu26Zq6HvWhywJrzwmwyIz4TCtQQTYPB1gJCaR=w138-h92-k-no",
    href: "https://www.google.com/maps/place/Heliconia+Cafe/data=!4m7!3m6!1s0x14de0dcddf36fd2f:0x5c1e78772c462348!8m2!3d35.3434505!4d33.2066879!16s%2Fg%2F11qbcd20bj!19sChIJL_02380N3hQRSCNGLHd4Hlw?authuser=0&hl=en&rclk=1",
    latitude: "35.3434505",
    longitude: "33.2066879",
  },
  {
    name: "Veni Vici",
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipNyH_hoAmdxoHI1GcGppFytLSYjqiDriWD9Tucb=w122-h92-k-no",
    href: "https://www.google.com/maps/place/Veni+Vici/data=!4m7!3m6!1s0x14de0c9bbcbd9093:0xe9a3f26d90d70c9a!8m2!3d35.3502183!4d33.1761785!16s%2Fg%2F1hfhb0fdc!19sChIJk5C9vJsM3hQRmgzXkG3yo-k?authuser=0&hl=en&rclk=1",
    latitude: "35.3502183",
    longitude: "33.1761785",
  },
  {
    name: "Yada Sushi",
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipNCttKAgI6em-qJAiKrjA4tQLGLKk0STul6MqPM=w139-h92-k-no",
    href: "https://www.google.com/maps/place/Yada+Sushi/data=!4m7!3m6!1s0x14de13eef490d777:0x791242389e135a80!8m2!3d35.3479368!4d33.2645587!16s%2Fg%2F11h62wt3k4!19sChIJd9eQ9O4T3hQRgFoTnjhCEnk?authuser=0&hl=en&rclk=1",
    latitude: "35.3479368",
    longitude: "33.2645587",
  },
  {
    name: "Kasaba da Kahvalt\u0131",
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipMk82NpDvBBrGv02PzzzbDwcDyhmepj_f1OId6Z=w122-h92-k-no",
    href: "https://www.google.com/maps/place/Kasaba+da+Kahvalt%C4%B1/data=!4m7!3m6!1s0x14de1370c88c4b1b:0x1d8bca6f8fb76e8!8m2!3d35.3209118!4d33.2760255!16s%2Fg%2F11q9hngt73!19sChIJG0uMyHAT3hQR6Hb7-Ka82AE?authuser=0&hl=en&rclk=1",
    latitude: "35.3209118",
    longitude: "33.2760255",
  },
  {
    name: "Blue Door Meyhane - Restaurant",
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipOcZP7vviR6xrAPhQ6VqUCQlp1JDFzIx1N8DU2V=w92-h92-k-no",
    href: "https://www.google.com/maps/place/Blue+Door+Meyhane+-+Restaurant/data=!4m7!3m6!1s0x14de0ce61ffb7bb3:0x27c61c40e8b8477d!8m2!3d35.3451583!4d33.2025764!16s%2Fg%2F1hg4vrh0_!19sChIJs3v7H-YM3hQRfUe46EAcxic?authuser=0&hl=en&rclk=1",
    latitude: "35.3451583",
    longitude: "33.2025764",
  },
  {
    name: "Fora Bal\u0131k Merit Park",
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipN1v1Y25s6tpLyeoplN9EZ4AwTTUCIz6by_9XOq=w137-h92-k-no",
    href: "https://www.google.com/maps/place/Fora+Bal%C4%B1k+Merit+Park/data=!4m7!3m6!1s0x14de0df5974a45b1:0xddce11bda45aae65!8m2!3d35.3494141!4d33.2570546!16s%2Fg%2F11gmglj3hp!19sChIJsUVKl_UN3hQRZa5apL0Rzt0?authuser=0&hl=en&rclk=1",
    latitude: "35.3494141",
    longitude: "33.2570546",
  },
  {
    name: "Cypriana Restaurant",
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipNcSK4k20OlehFb29xgx1-FUaWazTUiKSFBDUqu=w122-h92-k-no",
    href: "https://www.google.com/maps/place/Cypriana+Restaurant/data=!4m7!3m6!1s0x14de0de42ebf9dc7:0xd167d626ecd0cbd!8m2!3d35.284728!4d33.2423705!16s%2Fg%2F11b7fxlchr!19sChIJx52_LuQN3hQRvQzNbmJ9Fg0?authuser=0&hl=en&rclk=1",
    latitude: "35.284728",
    longitude: "33.2423705",
  },
  {
    name: "Kamares",
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipMBWojJjIdn7EPLs0a_3UsVLdw1t9VloTBFTDvb=w92-h92-k-no",
    href: "https://www.google.com/maps/place/Kamares/data=!4m7!3m6!1s0x14de12a69911d42b:0xb57206ecd8df82e5!8m2!3d35.3360418!4d33.2639385!16s%2Fg%2F12hm_3x9f!19sChIJK9QRmaYS3hQR5YLf2OwGcrU?authuser=0&hl=en&rclk=1",
    latitude: "35.3360418",
    longitude: "33.2639385",
  },
  {
    name: 'Chabad North Cyprus- \u05d7\u05d1"\u05d3 \u05e6\u05e4\u05d5\u05df \u05e7\u05e4\u05e8\u05d9\u05e1\u05d9\u05df',
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipNu1fW3NU4q3F0UIJltLQ5egC2DfrwQe9GGOtTJ=w199-h92-k-no",
    href: "https://www.google.com/maps/place/Chabad+North+Cyprus-+%D7%97%D7%91%22%D7%93+%D7%A6%D7%A4%D7%95%D7%9F+%D7%A7%D7%A4%D7%A8%D7%99%D7%A1%D7%99%D7%9F%E2%80%AD/data=!4m7!3m6!1s0x14de0d563837e6c1:0xb16030d99ba646c6!8m2!3d35.3445722!4d33.2575715!16s%2Fg%2F1pxq3l0jl!19sChIJweY3OFYN3hQRxkamm9kwYLE?authuser=0&hl=en&rclk=1",
    latitude: "35.3445722",
    longitude: "33.2575715",
  },
  {
    name: "Lapida Hotel",
    category: "restaurant",
    image_url:
      "https://lh3.googleusercontent.com/gps-proxy/ALd4DhHZLoHW1cDe4ZCuO11nAog0YhEcEhqJ2Eok-wRlMGt-IQ2kmNiLBSKvxx22DAmSLK5GwIRgH6BYAFQ1-57FpSShHgZ3cAwlAXbYaOE7DhNC1UEjvJlzmGyYroDWLXzHeONdOU8mRrG55oofz0L_N6P8Kn3_p3-ZSWUg4DniJGTn0LXD23qb-yt5aw=w163-h92-k-no",
    href: "https://www.google.com/maps/place/Lapida+Hotel/data=!4m10!3m9!1s0x14de1344cc851103:0x664646ed01428d07!5m2!4m1!1i2!8m2!3d35.3463389!4d33.1600333!16s%2Fg%2F1v89d3k5!19sChIJAxGFzEQT3hQRB41CAe1GRmY?authuser=0&hl=en&rclk=1",
    latitude: "35.3463389",
    longitude: "33.1600333",
  },
  {
    name: "Incirli Beach Restaurant",
    category: "restaurant",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipPwCVsszonmzHNBEIFSABTd_QR1JzMuuPacL-OH=w80-h106-k-no",
    href: "https://www.google.com/maps/place/Incirli+Beach+Restaurant/data=!4m7!3m6!1s0x14de0d17abe8362f:0xa25deeba272922ee!8m2!3d35.3515158!4d33.1691016!16s%2Fg%2F11scmyczxn!19sChIJLzboqxcN3hQR7iIpJ7ruXaI?authuser=0&hl=en&rclk=1",
    latitude: "35.3515158",
    longitude: "33.1691016",
  },
];
module.exports = restaurants;
