const hotels = [
  {
    name: "Caesar Resort & SPA",
    category: "hotel",
    image_url:
      "https://lh3.googleusercontent.com/gps-proxy/ALd4DhGMgMtt5mMA0rXB_P0R4ef7V-dV0XJRG_z6lh7PVp8dsepK1T_BNsgYe8NehgghXBUIDE3AWYWm8m2rQbf7Zch8uxSda9wxtDjjCiTilaooAYOciWy_16ju1JFperF7q5x9_mNJghg2eDMsei8YoUNbssILj7cZ-96ciu6zS4Ec0vtQ8-q-RbQG=w138-h92-k-no",
    href: "https://www.google.com/maps/place/Caesar+Resort+%26+SPA/data=!4m11!3m10!1s0x14dfb170dc1e85df:0x894f9e48923e5228!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.2609244!4d33.9030854!16s%2Fg%2F1hm2hp2z_!19sChIJ34Ue3HCx3xQRKFI-kkieT4k?authuser=0&hl=en&rclk=1",
    latitude: "35.2609244",
    longitude: "33.9030854",
  },
  {
    name: "Thalassa Beach Resort",
    category: "hotel",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipNkbeLp7BQcs3Y4vPyU9XNfXzbU1jGbFG59h5zt=w138-h92-k-no",
    href: "https://www.google.com/maps/place/Thalassa+Beach+Resort/data=!4m11!3m10!1s0x14dfa40068214b33:0x3748bc260cb4997a!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.330007!4d34.06075!16s%2Fg%2F1hc0sxnly!19sChIJM0shaACk3xQRepm0DCa8SDc?authuser=0&hl=en&rclk=1",
    latitude: "35.330007",
    longitude: "34.06075",
  },
  {
    name: "Courtyard Long Beach",
    category: "hotel",
    image_url:
      "https://lh3.googleusercontent.com/gps-proxy/ALd4DhFACTJrEmadsRbvpN2uLkGEd7UvAqx8BHKv0rCXLA7HXWkrxj9zUaO1pM3XhvisEVhhdT0_oA-cycC3W7_EsFoOg86PEanxmpCLBuhWzI8d9PjR7um27plJjLmeCkUqxttZUYU_xWyJmiCkcDlhkcgyZ4ttS-OVVmwC6X9sdEfqK5OqbVfDfU4Wpg=w138-h92-k-no",
    href: "https://www.google.com/maps/place/Courtyard+Long+Beach/data=!4m11!3m10!1s0x14dfb18451c458a7:0x7f2376c9fbd3a575!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.2567135!4d33.8985504!16s%2Fg%2F11f9xn6cdz!19sChIJp1jEUYSx3xQRdaXT-8l2I38?authuser=0&hl=en&rclk=1",
    latitude: "35.2567135",
    longitude: "33.8985504",
  },
  {
    name: "Karpaz Gate Marina Hotel",
    category: "hotel",
    image_url:
      "https://lh3.googleusercontent.com/gps-proxy/ALd4DhHvJjg-EB015jrOY7d4J2nZgBDcD6GxGZikc4gwAoRlvo8mm2UPC7KwpIDiDkMAAZtDzbfjPxZpHLhPoaxBAZv8oqWjy5CGqKKsDws_n2AoTsvJtf-tthX6ij47DHR4fH44sU9OTR9n8weA520oxS5amq3l-Qoxx2TXeM4pGsZbsyEtbakLf6a4=w138-h92-k-no",
    href: "https://www.google.com/maps/place/Karpaz+Gate+Marina+Hotel/data=!4m11!3m10!1s0x14df6d991bbfd09f:0x561d121aa9d26347!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.5570689!4d34.232565!16s%2Fg%2F11pv5hhy33!19sChIJn9C_G5lt3xQRR2PSqRoSHVY?authuser=0&hl=en&rclk=1",
    latitude: "35.5570689",
    longitude: "34.232565",
  },
  {
    name: "Limak Cyprus Deluxe Hotel",
    category: "hotel",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipPaMT3OdJ_oZtUbI84pVYBy6y3JVPa4tPDzP-21=w184-h92-k-no",
    href: "https://www.google.com/maps/place/Limak+Cyprus+Deluxe+Hotel/data=!4m11!3m10!1s0x14dfa128d7ce9035:0x595875dc302298ef!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.36324!4d34.0735189!16s%2Fg%2F11b6_f37sr!19sChIJNZDO1yih3xQR75giMNx1WFk?authuser=0&hl=en&rclk=1",
    latitude: "35.36324",
    longitude: "34.0735189",
  },
  {
    name: "Mimoza Beach Hotel",
    category: "hotel",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipPaR8NI-2y3ttsRDnLmYt1gY3RRm-k7H2PMrRm9=w163-h92-k-no",
    href: "https://www.google.com/maps/place/Mimoza+Beach+Hotel/data=!4m11!3m10!1s0x14dfb7ee48af744f:0x482fc7adc98770f8!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.2048588!4d33.8994395!16s%2Fg%2F11h8zwym45!19sChIJT3SvSO633xQR-HCHya3HL0g?authuser=0&hl=en&rclk=1",
    latitude: "35.2048588",
    longitude: "33.8994395",
  },
  {
    name: "Salamis Bay Conti Hotel",
    category: "hotel",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipOZ003qcxJX8017SnkFUZ-0gwyNJnSU6NwEsYhO=w122-h92-k-no",
    href: "https://www.google.com/maps/place/Salamis+Bay+Conti+Hotel/data=!4m11!3m10!1s0x14dfb69704fb4acb:0x87cc7e1e86d6d3cf!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.2056958!4d33.8990436!16s%2Fg%2F1tgc1_gb!19sChIJy0r7BJe23xQRz9PWhh5-zIc?authuser=0&hl=en&rclk=1",
    latitude: "35.2056958",
    longitude: "33.8990436",
  },
  {
    name: "Exotic Hotel & SPA",
    category: "hotel",
    image_url:
      "https://lh3.googleusercontent.com/gps-proxy/ALd4DhGlOPKbN6ap0yCqEy3PkgxS__VURu85hEcicYcQisxFSttoWhWKNIZe16mhlSuAREDBfN5P82ZEr339JnPkVrbpY77D8qKOqkyr85N_zyHRx39rWLOkSsQg44wqMpPmfqyNSqT_WFjav0KS3RYYN7mUofirCiseyDtnbY2pCtsRPB2mpzuOubuw7w=w163-h92-k-no",
    href: "https://www.google.com/maps/place/Exotic+Hotel+%26+SPA/data=!4m11!3m10!1s0x14dfafc68898a05b:0x922bdca68fec0cd2!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.3070769!4d33.9444286!16s%2Fg%2F1wfz19xp!19sChIJW6CYiMav3xQR0gzsj6bcK5I?authuser=0&hl=en&rclk=1",
    latitude: "35.3070769",
    longitude: "33.9444286",
  },
  {
    name: "THE ARKIN ISKELE HOTEL",
    category: "hotel",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipNvyHmEngfM2zv6HeiELW2ctvA1MD2U1CGIthhN=w163-h92-k-no",
    href: "https://www.google.com/maps/place/THE+ARKIN+ISKELE+HOTEL/data=!4m11!3m10!1s0x14dfb15a4e664111:0x61e37010747d455d!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.2671608!4d33.9148261!16s%2Fg%2F11s3b5ltpm!19sChIJEUFmTlqx3xQRXUV9dBBw42E?authuser=0&hl=en&rclk=1",
    latitude: "35.2671608",
    longitude: "33.9148261",
  },
  {
    name: "Celebi Garden Hotel",
    category: "hotel",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipMT1pCH3WpZ16Y3na3L6nLUvfNSW4X1FZv5N1fu=w163-h92-k-no",
    href: "https://www.google.com/maps/place/Celebi+Garden+Hotel/data=!4m11!3m10!1s0x14df0a024b23bbdd:0xd2d05cec8629544a!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.4144804!4d34.0670547!16s%2Fg%2F11g8bwqqk4!19sChIJ3bsjSwIK3xQRSlQphuxc0NI?authuser=0&hl=en&rclk=1",
    latitude: "35.4144804",
    longitude: "34.0670547",
  },
  {
    name: "Kaya Artemis Resort & Casino",
    category: "hotel",
    image_url:
      "https://lh3.googleusercontent.com/gps-proxy/ALd4DhFykwyBDazJS7sEE8Mgm8qXtIdlS-HbBqaxJOxOXla_iYDVB9u2VlNx0sLhIyAvg55rjmd3sGJpLRg810meC9XFnL1VJQkhfNUiuY0uY47nvqc624hggYaFCuSpjcml-ANWUxtjJyoiDVVvhqsyKApfdJbqUdqaYmW-sj4DxouLsrGstnpOQ1IJ=w138-h92-k-no",
    href: "https://www.google.com/maps/place/Kaya+Artemis+Resort+%26+Casino/data=!4m11!3m10!1s0x14dfa127e859854b:0xa3ac8afbbcf98b3e!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.3653614!4d34.0744903!16s%2Fg%2F1tdrhltr!19sChIJS4VZ6Ceh3xQRPov5vPuKrKM?authuser=0&hl=en&rclk=1",
    latitude: "35.3653614",
    longitude: "34.0744903",
  },
  {
    name: "Grand Sapphire Resort Hotel",
    category: "hotel",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipMKrtx3aVtbzRWILsGPh_jPT5jTF2FkYQhtmNtH=w163-h92-k-no",
    href: "https://www.google.com/maps/place/Grand+Sapphire+Resort+Hotel/data=!4m11!3m10!1s0x14dfb12a9566c461:0x8db45b17228cc406!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.2507078!4d33.8974287!16s%2Fg%2F11n6xxx3fn!19sChIJYcRmlSqx3xQRBsSMIhdbtI0?authuser=0&hl=en&rclk=1",
    latitude: "35.2507078",
    longitude: "33.8974287",
  },
  {
    name: "M\u0130RAY GUEST HOUSE BOUTIGUE HOTEL",
    category: "hotel",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipMaXSCjOfP61eukK9--GxDKh48RQKJw8RSeKCWo=w147-h92-k-no",
    href: "https://www.google.com/maps/place/M%C4%B0RAY+GUEST+HOUSE+BOUTIGUE+HOTEL/data=!4m11!3m10!1s0x14dfb1f8903609bb:0x8677be7e45992558!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.2518444!4d33.9000296!16s%2Fg%2F11h7g3xv_6!19sChIJuwk2kPix3xQRWCWZRX6-d4Y?authuser=0&hl=en&rclk=1",
    latitude: "35.2518444",
    longitude: "33.9000296",
  },
  {
    name: "theresahotel at Karpaz penincula",
    category: "hotel",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipOELGxZktX3slRIhl8VM1tChXLG5DGju3yFtmuh=w122-h92-k-no",
    href: "https://www.google.com/maps/place/theresahotel+at+Karpaz+penincula/data=!4m11!3m10!1s0x14df71fc790f5b33:0x4dffbef3f94905af!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.5696712!4d34.2612867!16s%2Fg%2F1tcw0nbq!19sChIJM1sPefxx3xQRrwVJ-fO-_00?authuser=0&hl=en&rclk=1",
    latitude: "35.5696712",
    longitude: "34.2612867",
  },
  {
    name: "Concorde Luxury Resort & Casino & Convention &\n                      Spa",
    category: "hotel",
    image_url:
      "https://lh3.googleusercontent.com/gps-proxy/ALd4DhEgijH_bL1KQvmnc90sYmGBoR2T7DiJg-46G1oTFDXUdSddG_6LN17l2-7MSByUoNhGeLBxU2bG9Ow8HDLVCzJaowydVD2pTlKbIn7W0OFS3VWpONTnTPeEguif61iuyWzARt3DjORVIkXQep1LTg_lSk8_kzelReLN29zgZ6IdzVy85X_N1NhG=w138-h92-k-no",
    href: "https://www.google.com/maps/place/Concorde+Luxury+Resort+%26+Casino+%26+Convention+%26+Spa/data=!4m11!3m10!1s0x14dfa1cb42ee2a2d:0x9dc2450873ca86ee!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.3546361!4d34.0731187!16s%2Fg%2F1tjcrq19!19sChIJLSruQsuh3xQR7obKcwhFwp0?authuser=0&hl=en&rclk=1",
    latitude: "35.3546361",
    longitude: "34.0731187",
  },
  {
    name: "Noah's Ark Deluxe Hotel & Spa/Nuh\u2019un Gemisi Hotel",
    category: "hotel",
    image_url:
      "https://lh3.googleusercontent.com/gps-proxy/ALd4DhE0LBcLXNarYT9B-eNHiEAsm3j5KQ_4Gzwf9cAhIw6i6uszqo7qgN9GVnSI7NFEETZ_wPiy8oN8oWkVq41PNPhLQMRhJMXJ_6nmSxUNOnuVPNRfkhggE1HuFiG4sRLB4IhMYcm-0cen8pjmwAnHMOO-VMBU_hVSU1Qts80mOvSMl3VxQ3ITJmz6=w154-h92-k-no",
    href: "https://www.google.com/maps/place/Noah%27s+Ark+Deluxe+Hotel+%26+Spa%2FNuh%E2%80%99un+Gemisi+Hotel/data=!4m11!3m10!1s0x14dfa0eafefede95:0x12c99864c2678cfa!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.379584!4d34.089011!16s%2Fg%2F1262dhkv8!19sChIJld7-_uqg3xQR-oxnwmSYyRI?authuser=0&hl=en&rclk=1",
    latitude: "35.379584",
    longitude: "34.089011",
  },
  {
    name: "CONCORDE LUXURY RESORT & Beach Club & Casino",
    category: "hotel",
    image_url:
      "https://lh3.googleusercontent.com/gps-proxy/ALd4DhHvfI9SkI69SIvlqQIQ7Hldy_q1a7YKEVB6I823nlEHSz64Z6luDNfxXTDMPkeP5MY8S8Ksf9iyOVLmFPO2Qyc6fwrffrXuVzPp8qoVs5KzWLE_QFcs2bh0l-uKLLC9CNWPHSh4_thXPHQbwWkKp3NFaNgXAzSjYlLZYTc9OfKuPXSHtZU3t0Hk=w80-h106-k-no",
    href: "https://www.google.com/maps/place/CONCORDE+LUXURY+RESORT+%26+Beach+Club+%26+Casino/data=!4m11!3m10!1s0x14dfa1307d0b7db9:0x62de3d80aacb25b9!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.3549431!4d34.074735!16s%2Fg%2F11rtcrb2xf!19sChIJuX0LfTCh3xQRuSXLqoA93mI?authuser=0&hl=en&rclk=1",
    latitude: "35.3549431",
    longitude: "34.074735",
  },
  {
    name: "Merit Cyprus Gardens Hotel, Casino & Spa",
    category: "hotel",
    image_url:
      "https://lh3.googleusercontent.com/gps-proxy/ALd4DhE4DOhwUvhX3XutswN3ExoEzq9xVv7ZZPJdIDRWGwzKR-VdpP9eF-ODPi_bXi5atlq4t51LQBBuJV6KjwCVFBdZ8ctHcyc1keOieYLjKKhPu7SBZGaMU9ZzCIOzGbVdu1EQSgmw29CFGNKsNqNQoy6ZgHjO_49mEUHrn-wdOlBcmE2E9g6Oyan7Mw=w154-h92-k-no",
    href: "https://www.google.com/maps/place/Merit+Cyprus+Gardens+Hotel,+Casino+%26+Spa/data=!4m11!3m10!1s0x14dfb1ca4589a9a7:0x7352d3ea904f007e!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.2798116!4d33.9266334!16s%2Fg%2F11rr4xs6zs!19sChIJp6mJRcqx3xQRfgBPkOrTUnM?authuser=0&hl=en&rclk=1",
    latitude: "35.2798116",
    longitude: "33.9266334",
  },
  {
    name: "Salamis Park Hotel & Casino",
    category: "hotel",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipPvptxErhkN9iGj3zXfXobYvpE785jq2Y7aMxU9=w122-h92-k-no",
    href: "https://www.google.com/maps/place/Salamis+Park+Hotel+%26+Casino/data=!4m11!3m10!1s0x14dfb69710f1675d:0xf70680620066d173!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.2058125!4d33.8989375!16s%2Fg%2F11sg472s8d!19sChIJXWfxEJe23xQRc9FmAGKABvc?authuser=0&hl=en&rclk=1",
    latitude: "35.2058125",
    longitude: "33.8989375",
  },
  {
    name: "Yelden Crystal Rock Resort",
    category: "hotel",
    image_url:
      "https://lh3.googleusercontent.com/gps-proxy/ALd4DhHaEocbPr6NRIVN3l9UoKiXWUeJmmbSFLoEpR5IvWgjtVd1pTH7E9tvRR3kpOF6sA-S5qf4FOPEx4kNyLL59CV6BtvPqRtfg_CrJIXyQeoPa_jw5fWg-DcoHV7c_Bb6ckaCqUYNEAtfwlnRZH1svZueYjwKO0EaQ1_tUPg1zaM0Lm3Ux3dilN5W=w136-h92-k-no",
    href: "https://www.google.com/maps/place/Yelden+Crystal+Rock+Resort/data=!4m11!3m10!1s0x14dfb6bcf2fa1743:0x9af4f016b1d3fac4!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.212458!4d33.89916!16s%2Fg%2F11b7q1k8lv!19sChIJQxf68ry23xQRxPrTsRbw9Jo?authuser=0&hl=en&rclk=1",
    latitude: "35.212458",
    longitude: "33.89916",
  },
  {
    name: "The Pine View Hotel Restaurant & Bungalows",
    category: "hotel",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipOG0haer9fJobsEIQOcLumZ4_8ibF-o6MJEWp2M=w92-h92-k-no",
    href: "https://www.google.com/maps/place/The+Pine+View+Hotel+Restaurant+%26+Bungalows/data=!4m11!3m10!1s0x14dfa7a56e322551:0x69cfca55c241e85!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.4060864!4d33.9877364!16s%2Fg%2F11h55zk16y!19sChIJUSUybqWn3xQRhR4kXKX8nAY?authuser=0&hl=en&rclk=1",
    latitude: "35.4060864",
    longitude: "33.9877364",
  },
  {
    name: "Club Di Mare",
    category: "hotel",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipMdVrDS7Evqnp83u1434V1Xs06GmYogcAAJ6iQm=w138-h92-k-no",
    href: "https://www.google.com/maps/place/Club+Di+Mare/data=!4m11!3m10!1s0x14df6d3ed0407423:0x20bf68be61572673!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.5551564!4d34.2160773!16s%2Fg%2F11n950jpc5!19sChIJI3RA0D5t3xQRcyZXYb5ovyA?authuser=0&hl=en&rclk=1",
    latitude: "35.5551564",
    longitude: "34.2160773",
  },
  {
    name: "Oscar Park Hotel",
    category: "hotel",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipNIJzl1XYEH1ShY1SyxEzVRXlpyNZfVp4bCYac6=w185-h92-k-no",
    href: "https://www.google.com/maps/place/Oscar+Park+Hotel/data=!4m11!3m10!1s0x14dfb67cf0775395:0x1361cfd64fd6a289!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.1878763!4d33.8947229!16s%2Fg%2F11c6qs18vd!19sChIJlVN38Hy23xQRiaLWT9bPYRM?authuser=0&hl=en&rclk=1",
    latitude: "35.1878763",
    longitude: "33.8947229",
  },
  {
    name: "Edelweiss Holiday Residence",
    category: "hotel",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipOtv57PkvzmkXmdOHchTZh2rKM60kv7u9e7qhBN=w122-h92-k-no",
    href: "https://www.google.com/maps/place/Edelweiss+Holiday+Residence/data=!4m11!3m10!1s0x14dfb1f08eeec921:0x1f6e5aef596e7b60!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.2725448!4d33.8953361!16s%2Fg%2F11h0cgxl8z!19sChIJIcnujvCx3xQRYHtuWe9abh8?authuser=0&hl=en&rclk=1",
    latitude: "35.2725448",
    longitude: "33.8953361",
  },
  {
    name: "Skali Tatil K\u00f6y\u00fc",
    category: "hotel",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipMRoX1wBL9BRzCZR6d7UVzdMdMewVjXhSLiRzjc=w122-h92-k-no",
    href: "https://www.google.com/maps/place/Skali+Tatil+K%C3%B6y%C3%BC/data=!4m11!3m10!1s0x14dfa9780a9b46f5:0x3889714d8f3dfc79!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.423968!4d33.8956654!16s%2Fg%2F11c0t9g187!19sChIJ9UabCnip3xQRefw9j01xiTg?authuser=0&hl=en&rclk=1",
    latitude: "35.423968",
    longitude: "33.8956654",
  },
  {
    name: "Osman A\u011fa Hotel",
    category: "hotel",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipOswCnZeC9ccweL3RqHAZxdjQhcIx_Mo1lMmDLa=w145-h92-k-no",
    href: "https://www.google.com/maps/place/Osman+A%C4%9Fa+Hotel/data=!4m11!3m10!1s0x14dfb132be606a11:0xb98e29af3cc2532c!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.2591604!4d33.9074625!16s%2Fg%2F11t28d6hqy!19sChIJEWpgvjKx3xQRLFPCPK8pjrk?authuser=0&hl=en&rclk=1",
    latitude: "35.2591604",
    longitude: "33.9074625",
  },
  {
    name: "Kaplica on a Beach",
    category: "hotel",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipNIOGEDGYaU-mf8cJmLQXHQe8i61uCRp1MdRHOz=w122-h92-k-no",
    href: "https://www.google.com/maps/place/Kaplica+on+a+Beach/data=!4m11!3m10!1s0x14dfa99d026e645d:0xf68f62a1f82f4e73!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.4252449!4d33.8992754!16s%2Fg%2F1ts6d9z5!19sChIJXWRuAp2p3xQRc04v-KFij_Y?authuser=0&hl=en&rclk=1",
    latitude: "35.4252449",
    longitude: "33.8992754",
  },
  {
    name: "Malibu Beach Hotel",
    category: "hotel",
    image_url:
      "https://lh3.googleusercontent.com/gps-proxy/ALd4DhE_MA9jPVWURDoqH0x4nh6XS2rKz5zVul9HPra_NB0zXvOa7BnTYKKozOTJoRbUZV9y1Jr9nuNS3ecp8VykROtoh7ofO4wD0Y8C5Qj0-l3wJmIKFogioVypw29QtJ_0yh5DlfLuYEUPiHzRQfddJWIS4GaNGI2FvQWMQwfL8-W5FBAZFq9V78c=w122-h92-k-no",
    href: "https://www.google.com/maps/place/Malibu+Beach+Hotel/data=!4m11!3m10!1s0x14df6c4b3d4243c3:0x603c83d61bf6e89c!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.5553339!4d34.2163718!16s%2Fg%2F1tdj7zvg!19sChIJw0NCPUts3xQRnOj2G9aDPGA?authuser=0&hl=en&rclk=1",
    latitude: "35.5553339",
    longitude: "34.2163718",
  },
  {
    name: "Bo\u011faz Beach Clup",
    category: "hotel",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipPN8TFWqjwCu8rKnpa3LpR2332k4Y2gxL0EHwt5=w122-h92-k-no",
    href: "https://www.google.com/maps/place/Bo%C4%9Faz+Beach+Clup/data=!4m11!3m10!1s0x14dfafbe10972e39:0x9e4fb693f7cfd43a!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.3130031!4d33.9519518!16s%2Fg%2F1td6jpz4!19sChIJOS6XEL6v3xQROtTP95O2T54?authuser=0&hl=en&rclk=1",
    latitude: "35.3130031",
    longitude: "33.9519518",
  },
  {
    name: "Balc\u0131 Plaza Hotel",
    category: "hotel",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipPj94GwDIAGVivuCKg55sH4R4fSc5o3Q-hqPYAv=w122-h92-k-no",
    href: "https://www.google.com/maps/place/Balc%C4%B1+Plaza+Hotel/data=!4m11!3m10!1s0x14df6fc581b0ab19:0x2c0203f3f3c7d063!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.5727783!4d34.272417!16s%2Fg%2F11rzh167dr!19sChIJGauwgcVv3xQRY9DH8_MDAiw?authuser=0&hl=en&rclk=1",
    latitude: "35.5727783",
    longitude: "34.272417",
  },
  {
    name: "Sea life hotel",
    category: "hotel",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipNIb0bOv8iE1AJPj9RYjaR4iXqsl7wBvwoPkyh8=w142-h92-k-no",
    href: "https://www.google.com/maps/place/Sea+life+hotel/data=!4m11!3m10!1s0x14dfb17355e6f17d:0x8fbc9c99f7e280ed!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.2596813!4d33.9077717!16s%2Fg%2F11f3n4xt6k!19sChIJffHmVXOx3xQR7YDi95mcvI8?authuser=0&hl=en&rclk=1",
    latitude: "35.2596813",
    longitude: "33.9077717",
  },
  {
    name: "NOYANLAR HOLIDAY HOMES",
    category: "hotel",
    image_url:
      "https://lh3.googleusercontent.com/gps-proxy/ALd4DhFkiSByANldyAVYlRYmOVdCezTHmwc2dPOUyu3ICAwVmvb7d-8-uw_8W5Y9xby3Q8yIImD1cOqnEcHR3Lz5XWIlMtG0sqIpUoSyG-uZGIVFcvm-1Hlq2LxDBFp7mm6ZT7wSUUbwWEXuaOdkra-wZpV0T7puTdV9_wnElpsTNNGfCDfGMdTIECw=w138-h92-k-no",
    href: "https://www.google.com/maps/place/NOYANLAR+HOLIDAY+HOMES/data=!4m11!3m10!1s0x14dfb131fd320a93:0xffd515445052634!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.255566!4d33.9025948!16s%2Fg%2F11j006sdfs!19sChIJkwoy_TGx3xQRNCYFRVRR_Q8?authuser=0&hl=en&rclk=1",
    latitude: "35.255566",
    longitude: "33.9025948",
  },
  {
    name: "Pine Bay Cyprus Resort",
    category: "hotel",
    image_url: "//maps.gstatic.com/tactile/pane/result-no-thumbnail-2x.png",
    href: "https://www.google.com/maps/place/Pine+Bay+Cyprus+Resort/data=!4m11!3m10!1s0x14dfa0d9709172e1:0xe5e9519fe4bf57c!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.3699758!4d34.0785277!16s%2Fg%2F1vc8lpq8!19sChIJ4XKRcNmg3xQRfPVL_hmVXg4?authuser=0&hl=en&rclk=1",
    latitude: "35.3699758",
    longitude: "34.0785277",
  },
  {
    name: "Melandra House",
    category: "hotel",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipNIdYPhKrBBmoqlx-lyxVoiT3k1tp4GSN-aOeeG=w138-h92-k-no",
    href: "https://www.google.com/maps/place/Melandra+House/data=!4m11!3m10!1s0x14dfb6ae5641186d:0x86cb0ece0789a146!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.2230911!4d33.8938865!16s%2Fg%2F12hk9m_k7!19sChIJbRhBVq623xQRRqGJB84Oy4Y?authuser=0&hl=en&rclk=1",
    latitude: "35.2230911",
    longitude: "33.8938865",
  },
  {
    name: "Babutsa Rooms",
    category: "hotel",
    image_url:
      "https://lh3.googleusercontent.com/gps-proxy/ALd4DhFUgBkmTZOAOCDQU2TZEsTx_a2kKjLjikZ9cWfTOljJmMlYxi6zKbB_a6g2E2LbZ3-0_3QQS-trMOX7XF1GSy-xhRIjwA9xI01k-Q8TXaVG3rsXZmRwB-ywM_poXlhEDiu8n3K6AMo4NvFt1Dr8sA_Uf58Ow_HQ_utUkxhAdZLa6bH6hNaWgtOkcQ=w122-h92-k-no",
    href: "https://www.google.com/maps/place/Babutsa+Rooms/data=!4m11!3m10!1s0x14dfb690d480b73d:0x21673227b92a0278!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.2037811!4d33.899311!16s%2Fg%2F11f4wt9875!19sChIJPbeA1JC23xQReAIquScyZyE?authuser=0&hl=en&rclk=1",
    latitude: "35.2037811",
    longitude: "33.899311",
  },
  {
    name: "Villa Kantara Hotel",
    category: "hotel",
    image_url:
      "https://lh3.googleusercontent.com/gps-proxy/ALd4DhHPua-iroS3FutmNsqEsQSkujNKgYv1SxR6EyZghTHgly3xFgxZeYYcDqsxGrdsQ4oA3_1nrT36mhT9bVPO6wIuSb_tyuHZ2GazcaD7UmO3WkZfdyxyM7fQe6qnf1MyO04jdFLp8m2tAQe8nG5HmJ3DHo2zQeHv2F1nodnECRnzRDJCYXAvW-9y=w138-h92-k-no",
    href: "https://www.google.com/maps/place/Villa+Kantara+Hotel/data=!4m11!3m10!1s0x14dfa94d1f0166eb:0xc384fbb23c1fcb5e!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.3852652!4d33.8995478!16s%2Fg%2F1pp2x7lx0!19sChIJ62YBH02p3xQRXssfPLL7hMM?authuser=0&hl=en&rclk=1",
    latitude: "35.3852652",
    longitude: "33.8995478",
  },
  {
    name: "The Nitovikla Garden Hotel",
    category: "hotel",
    image_url:
      "https://lh3.googleusercontent.com/gps-proxy/ALd4DhE0UQd-rKBfqMVonjUMZNxTPQ50eQAE5p46b9__FNcEuI3w2zTdV117FCjuICge0G1MvB43VSMwpphig_rnKulsB1ZtOs77RzxskKHtMEMaC8rxLxIE7gF7SLqwc1a3RC3_Yph-2jgM1WkB13xuVmj9fgzy8NmV3pXcrGfZtIhWwTymw-zRIbI=w122-h92-k-no",
    href: "https://www.google.com/maps/place/The+Nitovikla+Garden+Hotel/data=!4m11!3m10!1s0x14df0b1fc3673c7b:0x187c52d7c43ca2c5!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.4278666!4d34.1292268!16s%2Fg%2F1tfdtzvb!19sChIJezxnwx8L3xQRxaI8xNdSfBg?authuser=0&hl=en&rclk=1",
    latitude: "35.4278666",
    longitude: "34.1292268",
  },
  {
    name: "Helena ceaser blue",
    category: "hotel",
    image_url:
      "https://lh3.googleusercontent.com/gps-proxy/ALd4DhEt5RunJYFrbumrIUa0yUoiJkpMA6vmkViqCoykKNMjhUsW9Ji9SWumEZY6M10GC25zy2_tXRlubUcdRIVAKWICQxK6Q8CVPibEru8OA2zcJHRd_To1S0rNhvx7jslSrM5nrsKuIOKHzIKJkEQ2cSxT-13hj95_oBx854EZcek3u7olUdbf5teUsA=w149-h92-k-no",
    href: "https://www.google.com/maps/place/Helena+ceaser+blue/data=!4m11!3m10!1s0x14dfa5fabd9439d5:0xc8fa08d361c02d7!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.3280858!4d33.976355!16s%2Fg%2F11s9pcxy0s!19sChIJ1TmUvfql3xQR1wIcNo2gjww?authuser=0&hl=en&rclk=1",
    latitude: "35.3280858",
    longitude: "33.976355",
  },
  {
    name: "Cyprus Gardens Seafront Boutique & Beach & Casino",
    category: "hotel",
    image_url: "//maps.gstatic.com/tactile/pane/result-no-thumbnail-2x.png",
    href: "https://www.google.com/maps/place/Cyprus+Gardens+Seafront+Boutique+%26+Beach+%26+Casino/data=!4m11!3m10!1s0x14dfb174aa07f585:0x318ea3b951586128!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.2597418!4d33.9077799!16s%2Fg%2F11mnbwc5zv!19sChIJhfUHqnSx3xQRKGFYUbmjjjE?authuser=0&hl=en&rclk=1",
    latitude: "35.2597418",
    longitude: "33.9077799",
  },
  {
    name: "F&S Paradise Resort Hotel",
    category: "hotel",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipNpTnV-wzrRpcAYhOppLpGdUSD7mvbugmQcRl5F=w80-h169-k-no",
    href: "https://www.google.com/maps/place/F%26S+Paradise+Resort+Hotel/data=!4m11!3m10!1s0x14dfb69b2e0251a3:0xcd9b5bba0941b844!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.2013359!4d33.8939399!16s%2Fg%2F1tf45h48!19sChIJo1ECLpu23xQRRLhBCbpbm80?authuser=0&hl=en&rclk=1",
    latitude: "35.2013359",
    longitude: "33.8939399",
  },
  {
    name: "Long Beach Club Resort",
    category: "hotel",
    image_url:
      "https://lh3.googleusercontent.com/gps-proxy/ALd4DhF6NH8UaW4xHG36shmaWqNY4HNIrgg9DhbYpGyzskiuQo2JB9ZWdSoEwirf0mi8WXjheD4ydQe28DfePCntOfsPMgISVzaVHyXLKYi6WP-Ro-_tzw-_g_t5qipwzomv-8bjGwQeyPjahy1JDRM3Obold246i_PCimVL_tjubZ8fGHfa_2Smye7e6Q=w138-h92-k-no",
    href: "https://www.google.com/maps/place/Long+Beach+Club+Resort/data=!4m11!3m10!1s0x14dfb141f982e681:0x6f0b9e5f3d06aaf1!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.2468185!4d33.9032516!16s%2Fg%2F1tlx8lv7!19sChIJgeaC-UGx3xQR8aoGPV-eC28?authuser=0&hl=en&rclk=1",
    latitude: "35.2468185",
    longitude: "33.9032516",
  },
  {
    name: "Long Beach Villas",
    category: "hotel",
    image_url: "//maps.gstatic.com/tactile/pane/result-no-thumbnail-2x.png",
    href: "https://www.google.com/maps/place/Long+Beach+Villas/data=!4m11!3m10!1s0x14dfb16f4f010605:0x5f554059ba417911!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.253633!4d33.897818!16s%2Fg%2F11v15lz6tt!19sChIJBQYBT2-x3xQREXlBullAVV8?authuser=0&hl=en&rclk=1",
    latitude: "35.253633",
    longitude: "33.897818",
  },
  {
    name: "Royal sun residence",
    category: "hotel",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipO1axdZlqRrUvsEMgQiCnNH1TY02nulK7eZNFVl=w122-h92-k-no",
    href: "https://www.google.com/maps/place/Royal+sun+residence/data=!4m11!3m10!1s0x14dfb18b668ae927:0x7d73d70d8b1f5cb1!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.2529157!4d33.8990619!16s%2Fg%2F11h110p_85!19sChIJJ-mKZoux3xQRsVwfiw3Xc30?authuser=0&hl=en&rclk=1",
    latitude: "35.2529157",
    longitude: "33.8990619",
  },
  {
    name: "Salamina Houses",
    category: "hotel",
    image_url:
      "https://lh3.googleusercontent.com/gps-proxy/ALd4DhFw-860j3CItoLPHZe-OjEgXaiUFJmBFVobG6t3b8l7k8j4_l_nPYd0t-VgRRzAhnfP98h8c3gc_HHf7yKTkKFOMRgxWLxveA_uPVwYz9b4RHTfuFNaKvkmIFCWnlLMcydaMCrBQgTxnxPzgyna-5RJajmSBsubg0Nd031jYs_00dRS2GSh4jMvcg=w80-h106-k-no",
    href: "https://www.google.com/maps/place/Salamina+Houses/data=!4m11!3m10!1s0x14dfb13cec67f761:0xca140aeb2fa65935!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.2438731!4d33.9003016!16s%2Fg%2F11h92dtpxv!19sChIJYfdn7Dyx3xQRNVmmL-sKFMo?authuser=0&hl=en&rclk=1",
    latitude: "35.2438731",
    longitude: "33.9003016",
  },
  {
    name: "Kaplica on a Sandy Beach",
    category: "hotel",
    image_url:
      "https://lh3.googleusercontent.com/gps-proxy/ALd4DhHnyWVdfW15XfA7liYV_U0vNWPkOxBnRw8E0iqc2k-8NcaU--uBZI8uU23nik-kkjLrYVDzrjT64B_tSgq3OQ_7KemQHcTV2vM5OQy1_UYtMzn_65ynNq9TKN-99pEira0mUTFLOmnlOa6WFOcLaKQ52-slHHc0x5jHcpioCLnv-tusH2QVRm2u=w80-h106-k-no",
    href: "https://www.google.com/maps/place/Kaplica+on+a+Sandy+Beach/data=!4m11!3m10!1s0x14dfb189c12ecdad:0x397a88cb47868a8d!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.2842976!4d33.8869726!16s%2Fg%2F11fkm89k_5!19sChIJrc0uwYmx3xQRjYqGR8uIejk?authuser=0&hl=en&rclk=1",
    latitude: "35.2842976",
    longitude: "33.8869726",
  },
  {
    name: "Asut Guest House",
    category: "hotel",
    image_url:
      "https://lh3.googleusercontent.com/gps-proxy/ALd4DhGm-I22Pyr_Vo1cl0eprCyY_bhTjsA99pGuV3Y51w-6ETlbZPrEVnRsYVtnibKO3soo--knqHKlW7iIdoFO7srbzG80_vgCnzrW3IgYAb9pLhC_AUuDAP10VITZ13vbXA-hyX5yamMDvQxikHTHjrOrNe-LR1Zs2NpkgCCoJudqoardixqqPn4drA=w138-h92-k-no",
    href: "https://www.google.com/maps/place/Asut+Guest+House/data=!4m11!3m10!1s0x14dfa795bd670767:0x6b2693c6a2a38eee!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.4112022!4d34.000874!16s%2Fg%2F11g8bwtpb1!19sChIJZwdnvZWn3xQR7o6josaTJms?authuser=0&hl=en&rclk=1",
    latitude: "35.4112022",
    longitude: "34.000874",
  },
  {
    name: "La Medusa Gardens",
    category: "hotel",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipOnpYrxkh6UWgzQ2Ytf2SDzTw2zOEtcxNGJDxn9=w204-h92-k-no",
    href: "https://www.google.com/maps/place/La+Medusa+Gardens/data=!4m11!3m10!1s0x14df6fd1f49fe955:0x6dd0d9d1f273f066!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.5125523!4d34.2749787!16s%2Fg%2F11s4ycn3gp!19sChIJVemf9NFv3xQRZvBz8tHZ0G0?authuser=0&hl=en&rclk=1",
    latitude: "35.5125523",
    longitude: "34.2749787",
  },
  {
    name: "Crystal Rocks",
    category: "hotel",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipPw-WLkmvsE6dXG_lyoK2bJc7NzVNqHQFDEHQk=w122-h92-k-no",
    href: "https://www.google.com/maps/place/Crystal+Rocks/data=!4m11!3m10!1s0x14dfb69afe194235:0xe5b7ccef73f7d4e4!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.20297!4d33.89417!16s%2Fg%2F11qpmvnbnc!19sChIJNUIZ_pq23xQR5NT3c-_Mt-U?authuser=0&hl=en&rclk=1",
    latitude: "35.20297",
    longitude: "33.89417",
  },
  {
    name: "Deluxe Studios Caesar Resort & Spa",
    category: "hotel",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipOZ9fivH0-NwpYeYyEK_nEZnxxGKyNLH2NId8r-=w80-h92-k-no-pi-0-ya44.917805-ro-0-fo100",
    href: "https://www.google.com/maps/place/Deluxe+Studios+Caesar+Resort+%26+Spa/data=!4m11!3m10!1s0x14dfb16850f7f00d:0xec8ac240d4f5c768!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.261879!4d33.899442!16s%2Fg%2F11fngyf65l!19sChIJDfD3UGix3xQRaMf11EDCiuw?authuser=0&hl=en&rclk=1",
    latitude: "35.261879",
    longitude: "33.899442",
  },
  {
    name: "Venus Otel",
    category: "hotel",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipNUzFEV2buKKI-tjOqYS13EXmf_FmFR20Mr1lxj=w122-h92-k-no",
    href: "https://www.google.com/maps/place/Venus+Otel/data=!4m11!3m10!1s0x14dfb6893dd54e47:0xf7a9c894746ef2cd!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.1927795!4d33.9009361!16s%2Fg%2F1thjqt_9!19sChIJR07VPYm23xQRzfJudJTIqfc?authuser=0&hl=en&rclk=1",
    latitude: "35.1927795",
    longitude: "33.9009361",
  },
  {
    name: "CAEZAR Beach Apartments",
    category: "hotel",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipMCszGazBZqiEA82thV5pZP5ub31v8wtlvmlBU4=w122-h92-k-no",
    href: "https://www.google.com/maps/place/CAEZAR+Beach+Apartments/data=!4m11!3m10!1s0x14dfafed2ca5018b:0x9985cfb5fd1ef9!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.316774!4d33.9540969!16s%2Fg%2F11hzgm99qk!19sChIJiwGlLO2v3xQR-R79tc-FmQA?authuser=0&hl=en&rclk=1",
    latitude: "35.316774",
    longitude: "33.9540969",
  },
  {
    name: "Empresse Otel",
    category: "hotel",
    image_url: "//maps.gstatic.com/tactile/pane/result-no-thumbnail-2x.png",
    href: "https://www.google.com/maps/place/Empresse+Otel/data=!4m11!3m10!1s0x14dfb67d6ff9af29:0x593d9743015383e2!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.190196!4d33.8949003!16s%2Fg%2F11bycjgl_c!19sChIJKa_5b3223xQR4oNTAUOXPVk?authuser=0&hl=en&rclk=1",
    latitude: "35.190196",
    longitude: "33.8949003",
  },
  {
    name: "Majestic Beach Club Hotel",
    category: "hotel",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipOHHZDmZn-U-5P4KrDBPJFjU3AbmX7fL4RNVF3J=w122-h92-k-no",
    href: "https://www.google.com/maps/place/Majestic+Beach+Club+Hotel/data=!4m11!3m10!1s0x14dfaf99e8c3b68d:0x7af1414e5c99ad0c!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.318074!4d33.956843!16s%2Fg%2F1w8g3ff6!19sChIJjbbD6Jmv3xQRDK2ZXE5B8Xo?authuser=0&hl=en&rclk=1",
    latitude: "35.318074",
    longitude: "33.956843",
  },
  {
    name: "Rozagi Guest House",
    category: "hotel",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipPOgS-TEEpyEgzzOoRdbBczQ05ekHr1T_tFsso9=w122-h92-k-no",
    href: "https://www.google.com/maps/place/Rozagi+Guest+House/data=!4m11!3m10!1s0x14df0a19d1b64ab1:0xc4172b97b38eceac!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.4223787!4d34.074675!16s%2Fg%2F11dxd9zdf6!19sChIJsUq20RkK3xQRrM6Os5crF8Q?authuser=0&hl=en&rclk=1",
    latitude: "35.4223787",
    longitude: "34.074675",
  },
  {
    name: "Royal Life Poseidon",
    category: "hotel",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipP7l8MNX8VCQO9EJgT3HFNBRJKlQ0jGlr93MmFX=w80-h106-k-no",
    href: "https://www.google.com/maps/place/Royal+Life+Poseidon/data=!4m11!3m10!1s0x14dfb1dfd8bf8741:0xbdc84828a2b4b19d!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.2536576!4d33.9003713!16s%2Fg%2F11j8ztgk11!19sChIJQYe_2N-x3xQRnbG0oihIyL0?authuser=0&hl=en&rclk=1",
    latitude: "35.2536576",
    longitude: "33.9003713",
  },
  {
    name: "Emparess",
    category: "hotel",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipMvi_8pnrvEcPEpDxfQb1gQIzqVKw8E9YCbtaox=w80-h177-k-no",
    href: "https://www.google.com/maps/place/Emparess/data=!4m11!3m10!1s0x14dfb70d80e78ab5:0xb055c2e679d1e3e!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.1968015!4d33.8913539!16s%2Fg%2F11t64j6qdn!19sChIJtYrngA233xQRPh6dZy5cBQs?authuser=0&hl=en&rclk=1",
    latitude: "35.1968015",
    longitude: "33.8913539",
  },
  {
    name: "Galifes Guest House",
    category: "hotel",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipOlKFU-6zg1k56pA-rwCb5krcDsnK0SrzphIpia=w204-h92-k-no",
    href: "https://www.google.com/maps/place/Galifes+Guest+House/data=!4m11!3m10!1s0x14dfa7be28ba3f8b:0xdde4b1d2dff7648b!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.4097499!4d34.0007179!16s%2Fg%2F11dzdfx8wz!19sChIJiz-6KL6n3xQRi2T339Kx5N0?authuser=0&hl=en&rclk=1",
    latitude: "35.4097499",
    longitude: "34.0007179",
  },
  {
    name: "Gate Twenty Two Boutique Hotel",
    category: "hotel",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipOV6qxo54k1uru39yEUvdiJWqlC45ddUA78GOaH=w138-h92-k-no",
    href: "https://www.google.com/maps/place/Gate+Twenty+Two+Boutique+Hotel/data=!4m11!3m10!1s0x14de17d2f3cb215f:0x833799297c1f743d!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.1696181!4d33.3635091!16s%2Fg%2F11tckjvm1z!19sChIJXyHL89IX3hQRPXQffCmZN4M?authuser=0&hl=en&rclk=1",
    latitude: "35.1696181",
    longitude: "33.3635091",
  },
  {
    name: "Royal Palace North Cyprus",
    category: "hotel",
    image_url:
      "https://lh3.googleusercontent.com/gps-proxy/ALd4DhHmZwOL7QWFw5nd3PGQLaK4V4KO2aScpuc0dhjWA0skNTNiLWHisTE9fxsI6ByUbAuvk17JeCC6f0gxJ-HTg4Fez9WornmLK05MnTMjSXvXNVaDZgNfZOvG_PS3ijUotlwclU_1gFJYCDt0Ltrs6bu-tc8FtyfrOpdygeUS8goZl71DZ4v_dc3L=w91-h92-k-no",
    href: "https://www.google.com/maps/place/Royal+Palace+North+Cyprus/data=!4m11!3m10!1s0x14de10f9ab1518e3:0xdbf48f0325132e9d!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.211235!4d33.306618!16s%2Fg%2F11ft03_4t6!19sChIJ4xgVq_kQ3hQRnS4TJQOP9Ns?authuser=0&hl=en&rclk=1",
    latitude: "35.211235",
    longitude: "33.306618",
  },
  {
    name: "Madama Residence",
    category: "hotel",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipO1VjPOjE0aK-gYmGau-hYDpel8BlyM2QIt3vl5=w92-h92-k-no",
    href: "https://www.google.com/maps/place/Madama+Residence/data=!4m11!3m10!1s0x14de17c881468247:0x579880e55cac819c!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.1718568!4d33.3621638!16s%2Fg%2F11syz4h4bt!19sChIJR4JGgcgX3hQRnIGsXOWAmFc?authuser=0&hl=en&rclk=1",
    latitude: "35.1718568",
    longitude: "33.3621638",
  },
  {
    name: "Kipros Accomodation",
    category: "hotel",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipOX78vKmlDnKkwok_MYrewigDbfhFgjI4FL7NG2=w122-h92-k-no",
    href: "https://www.google.com/maps/place/Kipros+Accomodation/data=!4m11!3m10!1s0x14de174559db7ab9:0x6b5e4caa404da544!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.1735375!4d33.3600752!16s%2Fg%2F11cn9f0_63!19sChIJuXrbWUUX3hQRRKVNQKpMXms?authuser=0&hl=en&rclk=1",
    latitude: "35.1735375",
    longitude: "33.3600752",
  },
  {
    name: "Castelli Hotel Nicosia",
    category: "hotel",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipMONRUj89epAmpeUHZ7vuSB1OSQN0HQljbW6n5E=w145-h92-k-no",
    href: "https://www.google.com/maps/place/Castelli+Hotel+Nicosia/data=!4m11!3m10!1s0x14de1750208d6c31:0x6880b053d6efe93b!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.1728978!4d33.3578949!16s%2Fg%2F1tttj1qy!19sChIJMWyNIFAX3hQRO-nv1lOwgGg?authuser=0&hl=en&rclk=1",
    latitude: "35.1728978",
    longitude: "33.3578949",
  },
  {
    name: "SKY ROOF HOTEL",
    category: "hotel",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipPOTfcjBuwKj07FHDt6Pl41xJr2jgttA-AhrE6f=w122-h92-k-no",
    href: "https://www.google.com/maps/place/SKY+ROOF+HOTEL/data=!4m11!3m10!1s0x14de17efa76600f5:0x347104453e6e9840!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.1996794!4d33.367146!16s%2Fg%2F11f5q91b3j!19sChIJ9QBmp-8X3hQRQJhuPkUEcTQ?authuser=0&hl=en&rclk=1",
    latitude: "35.1996794",
    longitude: "33.367146",
  },
  {
    name: "The Classic Hotel",
    category: "hotel",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipMHIIIKij2eTCn7sa6MbV3rZ-zkR3nz8Qr5EnDj=w121-h92-k-no",
    href: "https://www.google.com/maps/place/The+Classic+Hotel/data=!4m11!3m10!1s0x14de1767ca4826c5:0x709898fe0622e871!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.173005!4d33.357375!16s%2Fg%2F1tfx_k8r!19sChIJxSZIymcX3hQRcegiBv6YmHA?authuser=0&hl=en&rclk=1",
    latitude: "35.173005",
    longitude: "33.357375",
  },
  {
    name: "Merit Hotel",
    category: "hotel",
    image_url:
      "https://lh3.googleusercontent.com/gps-proxy/ALd4DhHjkb1s3jCxzpWK4UBuL9D0OJ_7qhYmr_MFfbKDpvovw4Spq_WFyz7yzJ58L4G_Cp-cB21XBn3KEU6zAarwEJHzyAXUojI_A7glE4vzcXbRTeUlEO22Zle0405EGoouOe1hdrjAjK2hXZKzEjz8jGNMmmCw6XOuctznW1DUqrN0JjCQ1GNpx7tWsA=w122-h92-k-no",
    href: "https://www.google.com/maps/place/Merit+Hotel/data=!4m11!3m10!1s0x14de17338e8f7a91:0x7c09dc1ede0df051!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.1905452!4d33.3520779!16s%2Fg%2F1tkxjc33!19sChIJkXqPjjMX3hQRUfAN3h7cCXw?authuser=0&hl=en&rclk=1",
    latitude: "35.1905452",
    longitude: "33.3520779",
  },
  {
    name: "MAP Boutique Hotel",
    category: "hotel",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipOUYOjYT59ZI7O6A85gV_SDwHGH2J9d7WyQC4mw=w136-h92-k-no",
    href: "https://www.google.com/maps/place/MAP+Boutique+Hotel/data=!4m11!3m10!1s0x14de175b9bafc0fb:0xdf2b04f6a06122fe!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.168402!4d33.3624082!16s%2Fg%2F11j0t96dwg!19sChIJ-8Cvm1sX3hQR_iJhoPYEK98?authuser=0&hl=en&rclk=1",
    latitude: "35.168402",
    longitude: "33.3624082",
  },
  {
    name: "Concorde Tower Hotel & Casino & Convention &\n                      Spa",
    category: "hotel",
    image_url:
      "https://lh3.googleusercontent.com/gps-proxy/ALd4DhGq7yAQrOu10g54LPqrnwUuDFXCxCSlVK0Fr4YLrPwAUkyuTH_ix_w3w1971CSwUz9y6OwXwTb6pe3aTOjC1Dz5BIk6I57GI9XknYBXSLa4U61e3RV5AA8jdnJcegVYgQbno8TbtJcv8NfYhXblBZ0RxVxQs6sa09S0RkMaY4o_g8rDcc0gPwk0=w186-h92-k-no",
    href: "https://www.google.com/maps/place/Concorde+Tower+Hotel+%26+Casino+%26+Convention+%26+Spa/data=!4m11!3m10!1s0x14de11a3da835ca5:0xb92bb6742e24a439!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.20947!4d33.3223625!16s%2Fg%2F11j7xj04qy!19sChIJpVyD2qMR3hQROaQkLnS2K7k?authuser=0&hl=en&rclk=1",
    latitude: "35.20947",
    longitude: "33.3223625",
  },
  {
    name: "The Tony The Place To Stay",
    category: "hotel",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipMXK_5UJ67X2-o5KSI72fAlIM_W_FdJHLLAN_jq=w122-h92-k-no",
    href: "https://www.google.com/maps/place/The+Tony+The+Place+To+Stay/data=!4m11!3m10!1s0x14de175afc000001:0xe19d4a9af31fabcd!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.1700763!4d33.3622596!16s%2Fg%2F11c3198xhm!19sChIJAQAA_FoX3hQRzasf85pKneE?authuser=0&hl=en&rclk=1",
    latitude: "35.1700763",
    longitude: "33.3622596",
  },
  {
    name: "Enkaya Hotel",
    category: "hotel",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipPQ6Fbxn-wSuQOB1LO4Bl2OrpSEAlNf0GDdWNPY=w122-h92-k-no",
    href: "https://www.google.com/maps/place/Enkaya+Hotel/data=!4m11!3m10!1s0x14de177fd711f1d7:0x81e7d8db2bc6a887!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.1779708!4d33.3621292!16s%2Fg%2F11fr7vtp2p!19sChIJ1_ER138X3hQRh6jGK9vY54E?authuser=0&hl=en&rclk=1",
    latitude: "35.1779708",
    longitude: "33.3621292",
  },
  {
    name: "Djumba Hotel & Cafe",
    category: "hotel",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipMa1r7PU1f8zd1pujvikivsx2mfGWczPTvnSiPF=w163-h92-k-no",
    href: "https://www.google.com/maps/place/Djumba+Hotel+%26+Cafe/data=!4m11!3m10!1s0x14de172c0f43241b:0x552190c27e1bfb61!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.1773467!4d33.3582372!16s%2Fg%2F11fcr8l8fl!19sChIJGyRDDywX3hQRYfsbfsKQIVU?authuser=0&hl=en&rclk=1",
    latitude: "35.1773467",
    longitude: "33.3582372",
  },
  {
    name: "Grand Pasha Nicosia Hotel & Casino & Spa",
    category: "hotel",
    image_url:
      "https://lh3.googleusercontent.com/gps-proxy/ALd4DhEJyZXVhlErLj15tSE9CDus9bnAXPWZLn4u1G15jFlIH4Sr9VTfQWMnspVROXEn7Vk0yCz1s_2_jOH-bqHnFMR5Jq34dQ-V9FNA-XnQPtQXmbeb2W89vQxcT8pBVP6cG2z-N_V6AC79m-rYvYvQ2QODW6cZihzfraDEvkUgjXXxh75vATvKqJ7O=w138-h92-k-no",
    href: "https://www.google.com/maps/place/Grand+Pasha+Nicosia+Hotel+%26+Casino+%26+Spa/data=!4m11!3m10!1s0x14de10ccdd5e1671:0x8747bee76e32a62c!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.1935844!4d33.3474998!16s%2Fg%2F1v9d52pm!19sChIJcRZe3cwQ3hQRLKYybue-R4c?authuser=0&hl=en&rclk=1",
    latitude: "35.1935844",
    longitude: "33.3474998",
  },
  {
    name: "Cleopatra Hotel",
    category: "hotel",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipOY5M88ad7oAs-P27ZMaAfCEemgB-qal0_HwTDx=w187-h92-k-no",
    href: "https://www.google.com/maps/place/Cleopatra+Hotel/data=!4m11!3m10!1s0x14de175797d7e36d:0x68b6094416e45ef!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.1650671!4d33.3585292!16s%2Fg%2F11b7xw7yt2!19sChIJbePXl1cX3hQR70VuQZRgiwY?authuser=0&hl=en&rclk=1",
    latitude: "35.1650671",
    longitude: "33.3585292",
  },
  {
    name: "TasEv Boutique Hotel",
    category: "hotel",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipPxaS4VDY06sVqgsVogn01SRXpvklDPPRcgyF6a=w94-h92-k-no",
    href: "https://www.google.com/maps/place/TasEv+Boutique+Hotel/data=!4m11!3m10!1s0x14de17afd2ff9141:0x4473d303c4fc0346!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.1774099!4d33.358079!16s%2Fg%2F11gvzkgbs9!19sChIJQZH_0q8X3hQRRgP8xAPTc0Q?authuser=0&hl=en&rclk=1",
    latitude: "35.1774099",
    longitude: "33.358079",
  },
  {
    name: "Naga\u015f Hotel",
    category: "hotel",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipP4XxpOjZSA3U68fpxIF9xvzpt0SLPCtZDTW1CL=w122-h92-k-no",
    href: "https://www.google.com/maps/place/Naga%C5%9F+Hotel/data=!4m11!3m10!1s0x14de1784f5b56f09:0x92dc2cf729597f9b!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.1793929!4d33.3594268!16s%2Fg%2F11ghnyq5k5!19sChIJCW-19YQX3hQRm39ZKfcs3JI?authuser=0&hl=en&rclk=1",
    latitude: "35.1793929",
    longitude: "33.3594268",
  },
  {
    name: "Alya Rooms",
    category: "hotel",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipOPAXWcll1PyotDKrO0XVeRm_NBWj_55x7XSo6H=w138-h92-k-no",
    href: "https://www.google.com/maps/place/Alya+Rooms/data=!4m11!3m10!1s0x14de1734c31b2979:0xb68d3f5abf4b54a2!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.1903572!4d33.3493266!16s%2Fg%2F11fqv47crp!19sChIJeSkbwzQX3hQRolRLv1o_jbY?authuser=0&hl=en&rclk=1",
    latitude: "35.1903572",
    longitude: "33.3493266",
  },
  {
    name: "Delphi Hotel",
    category: "hotel",
    image_url:
      "https://lh3.googleusercontent.com/gps-proxy/ALd4DhFEk5_jEXd6kn5ZdSBSvy-6cqTtovi2btKx0ZmISRWJcv6N8m1z8nsUjRqPNo4GRfZnT268E1Grg8Bzi0C0qkrsk-ASknceIA3cheB5UgT7I1Lu2dFLxEn-92xwXrVXyrFieL-JO8GBjyCAKPlqob_sc3qEIFsbwJlOfo3JCCDL2-UXHDC7LrA=w122-h92-k-no",
    href: "https://www.google.com/maps/place/Delphi+Hotel/data=!4m11!3m10!1s0x14de17507dc9bf99:0xbed8b12a64bfa029!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.170762!4d33.3593833!16s%2Fg%2F11xlbt3dg!19sChIJmb_JfVAX3hQRKaC_ZCqx2L4?authuser=0&hl=en&rclk=1",
    latitude: "35.170762",
    longitude: "33.3593833",
  },
  {
    name: "Sofouli Suites",
    category: "hotel",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipMTfIDaFHinidsUTfC-wBY-8SUT7kTND-1OtYa6=w80-h142-k-no",
    href: "https://www.google.com/maps/place/Sofouli+Suites/data=!4m11!3m10!1s0x14de175129a8694d:0xf49a24c2c2a1821e!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.1693896!4d33.3566489!16s%2Fg%2F11dzd3gr31!19sChIJTWmoKVEX3hQRHoKhwsIkmvQ?authuser=0&hl=en&rclk=1",
    latitude: "35.1693896",
    longitude: "33.3566489",
  },
  {
    name: "Greenland Premium Residance",
    category: "hotel",
    image_url:
      "https://lh3.googleusercontent.com/gps-proxy/ALd4DhHjmvAW_Io1nQEqfrZbCM7vua7V35qgv2G_tnO7xYDuWbMjn646xWFeuBENQ5NV97FAafjmFIIE2Ty0jxGoNfr-EergRaM8GblFyp6HPLinGfTDDPm_0Bz6eo609FdA6h-JD3wPa3ZXuNX_MKVbuJXcG8CjNQXUeElSLk8n9raZnBs9Ol14gCM=w138-h92-k-no",
    href: "https://www.google.com/maps/place/Greenland+Premium+Residance/data=!4m11!3m10!1s0x14de16df868dff75:0x9941ad4323552b7a!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.1996159!4d33.3699564!16s%2Fg%2F11fmlj7ngg!19sChIJdf-Nht8W3hQReitVI0OtQZk?authuser=0&hl=en&rclk=1",
    latitude: "35.1996159",
    longitude: "33.3699564",
  },
  {
    name: "Cleopatra Hotel",
    category: "hotel",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipOY5M88ad7oAs-P27ZMaAfCEemgB-qal0_HwTDx=w187-h92-k-no",
    href: "https://www.google.com/maps/place/Cleopatra+Hotel/data=!4m11!3m10!1s0x14de175797d7e36d:0x68b6094416e45ef!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.1650671!4d33.3585292!16s%2Fg%2F11b7xw7yt2!19sChIJbePXl1cX3hQR70VuQZRgiwY?authuser=0&hl=en&rclk=1",
    latitude: "35.1650671",
    longitude: "33.3585292",
  },
  {
    name: "City Royal Lefkosa Turk republic of North Cyprus",
    category: "hotel",
    image_url:
      "https://lh3.googleusercontent.com/gps-proxy/ALd4DhHxo_Yl8Aeyu4ZX_ZFU9NV1D4BsMmY5DZlvbKWFVQwWi2gnm8qy-ewuazJxc-JClwFXN4N9rYwhHephLvl1M8-cxeS_4mw9WvJausqRt5Ola0shMxYfGTJIL1ivp_HNRDBT8sxrPeg1fh5V-w3hGwWmq0BkKmrbEGk69CMrepJBMLAgwTO9=w122-h92-k-no",
    href: "https://www.google.com/maps/place/City+Royal+Lefkosa+Turk+republic+of+North+Cyprus/data=!4m11!3m10!1s0x14de173c7ec85701:0x916745c783e1e94f!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.1869358!4d33.3651737!16s%2Fg%2F1td823t_!19sChIJAVfIfjwX3hQRT-nhg8dFZ5E?authuser=0&hl=en&rclk=1",
    latitude: "35.1869358",
    longitude: "33.3651737",
  },
  {
    name: "Cyprus Cottage Heights",
    category: "hotel",
    image_url: "//maps.gstatic.com/tactile/pane/result-no-thumbnail-2x.png",
    href: "https://www.google.com/maps/place/Cyprus+Cottage+Heights/data=!4m11!3m10!1s0x14de1a71421e0051:0x4d6801833951481b!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.1696351!4d33.3195025!16s%2Fg%2F11rnds8r_p!19sChIJUQAeQnEa3hQRG0hROYMBaE0?authuser=0&hl=en&rclk=1",
    latitude: "35.1696351",
    longitude: "33.3195025",
  },
  {
    name: "Hotel Sun",
    category: "hotel",
    image_url:
      "https://lh3.googleusercontent.com/gps-proxy/ALd4DhE2cxd5WO1TfUd-wQYGgU1ty10WKt007irAI8xcOQzl-_9O2uULFC2Z-m7sekqJfhUWKJZHeHVUDP2YAlYuFSgLj_3Ram9-LVCqs_YO30mSWSsoRFPVS7Czc02XeA-Y_SucJAMt64LaFnfzGQwRWkuE0xsYtuJOsCBcvmuqX1gj-R2UcVLtELCx=w163-h92-k-no",
    href: "https://www.google.com/maps/place/Hotel+Sun/data=!4m11!3m10!1s0x14de10cd089703af:0x94b5b17fe09d8cbc!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.1947734!4d33.3463304!16s%2Fg%2F11f55hw4r9!19sChIJrwOXCM0Q3hQRvIyd4H-xtZQ?authuser=0&hl=en&rclk=1",
    latitude: "35.1947734",
    longitude: "33.3463304",
  },
  {
    name: "Altius Boutique Hotel",
    category: "hotel",
    image_url:
      "https://lh3.googleusercontent.com/gps-proxy/ALd4DhFzryPgxBNWWNx5zE8g8OoMKLWIphGqBGy1L-A6MFqqR9wHFqWhXcxCHuhDpLySi1LXenn9eOI0jrLlXYK6ar7tpZJCjMx2yoavtDERUlJ1CFVQQTeLf43YwrfPLbRjS2A2CEWnvPTXdPZm6ZoVtXObzMsB9rSiwKj51PPpRUrpqqJ1LfadstR60A=w80-h106-k-no",
    href: "https://www.google.com/maps/place/Altius+Boutique+Hotel/data=!4m11!3m10!1s0x14de10aadcb3001b:0xea2247147e179007!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.1688376!4d33.3473942!16s%2Fg%2F11xjkf5cb!19sChIJGwCz3KoQ3hQRB5AXfhRHIuo?authuser=0&hl=en&rclk=1",
    latitude: "35.1688376",
    longitude: "33.3473942",
  },
  {
    name: "Sofouli Suites",
    category: "hotel",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipMTfIDaFHinidsUTfC-wBY-8SUT7kTND-1OtYa6=w80-h142-k-no",
    href: "https://www.google.com/maps/place/Sofouli+Suites/data=!4m11!3m10!1s0x14de175129a8694d:0xf49a24c2c2a1821e!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.1693896!4d33.3566489!16s%2Fg%2F11dzd3gr31!19sChIJTWmoKVEX3hQRHoKhwsIkmvQ?authuser=0&hl=en&rclk=1",
    latitude: "35.1693896",
    longitude: "33.3566489",
  },
  {
    name: "Valide Han\u0131m Konak",
    category: "hotel",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipOxNm-29Q-ytPXZJWrm-ntZLXrUhG9vEGV3Gdax=w80-h116-k-no",
    href: "https://www.google.com/maps/place/Valide+Han%C4%B1m+Konak/data=!4m11!3m10!1s0x14de17f895da3209:0xcc7727dc93e081ec!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.1804158!4d33.3614522!16s%2Fg%2F11fjmv8fvc!19sChIJCTLalfgX3hQR7IHgk9wnd8w?authuser=0&hl=en&rclk=1",
    latitude: "35.1804158",
    longitude: "33.3614522",
  },
  {
    name: "Cypriot Swallow Boutique Hotel",
    category: "hotel",
    image_url:
      "https://lh3.googleusercontent.com/gps-proxy/ALd4DhHyMKHusRXlzprAUZ4YPR73d-hUkW18n-BZQ6n0ueX0LIPY6kfMNCvebu_oqqT1LY-4BRMMqT0mV7QdYRvQ7kvIJkX-xso6SFOm72xy0fg4tqXv70fsxcbd7t8Bm8OQX-quOq8Vhr64pRljgel7zfYjm6gTBePNM0RXQ3jL4_5e__aO5b81BM4=w138-h92-k-no",
    href: "https://www.google.com/maps/place/Cypriot+Swallow+Boutique+Hotel/data=!4m11!3m10!1s0x14de1738a6cd778f:0x8e92df1055f5cec3!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.1815054!4d33.3643899!16s%2Fg%2F11b6hh_fhl!19sChIJj3fNpjgX3hQRw871VRDfko4?authuser=0&hl=en&rclk=1",
    latitude: "35.1815054",
    longitude: "33.3643899",
  },
  {
    name: "Dorana Residence",
    category: "hotel",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipPtSH7FKrxtdXdniWRM05VeqaiS0MoBrBVRRMJ6=w163-h92-k-no",
    href: "https://www.google.com/maps/place/Dorana+Residence/data=!4m11!3m10!1s0x14de1152472490e1:0xdbffff61b3c148ed!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.2296357!4d33.3206882!16s%2Fg%2F11j80l20hj!19sChIJ4ZAkR1IR3hQR7UjBs2H__9s?authuser=0&hl=en&rclk=1",
    latitude: "35.2296357",
    longitude: "33.3206882",
  },
  {
    name: "Nicosia Central Park Residences",
    category: "hotel",
    image_url:
      "https://lh3.googleusercontent.com/gps-proxy/ALd4DhGljNgX5Y6xgrSrefuwBtfGWijXAefZFUUQPXTwQNU9YGcxP2uih68xJcr5ejHc0AJg0B2LUZ2lMGtFHZhw_rlHPZdqwUUKcNAS6l7cRoXrVtFA6svnd4395w1qfbrQdWkvnPyDxtFefKOC9flabnp_w0PpCOIIIISdaudhbTWVf_GzVpIF6vc=w138-h92-k-no",
    href: "https://www.google.com/maps/place/Nicosia+Central+Park+Residences/data=!4m11!3m10!1s0x14de175723edd7c1:0xcf748f4c69de3a51!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.1675668!4d33.3570596!16s%2Fg%2F11dzdh737w!19sChIJwdftI1cX3hQRUTreaUyPdM8?authuser=0&hl=en&rclk=1",
    latitude: "35.1675668",
    longitude: "33.3570596",
  },
  {
    name: "Sylvias antique house",
    category: "hotel",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipO6F62z3rImiRcI4rNmzY4cZs22Qf9FIzQBbBV2=w80-h106-k-no",
    href: "https://www.google.com/maps/place/Sylvias+antique+house/data=!4m11!3m10!1s0x14de17ca1252da61:0x43c87f751f9ee6a6!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.1761162!4d33.3707592!16s%2Fg%2F11j_2zdt0g!19sChIJYdpSEsoX3hQRpuaeH3V_yEM?authuser=0&hl=en&rclk=1",
    latitude: "35.1761162",
    longitude: "33.3707592",
  },
  {
    name: "Gul Hanim House",
    category: "hotel",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipOvp39cAPiu-5Q1xShI31hTTZ2teE8inKh_UtK6=w138-h92-k-no",
    href: "https://www.google.com/maps/place/Gul+Hanim+House/data=!4m11!3m10!1s0x14de17476714f96f:0x4079329f9c5082c!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.181081!4d33.363947!16s%2Fg%2F11ckvds3yg!19sChIJb_kUZ0cX3hQRLAjF-SmTBwQ?authuser=0&hl=en&rclk=1",
    latitude: "35.181081",
    longitude: "33.363947",
  },
  {
    name: "Lykavitos Apartments",
    category: "hotel",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipPxG5Byi29N0md_m4Tl2hkWDYb6eNDiwDoFpPgH=w80-h106-k-no",
    href: "https://www.google.com/maps/place/Lykavitos+Apartments/data=!4m11!3m10!1s0x14de176f7fab4a7b:0x882e20be166ee26e!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.1671637!4d33.3792972!16s%2Fg%2F1hc573fkl!19sChIJe0qrf28X3hQRbuJuFr4gLog?authuser=0&hl=en&rclk=1",
    latitude: "35.1671637",
    longitude: "33.3792972",
  },
  {
    name: "Centrum Hotel",
    category: "hotel",
    image_url:
      "https://lh3.googleusercontent.com/gps-proxy/ALd4DhG_70zEMxWBRK1uxpFNVyCw8ndN85H1dQIPI1lT6fvXLu3NCpbBmJfNrAQAv1-QG8MDdY-nUaKRmsfUzDkeTECI4Il8Dq0ak19aNeEKLzCYkKROZW9-VgfFned45-OWXhoPMcqTa2Hvn_1jePcw7PdUJafBFSzmfQ50d_li6-XKrpu2icBf7nl7Tg=w80-h120-k-no",
    href: "https://www.google.com/maps/place/Centrum+Hotel/data=!4m11!3m10!1s0x14de175a5ff5ca07:0x1ff797ddfed87e75!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.1700277!4d33.3616795!16s%2Fg%2F1thvk4pq!19sChIJB8r1X1oX3hQRdX7Y_t2X9x8?authuser=0&hl=en&rclk=1",
    latitude: "35.1700277",
    longitude: "33.3616795",
  },
  {
    name: "Artisan Homes",
    category: "hotel",
    image_url:
      "https://lh3.googleusercontent.com/gps-proxy/ALd4DhHcl4a7Q2LKp2rPKmmTU8wJ8IYkXRyPmbCOGCXK1SUNPqA4cc84q6fdvjSOTHJmQ4iXEdm_qEjUAx7-uI3-B5vUk6I69A16VRy_hKoSi5hQsdkd9x8_4IzgdBEWrrYfsfpEBCtkBf3QX3DdsqKDlWVaCDKQefaJMcOj8upUBerRx1ohsG8rt2Ct=w138-h92-k-no",
    href: "https://www.google.com/maps/place/Artisan+Homes/data=!4m11!3m10!1s0x14dfc38f74afee97:0x1d513b1fbbfa68a0!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.1721826!4d33.360022!16s%2Fg%2F1tf556t4!19sChIJl-6vdI_D3xQRoGj6ux87UR0?authuser=0&hl=en&rclk=1",
    latitude: "35.1721826",
    longitude: "33.360022",
  },
  {
    name: "Maralia Hotel",
    category: "hotel",
    image_url:
      "https://lh3.googleusercontent.com/gps-proxy/ALd4DhHyNPLN0uCZx2KqzTemAw7nZ4BytN4Iwe-GqKARKcsEk3BddFwvlU-Si5Dl-3mcfy1C9oa9cKvmP0wlvxMbNmm6P-bTpYt-vqMkX-N_Xa43vaxGRtlid3HTp4vtpHwBXjUYM02K7ODU5N1WpkkII4MKKgzDRsU5GGgRN_ztiHHjXOEuMZtmjrd1=w136-h92-k-no",
    href: "https://www.google.com/maps/place/Maralia+Hotel/data=!4m11!3m10!1s0x14de171a129023b9:0x2eaff9b2d8644f30!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.1698716!4d33.3593544!16s%2Fg%2F11fk3_plzd!19sChIJuSOQEhoX3hQRME9k2LL5ry4?authuser=0&hl=en&rclk=1",
    latitude: "35.1698716",
    longitude: "33.3593544",
  },
  {
    name: "Royiatiko Hotel",
    category: "hotel",
    image_url:
      "https://lh3.googleusercontent.com/gps-proxy/ALd4DhGPJeQuCnq_bnGIKyowpMqlvtt4GFKil4UKdBRSvpDKagyzKQcsts6P2Dc2ILvzTjjj6xRdOgWJFIsP74pIHiz9mIgGWjQ2fxwdUuoy899hHsk4wcrIvF2BnZZhAJMArPZlIJq89BLFa7uK61gmglZz6koCC4A4N4lcsHQ2kVBwDtDDXpsIxCNjMg=w92-h92-k-no",
    href: "https://www.google.com/maps/place/Royiatiko+Hotel/data=!4m11!3m10!1s0x14de175aa47577e1:0x7c32875625bf1401!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.1711616!4d33.3603057!16s%2Fg%2F1tcvl9kp!19sChIJ4Xd1pFoX3hQRARS_JVaHMnw?authuser=0&hl=en&rclk=1",
    latitude: "35.1711616",
    longitude: "33.3603057",
  },
  {
    name: "Hotel Cyprus",
    category: "hotel",
    image_url: "//maps.gstatic.com/tactile/pane/result-no-thumbnail-2x.png",
    href: "https://www.google.com/maps/place/Hotel+Cyprus/data=!4m11!3m10!1s0x14de17503f46be69:0x332d67b6169cefc0!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.1723249!4d33.3580511!16s%2Fg%2F11c5h3_hn5!19sChIJab5GP1AX3hQRwO-cFrZnLTM?authuser=0&hl=en&rclk=1",
    latitude: "35.1723249",
    longitude: "33.3580511",
  },
  {
    name: "The Sendal Boutique Hotel",
    category: "hotel",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipM5mg9sxJ_i_RuIQEhoK5TX6YFo_yJbAtRig3dO=w137-h92-k-no",
    href: "https://www.google.com/maps/place/The+Sendal+Boutique+Hotel/data=!4m11!3m10!1s0x14de178751db4149:0x48a857e1c391b218!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.169967!4d33.3628131!16s%2Fg%2F11tx_tl2rz!19sChIJSUHbUYcX3hQRGLKRw-FXqEg?authuser=0&hl=en&rclk=1",
    latitude: "35.169967",
    longitude: "33.3628131",
  },
  {
    name: "Sky Hotel",
    category: "hotel",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipOjeMVnTruX42xDhBQjabaOfvXD5Vro2Yo5AWSZ=w80-h106-k-no",
    href: "https://www.google.com/maps/place/Sky+Hotel/data=!4m11!3m10!1s0x14de175ad83a9f81:0xf1255bba300d6a06!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.1707555!4d33.3621487!16s%2Fg%2F1tm6ttwb!19sChIJgZ862FoX3hQRBmoNMLpbJfE?authuser=0&hl=en&rclk=1",
    latitude: "35.1707555",
    longitude: "33.3621487",
  },
  {
    name: "Rimi Hotel",
    category: "hotel",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipPN4G82rBxJf5UCnEdgvRFXjecyxuguVGPDbIhT=w80-h106-k-no",
    href: "https://www.google.com/maps/place/Rimi+Hotel/data=!4m11!3m10!1s0x14de175af9ae355f:0x978c0609ba2b4861!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.1699669!4d33.3620637!16s%2Fg%2F1tf8k7vc!19sChIJXzWu-VoX3hQRYUgrugkGjJc?authuser=0&hl=en&rclk=1",
    latitude: "35.1699669",
    longitude: "33.3620637",
  },
  {
    name: "Old Stone Boutique Hotel - North Cyprus / Daily Rental\n                      Rooms / G\u00fcnl\u00fck Kiral\u0131k Odalar",
    category: "hotel",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipM_pTDQZfc_ajUpSlbKXmTyfWs4ygObZ5mrbpSD=w137-h92-k-no",
    href: "https://www.google.com/maps/place/Old+Stone+Boutique+Hotel+-+North+Cyprus+%2F+Daily+Rental+Rooms+%2F+G%C3%BCnl%C3%BCk+Kiral%C4%B1k+Odalar/data=!4m11!3m10!1s0x14de179fb52ee5f7:0x309a3dfd681d71e3!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.1798267!4d33.3614742!16s%2Fg%2F11tmr9plbm!19sChIJ9-UutZ8X3hQR43EdaP09mjA?authuser=0&hl=en&rclk=1",
    latitude: "35.1798267",
    longitude: "33.3614742",
  },
  {
    name: "Bastion Inn",
    category: "hotel",
    image_url:
      "https://lh3.googleusercontent.com/gps-proxy/ALd4DhHeBho1WFT3Eo3Z7YmVeXhYYjN7EhHHhCz6gM7UmuKybGtK2vs5HxZASmXoCSKssGAj6qSVyao-CiHTAjoYomBlD2K0UONj76gRUMkP1GhjstiFbDmJ-hHf4IHNvF7pNvkx1dWEaDw-Cy_gbK3qP3j7lr0Z6ooiEEXxZgydJlui9711pFuPIm0h=w122-h92-k-no",
    href: "https://www.google.com/maps/place/Bastion+Inn/data=!4m11!3m10!1s0x14de174f081d3ac3:0x8c021440b7209a70!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.1760689!4d33.3577579!16s%2Fg%2F11gghdw5f7!19sChIJwzodCE8X3hQRcJogt0AUAow?authuser=0&hl=en&rclk=1",
    latitude: "35.1760689",
    longitude: "33.3577579",
  },
  {
    name: "Saray Hotel",
    category: "hotel",
    image_url:
      "https://lh3.googleusercontent.com/gps-proxy/ALd4DhEcVxvVg08EX8zODZJNSHXzhN1lcwOiW2ZztMhOVtW5Q6oXSKX6VKLQ_PG2e4QzpPkX5r-c5QUuua3eekfyeT-EyzQ0jSOAQj_pA7fFO_rZagsQyU2K-Do6tNZxGLIsl-GnUdI3WFhGOi-q_FdzgjEsECU1f5FHJhciyGmT1d8lS7Cc20vReHKS=w138-h92-k-no",
    href: "https://www.google.com/maps/place/Saray+Hotel/data=!4m11!3m10!1s0x14de1745e1bf4943:0x8d94135edb7d6a6!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.1774582!4d33.36099!16s%2Fg%2F11h07y3190!19sChIJQ0m_4UUX3hQRpta37TVB2Qg?authuser=0&hl=en&rclk=1",
    latitude: "35.1774582",
    longitude: "33.36099",
  },
  {
    name: "Campus Cyprus",
    category: "hotel",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipNru8sqp9gkgF6oUARLBY1bCLPiog-vecMUMJeE=w122-h92-k-no",
    href: "https://www.google.com/maps/place/Campus+Cyprus/data=!4m11!3m10!1s0x14de115a0925031d:0x992f054ea6d60c45!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.2438583!4d33.3222694!16s%2Fg%2F11ffvvpg9v!19sChIJHQMlCVoR3hQRRQzWpk4FL5k?authuser=0&hl=en&rclk=1",
    latitude: "35.2438583",
    longitude: "33.3222694",
  },
  {
    name: "Crown Inn Hotel - Nicosia - Cyprus",
    category: "hotel",
    image_url:
      "https://lh3.googleusercontent.com/gps-proxy/ALd4DhF77hGfbAi88SInOiYM_bk5XfZJC8-lUb3DTa5yuh7E_VIGnK2ZeHMriVNLdmxqW2a79YBRueuCzrupfaiGzMUkJfQQhAKwMFoCLFkR2-0o4vZlWCUNgB0JZzCWd3CokmR7kl2TVZCMapwpqKm6WvC6osu0ID_Mx3UgSoUDwq0M-cuY9VEevjkx=w138-h92-k-no",
    href: "https://www.google.com/maps/place/Crown+Inn+Hotel+-+Nicosia+-+Cyprus/data=!4m11!3m10!1s0x14de10aea15b60cd:0x4c9a243e77fcdf29!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.174414!4d33.342532!16s%2Fg%2F1tdsm9jq!19sChIJzWBboa4Q3hQRKd_8dz4kmkw?authuser=0&hl=en&rclk=1",
    latitude: "35.174414",
    longitude: "33.342532",
  },
  {
    name: "Seslikaya Hotel",
    category: "hotel",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipONpSjQ4vFe9AV3ydK8YpiqaY84FnYuNmIrKg8L=w80-h116-k-no",
    href: "https://www.google.com/maps/place/Seslikaya+Hotel/data=!4m11!3m10!1s0x14de177dc0543409:0x202abb8f91692cb2!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.1778681!4d33.3613173!16s%2Fg%2F11j8lnnm69!19sChIJCTRUwH0X3hQRsixpkY-7KiA?authuser=0&hl=en&rclk=1",
    latitude: "35.1778681",
    longitude: "33.3613173",
  },
  {
    name: "Antik house hotel/pansiyon",
    category: "hotel",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipMiuUw6Kp0FRQK3cWXhnJA9wck_QvSc0dAfq12u=w80-h142-k-no",
    href: "https://www.google.com/maps/place/Antik+house+hotel%2Fpansiyon/data=!4m11!3m10!1s0x14de1744318be95d:0xe01d47e4fe9dbc42!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.1761564!4d33.3629287!16s%2Fg%2F11clycznl3!19sChIJXemLMUQX3hQRQryd_uRHHeA?authuser=0&hl=en&rclk=1",
    latitude: "35.1761564",
    longitude: "33.3629287",
  },
  {
    name: "Yerlikaya Hotel",
    category: "hotel",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipMInYxwu9vyMIf3V8lNR2OjxaQbkU22L8tiyZ1o=w80-h142-k-no",
    href: "https://www.google.com/maps/place/Yerlikaya+Hotel/data=!4m11!3m10!1s0x14de1747744326af:0x3d07d8cf9e617b32!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.1807732!4d33.3628926!16s%2Fg%2F11s1b7sm_5!19sChIJryZDdEcX3hQRMnthns_YBz0?authuser=0&hl=en&rclk=1",
    latitude: "35.1807732",
    longitude: "33.3628926",
  },
  {
    name: "22 Nicosia Boutique Hotel",
    category: "hotel",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipMu6d8GpD5KuzMG_xH3-d66Jj9viUr4eLcFGH04=w80-h106-k-no",
    href: "https://www.google.com/maps/place/22+Nicosia+Boutique+Hotel/data=!4m11!3m10!1s0x14de17dbecec2efd:0x9f0eafb7ea1c1b80!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.1773425!4d33.3639704!16s%2Fg%2F11s2pl9jw5!19sChIJ_S7s7NsX3hQRgBsc6revDp8?authuser=0&hl=en&rclk=1",
    latitude: "35.1773425",
    longitude: "33.3639704",
  },
  {
    name: "Unique Studio Phaneromenis 41",
    category: "hotel",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipNZRNfIDeXZDgwaYaJuNoOZiVXRW9MKu8Q5BqNm=w122-h92-k-no",
    href: "https://www.google.com/maps/place/Unique+Studio+Phaneromenis+41/data=!4m11!3m10!1s0x14de174bee29726f:0x4c83a755e40bdb89!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.1739859!4d33.3623274!16s%2Fg%2F11h93dzdvz!19sChIJb3Ip7ksX3hQRidsL5FWng0w?authuser=0&hl=en&rclk=1",
    latitude: "35.1739859",
    longitude: "33.3623274",
  },
  {
    name: "Central Square Apartment",
    category: "hotel",
    image_url:
      "https://lh3.googleusercontent.com/gps-proxy/ALd4DhEZrBJ1qNfQiqhLU6x7Qbke1Lasu93zO-kF22OrXlx278y0xAoAnsnr1049Zj4NWa8pfIOTzL6K0wPdEsn3yE5Z523G9-wOUS7AXUeXMwQNj5kPKXxE5-yRTjJKEu-zowLQESxApSaRNKgiIsSxUHQ8x31Heha5ZU9tZDdjTVqjdec1kGaHVgk=w122-h92-k-no",
    href: "https://www.google.com/maps/place/Central+Square+Apartment/data=!4m11!3m10!1s0x14de17c5290c0fb3:0x7c593290afd9a422!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.1704041!4d33.3600109!16s%2Fg%2F11f5q8jpg6!19sChIJsw8MKcUX3hQRIqTZr5AyWXw?authuser=0&hl=en&rclk=1",
    latitude: "35.1704041",
    longitude: "33.3600109",
  },
  {
    name: "Ender Elite Hotel",
    category: "hotel",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipOww3hoIcHxOME5OZBysLZ004C2rIuVr4_O1hiz=w80-h106-k-no",
    href: "https://www.google.com/maps/place/Ender+Elite+Hotel/data=!4m11!3m10!1s0x14de17a60fd467eb:0x372de3962ad7ea8c!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.1866708!4d33.3585083!16s%2Fg%2F11rfr84pvq!19sChIJ62fUD6YX3hQRjOrXKpbjLTc?authuser=0&hl=en&rclk=1",
    latitude: "35.1866708",
    longitude: "33.3585083",
  },
  {
    name: "Flor Guest House",
    category: "hotel",
    image_url: "//maps.gstatic.com/tactile/pane/result-no-thumbnail-2x.png",
    href: "https://www.google.com/maps/place/Flor+Guest+House/data=!4m11!3m10!1s0x14de174f20a18a99:0x2eb58b4dc2b39eef!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.177734!4d33.357053!16s%2Fg%2F11vpt153s3!19sChIJmYqhIE8X3hQR756zwk2LtS4?authuser=0&hl=en&rclk=1",
    latitude: "35.177734",
    longitude: "33.357053",
  },
  {
    name: "AKSARAY boutique hotel",
    category: "hotel",
    image_url:
      "https://lh3.googleusercontent.com/gps-proxy/ALd4DhHxc1K0y4Jw_jh43B4UH2uqr6ILmQh9-973M8UIZWgJmcS6GJY4NPON_7SCo1d0kjB2oiBdvoeZ1Ky5toOWuIpDplZMOV4ZBNaql7fo_f9i8XP6otasiOlPmA2FYo3e_sgpHbpY9-VYBOplHAQbdaBWiWW2dcG9fyV8p-fCdXfhOTfCPfaDb5no=w122-h92-k-no",
    href: "https://www.google.com/maps/place/AKSARAY+boutique+hotel/data=!4m11!3m10!1s0x14de170076424c75:0xdd657ab745f7391!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.1781275!4d33.3616566!16s%2Fg%2F11vs820khl!19sChIJdUxCdgAX3hQRkXNfdKtX1g0?authuser=0&hl=en&rclk=1",
    latitude: "35.1781275",
    longitude: "33.3616566",
  },
  {
    name: "Martin Hospitality Services",
    category: "hotel",
    image_url: "//maps.gstatic.com/tactile/pane/result-no-thumbnail-2x.png",
    href: "https://www.google.com/maps/place/Martin+Hospitality+Services/data=!4m11!3m10!1s0x14de17d976038c23:0xb94b4620e09482a3!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.1727899!4d33.3647365!16s%2Fg%2F11vs29vzjl!19sChIJI4wDdtkX3hQRo4KU4CBGS7k?authuser=0&hl=en&rclk=1",
    latitude: "35.1727899",
    longitude: "33.3647365",
  },
  {
    name: "Averof Hotel",
    category: "hotel",
    image_url:
      "https://lh3.googleusercontent.com/gps-proxy/ALd4DhGsIauj8C6SqtCGuDG2pKvyTjcsgBgP2Kp_8zzbvYmEZOH1ljVeCNAEk0qhFXeQQLn7aFaVi48LrmRmvnH4VsvVYryGE0HLx_AOC7sAuRHJ5vNqFeFlw4eKpZAlxfb9TtBHV1owDAAHGkNCSEw9MaxyMv5iL_MWZQgJUVrEIZ7QUhbQz1Z4AIGOVg=w130-h92-k-no",
    href: "https://www.google.com/maps/place/Averof+Hotel/data=!4m11!3m10!1s0x14de10b2ae7ce2e1:0x867173c18e133441!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.1773581!4d33.3469706!16s%2Fg%2F12214fvnb!19sChIJ4eJ8rrIQ3hQRQTQTjsFzcYY?authuser=0&hl=en&rclk=1",
    latitude: "35.1773581",
    longitude: "33.3469706",
  },
  {
    name: "The Moose Hotel",
    category: "hotel",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipO24TefYPVQKdzECfHQTQbC8Wdslne0gZOJwfwN=w122-h92-k-no",
    href: "https://www.google.com/maps/place/The+Moose+Hotel/data=!4m11!3m10!1s0x14de17489e97407f:0x9b283d9e01fb90a2!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.1794204!4d33.3595907!16s%2Fg%2F11j2s6hq8m!19sChIJf0CXnkgX3hQRopD7AZ49KJs?authuser=0&hl=en&rclk=1",
    latitude: "35.1794204",
    longitude: "33.3595907",
  },
  {
    name: "Bougainvillea Garden",
    category: "hotel",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipML9Vm3OyBR3uf8NhpkDPAnCHxm4dLVRaw_8ldO=w80-h106-k-no",
    href: "https://www.google.com/maps/place/Bougainvillea+Garden/data=!4m11!3m10!1s0x14de173b2e2c23af:0x9ff40635490ff3dc!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.1805538!4d33.3673933!16s%2Fg%2F11s75d3g3n!19sChIJryMsLjsX3hQR3PMPSTUG9J8?authuser=0&hl=en&rclk=1",
    latitude: "35.1805538",
    longitude: "33.3673933",
  },
  {
    name: "Nicosia Eagle Eye Boutique Hotel",
    category: "hotel",
    image_url:
      "https://lh3.googleusercontent.com/gps-proxy/ALd4DhEIbC5Ug_mf26dY3zctqkB2DVDEQgV40nM3Qon_ergbGmK_yAdsVvCWLYYiF95Arfykj7njIP2oHdgsrbuja0cf9DsQd1j47qpRCp8A7UGXmVWPFo80_1RNIIYw8tZ5uqUhmJgvAcmWDM9kLnjnANkDddlFsygt8mygoZe5ZbzktqIbIGzWLrRE=w80-h120-k-no",
    href: "https://www.google.com/maps/place/Nicosia+Eagle+Eye+Boutique+Hotel/data=!4m11!3m10!1s0x14de17df31dd6323:0x12db1d316e6979ff!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.1812763!4d33.3630434!16s%2Fg%2F11h9bk8qxd!19sChIJI2PdMd8X3hQR_3lpbjEd2xI?authuser=0&hl=en&rclk=1",
    latitude: "35.1812763",
    longitude: "33.3630434",
  },
  {
    name: "The \u0130skemleci",
    category: "hotel",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipNsvS2Nta2vkQ1qGY0fSTtNYCpvwULTY7PU_BR7=w122-h92-k-no",
    href: "https://www.google.com/maps/place/The+%C4%B0skemleci/data=!4m11!3m10!1s0x14de178944f75e79:0x8a38e0dda77acdf5!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.1807447!4d33.3608067!16s%2Fg%2F11gtslz8sb!19sChIJeV73RIkX3hQR9c16p93gOIo?authuser=0&hl=en&rclk=1",
    latitude: "35.1807447",
    longitude: "33.3608067",
  },
  {
    name: "Mount View",
    category: "hotel",
    image_url: "//maps.gstatic.com/tactile/pane/result-no-thumbnail-2x.png",
    href: "https://www.google.com/maps/place/Mount+View/data=!4m11!3m10!1s0x14de1750aff232b1:0xcdfc040fa6ba4a9f!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.1689092!4d33.3592319!16s%2Fg%2F11f4wv2tsg!19sChIJsTLyr1AX3hQRn0q6pg8E_M0?authuser=0&hl=en&rclk=1",
    latitude: "35.1689092",
    longitude: "33.3592319",
  },
  {
    name: "Xanthis Hostel Nicosia City Centre",
    category: "hotel",
    image_url:
      "https://lh3.googleusercontent.com/gps-proxy/ALd4DhEDwe00cJCfCQhGVQ7uBMU8pMFgECQN8-3_lYcoaMWwSyIKotonm1T-v2f6nb_Tj6xKKRXZ8Q3uH0bwdIjc6ZyRERWJLJ0GiGhv31ZpqozPisZ0VlXxx-3E7a2CUkIyBhVWV3iBoz3OUTq9XvtKPr54eH0_FeMYCb6fBGieX-gjHkaRXv2lDSLK=w138-h92-k-no",
    href: "https://www.google.com/maps/place/Xanthis+Hostel+Nicosia+City+Centre/data=!4m11!3m10!1s0x14de1762a3ccd901:0xc29727295f75e5f6!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.1699696!4d33.3650611!16s%2Fg%2F11l68bw6jp!19sChIJAdnMo2IX3hQR9uV1Xyknl8I?authuser=0&hl=en&rclk=1",
    latitude: "35.1699696",
    longitude: "33.3650611",
  },
  {
    name: "Chara Anastasia",
    category: "hotel",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipOKDWuLj1ZUd35j3wh8l-TwUSx_uDWPiIF7Js4Q=w130-h92-k-no",
    href: "https://www.google.com/maps/place/Chara+Anastasia/data=!4m11!3m10!1s0x14de17e3dd564fcd:0x91ebde27d6833353!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.1883999!4d33.3830998!16s%2Fg%2F11h5rf5c9t!19sChIJzU9W3eMX3hQRUzOD1ife65E?authuser=0&hl=en&rclk=1",
    latitude: "35.1883999",
    longitude: "33.3830998",
  },
  {
    name: "Ta\u015fkonak Hotel & Restaurant Nicosia",
    category: "hotel",
    image_url:
      "https://lh3.googleusercontent.com/gps-proxy/ALd4DhHs3Kn7MiXVSFzIL3P1maFRsbuMcFvqY9iMWIiPMW1ZQfWSzy4kyrxyI4AcWotafrc5bM6D1FSzsx-UcYFI6fUagbriHRxzMDnfZS04ToPnIKK74xjckScBKSoWgzf05SxlxAZlHLdbb0tvpaK3MjmM7EzHQ-0u6WVDQMxONUrDOuVWxvob2zxC=w138-h92-k-no",
    href: "https://www.google.com/maps/place/Ta%C5%9Fkonak+Hotel+%26+Restaurant+Nicosia/data=!4m11!3m10!1s0x14de1709fd0b1963:0xd10b9d807d04feda!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.1873767!4d33.3678048!16s%2Fg%2F11h_v19p89!19sChIJYxkL_QkX3hQR2v4EfYCdC9E?authuser=0&hl=en&rclk=1",
    latitude: "35.1873767",
    longitude: "33.3678048",
  },
  {
    name: "pedieos guest house",
    category: "hotel",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipNl1-FmhBwhDXQy1D5wvNjf3J1Qczl3d6qxcbHS=w80-h94-k-no",
    href: "https://www.google.com/maps/place/pedieos+guest+house/data=!4m11!3m10!1s0x14de1747489ee4e1:0xcaba5a75a71d84f9!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.1802194!4d33.3647633!16s%2Fg%2F11fxb65g4_!19sChIJ4eSeSEcX3hQR-YQdp3Vauso?authuser=0&hl=en&rclk=1",
    latitude: "35.1802194",
    longitude: "33.3647633",
  },
  {
    name: "Modern and cosy one bedroom apartment",
    category: "hotel",
    image_url:
      "https://lh3.googleusercontent.com/gps-proxy/ALd4DhHbtxNDfb73fJpbqrcMsUkWPKbZmCOPt-c3RFIiHKy-t7eF55VlkFku7M9-pe386JvYbbEp8BVzn2Sz1WeayPn3f4S3c75W0k88X9-i8P1WW5tE2tfufgT7NUe3FEnW8HmpThH29TDzGkhPDXv_iC9ITOqsrwUm-UBXJYLH4rSMxIhRD4j5EOp7=w163-h92-k-no",
    href: "https://www.google.com/maps/place/Modern+and+cosy+one+bedroom+apartment/data=!4m11!3m10!1s0x14de1b3b6e03892b:0xfd592f38cc283631!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.1721569!4d33.3296241!16s%2Fg%2F11gr4hgjk7!19sChIJK4kDbjsb3hQRMTYozDgvWf0?authuser=0&hl=en&rclk=1",
    latitude: "35.1721569",
    longitude: "33.3296241",
  },
  {
    name: "Mr. Studio",
    category: "hotel",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipNbLr51gnYyaavBZHddMdOAtUSzrBEE_VV_vfLs=w163-h92-k-no",
    href: "https://www.google.com/maps/place/Mr.+Studio/data=!4m11!3m10!1s0x14de1109f95deb45:0x7d4cd727ef3a25d7!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.1984866!4d33.3337435!16s%2Fg%2F11nghtchlx!19sChIJRetd-QkR3hQR1yU67yfXTH0?authuser=0&hl=en&rclk=1",
    latitude: "35.1984866",
    longitude: "33.3337435",
  },
  {
    name: "Executive Suites",
    category: "hotel",
    image_url:
      "https://lh3.googleusercontent.com/gps-proxy/ALd4DhGxpvUjh2rOruZlmSWnUGTXTW7JArkJt35M-m-cmLyUfgnRJwvp6G84MFDJNyvrKjqc_Vr88ar6ZR2tAhZELAZuqcUChtZDWhfGCtuQGu4s-FJBBG5po4QtExMCaEul9Ob7AVot0vqrsgpPz0XqixNny6EjkAE9i5W7Txt91T-W0P4j15LjtWc-=w122-h92-k-no",
    href: "https://www.google.com/maps/place/Executive+Suites/data=!4m11!3m10!1s0x14de10aea16eeb8b:0xf2d8299a87b667cc!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.1743734!4d33.3426087!16s%2Fg%2F12hmmjtbz!19sChIJi-tuoa4Q3hQRzGe2h5op2PI?authuser=0&hl=en&rclk=1",
    latitude: "35.1743734",
    longitude: "33.3426087",
  },
  {
    name: "55-1 Apartments",
    category: "hotel",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipM2LMTVywynjk2SkoddLarVfT3xtgeLscUpw4NZ=w122-h92-k-no",
    href: "https://www.google.com/maps/place/55-1+Apartments/data=!4m11!3m10!1s0x14de11387be3df29:0x18bb7c615f908703!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.197598!4d33.337425!16s%2Fg%2F11h0z9cybs!19sChIJKd_jezgR3hQRA4eQX2F8uxg?authuser=0&hl=en&rclk=1",
    latitude: "35.197598",
    longitude: "33.337425",
  },
  {
    name: "Suleyman Seba Apt",
    category: "hotel",
    image_url: "//maps.gstatic.com/tactile/pane/result-no-thumbnail-2x.png",
    href: "https://www.google.com/maps/place/Suleyman+Seba+Apt/data=!4m11!3m10!1s0x14de11b646c3b78f:0x52396cbac8e6819c!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.2008936!4d33.328381!16s%2Fg%2F11j0vxq9gj!19sChIJj7fDRrYR3hQRnIHmyLpsOVI?authuser=0&hl=en&rclk=1",
    latitude: "35.2008936",
    longitude: "33.328381",
  },
  {
    name: "Nicosia",
    category: "hotel",
    image_url: "//maps.gstatic.com/tactile/pane/result-no-thumbnail-2x.png",
    href: "https://www.google.com/maps/place/Nicosia/data=!4m11!3m10!1s0x14de17de06b07661:0x280a3cbf5f20ed2c!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.1859457!4d33.3852377!16s%2Fg%2F11sthy_djs!19sChIJYXawBt4X3hQRLO0gX788Cig?authuser=0&hl=en&rclk=1",
    latitude: "35.1859457",
    longitude: "33.3852377",
  },
  {
    name: "Amber's House",
    category: "hotel",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipN02UPHzYMYBnSo2oMbBdeY-9JfVPIWe3Wf_ZTH=w138-h92-k-no",
    href: "https://www.google.com/maps/place/Amber%27s+House/data=!4m11!3m10!1s0x14de17217cf97897:0xec71e3949fddbefb!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.195194!4d33.3675752!16s%2Fg%2F11fjx385ny!19sChIJl3j5fCEX3hQR-77dn5Tjcew?authuser=0&hl=en&rclk=1",
    latitude: "35.195194",
    longitude: "33.3675752",
  },
  {
    name: "3 Rooms Boutique Hotel",
    category: "hotel",
    image_url:
      "https://lh3.googleusercontent.com/gps-proxy/ALd4DhHrb8LHZKiuvM4P4akYoDLQbtuOMvqEMjzPCRX4S850eCKKGKNtStSYGEBp52wqrtSEVRJ_Ld3_d-xEGJa5tx5hwF_7QFOyNWvBKLANawwdhN-QiVnyGLzXXj4c72VveuvDcDkLIqlEDp3FiVdqZNCdxlxFAPc_pdR5N3YHLl1OuQ5nz_I5Vx30=w80-h106-k-no",
    href: "https://www.google.com/maps/place/3+Rooms+Boutique+Hotel/data=!4m11!3m10!1s0x14de1726eeab5707:0x8b0ad037ed6e3041!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.1711282!4d33.3611115!16s%2Fg%2F11f5vdf0t0!19sChIJB1er7iYX3hQRQTBu7TfQCos?authuser=0&hl=en&rclk=1",
    latitude: "35.1711282",
    longitude: "33.3611115",
  },
  {
    name: "Palm Garden Guest House lefkosa turk Republic of north\n                      cyprus",
    category: "hotel",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipNQtiXuHd50Jp0LaLObcoP9F45dcOxOsVRP8TOu=w138-h92-k-no",
    href: "https://www.google.com/maps/place/Palm+Garden+Guest+House+lefkosa+turk+Republic+of+north+cyprus/data=!4m11!3m10!1s0x14de170f0688f051:0xc06ea32e27f01839!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.1788493!4d33.3675641!16s%2Fg%2F11fl2l20sj!19sChIJUfCIBg8X3hQRORjwJy6jbsA?authuser=0&hl=en&rclk=1",
    latitude: "35.1788493",
    longitude: "33.3675641",
  },
  {
    name: "22 Twenty Two",
    category: "hotel",
    image_url:
      "https://lh5.googleusercontent.com/p/AF1QipMcmI6dOarB79VI9Gq5mKRGegI-w8bbVBH9Mt63=w122-h92-k-no",
    href: "https://www.google.com/maps/place/22+Twenty+Two/data=!4m11!3m10!1s0x14de174697af0b7d:0xe3f85c5f0bd8d4f5!5m3!1s2024-05-30!4m1!1i2!8m2!3d35.1773301!4d33.3639007!16s%2Fg%2F11jn_sw3qv!19sChIJfQuvl0YX3hQR9dTYC19c-OM?authuser=0&hl=en&rclk=1",
    latitude: "35.1773301",
    longitude: "33.3639007",
  },
];
module.exports = hotels;
