const museums = [
  {
    name: "Museum of the history of Cypriot Coinage",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipMxMxeF8yKBLt78Y8o9wIjHjGP5DcdcwhVAiK3G=w80-h106-k-no",
    href: "https://www.google.com/maps/place/Museum+of+the+history+of+Cypriot+Coinage/data=!4m7!3m6!1s0x14de177693956d99:0x41026241e725efd4!8m2!3d35.1729322!4d33.3622297!16s%2Fg%2F11ll61jvx7!19sChIJmW2Vk3YX3hQR1O8l50FiAkE?authuser=0&hl=en&rclk=1",
    latitude: "35.1729322",
    longitude: "33.3622297",
  },
  {
    name: "Cyprus Classic Motorcycle Museum",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipMX2-pa4kxl5c0ZtTgiFNIF8z8jGY0GrMTc5bXZ=w122-h92-k-no",
    href: "https://www.google.com/maps/place/Cyprus+Classic+Motorcycle+Museum/data=!4m7!3m6!1s0x14de17502299d2d5:0xa045a9d4dbba73df!8m2!3d35.1729336!4d33.3582753!16s%2Fm%2F0cc9nwr!19sChIJ1dKZIlAX3hQR33O629SpRaA?authuser=0&hl=en&rclk=1",
    latitude: "35.1729336",
    longitude: "33.3582753",
  },
  {
    name: "Cyprus Folk Art Museum",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipMuvcfq-WDFa_Ag97Agf24GMEjzLec0fJdrsGCW=w163-h92-k-no",
    href: "https://www.google.com/maps/place/Cyprus+Folk+Art+Museum/data=!4m7!3m6!1s0x14de1743ade7836b:0xf583b2117a7a4285!8m2!3d35.17344!4d33.3679354!16s%2Fg%2F1td_7qfh!19sChIJa4PnrUMX3hQRhUJ6ehGyg_U?authuser=0&hl=en&rclk=1",
    latitude: "35.17344",
    longitude: "33.3679354",
  },
  {
    name: "The Cyprus Museum",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipPJggKac0CjykcsjcutlTc2s1iSyoZL4H1HjsPQ=w122-h92-k-no",
    href: "https://www.google.com/maps/place/The+Cyprus+Museum/data=!4m7!3m6!1s0x14de1751bc94bcd9:0x6e455e53737055d9!8m2!3d35.1717252!4d33.3557162!16s%2Fm%2F02q6f3d!19sChIJ2byUvFEX3hQR2VVwc1NeRW4?authuser=0&hl=en&rclk=1",
    latitude: "35.1717252",
    longitude: "33.3557162",
  },
  {
    name: "Pancyprian Museum of Social and Education History",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipMKVRaKv7TLjEn-FVg0ZUFeKaYEvaRb-MkBB75b=w80-h115-k-no",
    href: "https://www.google.com/maps/place/Pancyprian+Museum+of+Social+and+Education+History/data=!4m7!3m6!1s0x14de17423c048631:0x2e001f037ea6345d!8m2!3d35.1740176!4d33.3693377!16s%2Fg%2F11f0xltfcp!19sChIJMYYEPEIX3hQRXTSmfgMfAC4?authuser=0&hl=en&rclk=1",
    latitude: "35.1740176",
    longitude: "33.3693377",
  },
  {
    name: "The Leventis Municipal Museum of Nicosia",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipPaqNoUFL4_B-fE3G1_OmbwGM_vrwuJ0eMJdJPr=w163-h92-k-no",
    href: "https://www.google.com/maps/place/The+Leventis+Municipal+Museum+of+Nicosia/data=!4m7!3m6!1s0x14de175af1f88d79:0xedc481824a22cac7!8m2!3d35.170472!4d33.3618494!16s%2Fm%2F0gvrcm5!19sChIJeY348VoX3hQRx8oiSoKBxO0?authuser=0&hl=en&rclk=1",
    latitude: "35.170472",
    longitude: "33.3618494",
  },
  {
    name: "Shacolas Tower Museum and Observatory",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipO_wU3dC6AW2UdMVupyHMj9tj3CMUvoXFM1xyGI=w122-h92-k-no",
    href: "https://www.google.com/maps/place/Shacolas+Tower+Museum+and+Observatory/data=!4m7!3m6!1s0x14de175ac6f76473:0xd14d299b5638755b!8m2!3d35.1716304!4d33.3616769!16s%2Fg%2F11cn9598gx!19sChIJc2T3xloX3hQRW3U4VpspTdE?authuser=0&hl=en&rclk=1",
    latitude: "35.1716304",
    longitude: "33.3616769",
  },
  {
    name: "State Gallery of Contemporary Art",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipO0Tamg35UlATXimAmKxH1PVZmBVtPuKN1sVlhe=w122-h92-k-no",
    href: "https://www.google.com/maps/place/State+Gallery+of+Contemporary+Art/data=!4m7!3m6!1s0x14de175c7716384d:0x693b64fec4ea624d!8m2!3d35.1679915!4d33.3657052!16s%2Fg%2F11c2jk52by!19sChIJTTgWd1wX3hQRTWLqxP5kO2k?authuser=0&hl=en&rclk=1",
    latitude: "35.1679915",
    longitude: "33.3657052",
  },
  {
    name: "Postal Museum",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipNtZMb8XeEjAvgOh2xFd8KNMHCK1WNeec6iEGDz=w122-h92-k-no",
    href: "https://www.google.com/maps/place/Postal+Museum/data=!4m7!3m6!1s0x14de175b38306267:0xc687fff5e960bad6!8m2!3d35.1710793!4d33.36359!16s%2Fm%2F0cc8c18!19sChIJZ2IwOFsX3hQR1rpg6fX_h8Y?authuser=0&hl=en&rclk=1",
    latitude: "35.1710793",
    longitude: "33.36359",
  },
  {
    name: "The House of Hadjigeorgakis Kornesios - Ethnological Museum",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipOzcgMl4dMgoUaiORBQpSVBFFES2UmmCkbtio_J=w122-h92-k-no",
    href: "https://www.google.com/maps/place/The+House+of+Hadjigeorgakis+Kornesios+-+Ethnological+Museum/data=!4m7!3m6!1s0x14de1a663fd38b87:0xe04e55de76a2bf52!8m2!3d35.1718833!4d33.3669733!16s%2Fm%2F0h3wlzp!19sChIJh4vTP2Ya3hQRUr-idt5VTuA?authuser=0&hl=en&rclk=1",
    latitude: "35.1718833",
    longitude: "33.3669733",
  },
  {
    name: "Fairy Tale Museum",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipPx886Bt8qBPjp2ZSgLVsXVNdLnmASYWJwSemw=w122-h92-k-no",
    href: "https://www.google.com/maps/place/Fairy+Tale+Museum/data=!4m7!3m6!1s0x14de17501f128ef1:0xc1595f7aea64890a!8m2!3d35.1735277!4d33.358666!16s%2Fg%2F11c76vl4lr!19sChIJ8Y4SH1AX3hQRColk6npfWcE?authuser=0&hl=en&rclk=1",
    latitude: "35.1735277",
    longitude: "33.358666",
  },
  {
    name: "Museum of Barbarism",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipPx1WqEUCuwgaXTnOIF76bKPrfbKBSaPg90SpHi=w163-h92-k-no",
    href: "https://www.google.com/maps/place/Museum+of+Barbarism/data=!4m7!3m6!1s0x14de1718d122eadf:0x37ea80d25a6e260f!8m2!3d35.1905827!4d33.3492706!16s%2Fg%2F122y5wcc!19sChIJ3-oi0RgX3hQRDyZuWtKA6jc?authuser=0&hl=en&rclk=1",
    latitude: "35.1905827",
    longitude: "33.3492706",
  },
  {
    name: "Lapidary Museum, Nicosia",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipN33lFKBcp4J5Lxg-Z2MwdXZFoasg8qZceYwEVW=w122-h92-k-no",
    href: "https://www.google.com/maps/place/Lapidary+Museum,+Nicosia/data=!4m7!3m6!1s0x14de174139555555:0xe30f85231a304b2d!8m2!3d35.1765976!4d33.3656669!16s%2Fg%2F11h02cg3rs!19sChIJVVVVOUEX3hQRLUswGiOFD-M?authuser=0&hl=en&rclk=1",
    latitude: "35.1765976",
    longitude: "33.3656669",
  },
  {
    name: "Ledra City Archaeological Museum",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipNifBzlOybJmcA9F5N37j7xHcuAQ_emdsT5rYKa=w80-h106-k-no",
    href: "https://www.google.com/maps/place/Ledra+City+Archaeological+Museum/data=!4m7!3m6!1s0x14de17b564a9206b:0x2d3ae2da9034b665!8m2!3d35.1657465!4d33.3563952!16s%2Fg%2F11sj29x35v!19sChIJayCpZLUX3hQRZbY0kNriOi0?authuser=0&hl=en&rclk=1",
    latitude: "35.1657465",
    longitude: "33.3563952",
  },
  {
    name: "NiMAC",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipP8QBMSxTHOcYxH0-JW9PCftw0trzF1aNhiYWKU=w122-h92-k-no",
    href: "https://www.google.com/maps/place/NiMAC/data=!4m7!3m6!1s0x14de17439a1a166d:0xbf3fe077e903ac74!8m2!3d35.173918!4d33.36646!16s%2Fg%2F1pp2vbh5v!19sChIJbRYamkMX3hQRdKwD6XfgP78?authuser=0&hl=en&rclk=1",
    latitude: "35.173918",
    longitude: "33.36646",
  },
  {
    name: "Museum of the National Struggle",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipPEK9fNGdybfc0YpacwrfwXTh9evm8gm8AXRnAl=w138-h92-k-no",
    href: "https://www.google.com/maps/place/Museum+of+the+National+Struggle/data=!4m7!3m6!1s0x14de1743ad528e07:0xd88b73e26c1cc79!8m2!3d35.1736464!4d33.3681112!16s%2Fg%2F11g6nby5qn!19sChIJB45SrUMX3hQReczBJj63iA0?authuser=0&hl=en&rclk=1",
    latitude: "35.1736464",
    longitude: "33.3681112",
  },
  {
    name: "CVAR - Severis Foundation",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipNq8RQjAQv0NBsJySOVquTYHodsjpftT_kaHSIi=w122-h92-k-no",
    href: "https://www.google.com/maps/place/CVAR+-+Severis+Foundation/data=!4m7!3m6!1s0x14de17419b4a7821:0x99d5d847abca06ff!8m2!3d35.1757193!4d33.368746!16s%2Fg%2F11b6bwf3_w!19sChIJIXhKm0EX3hQR_wbKq0fY1Zk?authuser=0&hl=en&rclk=1",
    latitude: "35.1757193",
    longitude: "33.368746",
  },
  {
    name: "National Struggle Museum",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipMgcFMhHxJ6C9flfyF9vwGKIc8W7aiiaEzPuNNu=w199-h92-k-no",
    href: "https://www.google.com/maps/place/National+Struggle+Museum/data=!4m7!3m6!1s0x14de1738977405b1:0xdd55c1e3e1b54611!8m2!3d35.182112!4d33.3637376!16s%2Fg%2F11h3lfxv7t!19sChIJsQV0lzgX3hQREUa14ePBVd0?authuser=0&hl=en&rclk=1",
    latitude: "35.182112",
    longitude: "33.3637376",
  },
  {
    name: "Pierides Museum - Bank of Cyprus Cultural Foundation",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipPzUVrCNQ_LHUIbNFIwiPz9nZjgWsVIM63R2-Tt=w122-h92-k-no",
    href: "https://www.google.com/maps/place/Pierides+Museum+-+Bank+of+Cyprus+Cultural+Foundation/data=!4m7!3m6!1s0x14e0838d946f03bd:0x2bb52dac86ea31bc!8m2!3d34.9162407!4d33.6363169!16s%2Fm%2F0qktzmt!19sChIJvQNvlI2D4BQRvDHqhqwttSs?authuser=0&hl=en&rclk=1",
    latitude: "34.9162407",
    longitude: "33.6363169",
  },
  {
    name: "A. G. Leventis Gallery",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipMTdtMDr-dQxWyEt_vIxmnUJpD6D-SuCHAV_zk-=w122-h92-k-no",
    href: "https://www.google.com/maps/place/A.+G.+Leventis+Gallery/data=!4m7!3m6!1s0x14de1750c7736f87:0x20e4977b50ce11ac!8m2!3d35.169375!4d33.3583083!16s%2Fm%2F0105r3kh!19sChIJh29zx1AX3hQRrBHOUHuX5CA?authuser=0&hl=en&rclk=1",
    latitude: "35.169375",
    longitude: "33.3583083",
  },
  {
    name: "Archaeological Museum of Ancient Idalion",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipM-3WKgC2VZeyTtdzxHXuEt_A8jwI5KuNE3QfA7=w122-h92-k-no",
    href: "https://www.google.com/maps/place/Archaeological+Museum+of+Ancient+Idalion/data=!4m7!3m6!1s0x14de1f9bb0c55ec5:0x35ebc61e2e8abeda!8m2!3d35.0192252!4d33.4233303!16s%2Fg%2F11g6nbvntq!19sChIJxV7FsJsf3hQR2r6KLh7G6zU?authuser=0&hl=en&rclk=1",
    latitude: "35.0192252",
    longitude: "33.4233303",
  },
  {
    name: "Cyprus Car Museum",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipM2oRSyFzQ7N0PAoU8oeLvWze_jGGn_gd5eyVTt=w80-h142-k-no",
    href: "https://www.google.com/maps/place/Cyprus+Car+Museum/data=!4m7!3m6!1s0x14de11170df01dc1:0xa99d062bdd5c8d81!8m2!3d35.225104!4d33.3227964!16s%2Fg%2F11b6gqnr30!19sChIJwR3wDRcR3hQRgY1c3SsGnak?authuser=0&hl=en&rclk=1",
    latitude: "35.225104",
    longitude: "33.3227964",
  },
  {
    name: "K\u0131br\u0131s T\u00fcrk \u0130slam Eserleri M\u00fczesi",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipOuEreqY3Hb75y7fs3_v7fqoaTZZhFM8_lKh-2F=w122-h92-k-no",
    href: "https://www.google.com/maps/place/K%C4%B1br%C4%B1s+T%C3%BCrk+%C4%B0slam+Eserleri+M%C3%BCzesi/data=!4m7!3m6!1s0x14de17441c0f8df9:0xd76e364699463bf4!8m2!3d35.1761581!4d33.3644416!16s%2Fg%2F11f5dcsjff!19sChIJ-Y0PHEQX3hQR9DtGmUY2btc?authuser=0&hl=en&rclk=1",
    latitude: "35.1761581",
    longitude: "33.3644416",
  },
  {
    name: "APOEL MUSEUM",
    category: "museums",
    image_url: "//maps.gstatic.com/tactile/pane/result-no-thumbnail-2x.png",
    href: "https://www.google.com/maps/place/APOEL+MUSEUM/data=!4m7!3m6!1s0x14de19dfbab20239:0x31872048cb81bff2!8m2!3d35.1572705!4d33.3731394!16s%2Fg%2F11crzzzjf4!19sChIJOQKyut8Z3hQR8r-By0gghzE?authuser=0&hl=en&rclk=1",
    latitude: "35.1572705",
    longitude: "33.3731394",
  },
  {
    name: "Fikardou Rural Museum",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipNWTZdG9JP4yg-1atj4shVzQSqwL2ubZ710tUJC=w122-h92-k-no",
    href: "https://www.google.com/maps/place/Fikardou+Rural+Museum/data=!4m7!3m6!1s0x14e0ae9db3d3e5e7:0x92b4a8707c72d120!8m2!3d34.9599727!4d33.1713914!16s%2Fg%2F11dx8m8thx!19sChIJ5-XTs52u4BQRINFyfHCotJI?authuser=0&hl=en&rclk=1",
    latitude: "34.9599727",
    longitude: "33.1713914",
  },
  {
    name: "Walled City Museum - Surlari\u00e7i \u015eehir M\u00fczesi",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipMCDtfVHLxsBE3pOSQBpeRvokxlZVF-hc_Z5xz_=w122-h92-k-no",
    href: "https://www.google.com/maps/place/Walled+City+Museum+-+Surlari%C3%A7i+%C5%9Eehir+M%C3%BCzesi/data=!4m7!3m6!1s0x14de172d6fb48a23:0xe8bf2127759ceb6f!8m2!3d35.1811872!4d33.3615595!16s%2Fg%2F11qnzk90p7!19sChIJI4q0by0X3hQRb-ucdSchv-g?authuser=0&hl=en&rclk=1",
    latitude: "35.1811872",
    longitude: "33.3615595",
  },
  {
    name: "Peace and Freedom Museum",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipND_fGWMm_P5hx0SrlN4DsAHs5J6sVko6Ox5zj5=w138-h92-k-no",
    href: "https://www.google.com/maps/place/Peace+and+Freedom+Museum/data=!4m7!3m6!1s0x14de0d467b79c259:0x34e38a0ad68bce94!8m2!3d35.3442877!4d33.2415911!16s%2Fg%2F1tdmxvyg!19sChIJWcJ5e0YN3hQRlM6L1gqK4zQ?authuser=0&hl=en&rclk=1",
    latitude: "35.3442877",
    longitude: "33.2415911",
  },
  {
    name: "Cyprus Modern Art Museum",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipMZaFYKkR53Mb-7KeNr2S6x5H1eB9g-wyT3CZtP=w126-h92-k-no",
    href: "https://www.google.com/maps/place/Cyprus+Modern+Art+Museum/data=!4m7!3m6!1s0x14de11149b5b4595:0x60fbe7ec6809e137!8m2!3d35.2248746!4d33.3237399!16s%2Fg%2F11h0mschpm!19sChIJlUVbmxQR3hQRN-EJaOzn-2A?authuser=0&hl=en&rclk=1",
    latitude: "35.2248746",
    longitude: "33.3237399",
  },
  {
    name: "Archaeological Museum of Larnaka District",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipPKoA9PiGio0VHC4XIjvpCHfFtW1TqzOcFob_sZ=w163-h92-k-no",
    href: "https://www.google.com/maps/place/Archaeological+Museum+of+Larnaka+District/data=!4m7!3m6!1s0x14e082a727a064e7:0x437ec0ec71cb3a4f!8m2!3d34.9191425!4d33.6334909!16s%2Fm%2F0ql4w7s!19sChIJ52SgJ6eC4BQRTzrLcezAfkM?authuser=0&hl=en&rclk=1",
    latitude: "34.9191425",
    longitude: "33.6334909",
  },
  {
    name: "Mevlevi Lodge Museum",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipOe1ZLkLFBKWkV0Ji4KU1XywuCrHA-mJpD_jqGv=w163-h92-k-no",
    href: "https://www.google.com/maps/place/Mevlevi+Lodge+Museum/data=!4m7!3m6!1s0x14de1747bce16755:0xc15ff529b28b8de1!8m2!3d35.1807237!4d33.361809!16s%2Fg%2F11bc91n252!19sChIJVWfhvEcX3hQR4Y2Lsin1X8E?authuser=0&hl=en&rclk=1",
    latitude: "35.1807237",
    longitude: "33.361809",
  },
  {
    name: "Sofa factory",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipP9j4mQgE-UX5DFndRFEm_DQX7hEXaO0BuTNWWS=w122-h92-k-no",
    href: "https://www.google.com/maps/place/Sofa+factory/data=!4m7!3m6!1s0x14de17590a4fcc13:0x8413b4bcea58a9e8!8m2!3d35.174946!4d33.3636978!16s%2Fg%2F11fq884123!19sChIJE8xPClkX3hQR6KlY6ry0E4Q?authuser=0&hl=en&rclk=1",
    latitude: "35.174946",
    longitude: "33.3636978",
  },
  {
    name: "Medieval Stone Artifacts Museum",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipNe2YaR5jBzO7qIJA14Zqa_b7a3rQKSSg63EvAR=w163-h92-k-no",
    href: "https://www.google.com/maps/place/Medieval+Stone+Artifacts+Museum/data=!4m7!3m6!1s0x14de17414deec217:0x943e7b0661a3733!8m2!3d35.1766994!4d33.3657005!16s%2Fg%2F11b7q3my6b!19sChIJF8LuTUEX3hQRMzcaZrDnQwk?authuser=0&hl=en&rclk=1",
    latitude: "35.1766994",
    longitude: "33.3657005",
  },
  {
    name: "Crossing",
    category: "museums",
    image_url: "//maps.gstatic.com/tactile/pane/result-no-thumbnail-2x.png",
    href: "https://www.google.com/maps/place/Crossing/data=!4m7!3m6!1s0x14de17003ba6abf3:0x25fd1a3f3d29c18f!8m2!3d35.1753549!4d33.3615085!16s%2Fg%2F11ldrnzcgm!19sChIJ86umOwAX3hQRj8EpPT8a_SU?authuser=0&hl=en&rclk=1",
    latitude: "35.1753549",
    longitude: "33.3615085",
  },
  {
    name: "Ancient Kition Entrance",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipPekaMDJyLgYLk3j5kpFyTOD4MDU-uliuznWNOB=w80-h164-k-no",
    href: "https://www.google.com/maps/place/Ancient+Kition+Entrance/data=!4m7!3m6!1s0x14de297cb94dc783:0x48ed125c7ef2678f!8m2!3d34.9225691!4d33.630591!16s%2Fg%2F11h1l0y4hr!19sChIJg8dNuXwp3hQRj2fyflwS7Ug?authuser=0&hl=en&rclk=1",
    latitude: "34.9225691",
    longitude: "33.630591",
  },
  {
    name: "Kallinikeio Municipal Museum of Athienou",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipNLkyvcYIfzOKjH_-cgxT3pZat-dZFNupVHkV8I=w138-h92-k-no",
    href: "https://www.google.com/maps/place/Kallinikeio+Municipal+Museum+of+Athienou/data=!4m7!3m6!1s0x14de247caf23754b:0x697a4b353b2664c2!8m2!3d35.06387!4d33.5390362!16s%2Fg%2F12hq81wv5!19sChIJS3Ujr3wk3hQRwmQmOzVLemk?authuser=0&hl=en&rclk=1",
    latitude: "35.06387",
    longitude: "33.5390362",
  },
  {
    name: "National History Museum Of Ayia Napa",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipPhvk2BGGjrADbZ9YnBu6QhRba3pUp6mo2mLOyE=w80-h106-k-no",
    href: "https://www.google.com/maps/place/National+History+Museum+Of+Ayia+Napa/data=!4m7!3m6!1s0x14dfc56c34c0ca57:0x7b0ef5b98a474e56!8m2!3d34.9915829!4d33.9930406!16s%2Fg%2F11c1wwsr7x!19sChIJV8rANGzF3xQRVk5Hirn1Dns?authuser=0&hl=en&rclk=1",
    latitude: "34.9915829",
    longitude: "33.9930406",
  },
  {
    name: "JMC JEWISH MUSEUM OF CYPRUS",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipPsvmlf7kI9BNavvZ_HhkG8EgAuKuiWo2-CDogm=w194-h92-k-no",
    href: "https://www.google.com/maps/place/JMC+JEWISH+MUSEUM+OF+CYPRUS/data=!4m7!3m6!1s0x14e08321af0b1071:0x519218139e7cb42d!8m2!3d34.9123412!4d33.6325099!16s%2Fg%2F11r9h33yh1!19sChIJcRALryGD4BQRLbR8nhMYklE?authuser=0&hl=en&rclk=1",
    latitude: "34.9123412",
    longitude: "33.6325099",
  },
  {
    name: "Archbishop Makarios III Foundation Art Galleries",
    category: "museums",
    image_url: "//maps.gstatic.com/tactile/pane/result-no-thumbnail-2x.png",
    href: "https://www.google.com/maps/place/Archbishop+Makarios+III+Foundation+Art+Galleries/data=!4m7!3m6!1s0x14de17c63e7729a1:0x5b2f62422dd849d4!8m2!3d35.172558!4d33.3683474!16s%2Fg%2F11vkcfsm_0!19sChIJoSl3PsYX3hQR1EnYLUJiL1s?authuser=0&hl=en&rclk=1",
    latitude: "35.172558",
    longitude: "33.3683474",
  },
  {
    name: "Thalassa",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipNe_AUC5qKkne1fuU_GTKSySyt7hnu1F5qMZ18f=w122-h92-k-no",
    href: "https://www.google.com/maps/place/Thalassa/data=!4m7!3m6!1s0x14dfc513dbe4625d:0x450e6bb580cd9!8m2!3d34.9875239!4d34.0026259!16s%2Fg%2F11g0kd1cxp!19sChIJXWLk2xPF3xQR2QxYu-ZQBAA?authuser=0&hl=en&rclk=1",
    latitude: "34.9875239",
    longitude: "34.0026259",
  },
  {
    name: "Larnaka Historic Archives Museum",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipMcYgdShzdV5BeuBUHJfZtqfF4RgC3inchhtAON=w122-h92-k-no",
    href: "https://www.google.com/maps/place/Larnaka+Historic+Archives+Museum/data=!4m7!3m6!1s0x14e082a1a227dccf:0xd541de020c6e82dd!8m2!3d34.9166905!4d33.6375151!16s%2Fg%2F1td816lm!19sChIJz9wnoqGC4BQR3YJuDALeQdU?authuser=0&hl=en&rclk=1",
    latitude: "34.9166905",
    longitude: "33.6375151",
  },
  {
    name: "HAMBIS MUNICIPAL MUSEUM OF PRINTMAKING",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipOsu6iGSpbun7xYrXyOJ35kZ18FL307RIIVYg2t=w122-h92-k-no",
    href: "https://www.google.com/maps/place/HAMBIS+MUNICIPAL+MUSEUM+OF+PRINTMAKING/data=!4m7!3m6!1s0x14de171f4074bce7:0x4428dc6736972813!8m2!3d35.1748508!4d33.3702106!16s%2Fg%2F11h8ggndgr!19sChIJ57x0QB8X3hQREyiXNmfcKEQ?authuser=0&hl=en&rclk=1",
    latitude: "35.1748508",
    longitude: "33.3702106",
  },
  {
    name: "Cyprus Museum of Natural History",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipMWeJuYk_Z8nT7lk68P7ou70BuAbXC5sD7Jx9zn=w122-h92-k-no",
    href: "https://www.google.com/maps/place/Cyprus+Museum+of+Natural+History/data=!4m7!3m6!1s0x14de1ed20a833257:0xaf611d858c5ceced!8m2!3d35.0755592!4d33.3817075!16s%2Fm%2F0cc545m!19sChIJVzKDCtIe3hQR7excjIUdYa8?authuser=0&hl=en&rclk=1",
    latitude: "35.0755592",
    longitude: "33.3817075",
  },
  {
    name: "Bicycle Museum",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipMaL-oIS88ArV3zv2PIlvohMaoRNh02ZYye4VIe=w122-h92-k-no",
    href: "https://www.google.com/maps/place/Bicycle+Museum/data=!4m7!3m6!1s0x14e0ad0022ae14ed:0xe0abb71ab31b65d3!8m2!3d34.9573789!4d33.1585103!16s%2Fg%2F11y3jqd9v9!19sChIJ7RSuIgCt4BQR02Ubsxq3q-A?authuser=0&hl=en&rclk=1",
    latitude: "34.9573789",
    longitude: "33.1585103",
  },
  {
    name: "MUSAN Museum of Underwater Sculpture Ayia Napa",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipMPE-S25_d6OdHc4jNjDvvRLS_r5a886LQtGKyr=w122-h92-k-no",
    href: "https://www.google.com/maps/place/MUSAN+Museum+of+Underwater+Sculpture+Ayia+Napa/data=!4m7!3m6!1s0x14dfc59ccdef899b:0xc260b2c06a6dd902!8m2!3d34.9852066!4d33.9838027!16s%2Fg%2F11rs05ksm0!19sChIJm4nvzZzF3xQRAtltasCyYMI?authuser=0&hl=en&rclk=1",
    latitude: "34.9852066",
    longitude: "33.9838027",
  },
  {
    name: "Urban Gorillas",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipO421gHxuL_Klag9I9KsZFBOTYEOQd0fYeIOjAX=w80-h173-k-no",
    href: "https://www.google.com/maps/place/Urban+Gorillas/data=!4m7!3m6!1s0x14de17108523bdb9:0x7f4baed962b2679c!8m2!3d35.1862252!4d33.3788806!16s%2Fg%2F11c1tr877m!19sChIJub0jhRAX3hQRnGeyYtmuS38?authuser=0&hl=en&rclk=1",
    latitude: "35.1862252",
    longitude: "33.3788806",
  },
  {
    name: "Shipwreck Museum",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipNYLy0VJfBFduGTmEn7jhlCxq6ZWVRBfJ1WvKQy=w122-h92-k-no",
    href: "https://www.google.com/maps/place/Shipwreck+Museum/data=!4m7!3m6!1s0x14de6cc6294cfdef:0xb5807dfb6c3aae10!8m2!3d35.3415528!4d33.322872!16s%2Fg%2F1q5blqp0h!19sChIJ7_1MKcZs3hQREK46bPt9gLU?authuser=0&hl=en&rclk=1",
    latitude: "35.3415528",
    longitude: "33.322872",
  },
  {
    name: "Musan underwater sculpture spot",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipN-CDaWKXQIwS3bnx3-wztoJPHvtHcA1BW848Cc=w163-h92-k-no",
    href: "https://www.google.com/maps/place/Musan+underwater+sculpture+spot/data=!4m7!3m6!1s0x14dfc53ed30738bb:0x56ddd4f7610fadcf!8m2!3d34.9812208!4d34.0002803!16s%2Fg%2F11td_t9wgn!19sChIJuzgH0z7F3xQRz60PYffU3VY?authuser=0&hl=en&rclk=1",
    latitude: "34.9812208",
    longitude: "34.0002803",
  },
  {
    name: "The Noble Peasant Statue",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipOlTkzabKbp7sN3SxNVAZHt_j83wL7IYYA9YORx=w163-h92-k-no",
    href: "https://www.google.com/maps/place/The+Noble+Peasant+Statue/data=!4m7!3m6!1s0x14de13268d50ff21:0x16de75ab2ed93326!8m2!3d35.3137014!4d33.3323606!16s%2Fg%2F11qn_9cg3v!19sChIJIf9QjSYT3hQRJjPZLqt13hY?authuser=0&hl=en&rclk=1",
    latitude: "35.3137014",
    longitude: "33.3323606",
  },
  {
    name: "Simoni Symeonidou's Studio",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipMgMX48cI-9ybofggFxsrWxyu4FNBmEuWjiOWTb=w137-h92-k-no",
    href: "https://www.google.com/maps/place/Simoni+Symeonidou%27s+Studio/data=!4m7!3m6!1s0x14de1744c68bbee9:0xc59c312f65238e99!8m2!3d35.1725104!4d33.3638362!16s%2Fg%2F11g873n2n4!19sChIJ6b6LxkQX3hQRmY4jZS8xnMU?authuser=0&hl=en&rclk=1",
    latitude: "35.1725104",
    longitude: "33.3638362",
  },
  {
    name: "KK VIOLIN MUSEUM",
    category: "museums",
    image_url: "//maps.gstatic.com/tactile/pane/result-no-thumbnail-2x.png",
    href: "https://www.google.com/maps/place/KK+VIOLIN+MUSEUM/data=!4m7!3m6!1s0x14de174b2504e3fb:0xdfb7570dc13c4928!8m2!3d35.1632569!4d33.3913776!16s%2Fg%2F11lcrzytb0!19sChIJ--MEJUsX3hQRKEk8wQ1Xt98?authuser=0&hl=en&rclk=1",
    latitude: "35.1632569",
    longitude: "33.3913776",
  },
  {
    name: "Char. Pilakoutas Heritage",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipP4FN0p4a66K1nmivjXjl5RPFfFOOqGPFJPcETK=w80-h106-k-no",
    href: "https://www.google.com/maps/place/Char.+Pilakoutas+Heritage/data=!4m7!3m6!1s0x14de19cc9397b06f:0xa219c1808f164b2c!8m2!3d35.1254525!4d33.3647974!16s%2Fg%2F11p75b1vph!19sChIJb7CXk8wZ3hQRLEsWj4DBGaI?authuser=0&hl=en&rclk=1",
    latitude: "35.1254525",
    longitude: "33.3647974",
  },
  {
    name: "Police Museum",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipMSic-ezH2sJA-Lk1BWVHPk3mbT_YUg8K94JnWb=w138-h92-k-no",
    href: "https://www.google.com/maps/place/Police+Museum/data=!4m7!3m6!1s0x14de19c3ce0a2bc3:0xee3d0bd7596ccd63!8m2!3d35.1447267!4d33.3742225!16s%2Fm%2F0cc5pb5!19sChIJwysKzsMZ3hQRY81sWdcLPe4?authuser=0&hl=en&rclk=1",
    latitude: "35.1447267",
    longitude: "33.3742225",
  },
  {
    name: "\u03a0\u03b1\u03c1\u03b1\u03b4\u03bf\u03c3\u03b9\u03b1\u03ba\u03cc \u03a3\u03c0\u03af\u03c4\u03b9 \u03a0\u03b1\u03c1\u03b1\u03bb\u03b9\u03bc\u03bd\u03af\u03bf\u03c5 (Paralimni Folkloric Museum))",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipPcpzlP2OGrJzoNmu7x2YX-5wQUtd0BLMYdJtut=w122-h92-k-no",
    href: "https://www.google.com/maps/place/%CE%A0%CE%B1%CF%81%CE%B1%CE%B4%CE%BF%CF%83%CE%B9%CE%B1%CE%BA%CF%8C+%CE%A3%CF%80%CE%AF%CF%84%CE%B9+%CE%A0%CE%B1%CF%81%CE%B1%CE%BB%CE%B9%CE%BC%CE%BD%CE%AF%CE%BF%CF%85+%28Paralimni+Folkloric+Museum%29%29/data=!4m7!3m6!1s0x14dfc53a4f9d4633:0x77535017e176178!8m2!3d35.036358!4d33.9831972!16s%2Fg%2F11pb1fc317!19sChIJM0adTzrF3xQReGEXfgE1dQc?authuser=0&hl=en&rclk=1",
    latitude: "35.036358",
    longitude: "33.9831972",
  },
  {
    name: "Byzantine Museum of Saint Lazarus",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipN5cjvzLmvt5ycz9__9mESU1lLe6oL7ZsXJnW3z=w163-h92-k-no",
    href: "https://www.google.com/maps/place/Byzantine+Museum+of+Saint+Lazarus/data=!4m7!3m6!1s0x14e082a354da96fd:0x86b5c75adf4d3370!8m2!3d34.9114108!4d33.6345396!16s%2Fg%2F11d_88chrz!19sChIJ_ZbaVKOC4BQRcDNN31rHtYY?authuser=0&hl=en&rclk=1",
    latitude: "34.9114108",
    longitude: "33.6345396",
  },
  {
    name: "Folklore Museum",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipMgwdM0hHmbWZJqwHHywPT7Um9o1A34z9DLY-Cz=w163-h92-k-no",
    href: "https://www.google.com/maps/place/Folklore+Museum/data=!4m7!3m6!1s0x14de02d3d1a34373:0xcc2df1e6a1fb9c78!8m2!3d35.0715277!4d33.2537371!16s%2Fg%2F11fy2vqc9p!19sChIJc0Oj0dMC3hQReJz7oebxLcw?authuser=0&hl=en&rclk=1",
    latitude: "35.0715277",
    longitude: "33.2537371",
  },
  {
    name: "Lusignan House",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipO3dt1oxHWcFVU6qnUhBPRN5TF87GBP1yzoco8d=w122-h92-k-no",
    href: "https://www.google.com/maps/place/Lusignan+House/data=!4m7!3m6!1s0x14de174127469d63:0x5098adb5870a7b37!8m2!3d35.178135!4d33.366358!16s%2Fm%2F0131vh5w!19sChIJY51GJ0EX3hQRN3sKh7WtmFA?authuser=0&hl=en&rclk=1",
    latitude: "35.178135",
    longitude: "33.366358",
  },
  {
    name: "Platini Museum",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipOKI3J4HklrrXijJsw_nwJREEMhLtEo_w0NRjJ8=w145-h92-k-no",
    href: "https://www.google.com/maps/place/Platini+Museum/data=!4m7!3m6!1s0x14e0a02e0309956f:0x25cb5ad09f299026!8m2!3d34.9515718!4d33.4274711!16s%2Fg%2F1pw3xqjmy!19sChIJb5UJAy6g4BQRJpApn9BayyU?authuser=0&hl=en&rclk=1",
    latitude: "34.9515718",
    longitude: "33.4274711",
  },
  {
    name: "Classic Car Museum",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipPV5ecmvg-OdU1xw5DZP1F5cO74SaKdnUWs7HwQ=w163-h92-k-no",
    href: "https://www.google.com/maps/place/Classic+Car+Museum/data=!4m7!3m6!1s0x14de2d2228828513:0x3e598e2f8b8b11af!8m2!3d34.9992022!4d33.7762157!16s%2Fg%2F11cn6lc4gt!19sChIJE4WCKCIt3hQRrxGLiy-OWT4?authuser=0&hl=en&rclk=1",
    latitude: "34.9992022",
    longitude: "33.7762157",
  },
  {
    name: "Canbulat Museum",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipMsKvvea87m_5bmX6xPgkK5yvCFun-HpFFCy8IK=w122-h92-k-no",
    href: "https://www.google.com/maps/place/Canbulat+Museum/data=!4m7!3m6!1s0x14dfc83c7ff9ca31:0xa902d0ecc904bf84!8m2!3d35.123187!4d33.94711!16s%2Fg%2F1tfhw9zh!19sChIJMcr5fzzI3xQRhL8EyezQAqk?authuser=0&hl=en&rclk=1",
    latitude: "35.123187",
    longitude: "33.94711",
  },
  {
    name: "The Salt & Pepper Museum",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipOql9AdXXzrSwu9en0bNzc8Fw9dTwuvgc1AXxru=w122-h92-k-no",
    href: "https://www.google.com/maps/place/The+Salt+%26+Pepper+Museum/data=!4m7!3m6!1s0x14e083986394de5f:0xbc520aa99b0c8b6d!8m2!3d34.9109583!4d33.6338599!16s%2Fg%2F11h5vfphmb!19sChIJX96UY5iD4BQRbYsMm6kKUrw?authuser=0&hl=en&rclk=1",
    latitude: "34.9109583",
    longitude: "33.6338599",
  },
  {
    name: "Craft of Caning Museum",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipNJxbvl7VqQCOZ_cRdd3l1boWaOL7EdimlxP1Xn=w163-h92-k-no",
    href: "https://www.google.com/maps/place/Craft+of+Caning+Museum/data=!4m7!3m6!1s0x14de2913d4758c65:0x12078164ea3b4bfe!8m2!3d34.9556247!4d33.6262721!16s%2Fg%2F11h64psw3s!19sChIJZYx11BMp3hQR_ks76mSBBxI?authuser=0&hl=en&rclk=1",
    latitude: "34.9556247",
    longitude: "33.6262721",
  },
  {
    name: "Mutlu \u00c7ocuklar Bilim Park\u0131",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipMc_WXOau1FoEGz73J5rXgNImGPiWL0D2V24oek=w122-h92-k-no",
    href: "https://www.google.com/maps/place/Mutlu+%C3%87ocuklar+Bilim+Park%C4%B1/data=!4m7!3m6!1s0x14de0f0f345aa127:0x1b394a0b8d669f83!8m2!3d35.2818019!4d33.2814736!16s%2Fg%2F11pz5dm67c!19sChIJJ6FaNA8P3hQRg59mjQtKORs?authuser=0&hl=en&rclk=1",
    latitude: "35.2818019",
    longitude: "33.2814736",
  },
  {
    name: "National Modern Art Gallery, Nicosia",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipMUKZIGF0GFwyHeqvZIVzkR60IYyTpkUvvozF9A=w122-h92-k-no",
    href: "https://www.google.com/maps/place/National+Modern+Art+Gallery,+Nicosia/data=!4m7!3m6!1s0x14de175b8ffb62a9:0x8d5a144fbe26da56!8m2!3d35.1680795!4d33.3657365!16s%2Fg%2F1s04hshmj!19sChIJqWL7j1sX3hQRVtomvk8UWo0?authuser=0&hl=en&rclk=1",
    latitude: "35.1680795",
    longitude: "33.3657365",
  },
  {
    name: "Pattichion Municapal Museum f The Historical Archives of Larnaca",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipPyCh4edyI47I_EzsAO8sqtdhixqG9OQYCyEdVF=w163-h92-k-no",
    href: "https://www.google.com/maps/place/Pattichion+Municapal+Museum+f+The+Historical+Archives+of+Larnaca/data=!4m7!3m6!1s0x14e083546627c233:0x218d55e1e81ee09e!8m2!3d34.9166759!4d33.6375085!16s%2Fg%2F11j_2fk5gz!19sChIJM8InZlSD4BQRnuAe6OFVjSE?authuser=0&hl=en&rclk=1",
    latitude: "34.9166759",
    longitude: "33.6375085",
  },
  {
    name: "\u0391\u03a1\u03a7\u0391\u0399\u039f\u039b\u039f\u0393\u0399\u039a\u039f \u039c\u039f\u03a5\u03a3\u0395\u0399\u039f",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipPbHQJKb7upXIqtmyOoFP7V4f3xhmvevNEJFa7o=w122-h92-k-no",
    href: "https://www.google.com/maps/place/%CE%91%CE%A1%CE%A7%CE%91%CE%99%CE%9F%CE%9B%CE%9F%CE%93%CE%99%CE%9A%CE%9F+%CE%9C%CE%9F%CE%A5%CE%A3%CE%95%CE%99%CE%9F/data=!4m7!3m6!1s0x14de174526a5c319:0xa602cf9e4de0727b!8m2!3d35.173016!4d33.3622391!16s%2Fg%2F11b7lhblt7!19sChIJGcOlJkUX3hQRe3LgTZ7PAqY?authuser=0&hl=en&rclk=1",
    latitude: "35.173016",
    longitude: "33.3622391",
  },
  {
    name: "Dr. Faz\u0131l K\u00fc\u00e7\u00fck M\u00fczesi",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipPOgVK3DBcuod8yYQL2Ms_Gha_-pIpNb5uSBd7K=w122-h92-k-no",
    href: "https://www.google.com/maps/place/Dr.+Faz%C4%B1l+K%C3%BC%C3%A7%C3%BCk+M%C3%BCzesi/data=!4m7!3m6!1s0x14de1747b6d26155:0x6817872aac6f492c!8m2!3d35.1801864!4d33.3615842!16s%2Fg%2F11h06pdsvc!19sChIJVWHStkcX3hQRLElvrCqHF2g?authuser=0&hl=en&rclk=1",
    latitude: "35.1801864",
    longitude: "33.3615842",
  },
  {
    name: "Kyriazis Medical Museum",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipMhzZA95sgIgsRuU-ZF__IE4EOpRLIL4xCNBu2b=w122-h92-k-no",
    href: "https://www.google.com/maps/place/Kyriazis+Medical+Museum/data=!4m7!3m6!1s0x14e082a362202669:0x18af35fbda53dade!8m2!3d34.9129545!4d33.6344126!16s%2Fm%2F0n4bcjz!19sChIJaSYgYqOC4BQR3tpT2vs1rxg?authuser=0&hl=en&rclk=1",
    latitude: "34.9129545",
    longitude: "33.6344126",
  },
  {
    name: "K\u0131br\u0131s Herbaryum ve Do\u011fa Tarihi M\u00fczesi",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipN5Pa0pa3LDh4tvX6xvQ_Q9JI0VnPoFqosI7yxW=w120-h92-k-no",
    href: "https://www.google.com/maps/place/K%C4%B1br%C4%B1s+Herbaryum+ve+Do%C4%9Fa+Tarihi+M%C3%BCzesi/data=!4m7!3m6!1s0x14de1151112cbe99:0x44c9d81d0ec29e03!8m2!3d35.2291099!4d33.3218576!16s%2Fg%2F11fl5dfmsy!19sChIJmb4sEVER3hQRA57CDh3YyUQ?authuser=0&hl=en&rclk=1",
    latitude: "35.2291099",
    longitude: "33.3218576",
  },
  {
    name: "Ethnographic Museum of Avgorou",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipOsG6H7XeXJ0sBaXTeV19KiRqfcTAP8gFUVvczc=w122-h92-k-no",
    href: "https://www.google.com/maps/place/Ethnographic+Museum+of+Avgorou/data=!4m7!3m6!1s0x14dfcdc81417defd:0xdbb342ee24a6fbde!8m2!3d35.0397924!4d33.840167!16s%2Fg%2F11hdvc60d7!19sChIJ_d4XFMjN3xQR3vumJO5Cs9s?authuser=0&hl=en&rclk=1",
    latitude: "35.0397924",
    longitude: "33.840167",
  },
  {
    name: "Lefko\u015fa \u015eehir Muzesi",
    category: "museums",
    image_url: "//maps.gstatic.com/tactile/pane/result-no-thumbnail-2x.png",
    href: "https://www.google.com/maps/place/Lefko%C5%9Fa+%C5%9Eehir+Muzesi/data=!4m7!3m6!1s0x14de1746bc00bb57:0x644971978e2baad9!8m2!3d35.1773479!4d33.3643922!16s%2Fg%2F11kq1ftmkz!19sChIJV7sAvEYX3hQR2aorjpdxSWQ?authuser=0&hl=en&rclk=1",
    latitude: "35.1773479",
    longitude: "33.3643922",
  },
  {
    name: "\u039c\u03bf\u03c5\u03c3\u03b5\u03af\u03bf \u03a5\u03c0\u03bf\u03bb\u03bf\u03b3\u03b9\u03c3\u03c4\u03ce\u03bd \u039a\u03cd\u03c0\u03c1\u03bf\u03c5 | Cyprus History Museum",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipNjA51hJrk7C_H21YNhyXn2ln9n-ICyxSXEzCyp=w122-h92-k-no",
    href: "https://www.google.com/maps/place/%CE%9C%CE%BF%CF%85%CF%83%CE%B5%CE%AF%CE%BF+%CE%A5%CF%80%CE%BF%CE%BB%CE%BF%CE%B3%CE%B9%CF%83%CF%84%CF%8E%CE%BD+%CE%9A%CF%8D%CF%80%CF%81%CE%BF%CF%85+%7C+Cyprus+History+Museum/data=!4m7!3m6!1s0x14de1bb6c95cfbd9:0x389c92c056693a3d!8m2!3d35.1686199!4d33.3248092!16s%2Fg%2F11twg_c85y!19sChIJ2ftcybYb3hQRPTppVsCSnDg?authuser=0&hl=en&rclk=1",
    latitude: "35.1686199",
    longitude: "33.3248092",
  },
  {
    name: "\u039c\u03bf\u03c5\u03c3\u03b5\u03af\u03bf \u0391\u03b3\u03ce\u03bd\u03bf\u03c2",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipOVJgD9RVNqnlRRJobpuXgmb8uPxv21jDh5XFwo=w122-h92-k-no",
    href: "https://www.google.com/maps/place/%CE%9C%CE%BF%CF%85%CF%83%CE%B5%CE%AF%CE%BF+%CE%91%CE%B3%CF%8E%CE%BD%CE%BF%CF%82/data=!4m7!3m6!1s0x14de1863d053d9d7:0xc7bb7b2097a4bdc8!8m2!3d35.1076393!4d33.4220657!16s%2Fg%2F11r8bj0x0!19sChIJ19lT0GMY3hQRyL2klyB7u8c?authuser=0&hl=en&rclk=1",
    latitude: "35.1076393",
    longitude: "33.4220657",
  },
  {
    name: "Olive-Mill Museum",
    category: "museums",
    image_url: "//maps.gstatic.com/tactile/pane/result-no-thumbnail-2x.png",
    href: "https://www.google.com/maps/place/Olive-Mill+Museum/data=!4m7!3m6!1s0x14e74dd3ff42a907:0xc1b4a74caf773414!8m2!3d34.9271028!4d32.9945095!16s%2Fg%2F11c6v98bg3!19sChIJB6lC_9NN5xQRFDR3r0yntME?authuser=0&hl=en&rclk=1",
    latitude: "34.9271028",
    longitude: "32.9945095",
  },
  {
    name: "Riverside studio",
    category: "museums",
    image_url: "//maps.gstatic.com/tactile/pane/result-no-thumbnail-2x.png",
    href: "https://www.google.com/maps/place/Riverside+studio/data=!4m7!3m6!1s0x14de1741f623649d:0xb5a2c6076f026d85!8m2!3d35.1754302!4d33.3699195!16s%2Fg%2F11vfbf507w!19sChIJnWQj9kEX3hQRhW0CbwfGorU?authuser=0&hl=en&rclk=1",
    latitude: "35.1754302",
    longitude: "33.3699195",
  },
  {
    name: "Museum For Stone Sculpture",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipMl0MrCxC00fpjCGwAjpJGuorZJnbcdVzylhj0i=w122-h92-k-no",
    href: "https://www.google.com/maps/place/Museum+For+Stone+Sculpture/data=!4m7!3m6!1s0x14de204097089379:0x835beb28569d03e1!8m2!3d34.9981132!4d33.4616015!16s%2Fg%2F11c40tx1kz!19sChIJeZMIl0Ag3hQR4QOdVijrW4M?authuser=0&hl=en&rclk=1",
    latitude: "34.9981132",
    longitude: "33.4616015",
  },
  {
    name: "\u039c\u03bf\u03c5\u03c3\u03b5\u03af\u03bf \u0392\u03c5\u03b6\u03b1\u03bd\u03c4\u03b9\u03bd\u03ae\u03c2 \u039a\u03bb\u03b7\u03c1\u03bf\u03bd\u03bf\u03bc\u03b9\u03ac\u03c2 \u03a0\u03b1\u03bb\u03b1\u03b9\u03c7\u03c9\u03c1\u03af\u03bf\u03c5 - Byzantine Museum",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipMJUCsgFBS44KSHQPOmHhPYwmJcGuoq9ZfamCbN=w80-h106-k-no",
    href: "https://www.google.com/maps/place/%CE%9C%CE%BF%CF%85%CF%83%CE%B5%CE%AF%CE%BF+%CE%92%CF%85%CE%B6%CE%B1%CE%BD%CF%84%CE%B9%CE%BD%CE%AE%CF%82+%CE%9A%CE%BB%CE%B7%CF%81%CE%BF%CE%BD%CE%BF%CE%BC%CE%B9%CE%AC%CF%82+%CE%A0%CE%B1%CE%BB%CE%B1%CE%B9%CF%87%CF%89%CF%81%CE%AF%CE%BF%CF%85+-+Byzantine+Museum/data=!4m7!3m6!1s0x14e0b2a527ce9e57:0xf01ef3b24adb1012!8m2!3d34.9225167!4d33.092868!16s%2Fg%2F11g9j5s1tw!19sChIJV57OJ6Wy4BQREhDbSrLzHvA?authuser=0&hl=en&rclk=1",
    latitude: "34.9225167",
    longitude: "33.092868",
  },
  {
    name: "Ravelin Bastion",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipNfO883sUNafrxDe4fIquxbX6eZ-ZOo-fRhHqXA=w80-h106-k-no",
    href: "https://www.google.com/maps/place/Ravelin+Bastion/data=!4m7!3m6!1s0x14dfc985db778775:0x3a42d3d42f84c03d!8m2!3d35.1216235!4d33.9392698!16s%2Fg%2F11flv23xgk!19sChIJdYd324XJ3xQRPcCEL9TTQjo?authuser=0&hl=en&rclk=1",
    latitude: "35.1216235",
    longitude: "33.9392698",
  },
  {
    name: "Dervi\u015f Pa\u015fa Etno\u011frafya M\u00fczesi",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipNiw_QqvEADJxXccCwKNYP_G6kxPCuhDO4N46zd=w122-h92-k-no",
    href: "https://www.google.com/maps/place/Dervi%C5%9F+Pa%C5%9Fa+Etno%C4%9Frafya+M%C3%BCzesi/data=!4m7!3m6!1s0x14de174f72b814ff:0xf7865e04a7745c08!8m2!3d35.1764035!4d33.3584826!16s%2Fg%2F1tyh4qfs!19sChIJ_xS4ck8X3hQRCFx0pwRehvc?authuser=0&hl=en&rclk=1",
    latitude: "35.1764035",
    longitude: "33.3584826",
  },
  {
    name: "\u03a0\u03b1\u03c4\u03c1\u03b9\u03ba\u03ae \u03bf\u03b9\u03ba\u03af\u03b1 \u03bc\u03bf\u03bd\u03b1\u03c7\u03bf\u03cd \u039a\u03b1\u03bb\u03bb\u03b9\u03bd\u03b9\u03ba\u03bf\u03c5 \u03ba\u03b1\u03b9 \u03a0\u03b1\u03bb\u03b1\u03b9\u03cc \u03a4\u03c5\u03c1\u03bf\u03ba\u03bf\u03bc\u03b5\u03af\u03bf",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipMjyj62IuYN6kGXHVE3E-KqvL4jv77A9RyP-Rfl=w155-h92-k-no",
    href: "https://www.google.com/maps/place/%CE%A0%CE%B1%CF%84%CF%81%CE%B9%CE%BA%CE%AE+%CE%BF%CE%B9%CE%BA%CE%AF%CE%B1+%CE%BC%CE%BF%CE%BD%CE%B1%CF%87%CE%BF%CF%8D+%CE%9A%CE%B1%CE%BB%CE%BB%CE%B9%CE%BD%CE%B9%CE%BA%CE%BF%CF%85+%CE%BA%CE%B1%CE%B9+%CE%A0%CE%B1%CE%BB%CE%B1%CE%B9%CF%8C+%CE%A4%CF%85%CF%81%CE%BF%CE%BA%CE%BF%CE%BC%CE%B5%CE%AF%CE%BF/data=!4m7!3m6!1s0x14de25d5b2c797b7:0x1abccbbb9ef5f5a7!8m2!3d35.063275!4d33.5403095!16s%2Fg%2F11nn19kw9h!19sChIJt5fHstUl3hQRp_X1nrvLvBo?authuser=0&hl=en&rclk=1",
    latitude: "35.063275",
    longitude: "33.5403095",
  },
  {
    name: "\u03a3\u03c4\u03c1\u03b1\u03c4\u03b9\u03c9\u03c4\u03b9\u03ba\u03cc \u039c\u03bd\u03b7\u03bc\u03b5\u03af\u03bf",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipPeIYXCicpw4mIDMzpBqitrcoB0pAExLhcr6Plt=w122-h92-k-no",
    href: "https://www.google.com/maps/place/%CE%A3%CF%84%CF%81%CE%B1%CF%84%CE%B9%CF%89%CF%84%CE%B9%CE%BA%CF%8C+%CE%9C%CE%BD%CE%B7%CE%BC%CE%B5%CE%AF%CE%BF/data=!4m7!3m6!1s0x14de1be87fc2ed05:0x63f22eaef22734fa!8m2!3d35.154331!4d33.308213!16s%2Fg%2F11h_2fk7xg!19sChIJBe3Cf-gb3hQR-jQn8q4u8mM?authuser=0&hl=en&rclk=1",
    latitude: "35.154331",
    longitude: "33.308213",
  },
  {
    name: "Byzantine Museum",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipMAz_smuOpB_5CDXAXIB9PQb3mcJFTIKFVzoUM2=w122-h92-k-no",
    href: "https://www.google.com/maps/place/Byzantine+Museum/data=!4m7!3m6!1s0x14de175dca22f11b:0xb9aa0e009edc6819!8m2!3d35.1733421!4d33.3674694!16s%2Fg%2F1vp5_7jk!19sChIJG_Eiyl0X3hQRGWjcngAOqrk?authuser=0&hl=en&rclk=1",
    latitude: "35.1733421",
    longitude: "33.3674694",
  },
  {
    name: "Larnaca Municipal Art Gallery",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipP8HyZWsOnnJ5ltRo4M04OlS7IlzNFop-Cka4I8=w138-h92-k-no",
    href: "https://www.google.com/maps/place/Larnaca+Municipal+Art+Gallery/data=!4m7!3m6!1s0x14e082a1a41d7ea1:0x6aab09757edfed30!8m2!3d34.9169105!4d33.6375525!16s%2Fg%2F1tf84flm!19sChIJoX4dpKGC4BQRMO3ffnUJq2o?authuser=0&hl=en&rclk=1",
    latitude: "34.9169105",
    longitude: "33.6375525",
  },
  {
    name: "Contemporary Art Museum",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipPhXYwgoLo34cCRbg6IQIc6NOM9dYsf5bfNzZAb=w80-h142-k-no",
    href: "https://www.google.com/maps/place/Contemporary+Art+Museum/data=!4m7!3m6!1s0x14de1743970d75e1:0x52efa58abe18ecad!8m2!3d35.1739301!4d33.3667181!16s%2Fg%2F1hd_fd5k2!19sChIJ4XUNl0MX3hQRrewYvoql71I?authuser=0&hl=en&rclk=1",
    latitude: "35.1739301",
    longitude: "33.3667181",
  },
  {
    name: "Ledra Museum - Observatory",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipPT5u3-hbXxy_LPp1noiyxLOojx0QWGskPRBk6n=w122-h92-k-no",
    href: "https://www.google.com/maps/place/Ledra+Museum+-+Observatory/data=!4m7!3m6!1s0x14de175a83508fd1:0x864448fb5f0c4f11!8m2!3d35.171001!4d33.360157!16s%2Fg%2F1td3nvb4!19sChIJ0Y9Qg1oX3hQREU8MX_tIRIY?authuser=0&hl=en&rclk=1",
    latitude: "35.171001",
    longitude: "33.360157",
  },
  {
    name: "Nicosia Old City",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipN8jgB3ChGri3uc5nRR6VoLWVzZII_cWcyUcx0n=w163-h92-k-no",
    href: "https://www.google.com/maps/place/Nicosia+Old+City/data=!4m7!3m6!1s0x14de17686f79d1e1:0xbde430d1a61e9e2e!8m2!3d35.1701159!4d33.3609942!16s%2Fg%2F11thh8l7d9!19sChIJ4dF5b2gX3hQRLp4eptEw5L0?authuser=0&hl=en&rclk=1",
    latitude: "35.1701159",
    longitude: "33.3609942",
  },
  {
    name: "Meletion Museum",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipNLOVvRkjF7vKp_hPG_cIK8aB4LcpT_AcDic8M-=w163-h92-k-no",
    href: "https://www.google.com/maps/place/Meletion+Museum/data=!4m7!3m6!1s0x14dfcf6cfe3cb67b:0xcac3991452477d45!8m2!3d35.0280043!4d33.9552463!16s%2Fg%2F11c7hfz5l4!19sChIJe7Y8_mzP3xQRRX1HUhSZw8o?authuser=0&hl=en&rclk=1",
    latitude: "35.0280043",
    longitude: "33.9552463",
  },
  {
    name: "The Cyprus Museum Cafe",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipMXSA8lZBAQ2BWFOeitjtgK-Gushh9qRgkymGl1=w163-h92-k-no",
    href: "https://www.google.com/maps/place/The+Cyprus+Museum+Cafe/data=!4m7!3m6!1s0x14de17922921a545:0x975a6f896eb19cec!8m2!3d35.1716079!4d33.3553867!16s%2Fg%2F11scw3lw6n!19sChIJRaUhKZIX3hQR7JyxbolvWpc?authuser=0&hl=en&rclk=1",
    latitude: "35.1716079",
    longitude: "33.3553867",
  },
  {
    name: "BRTK YAYINCILIK TAR\u0130H\u0130 M\u00dcZES\u0130",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipPet_7iwd5ztchVvqvVPP-5pAz-8EYzUFBpj_Nc=w138-h92-k-no",
    href: "https://www.google.com/maps/place/BRTK+YAYINCILIK+TAR%C4%B0H%C4%B0+M%C3%9CZES%C4%B0/data=!4m7!3m6!1s0x14de17458c27a61f:0x76684b24677efffb!8m2!3d35.2121506!4d33.3592843!16s%2Fg%2F11nmzdmhq2!19sChIJH6YnjEUX3hQR-_9-ZyRLaHY?authuser=0&hl=en&rclk=1",
    latitude: "35.2121506",
    longitude: "33.3592843",
  },
  {
    name: "Morphou Archaeology and Nature Museum",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipM-KlOd2g28WZxzIYFwjf96kMOQfwKFYqYP61xg=w137-h92-k-no",
    href: "https://www.google.com/maps/place/Morphou+Archaeology+and+Nature+Museum/data=!4m7!3m6!1s0x14ddfc00596ae17f:0x8c59981bbb3f0942!8m2!3d35.2007148!4d32.9906115!16s%2Fg%2F1v9nkbnr!19sChIJf-FqWQD83RQRQgk_uxuYWYw?authuser=0&hl=en&rclk=1",
    latitude: "35.2007148",
    longitude: "32.9906115",
  },
  {
    name: "A.Soulis Museum",
    category: "museums",
    image_url: "//maps.gstatic.com/tactile/pane/result-no-thumbnail-2x.png",
    href: "https://www.google.com/maps/place/A.Soulis+Museum/data=!4m7!3m6!1s0x14e09d37c326c595:0x11ffb2cfed093b77!8m2!3d34.9092918!4d33.5647674!16s%2Fg%2F11vp_nbfwr!19sChIJlcUmwzed4BQRdzsJ7c-y_xE?authuser=0&hl=en&rclk=1",
    latitude: "34.9092918",
    longitude: "33.5647674",
  },
  {
    name: "\u039a\u03a1\u0391\u03a4\u0399\u039a\u0397 \u03a0\u0399\u039d\u0391\u039a\u039f\u0398\u0397\u039a\u0397 \u03a3\u03a5\u0393\u03a7\u03a1\u039f\u039d\u0397\u03a3 \u03a4\u0395\u03a7\u039d\u0397\u03a3 \u03a3\u03a0\u0395\u039b / SPEL",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipPam9vbTqVPfVfqMCyMyK7Zw0cXh41ZEaUtKE27=w262-h92-k-no",
    href: "https://www.google.com/maps/place/%CE%9A%CE%A1%CE%91%CE%A4%CE%99%CE%9A%CE%97+%CE%A0%CE%99%CE%9D%CE%91%CE%9A%CE%9F%CE%98%CE%97%CE%9A%CE%97+%CE%A3%CE%A5%CE%93%CE%A7%CE%A1%CE%9F%CE%9D%CE%97%CE%A3+%CE%A4%CE%95%CE%A7%CE%9D%CE%97%CE%A3+%CE%A3%CE%A0%CE%95%CE%9B+%2F+SPEL/data=!4m7!3m6!1s0x14de179d0e258a99:0x5ece797c2887e1df!8m2!3d35.1746436!4d33.3706898!16s%2Fg%2F11gy9xgr_k!19sChIJmYolDp0X3hQR3-GHKHx5zl4?authuser=0&hl=en&rclk=1",
    latitude: "35.1746436",
    longitude: "33.3706898",
  },
  {
    name: "The Eaved House",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipNUv6E427DlYPnHBcPayf4lV4Bci7QRDNqJwvRQ=w122-h92-k-no",
    href: "https://www.google.com/maps/place/The+Eaved+House/data=!4m7!3m6!1s0x14de1746aae74b1f:0x667fb5d8ffcc45f5!8m2!3d35.1763033!4d33.3653712!16s%2Fg%2F11clgf410h!19sChIJH0vnqkYX3hQR9UXM_9i1f2Y?authuser=0&hl=en&rclk=1",
    latitude: "35.1763033",
    longitude: "33.3653712",
  },
  {
    name: "Bufavento kale",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipOrXe5RZhecmO-r36_OePxdTY-TBWvr5byLX8Rt=w80-h106-k-no",
    href: "https://www.google.com/maps/place/Bufavento+kale/data=!4m7!3m6!1s0x14de15007322bf35:0x3d2985f1151a185e!8m2!3d35.2875695!4d33.4099202!16s%2Fg%2F11vwvjwmml!19sChIJNb8icwAV3hQRXhgaFfGFKT0?authuser=0&hl=en&rclk=1",
    latitude: "35.2875695",
    longitude: "33.4099202",
  },
  {
    name: "KIBRIS \u00d6ZEL ETNO\u011eRAFYA M\u00dcZES\u0130",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipMdHgYWv159yJHLztIkKUyNc_tmD8Ou7jmsUBot=w80-h106-k-no",
    href: "https://www.google.com/maps/place/KIBRIS+%C3%96ZEL+ETNO%C4%9ERAFYA+M%C3%9CZES%C4%B0/data=!4m7!3m6!1s0x14de1731b332f877:0x6ad961f72fdfab4b!8m2!3d35.1917652!4d33.3570203!16s%2Fg%2F11h07xz3xg!19sChIJd_gyszEX3hQRS6vfL_dh2Wo?authuser=0&hl=en&rclk=1",
    latitude: "35.1917652",
    longitude: "33.3570203",
  },
  {
    name: "\u039c\u03bf\u03c5\u03c3\u03b5\u03af\u03bf \u039b\u03b1\u03ca\u03ba\u03b7\u03c2 \u03a4\u03ad\u03c7\u03bd\u03b7\u03c2 \u0393\u03bf\u03c5\u03c1\u03c1\u03af\u03bf\u03c5",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipN0z5lfZKasJgDByqHprK4Jb6rNYg9yFgy-Vtyl=w122-h92-k-no",
    href: "https://www.google.com/maps/place/%CE%9C%CE%BF%CF%85%CF%83%CE%B5%CE%AF%CE%BF+%CE%9B%CE%B1%CF%8A%CE%BA%CE%B7%CF%82+%CE%A4%CE%AD%CF%87%CE%BD%CE%B7%CF%82+%CE%93%CE%BF%CF%85%CF%81%CF%81%CE%AF%CE%BF%CF%85/data=!4m7!3m6!1s0x14e0adcf95357e9d:0x3d5253e08a290f45!8m2!3d34.9569759!4d33.1577162!16s%2Fg%2F11h59zqkw4!19sChIJnX41lc-t4BQRRQ8piuBTUj0?authuser=0&hl=en&rclk=1",
    latitude: "34.9569759",
    longitude: "33.1577162",
  },
  {
    name: "Local Archaeological Museum Ledroi",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipMG2wh2DYbdggZ5Ohdoqs4g0WJ-GupdlIKROYAk=w137-h92-k-no",
    href: "https://www.google.com/maps/place/Local+Archaeological+Museum+Ledroi/data=!4m7!3m6!1s0x14de171a3cf7b14d:0xeffe898bab4a8aa3!8m2!3d35.1660535!4d33.3563147!16s%2Fg%2F11sf939txq!19sChIJTbH3PBoX3hQRo4pKq4uJ_u8?authuser=0&hl=en&rclk=1",
    latitude: "35.1660535",
    longitude: "33.3563147",
  },
  {
    name: "Sultan 2. Mahmut K\u00fct\u00fcphanesi",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipMPAFhblXkyDsxCR1BB0ZFb4OatnSnnonk8AVL3=w122-h92-k-no",
    href: "https://www.google.com/maps/place/Sultan+2.+Mahmut+K%C3%BCt%C3%BCphanesi/data=!4m7!3m6!1s0x14de1746aeaea149:0x873e8077614b01df!8m2!3d35.1765646!4d33.3650668!16s%2Fg%2F1219h5zq!19sChIJSaGurkYX3hQR3wFLYXeAPoc?authuser=0&hl=en&rclk=1",
    latitude: "35.1765646",
    longitude: "33.3650668",
  },
  {
    name: "Icon Museum",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipMMvNL11IQLoIKrnyU2qeRLDEKH74JIrKDE_i2W=w163-h92-k-no",
    href: "https://www.google.com/maps/place/Icon+Museum/data=!4m7!3m6!1s0x14de6cc589f17653:0xfc617aa70bc2aa77!8m2!3d35.3421068!4d33.3187012!16s%2Fg%2F122t1qqw!19sChIJU3bxicVs3hQRd6rCC6d6Yfw?authuser=0&hl=en&rclk=1",
    latitude: "35.3421068",
    longitude: "33.3187012",
  },
  {
    name: "Embassy of Kuwait",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipP5FirIJXygx8EnS8JZeKLmpqAZ_OywUxN80_FL=w80-h114-k-no",
    href: "https://www.google.com/maps/place/Embassy+of+Kuwait/data=!4m7!3m6!1s0x14de19e7ad1e72d1:0x73eff3b70577f958!8m2!3d35.1527432!4d33.3683917!16s%2Fg%2F11f2dr9qh6!19sChIJ0XIerecZ3hQRWPl3Bbfz73M?authuser=0&hl=en&rclk=1",
    latitude: "35.1527432",
    longitude: "33.3683917",
  },
  {
    name: "Museum Fotis Pittas",
    category: "museums",
    image_url: "//maps.gstatic.com/tactile/pane/result-no-thumbnail-2x.png",
    href: "https://www.google.com/maps/place/Museum+Fotis+Pittas/data=!4m7!3m6!1s0x14dfcf00789f8693:0xb59958fb872f42d4!8m2!3d35.0420181!4d33.9207594!16s%2Fg%2F11y2y3wfz4!19sChIJk4afeADP3xQR1EIvh_tYmbU?authuser=0&hl=en&rclk=1",
    latitude: "35.0420181",
    longitude: "33.9207594",
  },
  {
    name: "Larnaka Medieval Fort",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipNcXuGcXP-zTvNysyHghoXYFux2ZFvwQUQ4G7zt=w80-h106-k-no",
    href: "https://www.google.com/maps/place/Larnaka+Medieval+Fort/data=!4m7!3m6!1s0x14e082bd2c938593:0x811447d1f5d741ad!8m2!3d34.910338!4d33.6376042!16s%2Fg%2F1tfd9t1f!19sChIJk4WTLL2C4BQRrUHX9dFHFIE?authuser=0&hl=en&rclk=1",
    latitude: "34.910338",
    longitude: "33.6376042",
  },
  {
    name: "\u039c\u03bf\u03c5\u03c3\u03b5\u03af\u03bf \u0395\u03b8\u03bd\u03bf\u03bc\u03ac\u03c1\u03c4\u03c5\u03c1\u03bf\u03c2 \u039a\u03c5\u03c0\u03c1\u03b9\u03b1\u03bd\u03bf\u03cd",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipPXwSlCy9YWKlMJgVWnjUpXeYJ0an32D8hdzWYy=w204-h92-k-no",
    href: "https://www.google.com/maps/place/%CE%9C%CE%BF%CF%85%CF%83%CE%B5%CE%AF%CE%BF+%CE%95%CE%B8%CE%BD%CE%BF%CE%BC%CE%AC%CF%81%CF%84%CF%85%CF%81%CE%BF%CF%82+%CE%9A%CF%85%CF%80%CF%81%CE%B9%CE%B1%CE%BD%CE%BF%CF%8D/data=!4m7!3m6!1s0x14de1bf4d7ca0367:0x9b4d98f3eca6be54!8m2!3d35.1462608!4d33.3400869!16s%2Fg%2F11rz9mt29v!19sChIJZwPK1_Qb3hQRVL6m7POYTZs?authuser=0&hl=en&rclk=1",
    latitude: "35.1462608",
    longitude: "33.3400869",
  },
  {
    name: "Achironas EOKA monument and museum",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipOxP2Q6usZIFRxBytRbj0oqbDFRMDqwZqcZu2ND=w137-h92-k-no",
    href: "https://www.google.com/maps/place/Achironas+EOKA+monument+and+museum/data=!4m7!3m6!1s0x14dfcf298d574ce1:0xd0782be6de7af2aa!8m2!3d35.0083966!4d33.8931557!16s%2Fg%2F11flgdcp4w!19sChIJ4UxXjSnP3xQRqvJ63uYreNA?authuser=0&hl=en&rclk=1",
    latitude: "35.0083966",
    longitude: "33.8931557",
  },
  {
    name: "Costa Myrianthea Cultural Centre",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipPrPbv5JLgUKX3Xdj3n0nNC3Hiozn2yDZD2wzNV=w80-h106-k-no",
    href: "https://www.google.com/maps/place/Costa+Myrianthea+Cultural+Centre/data=!4m7!3m6!1s0x14de1bbf69abd5e7:0x2e7d84a1087f8554!8m2!3d35.1475595!4d33.3413972!16s%2Fg%2F11jzcf4c3m!19sChIJ59Wrab8b3hQRVIV_CKGEfS4?authuser=0&hl=en&rclk=1",
    latitude: "35.1475595",
    longitude: "33.3413972",
  },
  {
    name: "Saint Barnabas Monastery",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipNmjWCVWCIaXlQflIBDmzo5fh0jKBWH5d_KUSmC=w122-h92-k-no",
    href: "https://www.google.com/maps/place/Saint+Barnabas+Monastery/data=!4m7!3m6!1s0x14dfb5e0b5e93567:0x9f7304b7a30b7f63!8m2!3d35.1747436!4d33.8803749!16s%2Fg%2F1thlqm14!19sChIJZzXpteC13xQRY38Lo7cEc58?authuser=0&hl=en&rclk=1",
    latitude: "35.1747436",
    longitude: "33.8803749",
  },
  {
    name: "Gregoris Afxentiou Museum",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipO4B_dRIOZyA-upGVHIUB9afJ4XvKVrEpUoT7P6=w163-h92-k-no",
    href: "https://www.google.com/maps/place/Gregoris+Afxentiou+Museum/data=!4m7!3m6!1s0x14e0afad72d21ed9:0xc8fe89216b8b358e!8m2!3d34.9405774!4d33.1920194!16s%2Fg%2F11fl9p609w!19sChIJ2R7Scq2v4BQRjjWLayGJ_sg?authuser=0&hl=en&rclk=1",
    latitude: "34.9405774",
    longitude: "33.1920194",
  },
  {
    name: "Alambra Archeological Site",
    category: "museums",
    image_url: "//maps.gstatic.com/tactile/pane/result-no-thumbnail-2x.png",
    href: "https://www.google.com/maps/place/Alambra+Archeological+Site/data=!4m7!3m6!1s0x14e0a100528b3b25:0xc4d227932e3c085a!8m2!3d34.9843558!4d33.3959549!16s%2Fg%2F11vq7vdb0c!19sChIJJTuLUgCh4BQRWgg8LpMn0sQ?authuser=0&hl=en&rclk=1",
    latitude: "34.9843558",
    longitude: "33.3959549",
  },
  {
    name: "Karababa Tomb",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipPUO8UP5br_8tgaCK_OAOx4ZURcrThbFC7raKZN=w138-h92-k-no",
    href: "https://www.google.com/maps/place/Karababa+Tomb/data=!4m7!3m6!1s0x14de1741146d2111:0xcff5088ce571ef7!8m2!3d35.1770291!4d33.3672172!16s%2Fg%2F11fjxfh5hc!19sChIJESFtFEEX3hQR9x5XzohQ_ww?authuser=0&hl=en&rclk=1",
    latitude: "35.1770291",
    longitude: "33.3672172",
  },
  {
    name: "Trade Secrets",
    category: "museums",
    image_url: "//maps.gstatic.com/tactile/pane/result-no-thumbnail-2x.png",
    href: "https://www.google.com/maps/place/Trade+Secrets/data=!4m7!3m6!1s0x14de17d425e071d9:0x1a2e6418d971b611!8m2!3d35.1784783!4d33.3789925!16s%2Fg%2F11sr8tq_13!19sChIJ2XHgJdQX3hQREbZx2RhkLho?authuser=0&hl=en&rclk=1",
    latitude: "35.1784783",
    longitude: "33.3789925",
  },
  {
    name: "Ecclesiastical Museum",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipMbxB23heDM8GhRSBRHFNS-dMFiv3a_3ZNEw8UN=w80-h106-k-no",
    href: "https://www.google.com/maps/place/Ecclesiastical+Museum/data=!4m7!3m6!1s0x14dfcf6d2d777549:0x8262a0931818864b!8m2!3d35.0281514!4d33.9528662!16s%2Fg%2F12hpl70kh!19sChIJSXV3LW3P3xQRS4YYGJOgYoI?authuser=0&hl=en&rclk=1",
    latitude: "35.0281514",
    longitude: "33.9528662",
  },
  {
    name: "Costas Kaimakliotis Folklore Museum",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipNIUU_VIu1ZC-I5v4apslZI7GQr3AJ8xjSOy7s=w122-h92-k-no",
    href: "https://www.google.com/maps/place/Costas+Kaimakliotis+Folklore+Museum/data=!4m7!3m6!1s0x14de2796943b8c55:0xb315e1e08a8a3ba4!8m2!3d34.9516613!4d33.5884868!16s%2Fg%2F11c4bhbjy2!19sChIJVYw7lJYn3hQRpDuKiuDhFbM?authuser=0&hl=en&rclk=1",
    latitude: "34.9516613",
    longitude: "33.5884868",
  },
  {
    name: "Wather House",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipOtUata95AAbnkcwfrsHQ-smY4Isua57TTBvOyQ=w163-h92-k-no",
    href: "https://www.google.com/maps/place/Wather+House/data=!4m7!3m6!1s0x14de070123df36eb:0xab907b78da0b2707!8m2!3d35.1461663!4d33.1665563!16s%2Fg%2F11sz2twxxq!19sChIJ6zbfIwEH3hQRBycL2nh7kKs?authuser=0&hl=en&rclk=1",
    latitude: "35.1461663",
    longitude: "33.1665563",
  },
  {
    name: "Kibris karpaz",
    category: "museums",
    image_url: "//maps.gstatic.com/tactile/pane/result-no-thumbnail-2x.png",
    href: "https://www.google.com/maps/place/Kibris+karpaz/data=!4m7!3m6!1s0x14de6d18a2d84b0d:0x368818f9de9eed5b!8m2!3d35.33526!4d33.3109441!16s%2Fg%2F11vdh1wfzp!19sChIJDUvYohht3hQRW-2e3vkYiDY?authuser=0&hl=en&rclk=1",
    latitude: "35.33526",
    longitude: "33.3109441",
  },
  {
    name: "T\u00fcrk \u0130slam Eserleri M\u00fczesi - otopark",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipNDO0rBXQ7ICwCPwyd81VAilbBA52aCgvQXQ2HX=w122-h92-k-no",
    href: "https://www.google.com/maps/place/T%C3%BCrk+%C4%B0slam+Eserleri+M%C3%BCzesi+-+otopark/data=!4m7!3m6!1s0x14de17441a47867b:0x4825648974e7b85e!8m2!3d35.175914!4d33.364484!16s%2Fg%2F11b7q8b79j!19sChIJe4ZHGkQX3hQRXrjndIlkJUg?authuser=0&hl=en&rclk=1",
    latitude: "35.175914",
    longitude: "33.364484",
  },
  {
    name: "\u03a4\u03bf \u03c3\u03c0\u03af\u03c4\u03b9 \u03bc\u03b5 \u03c4\u03b9\u03c2 \u03a6\u03bf\u03b9\u03bd\u03b9\u03ba\u03b9\u03ad\u03c2",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipOs64eKCBPCBwdIuwjmrDo_tp2tOhxfVSTVHqmF=w148-h92-k-no",
    href: "https://www.google.com/maps/place/%CE%A4%CE%BF+%CF%83%CF%80%CE%AF%CF%84%CE%B9+%CE%BC%CE%B5+%CF%84%CE%B9%CF%82+%CE%A6%CE%BF%CE%B9%CE%BD%CE%B9%CE%BA%CE%B9%CE%AD%CF%82/data=!4m7!3m6!1s0x14de1f7795c7978d:0x9f6d93e9f2c96417!8m2!3d35.0282218!4d33.3781281!16s%2Fg%2F11h1fwlqpp!19sChIJjZfHlXcf3hQRF2TJ8umTbZ8?authuser=0&hl=en&rclk=1",
    latitude: "35.0282218",
    longitude: "33.3781281",
  },
  {
    name: "Giant olive tree",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipM69oV31l8_V40D02H36OZIyFNOPCwvZ6BQVka2=w153-h92-k-no",
    href: "https://www.google.com/maps/place/Giant+olive+tree/data=!4m7!3m6!1s0x14de17890fcd8bd5:0xf4daa5eeb5200cd9!8m2!3d35.1724679!4d33.3760452!16s%2Fg%2F11j41x3_76!19sChIJ1YvND4kX3hQR2Qwgte6l2vQ?authuser=0&hl=en&rclk=1",
    latitude: "35.1724679",
    longitude: "33.3760452",
  },
  {
    name: "Tripoli Bastion",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipMRsJgBkWl6GBgAvxTfLMbORUB6nCV1vaDnD_tp=w122-h92-k-no",
    href: "https://www.google.com/maps/place/Tripoli+Bastion/data=!4m7!3m6!1s0x14de1750fe92a23f:0x96861b1f5dfc73f7!8m2!3d35.1710919!4d33.3572521!16s%2Fg%2F11c7sr2xd9!19sChIJP6KS_lAX3hQR93P8XR8bhpY?authuser=0&hl=en&rclk=1",
    latitude: "35.1710919",
    longitude: "33.3572521",
  },
  {
    name: "ACHEON AKTI POLYTHEMATIC MUSEUM",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipMLTP1j0MwasBPFs7QcwhHJ0YoZMkEfxxBcwug6=w138-h92-k-no",
    href: "https://www.google.com/maps/place/ACHEON+AKTI+POLYTHEMATIC+MUSEUM/data=!4m7!3m6!1s0x14de1bfe3b076e43:0xcc416a340a10d673!8m2!3d35.1384958!4d33.403232!16s%2Fg%2F11q8v2mmyz!19sChIJQ24HO_4b3hQRc9YQCjRqQcw?authuser=0&hl=en&rclk=1",
    latitude: "35.1384958",
    longitude: "33.403232",
  },
  {
    name: "ttsoaldr",
    category: "museums",
    image_url: "//maps.gstatic.com/tactile/pane/result-no-thumbnail-2x.png",
    href: "https://www.google.com/maps/place/ttsoaldr/data=!4m7!3m6!1s0x14de17d984ed1541:0x5ae4093d11d46cd8!8m2!3d35.1784717!4d33.3789824!16s%2Fg%2F11q3nzj_kl!19sChIJQRXthNkX3hQR2GzUET0J5Fo?authuser=0&hl=en&rclk=1",
    latitude: "35.1784717",
    longitude: "33.3789824",
  },
  {
    name: "Garden Caf\u00e9. Museum Street. Nicosia.",
    category: "museums",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipOsnPqhCeseTlQTKjTF2e8M0FgAkWbJ8rVMdBHj=w80-h106-k-no",
    href: "https://www.google.com/maps/place/Garden+Caf%C3%A9.+Museum+Street.+Nicosia./data=!4m7!3m6!1s0x14de175177cf0227:0x25344d20f741cf74!8m2!3d35.1719716!4d33.354974!16s%2Fg%2F11cn93sn8t!19sChIJJwLPd1EX3hQRdM9B9yBNNCU?authuser=0&hl=en&rclk=1",
    latitude: "35.1719716",
    longitude: "33.354974",
  },
];
module.exports = museums;
