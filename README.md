# Year in Review

This document provides just some raw information about 2024 in cards. Some more written form analysis can be found in the dispatch.

Go to section

- [A Brief Comparison with 2024 and 2023](#a-brief-comparison-with-2024-and-2023)
  - [2024](#2024)
  - [2023](#2023)
  - [Useless Insights](#useless-insights)
- [More Into 2024 Numbers](#more-into-2024-numbers)
  - [Rarities](#2024-rarities)
  - [Seasons](#2024-by-season)
  - [Rarities and Seasons](#2024-by-both-rarity-and-season)
- [Trades](#trades)
  - [Top Trades](#top-trades-of-the-year)
  - By Rarity
    - [Common](#top-common-trades-of-the-year)
    - [Uncommon](#top-uncommon-trades-of-the-year)
    - [Rare](#top-rare-trades-of-the-year)
    - [Ultra Rare](#top-ultra-rare-trades-of-the-year)
    - [Epic](#top-epic-trades-of-the-year)
    - [Legendary](#top-legendary-trades-of-the-year)
      - [S1](#top-s1-legendary-trades-of-the-year)
  - [Specific Cards](#individual-cards)
    - [Most Moved Card](#most-moved-cards)
    - [Most Bank](#most-money-moved-per-card)
    - [Most Traded Legendary ( > 0 )](#most-traded-legendary)
    - [Most Bank Moved By Legendary](#most-bank-moved-by-legendary)
- [Traders](#buyers-and-sellers)
  - [Bank Movement](#bank-movers)
    - [Most Bank Moved](#most-bank-moved)
      - [As Buyer](#most-bank-moved-as-buyer)
      - [As Seller](#most-bank-moved-as-seller)
    - [Trade Count](#trade-count)
      - [Most Active Trader](#most-active-traders)
      - [Most Active Trader ( > 0 )](#most-active-traders-non-gift-non-zero)
      - [Most Active Buyers](#most-cards-bought)
      - [Most Active Buyers ( > 0 )](#most-cards-bought-for-more-than-zero)
      - [Most Active Sellers](#most-cards-sold)
      - [Most Active Sellers ( > 0 )](#most-cards-sold-for-more-than-zero)
      - [Most Gifts](#most-cards-gifted)
      - [Most Cards Bought at 250+](#most-cards-bought-250)
      - [Most Cards Sold at 250+](#most-cards-sold-250)
    - [Buyers By Season](#buyers-by-season)
      - [S1](#season-1)
      - [S1 ( > 0 )](#season-1-non-zero)
      - [S2](#season-2)
      - [S2 ( > 0 )](#season-2-non-zero)
      - [S3](#season-3)
      - [S3 ( > 0 )](#season-3-non-zero)
    - [Buyers By Rarity ( > 0 )](#buyers-by-rarity-non-zero)
      - [Common](#common)
      - [Uncommon](#uncommon)
      - [Rare](#rare-1)
      - [Ultra Rare](#ultra-rare-1)
      - [Epic](#epic-1)
      - Legendaries
        - [Legendaries](#legendaries-bought)
        - [Legendaries ( > 0 )](#legendaries-bought-non-zero)
        - [Legendaries Gifted](#legendaries-gifted)
        - [Legendaries Received](#legendaries-received)
- [Temporal Stuff](#time-breakdown)
  - Year in Halves
    - [Jan-July](#first-half-of-the-year)
      - [As Buyer](#most-bank-moved-as-buyer)
      - [As Seller](#most-bank-moved-as-seller)
      - [Most Active Buyers](#most-cards-bought-1)
      - [Most Active Buyers ( > 0 )](#most-cards-bought-non-zero)
      - [Most Active Sellers](#most-cards-sold-1)
      - [Most Active Sellers ( > 0 )](#most-cards-sold-non-zero)
    - [July-Jan 2024](#last-half-of-the-year)
      - [As Buyer](#most-bank-moved-as-buyer-1)
      - [As Seller](#most-bank-moved-as-seller-1)
      - [Most Active Buyers](#most-cards-bought-2)
      - [Most Active Buyers ( > 0 )](#most-cards-bought-non-zero-1)
      - [Most Active Sellers](#most-cards-sold-2)
      - [Most Active Sellers ( > 0 )](#most-cards-sold-non-zero-1)
  - [Hours, Days, Months](#hours-days-months)
    - [Most Active Day](#most-active-day)
    - [Hours of the Day](#hour-of-the-day)
    - [Days of the Week](#day-of-the-week)
    - [Months of the Year](#month-of-the-year)
  - [Cards, Traders](#cards-traders)
    - [Top Traders Per Month](#traders-per-month-non-zero)
    - [Most Bank Moved Per Month](#most-bank-moved-per-month)
    - [Unique Cards Sold Per Month](#number-of-unique-cards-traded-each-month)
    - [Top 3 Legendaries By Bank Per Month](#top-3-legendaries-by-bank-each-month)

## A Brief Comparison with 2024 and 2023:

### 2024

- Total Trades: `2,457,636`
- Total Trades Excluding Gifts: `1,028,833` (41.9%)
- Average Bank Per Non Gift Trade: `3.61`
- Total Bank Moved: `3,716,289.74`
- Unique Buyers: `81,490`
- Unique Sellers: `121,834`
- Unique Participants: `134,450`
- Trades with over 250 bank: `1118`
- Trades with over 500 bank: `467`

### 2023:

- Total Trades: `2,494,954`
- Total Trades Excluding Gifts: `1,140,962` (45.7%)
- Average Bank Per Non Gift Trade: `2.73`
- Total Bank Moved: `3,120,024`
- Unique Buyers: `72,149`
- Unique Sellers: `116,028`
- Unique Participants: `126,671`
- Trades with over 250 bank: `739`
- Trades with over 500 bank: `200`

## More Into 2024 Numbers

The following will be a lot of numbers, a lot of sql queries, and potentially a lot of mistakes.

### 2024 Rarities

The below chart details a breakdown of the movement of rarities on the market during 2024.

|                | Trades Involved In | Non-Gift Trades | Average Price (!0) | Bank Moved |
| -------------- | ------------------ | --------------- | ------------------ | ---------- |
| **Common**     | 1,297,316          | 562,746         | 2.61               | 1,469,787  |
| **Uncommon**   | 410,977            | 181,332         | 1.34               | 242,409    |
| **Rare**       | 211,740            | 88,675          | 2.94               | 261,051    |
| **Ultra-Rare** | 230,743            | 89,801          | 2.56               | 229,936    |
| **Epic**       | 217,057            | 90,578          | 3.30               | 298,622    |
| **Legendary**  | 89,803             | 15,701          | 77.35              | 1,214,485  |

### 2024 By Season

The below chart details a breakdown of the movement of each season on the market during 2024.

|        | Trades Involved In | Non-Gift Trades | Average Price (!0) | Bank Moved |
| ------ | ------------------ | --------------- | ------------------ | ---------- |
| **S1** | 135,452            | 56,385          | 10.58              | 596,406    |
| **S2** | 234,980            | 103,498         | 7.65               | 791,639    |
| **S3** | 2,087,204          | 868,950         | 2.68               | 2,328,244  |

### 2024 By Both Rarity and Season

The below chart details per season, a breakdown of each card rarity's movement on the market during 2023.

#### Commons

|        | Trades Involved In | Non-Gift Trades | Average Price (!0) | Bank Moved |
| ------ | ------------------ | --------------- | ------------------ | ---------- |
| **S1** | 88,653             | 36,319          | 7.70               | 279,674    |
| **S2** | 155,170            | 67,937          | 7.05               | 479,122    |
| **S3** | 1,053,493          | 458,490         | 1.55               | 710,991    |

#### Uncommons

|        | Trades Involved In | Non-Gift Trades | Average Price (!0) | Bank Moved |
| ------ | ------------------ | --------------- | ------------------ | ---------- |
| **S1** | 24,669             | 10,297          | 2.00               | 20,565     |
| **S2** | 31,962             | 13,381          | 5.64               | 75,482     |
| **S3** | 354,346            | 157,654         | 0.93               | 146,361    |

#### Rare

|        | Trades Involved In | Non-Gift Trades | Average Price (!0) | Bank Moved |
| ------ | ------------------ | --------------- | ------------------ | ---------- |
| **S1** | 8,422              | 3,521           | 1.28               | 4,510      |
| **S2** | 10,151             | 5,724           | 2.18               | 12,495     |
| **S3** | 193,167            | 79,430          | 3.07               | 244,046    |

#### Ultra Rare

|        | Trades Involved In | Non-Gift Trades | Average Price (!0) | Bank Moved |
| ------ | ------------------ | --------------- | ------------------ | ---------- |
| **S1** | 6,547              | 3,209           | 5.00               | 16,030     |
| **S2** | 24,134             | 10,572          | 5.24               | 55,361     |
| **S3** | 200,062            | 76,020          | 2.09               | 158,544    |

#### Epic

|        | Trades Involved In | Non-Gift Trades | Average Price (!0) | Bank Moved |
| ------ | ------------------ | --------------- | ------------------ | ---------- |
| **S1** | 5,153              | 2,514           | 35.68              | 89,706     |
| **S2** | 7,652              | 4,434           | 8.65               | 38,373     |
| **S3** | 204,252            | 83,630          | 2.04               | 170,545    |

#### Legendary

|        | Trades Involved In | Non-Gift Trades | Average Price (!0) | Bank Moved |
| ------ | ------------------ | --------------- | ------------------ | ---------- |
| **S1** | 2,008              | 525             | 354                | 185,922    |
| **S2** | 5,911              | 1,450           | 90.2               | 130,806    |
| **S3** | 81,884             | 13,726          | 65.4               | 897,757    |

## Trades

The below chart details per season, a breakdown of each card rarity's movement on the market during 2023.

### Top Trades of the Year

Here's a similar markdown table based on the provided data:

| Rank | Seller   | Buyer          | Price   | Card                                           | Date       |
| ---- | -------- | -------------- | ------- | ---------------------------------------------- | ---------- |
| 1    | Kractero | Rain Delay     | 10000.0 | Season 1 Epic 9003                             | 2024-04-13 |
| 2    | 9006     | Hujen          | 10000.0 | Season 1 Epic 9003                             | 2024-04-13 |
| 3    | 9006     | 9003           | 10000.0 | Season 1 Common Ooga boogag                    | 2024-02-22 |
| 4    | 9006     | 9003           | 10000.0 | Season 1 Common Trongistan14                   | 2024-02-19 |
| 5    | 9006     | 9003           | 10000.0 | Season 1 Common Liberty Republicans            | 2024-02-11 |
| 6    | 9006     | 9007           | 10000.0 | Season 1 Epic 9003                             | 2024-07-27 |
| 7    | Osheiga  | Valoptia       | 10000.0 | Season 3 Legendary Annihilators of Chan Island | 2024-08-05 |
| 8    | Valoptia | Mustard Gasses | 10000.0 | Season 3 Legendary Annihilators of Chan Island | 2024-11-15 |
| 9    | 9007     | South Zealande | 9999.0  | Season 1 Epic 9003                             | 2024-08-30 |
| 10   | Valoptia | Elista Rus     | 9001.0  | Season 3 Legendary Annihilators of Chan Island | 2024-08-05 |

### Top Common Trades of the Year

| Rank | Seller             | Buyer         | Price   | Card                             | Date       |
| ---- | ------------------ | ------------- | ------- | -------------------------------- | ---------- |
| 1    | 9003               | 9006          | 10000.0 | Season 1 Ooga boogag             | 2024-02-22 |
| 2    | 9003               | 9006          | 10000.0 | Season 1 Trongistan14            | 2024-02-19 |
| 3    | 9003               | 9006          | 10000.0 | Season 1 Liberty Republicans     | 2024-02-11 |
| 4    | New Kowloon Bay    | Upper Tuchoim | 1400.0  | Season 1 Commie Aussies          | 2024-11-10 |
| 5    | Angel Beats1       | Avrelis       | 1250.0  | Season 3 Arlecchino              | 2024-06-06 |
| 6    | Portugal is Great  | Conexia       | 1250.0  | Season 1 Shakandia               | 2024-12-10 |
| 7    | The Realizer       | Avrelis       | 1168.5  | Season 3 Arlecchino              | 2024-06-06 |
| 8    | AFN44              | Glastol       | 1000.0  | Season 2 Margaret Hilda Thatcher | 2024-09-03 |
| 9    | Empire of Caldrasa | Smallboy3     | 998.5   | Season 2 Tsum Tsum Island        | 2024-11-25 |
| 10   | Empire of Caldrasa | Smallboy2     | 998.5   | Season 2 Tsum Tsum Island        | 2024-11-25 |

### Top Uncommon Trades of the Year

| Rank | Seller               | Buyer              | Price  | Card               | Date       |
| ---- | -------------------- | ------------------ | ------ | ------------------ | ---------- |
| 1    | -0-                  | Panagouge          | 3000.0 | Season 2 Panagouge | 2024-04-07 |
| 2    | Vylixan Dora         | Varanius           | 1000.0 | Season 2 Varanius  | 2024-08-15 |
| 3    | Le Libertia          | Varanius           | 1000.0 | Season 2 Varanius  | 2024-11-27 |
| 4    | Cal-Card-Farming-003 | Empire of Caldrasa | 554.45 | Season 3 Lloenflys | 2024-11-08 |
| 5    | Cal-Card-Farming-000 | Empire of Caldrasa | 554.45 | Season 3 Lloenflys | 2024-11-08 |
| 6    | Cal-Card-Farming-001 | Empire of Caldrasa | 554.45 | Season 3 Lloenflys | 2024-11-08 |
| 7    | Cal-Card-Farming-004 | Empire of Caldrasa | 554.45 | Season 3 Lloenflys | 2024-11-08 |
| 8    | Cal-Card-Farming-005 | Empire of Caldrasa | 554.45 | Season 3 Lloenflys | 2024-11-08 |
| 9    | Cal-Card-Farming-002 | Empire of Caldrasa | 554.45 | Season 3 Lloenflys | 2024-11-08 |
| 10   | Cal-Card-Farming-006 | Empire of Caldrasa | 554.45 | Season 3 Lloenflys | 2024-11-08 |

### Top Rare Trades of the Year

Here’s the markdown table for the provided data:

| Rank | Seller          | Buyer         | Price   | Card                                | Date       |
| ---- | --------------- | ------------- | ------- | ----------------------------------- | ---------- |
| 1    | Bigboy2         | Upper Tuchoim | 1387.78 | Season 3 The Greater Bosnian Empire | 2024-07-07 |
| 2    | Bigboy7         | Upper Tuchoim | 1387.78 | Season 3 The Greater Bosnian Empire | 2024-07-07 |
| 3    | Bigboy6         | Upper Tuchoim | 1387.78 | Season 3 The Greater Bosnian Empire | 2024-07-07 |
| 4    | Bigboy5         | Upper Tuchoim | 1387.78 | Season 3 The Greater Bosnian Empire | 2024-07-07 |
| 5    | Bigboy4         | Upper Tuchoim | 1387.78 | Season 3 The Greater Bosnian Empire | 2024-07-07 |
| 6    | Bigboy3         | Upper Tuchoim | 1387.78 | Season 3 The Greater Bosnian Empire | 2024-07-07 |
| 7    | Bigboy1         | Upper Tuchoim | 1387.78 | Season 3 The Greater Bosnian Empire | 2024-07-07 |
| 8    | War Dogs Cdxlix | War Dogs IV   | 1270.0  | Season 3 The Greater Bosnian Empire | 2024-11-14 |
| 9    | Upper Tuchoim   | Bigboy6       | 1250.0  | Season 3 The Greater Bosnian Empire | 2024-07-07 |
| 10   | Upper Tuchoim   | Bigboy7       | 1250.0  | Season 3 The Greater Bosnian Empire | 2024-07-07 |

### Top Ultra Rare Trades of the Year

Here’s the markdown table for the provided data:

| Rank | Seller                      | Buyer                       | Price | Card                   | Date       |
| ---- | --------------------------- | --------------------------- | ----- | ---------------------- | ---------- |
| 1    | an_actual_hurricane         | Refuge Isle                 | 868.0 | Season 2 Lower Holland | 2024-04-07 |
| 2    | xink_cards                  | Brexas7                     | 632.0 | Season 1 Brexas        | 2024-07-08 |
| 3    | Vulxo                       | Brexas7                     | 600.0 | Season 1 Brexas        | 2024-09-23 |
| 4    | I Love Juice                | Thelandoffunfunfun          | 400.0 | Season 3 Meadowfields  | 2024-06-15 |
| 5    | Landoffunpuppet32           | Thelandoffunfunfun          | 400.0 | Season 3 Meadowfields  | 2024-06-15 |
| 6    | Angry Fun                   | Thelandoffunfunfun          | 400.0 | Season 3 Meadowfields  | 2024-06-15 |
| 7    | Colourful Bright Blue Blobs | Thelandoffunfunfun          | 400.0 | Season 3 Meadowfields  | 2024-06-15 |
| 8    | Thelandoffunfunfun          | Colourful Bright Blue Blobs | 400.0 | Season 3 Meadowfields  | 2024-06-16 |
| 9    | Thelandoffunfunfun          | I Love Juice                | 400.0 | Season 3 Meadowfields  | 2024-06-16 |
| 10   | Thelandoffunfunfun          | Landoffunpuppet32           | 400.0 | Season 3 Meadowfields  | 2024-06-16 |

### Top Epic Trades of the Year

| Rank | Seller               | Buyer         | Price   | Card              | Date       |
| ---- | -------------------- | ------------- | ------- | ----------------- | ---------- |
| 1    | Rain Delay           | Kractero      | 10000.0 | Season 1 9003     | 2024-04-13 |
| 2    | Hujen                | 9006          | 10000.0 | Season 1 9003     | 2024-04-13 |
| 3    | 9007                 | 9006          | 10000.0 | Season 1 9003     | 2024-07-27 |
| 4    | South Zealande       | 9007          | 9999.0  | Season 1 9003     | 2024-08-30 |
| 5    | Feu De Glace         | 9006          | 5000.0  | Season 1 9003     | 2024-08-07 |
| 6    | Eugeniee             | 9006          | 5000.0  | Season 1 9003     | 2024-08-08 |
| 7    | Feu De Glace         | 9006          | 4000.0  | Season 1 9003     | 2024-09-15 |
| 8    | Feu De Glace         | Eugeniee      | 3000.0  | Season 1 9003     | 2024-07-30 |
| 9    | The Sigometh Dynasty | 9006          | 2937.5  | Season 1 9003     | 2024-07-29 |
| 10   | Bigboy1              | Upper Tuchoim | 1110.0  | Season 3 Fauzjhia | 2024-09-29 |

### Top Legendary Trades of the Year

| Rank | Seller         | Buyer       | Price   | Card                                 | Date       |
| ---- | -------------- | ----------- | ------- | ------------------------------------ | ---------- |
| 1    | Valoptia       | Osheiga     | 10000.0 | Season 3 Annihilators of Chan Island | 2024-08-05 |
| 2    | Mustard Gasses | Valoptia    | 10000.0 | Season 3 Annihilators of Chan Island | 2024-11-15 |
| 3    | Elista Rus     | Valoptia    | 9001.0  | Season 3 Annihilators of Chan Island | 2024-08-05 |
| 4    | Valoprawr      | Elista Rus  | 8101.9  | Season 3 Annihilators of Chan Island | 2024-08-05 |
| 5    | Osheiga        | Valoprawr   | 7291.71 | Season 3 Annihilators of Chan Island | 2024-08-05 |
| 6    | Triseria       | Dr Hooves   | 6500.0  | Season 3 Annihilators of Chan Island | 2024-12-08 |
| 7    | Yzyland        | War Dogs IV | 6200.0  | Season 3 Annihilators of Chan Island | 2024-12-13 |
| 8    | Dapant         | Kractero    | 5000.0  | Season 3 Chan Island                 | 2024-06-03 |
| 9    | Giraffeton     | Kakastania  | 5000.0  | Season 3 Morover                     | 2024-06-05 |
| 10   | Avrelis        | Varanius    | 5000.0  | Season 3 Annihilators of Chan Island | 2024-10-27 |

### Top S1 Legendary Trades of the Year

| Rank | Seller               | Buyer                | Price   | Card                                 | Date       |
| ---- | -------------------- | -------------------- | ------- | ------------------------------------ | ---------- |
| 1    | Empire of Caldrasa   | Empire of Caldrasa   | 3500.01 | Season 1 Soops                       | 2024-11-15 |
| 2    | Geidi Centauri Prime | Mustard Gasses       | 2798.5  | Season 1 Annihilators of Chan Island | 2024-11-16 |
| 3    | 9006                 | Waterfall State      | 2749.99 | Season 1 Soops                       | 2024-07-31 |
| 4    | Refuge Isle          | 9006                 | 1600.0  | Season 1 Soops                       | 2024-07-31 |
| 5    | Refuge Isle          | Kractero             | 1500.0  | Season 1 Soops                       | 2024-01-23 |
| 6    | Shibutani            | Parenthos            | 1500.0  | Season 1 Testlandia                  | 2024-11-04 |
| 7    | Shibutani            | New Kowloon Bay      | 1500.0  | Season 1 Testlandia                  | 2024-12-15 |
| 8    | Hujen                | Rain Delay           | 1350.0  | Season 1 Testlandia                  | 2024-05-12 |
| 9    | Aerilia              | Kractero             | 1250.0  | Season 1 Bothia                      | 2024-09-28 |
| 10   | Xoriet               | Darklight Girl Sarah | 1250.0  | Season 1 Crazy Girl                  | 2024-11-24 |

### Top S2 Legendary Trades of the Year

| Rank | Seller         | Buyer           | Price   | Card                                 | Date       |
| ---- | -------------- | --------------- | ------- | ------------------------------------ | ---------- |
| 1    | Frisbeeteria   | Pumpty Dumpty   | 1234.56 | Season 2 S_diego                     | 2024-04-09 |
| 2    | Hasonia        | Kractero        | 1234.0  | Season 2 S_diego                     | 2024-11-07 |
| 3    | Conexia        | Valoptia        | 1222.0  | Season 2 S_diego                     | 2024-09-23 |
| 4    | Seanat         | Mustard Gasses  | 1180.0  | Season 2 Annihilators of Chan Island | 2024-11-16 |
| 5    | Conexia        | Pumpty Dumpty   | 1069.0  | Season 2 S_diego                     | 2024-04-09 |
| 6    | Tordek Redfist | Pumpty Dumpty   | 750.0   | Season 2 S_diego                     | 2024-04-09 |
| 7    | Pygania        | Conexia         | 650.0   | Season 2 S_diego                     | 2024-05-11 |
| 8    | Benevolent 1   | Melenavenia     | 600.0   | Season 2 Carrasastova                | 2024-02-27 |
| 9    | Conexia        | Waterfall State | 600.0   | Season 2 Nova Hollandia              | 2024-02-07 |
| 10   | Fhaengshia     | Avrelis         | 600.0   | Season 2 Holy Oranz                  | 2024-10-27 |

### Individual Cards

#### Most Moved Cards

| Rank | Card                | Trade Count |
| ---- | ------------------- | ----------- |
| 1    | Autistria           | 14143       |
| 2    | -ii                 | 12553       |
| 3    | El Alto Parana      | 11918       |
| 4    | Pittsburgh Penguins | 11120       |
| 5    | 9003                | 8817        |
| 6    | Valoptia            | 6317        |
| 7    | Youm                | 4981        |
| 8    | Holy Communion      | 4532        |
| 9    | Doctor Mad          | 4339        |
| 10   | Taelenstrom         | 4180        |

#### Most Bank Moved Per Card

| Rank | Card                        | Bank Moved | Transfer Count |
| ---- | --------------------------- | ---------- | -------------- |
| 1    | 9003                        | 59,936.50  | 23             |
| 2    | -ii                         | 62,761.01  | 12,553         |
| 3    | Autistria                   | 69,811.16  | 14,143         |
| 4    | Annihilators of Chan Island | 65,594.61  | 42             |
| 5    | Pittsburgh Penguins         | 55,519.51  | 11,120         |
| 6    | 9003 (UR)                   | 44,227.83  | 8,817          |
| 7    | Upper Tuchoim               | 62,157.09  | 485            |
| 8    | New Visayan Islands         | 34,375.96  | 583            |
| 9    | Valoptia                    | 34,218.75  | 6,317          |
| 10   | Youm                        | 24,038.79  | 4,981          |

### Most Traded Legendary

| Rank | Card Name              | Trades |
| ---- | ---------------------- | ------ |
| 1    | S3 Valkalan            | 154    |
| 2    | S3 Topid               | 103    |
| 3    | S3 The-CID             | 102    |
| 4    | S3 Imperium Anglorum   | 93     |
| 5    | S3 Ethnon              | 92     |
| 6    | S3 Ko-oren             | 92     |
| 7    | S3 Zurkerx             | 92     |
| 8    | S3 SalusaSecondus      | 91     |
| 9    | S3 The Archregimancy   | 91     |
| 10   | S3 New Visayan Islands | 90     |

#### Most Bank Moved By Legendary

| Rank | Card Name                   | Bank Moved |
| ---- | --------------------------- | ---------- |
| 1    | Annihilators of Chan Island | 65594.61   |
| 2    | New Visayan Islands         | 34375.96   |
| 3    | Crazy girl                  | 24001.49   |
| 4    | Chan Island                 | 19478.5    |
| 5    | Noahs Second Country        | 17901.66   |
| 6    | Safj                        | 17771.79   |
| 7    | Giovanniland                | 17570.68   |
| 8    | Racoda                      | 15110.49   |
| 9    | The Stalker                 | 14047.86   |
| 10   | Sedgistan                   | 13614.18   |

## Buyers and Sellers

This next section will focus on the players of the game: those that bought and sold cards.

### Bank Movers

#### Most Bank Moved

| Rank | Trader               | Total Bank Moved |
| ---- | -------------------- | ---------------- |
| 1    | Noahs Second Country | 206357.67        |
| 2    | Koem Kab             | 197967.06        |
| 3    | Mikeswill            | 149162.26        |
| 4    | Upper Tuchoim        | 145393.7         |
| 5    | Kractero             | 136169.07        |
| 6    | Valoptia             | 125648.82        |
| 7    | 9006                 | 115150.93        |
| 8    | Osheiga              | 106965.14        |
| 9    | Varanius             | 105223.43        |
| 10   | Giovanniland         | 81752.37         |

#### Bank Moved as buyer

| Rank | Trader             | Total Bank Spent |
| ---- | ------------------ | ---------------- |
| 1    | Kractero           | 120,153.33       |
| 2    | Upper Tuchoim      | 112,380.38       |
| 3    | Valoptia           | 96,486.26        |
| 4    | 9006               | 74,488.43        |
| 5    | Koem Kab           | 68,679.56        |
| 6    | Varanius           | 63,913.26        |
| 7    | Fauzjhia           | 63,597.96        |
| 8    | Giovanniland       | 46,357.03        |
| 9    | Osheiga            | 43,410.93        |
| 10   | Empire of Caldrasa | 42,876.62        |

#### Bank Moved as seller

| Rank | Trader               | Total Bank Sold |
| ---- | -------------------- | --------------- |
| 1    | Noahs Second Country | 133,290.39      |
| 2    | Mikeswill            | 110,912.58      |
| 3    | Koem Kab             | 91,240.73       |
| 4    | Osheiga              | 69,611.67       |
| 5    | Seanat               | 58,217.86       |
| 6    | Varanius             | 55,032.30       |
| 7    | Fauzjhia             | 44,385.62       |
| 8    | Giovanniland         | 44,143.87       |
| 9    | 9006                 | 42,169.43       |
| 10   | Thorn1000            | 37,520.27       |

### Trade Count

#### Most Active Traders

| Rank | Trader                | Trade Count |
| ---- | --------------------- | ----------- |
| 1    | War Dogs IV           | 259,388     |
| 2    | The Colonial Buccaruu | 78,958      |
| 3    | Mikeswill             | 41,365      |
| 4    | Communist-Denmark     | 38,618      |
| 5    | Kractero              | 34,453      |
| 6    | Koem Kab              | 30,532      |
| 7    | Varanius              | 30,448      |
| 8    | Yodle                 | 29,418      |
| 9    | Anarco Argentina      | 27,710      |
| 10   | Noahs Second Country  | 27,302      |

#### Most Active Traders Non-Zero

| Rank | Trader                               | Trade Count |
| ---- | ------------------------------------ | ----------- |
| 1    | War Dogs IV                          | 60,653      |
| 2    | Midlands                             | 25,423      |
| 3    | Il Sonno Della Ragione Genera Mostri | 22,376      |
| 4    | Card Cleaver                         | 20,255      |
| 5    | Communist-Denmark                    | 19,872      |
| 6    | Anarco Argentina                     | 19,784      |
| 7    | Mikeswill                            | 17,980      |
| 8    | Giovanniland                         | 16,455      |
| 9    | Kractero                             | 14,603      |
| 10   | Yodle                                | 14,468      |

#### Most Cards Bought

| Rank | Trader                | Cards Bought |
| ---- | --------------------- | ------------ |
| 1    | War Dogs IV           | 199,763      |
| 2    | The Colonial Buccaruu | 70,165       |
| 3    | Communist-Denmark     | 32,394       |
| 4    | Mikeswill             | 31,090       |
| 5    | Varanius              | 24,328       |
| 6    | Giovanniland          | 22,967       |
| 7    | Card Cleaver          | 20,267       |
| 8    | Kractero              | 20,139       |
| 9    | Yodle                 | 19,442       |
| 10   | Koem Kab              | 19,239       |

#### Most Cards Bought For More Than Zero

| Rank | Trader                               | Cards Bought > 0 |
| ---- | ------------------------------------ | ---------------- |
| 1    | Card Cleaver                         | 20,221           |
| 2    | Anarco Argentina                     | 18,074           |
| 3    | War Dogs IV                          | 15,508           |
| 4    | Il Sonno Della Ragione Genera Mostri | 15,183           |
| 5    | Giovanniland                         | 14,923           |
| 6    | Communist-Denmark                    | 14,874           |
| 7    | Midlands                             | 14,652           |
| 8    | Yodle                                | 13,950           |
| 9    | Mikeswill                            | 12,412           |
| 10   | Giraffeton                           | 11,396           |

#### Most Cards Sold

| Rank | Trader               | Cards Sold |
| ---- | -------------------- | ---------- |
| 1    | War Dogs IV          | 59,625     |
| 2    | Kractero             | 14,314     |
| 3    | Noahs Second Country | 11,522     |
| 4    | Koem Kab             | 11,293     |
| 5    | Midlands             | 10,780     |
| 6    | Mikeswill            | 10,275     |
| 7    | Fauzjhia             | 10,184     |
| 8    | Yodle                | 9,976      |
| 9    | 9006                 | 9,713      |
| 10   | Anarco Argentina     | 8,929      |

#### Most Cards Sold For More Than Zero

| Rank | Trader                               | Cards Sold > 0 |
| ---- | ------------------------------------ | -------------- |
| 1    | War Dogs IV                          | 45,145         |
| 2    | Kractero                             | 12,362         |
| 3    | Noahs Second Country                 | 11,499         |
| 4    | Koem Kab                             | 11,292         |
| 5    | Midlands                             | 10,771         |
| 6    | Upper Tuchoim                        | 8,216          |
| 7    | The Colonial Buccaruu                | 7,355          |
| 8    | Il Sonno Della Ragione Genera Mostri | 7,193          |
| 9    | New Makasta                          | 5,972          |
| 10   | Valoptia                             | 5,679          |

#### Most Cards Gifted

| Rank | Trader              | Cards Gifted |
| ---- | ------------------- | ------------ |
| 1    | War Dogs IV         | 14,480       |
| 2    | Yodle               | 9,458        |
| 3    | Fauzjhia            | 8,112        |
| 4    | Anarco Argentina    | 7,219        |
| 5    | Lake Floria         | 7,135        |
| 6    | Vylixan Dora        | 5,802        |
| 7    | Rhalzcairia         | 5,524        |
| 8    | An Actual Hurricane | 5,031        |
| 9    | Apexiala            | 4,889        |
| 10   | Mikeswill           | 4,707        |

#### Most Cards Bought (250+)

| Rank | Trader                  | Cards Bought |
| ---- | ----------------------- | ------------ |
| 1    | Upper Tuchoim           | 195          |
| 2    | Giovanniland            | 113          |
| 3    | Valoptia                | 105          |
| 4    | Kractero                | 100          |
| 5    | Shibutani               | 45           |
| 6    | Empire of Caldrasa      | 42           |
| 7    | War Dogs IV             | 40           |
| 8    | Osheiga                 | 40           |
| 9    | Fauzjhia                | 36           |
| 10   | The Land of Fun Fun Fun | 31           |

| Rank | Trader          | Legs Bought |
| ---- | --------------- | ----------- |
| 1    | Valoptia        | 104         |
| 2    | Kractero        | 99          |
| 3    | Giovanniland    | 57          |
| 4    | Osheiga         | 40          |
| 5    | War Dogs IV     | 39          |
| 6    | Shibutani       | 28          |
| 7    | Fauzjhia        | 28          |
| 8    | New Kowloon Bay | 23          |
| 9    | Rain Delay      | 18          |
| 10   | Auranzjinilhe   | 15          |

#### Most Cards Sold (250+)

| Rank | Trader                  | Cards Sold |
| ---- | ----------------------- | ---------- |
| 1    | Empire of Caldrasa      | 55         |
| 2    | Shibutani               | 53         |
| 3    | The Land of Fun Fun Fun | 49         |
| 4    | Giovanniland            | 45         |
| 5    | Frisbeeteria            | 44         |
| 6    | Upper Tuchoim           | 36         |
| 7    | Eugeniee                | 30         |
| 8    | Kractero                | 28         |
| 9    | Midlands                | 24         |
| 10   | 9006                    | 22         |

| Rank | Trader             | Legs Sold |
| ---- | ------------------ | --------- |
| 1    | Shibutani          | 52        |
| 2    | Frisbeeteria       | 43        |
| 3    | Midlands           | 24        |
| 4    | Eugeniee           | 23        |
| 5    | 9006               | 21        |
| 6    | Xoriet             | 20        |
| 7    | Refuge Isle        | 18        |
| 8    | Empire of Caldrasa | 17        |
| 9    | Benevolent 1       | 15        |
| 10   | Portsville         | 14        |

### Buyers By Season

#### Season 1

| Rank | Trader             | Cards Bought |
| ---- | ------------------ | ------------ |
| 1    | War Dogs IV        | 10,221       |
| 2    | Talakmachen        | 8,993        |
| 3    | Kractero           | 8,650        |
| 4    | Mikeswill          | 4,798        |
| 5    | Cartagriem 011     | 4,169        |
| 6    | War Dogs VII       | 3,564        |
| 7    | Caffeinated        | 2,138        |
| 8    | Kwaj               | 1,851        |
| 9    | Klaus Devestatorie | 1,764        |
| 10   | Koem Kab           | 1,700        |

#### Season 1 Non-Zero

| Rank | Trader           | Cards Sold |
| ---- | ---------------- | ---------- |
| 1    | War Dogs IV      | 9,230      |
| 2    | Cartagriem 011   | 2,697      |
| 3    | Caffeinated      | 1,854      |
| 4    | CSB PM Union     | 936        |
| 5    | Yodle            | 797        |
| 6    | Apexiala         | 463        |
| 7    | Kushinas Parrots | 343        |
| 8    | The Realizer     | 318        |
| 9    | Mikeswill        | 318        |
| 10   | Rain Delay       | 314        |

#### Season 2

| Rank | Trader               | Cards Bought |
| ---- | -------------------- | ------------ |
| 1    | Noahs Second Country | 11,490       |
| 2    | Koem Kab             | 9,813        |
| 3    | New Makasta          | 6,271        |
| 4    | Mikeswill            | 5,347        |
| 5    | Refuge Isle          | 5,262        |
| 6    | War Dogs IV          | 4,647        |
| 7    | 9006                 | 4,635        |
| 8    | Yodle                | 3,831        |
| 9    | Aerilia              | 2,836        |
| 10   | Seanat               | 2,523        |

#### Season 2 Non-Zero

| Rank | Trader                               | Cards Bought |
| ---- | ------------------------------------ | ------------ |
| 1    | War Dogs IV                          | 1,833        |
| 2    | Yodle                                | 1,619        |
| 3    | Card Cleaver                         | 1,348        |
| 4    | CSB PM Union                         | 1,208        |
| 5    | Il Sonno Della Ragione Genera Mostri | 799          |
| 6    | Free Land of Rebellium               | 743          |
| 7    | The Republic of Konsa                | 688          |
| 8    | Kushinas Parrots                     | 599          |
| 9    | Apexiala                             | 548          |
| 10   | The Colonial Buccaruu                | 533          |

#### Season 3

> Buyer of Season 3:

| Rank | Trader                | Cards Bought |
| ---- | --------------------- | ------------ |
| 1    | War Dogs IV           | 184,895      |
| 2    | The Colonial Buccaruu | 67,701       |
| 3    | Communist-Denmark     | 31,874       |
| 4    | Varanius              | 23,953       |
| 5    | Giovanniland          | 21,733       |
| 6    | Mikeswill             | 20,945       |
| 7    | Card Cleaver          | 18,856       |
| 8    | Anarco Argentina      | 18,125       |
| 9    | Shyshaeian Nation     | 17,896       |
| 10   | Yodle                 | 14,561       |

#### Season 3 Non-Zero

| Rank | Trader                               | Cards Bought |
| ---- | ------------------------------------ | ------------ |
| 1    | Card Cleaver                         | 18,815       |
| 2    | Anarco Argentina                     | 17,460       |
| 3    | Communist-Denmark                    | 14,872       |
| 4    | Giovanniland                         | 14,652       |
| 5    | Midlands                             | 14,249       |
| 6    | Il Sonno Della Ragione Genera Mostri | 14,198       |
| 7    | Mikeswill                            | 11,858       |
| 8    | Yodle                                | 11,534       |
| 9    | Giraffeton                           | 11,394       |
| 10   | Philville-Uncommons                  | 10,241       |

### Buyers By Rarity Non-Zero

#### Common

| Rank | Trader                               | Cards Bought |
| ---- | ------------------------------------ | ------------ |
| 1    | Communist-Denmark                    | 13,956       |
| 2    | Anarco Argentina                     | 12,672       |
| 3    | Giovanniland                         | 12,480       |
| 4    | Il Sonno Della Ragione Genera Mostri | 11,982       |
| 5    | Giraffeton                           | 10,625       |
| 6    | War Dogs IV                          | 9,431        |
| 7    | Apexiala                             | 7,215        |
| 8    | Yodle                                | 6,780        |
| 9    | Free Land of Rebellium               | 5,986        |
| 10   | Card Cleaver                         | 4,787        |

#### Uncommon

| Rank | Trader                 | Cards Bought |
| ---- | ---------------------- | ------------ |
| 1    | Philville-Uncommons    | 10,388       |
| 2    | Card Cleaver           | 6,683        |
| 3    | Yodle                  | 4,357        |
| 4    | Pierpontia             | 3,595        |
| 5    | Kushinas Parrots       | 3,302        |
| 6    | Free Land of Rebellium | 2,993        |
| 7    | Anarco Argentina       | 2,809        |
| 8    | Cartagriem 011         | 2,697        |
| 9    | Alliestrum             | 2,571        |
| 10   | Krupp Industries       | 2,098        |

#### Rare

| Rank | Trader                 | Cards Bought |
| ---- | ---------------------- | ------------ |
| 1    | New Zander             | 6,853        |
| 2    | Card Cleaver           | 3,701        |
| 3    | Mikeswill              | 1,907        |
| 4    | Anarco Argentina       | 1,640        |
| 5    | Yodle                  | 1,597        |
| 6    | Kushinas Parrots       | 1,506        |
| 7    | Pierpontia             | 1,492        |
| 8    | Midlands               | 1,174        |
| 9    | Free Land of Rebellium | 981          |
| 10   | Demeter                | 956          |

#### Ultra Rare

| Rank | Trader                | Cards Bought |
| ---- | --------------------- | ------------ |
| 1    | Mikeswill             | 6,534        |
| 2    | Refuge Isle           | 5,716        |
| 3    | Philville-Ultra-Rares | 4,218        |
| 4    | CSB PM Union          | 3,610        |
| 5    | Midlands              | 2,714        |
| 6    | Card Cleaver          | 2,660        |
| 7    | Demeter               | 1,408        |
| 8    | Rhalzcairia           | 1,247        |
| 9    | Yodle                 | 845          |
| 10   | Kushinas Parrots      | 762          |

#### Epic

| Rank | Trader                 | Cards Bought |
| ---- | ---------------------- | ------------ |
| 1    | Frisbeeteria           | 15,534       |
| 2    | Fauzjhia               | 3,873        |
| 3    | Tuptoogza              | 2,067        |
| 4    | Midlands               | 2,052        |
| 5    | Altivia Stock Exchange | 1,850        |
| 6    | Celzlhi                | 1,780        |
| 7    | Timao                  | 1,749        |
| 8    | Discgolfland           | 1,641        |
| 9    | Shion Uzuki            | 1,582        |
| 10   | Auranzjinilhe          | 1,350        |

### Legendaries

#### Legendaries Bought

| Rank | Trader                | Cards Bought |
| ---- | --------------------- | ------------ |
| 1    | Kractero              | 5,424        |
| 2    | Koem Kab              | 4,799        |
| 3    | Mikeswill             | 4,414        |
| 4    | Noah's Second Country | 4,265        |
| 5    | Varanius              | 3,051        |
| 6    | Aragesh               | 2,822        |
| 7    | UPC                   | 2,645        |
| 8    | Vulxo                 | 2,390        |
| 9    | Valoptia              | 1,918        |
| 10   | Communist-Denmark     | 1,913        |

#### Legendaries Bought Non-Zero

| Rank | Trader                | Cards Bought |
| ---- | --------------------- | ------------ |
| 1    | Koem Kab              | 1,889        |
| 2    | Varanius              | 672          |
| 3    | Kractero              | 602          |
| 4    | Osheiga               | 586          |
| 5    | New Makasta           | 533          |
| 6    | Eugeniee              | 452          |
| 7    | Midlands              | 420          |
| 8    | Valoptia              | 410          |
| 9    | The Shaymen           | 403          |
| 10   | Noah's Second Country | 365          |

#### Legendaries Gifted

| Rank | Trader                         | Gifted |
| ---- | ------------------------------ | ------ |
| 1    | The United Peoples of Centrism | 2,535  |
| 2    | Refuge Isle                    | 844    |
| 3    | Valoptia                       | 836    |
| 4    | Venico                         | 676    |
| 5    | 9006                           | 563    |
| 6    | Warden of the Spring           | 225    |
| 7    | Zhensheng Xue                  | 201    |
| 8    | Burattino                      | 175    |
| 9    | War Dogs IV                    | 165    |
| 10   | East Chimore                   | 163    |

#### Legendaries Received

| Rank | Trader               | Received |
| ---- | -------------------- | -------- |
| 1    | Kractero             | 4,822    |
| 2    | Mikeswill            | 4,406    |
| 3    | Noahs Second Country | 3,900    |
| 4    | Koem Kab             | 2,910    |
| 5    | Aragesh              | 2,809    |
| 6    | UPC                  | 2,614    |
| 7    | Varanius             | 2,379    |
| 8    | Vulxo                | 2,203    |
| 9    | Communist-Denmark    | 1,859    |
| 10   | Valoptia             | 1,508    |

## Time Breakdown

### First Half of the Year

#### Most Bank Moved

| Rank | Trader                | Bank Moved |
| ---- | --------------------- | ---------- |
| 1    | Koem Kab              | 105542.82  |
| 2    | Kractero              | 101960.97  |
| 3    | Upper Tuchoim         | 97573.83   |
| 4    | 9006                  | 90406.13   |
| 5    | Valoptia              | 85413.22   |
| 6    | Varanius              | 64160.15   |
| 7    | Giovanniland          | 55062.39   |
| 8    | Noah's Second Country | 52664.81   |
| 9    | Mikeswill             | 52559.90   |
| 10   | Fauzjhia              | 49657.79   |

#### Most Bank Moved as Buyer

| Rank | Trader             | Bank Moved |
| ---- | ------------------ | ---------- |
| 1    | Upper Tuchoim      | 47854.15   |
| 2    | Kractero           | 47536.88   |
| 3    | Koem Kab           | 45756.75   |
| 4    | 9006               | 43599.26   |
| 5    | Valoptia           | 40992.11   |
| 6    | Varanius           | 36316.26   |
| 7    | Giovanniland       | 28773.98   |
| 8    | Fauzjhia           | 25340.61   |
| 9    | Mikeswill          | 22073.96   |
| 10   | Thelandoffunfunfun | 16450.44   |

#### Most Bank Moved as Seller

| Rank | Trader            | Bank Moved |
| ---- | ----------------- | ---------- |
| 1    | Navasota-TX       | 47854.15   |
| 2    | Osheiga           | 47536.88   |
| 3    | Yolanda Opus      | 45756.75   |
| 4    | Annette           | 43599.26   |
| 5    | Universe Dragonia | 40992.11   |
| 6    | Vara 89           | 36316.26   |
| 7    | Fantaunhzluna     | 28773.98   |
| 8    | Varanius          | 25340.61   |
| 9    | KSN90             | 22073.96   |
| 10   | Fherlexzfhaizi    | 16450.44   |

#### Most Cards Bought

| Rank | Trader                | Cards Bought |
| ---- | --------------------- | ------------ |
| 1    | War Dogs IV           | 125606       |
| 2    | The Colonial Buccaruu | 39496        |
| 3    | Card Cleaver          | 20265        |
| 4    | Shyshaeian Nation     | 18088        |
| 5    | Giovanniland          | 15037        |
| 6    | Koem Kab              | 11539        |
| 7    | Varanius              | 11323        |
| 8    | Mikeswill             | 9638         |
| 9    | War Dogs VI           | 9626         |
| 10   | New Makasta           | 8604         |

#### Most Cards Bought Non-Zero

| Rank | Trader                               | Cards Bought > 0 |
| ---- | ------------------------------------ | ---------------- |
| 1    | Card Cleaver                         | 20220            |
| 2    | Giovanniland                         | 9579             |
| 3    | Il Sonno Della Ragione Genera Mostri | 7766             |
| 4    | War Dogs IV                          | 6160             |
| 5    | Giraffeton                           | 5268             |
| 6    | Midlands                             | 4631             |
| 7    | Timao                                | 4235             |
| 8    | Yodle                                | 4140             |
| 9    | Kushina's Parrots                    | 3644             |
| 10   | Mikeswill                            | 3522             |

#### Most Cards Sold

| Rank | Trader                | Cards Sold |
| ---- | --------------------- | ---------- |
| 1    | War Dogs IV           | 21309      |
| 2    | Kractero              | 6732       |
| 3    | Fauzjhia              | 5957       |
| 4    | Koem Kab              | 5945       |
| 5    | An Actual Hurricane   | 5036       |
| 6    | 9006                  | 4738       |
| 7    | Upper Tuchoim         | 4515       |
| 8    | Noah's Second Country | 4258       |
| 9    | Rhalzcairia           | 4133       |
| 10   | New Makasta           | 3815       |

#### Most Cards Sold Non-Zero

| Rank | Trader                | Cards Sold |
| ---- | --------------------- | ---------- |
| 1    | War Dogs IV           | 14242      |
| 2    | Koem Kab              | 5944       |
| 3    | Kractero              | 5062       |
| 4    | 9006                  | 4289       |
| 5    | Upper Tuchoim         | 4266       |
| 6    | Noah's Second Country | 4253       |
| 7    | New Makasta           | 3808       |
| 8    | Midlands              | 3769       |
| 9    | Varanius              | 2631       |
| 10   | Timao                 | 2616       |

### Last Half of the Year

#### Most Bank Moved

| Rank | Trader                | Bank Moved |
| ---- | --------------------- | ---------- |
| 1    | Kractero              | 148391.37  |
| 2    | Upper Tuchoim         | 128321.54  |
| 3    | Valoptia              | 111387.13  |
| 4    | Empire of Caldrasa    | 93697.09   |
| 5    | Noah's Second Country | 89246.80   |
| 6    | Koem Kab              | 76417.82   |
| 7    | Eugeniee              | 70921.17   |
| 8    | 9006                  | 62787.10   |
| 9    | Shibutani             | 59743.73   |
| 10   | War Dogs IV           | 57603.89   |

#### Most Bank Moved as Buyer

| Rank | Trader             | Bank Spent |
| ---- | ------------------ | ---------- |
| 1    | Kractero           | 72616.45   |
| 2    | Upper Tuchoim      | 64526.23   |
| 3    | Valoptia           | 55494.15   |
| 4    | Empire of Caldrasa | 42787.76   |
| 5    | Fauzjhia           | 38257.35   |
| 6    | Eugeniee           | 33353.77   |
| 7    | 9006               | 30889.17   |
| 8    | War Dogs IV        | 29897.06   |
| 9    | Shibutani          | 27936.26   |
| 10   | Varanius           | 27597.00   |

#### Most Bank Moved as Seller

| Rank | Trader             | Bank Sold |
| ---- | ------------------ | --------- |
| 1    | Kractero           | 72616.45  |
| 2    | Upper Tuchoim      | 64526.23  |
| 3    | Valoptia           | 55494.15  |
| 4    | Empire of Caldrasa | 42787.76  |
| 5    | Fauzjhia           | 38257.35  |
| 6    | Eugeniee           | 33353.77  |
| 7    | 9006               | 30889.17  |
| 8    | War Dogs IV        | 29897.06  |
| 9    | Shibutani          | 27936.26  |
| 10   | Varanius           | 27597.00  |

#### Most Cards Bought

| Rank | Trader                | Cards Bought |
| ---- | --------------------- | ------------ |
| 1    | War Dogs IV           | 74157        |
| 2    | The Colonial Buccaruu | 30669        |
| 3    | Communist-Denmark     | 27624        |
| 4    | Mikeswill             | 21452        |
| 5    | Anarco Argentina      | 17617        |
| 6    | Varanius              | 13005        |
| 7    | Lake Floria           | 12627        |
| 8    | Philville-Uncommons   | 12390        |
| 9    | Kractero              | 12308        |
| 10   | Yodle                 | 11969        |

#### Most Cards Bought Non-Zero

| Rank | Trader                               | Cards Bought |
| ---- | ------------------------------------ | ------------ |
| 1    | Anarco Argentina                     | 16980        |
| 2    | Communist-Denmark                    | 14530        |
| 3    | Philville-Uncommons                  | 10396        |
| 4    | Midlands                             | 10021        |
| 5    | Yodle                                | 9810         |
| 6    | War Dogs IV                          | 9348         |
| 7    | Mikeswill                            | 8890         |
| 8    | Free Land of Rebellium               | 7815         |
| 9    | Il Sonno Della Ragione Genera Mostri | 7417         |
| 10   | Giraffeton                           | 6128         |

#### Most Cards Sold

| Rank | Trader                | Cards Sold |
| ---- | --------------------- | ---------- |
| 1    | War Dogs IV           | 38316      |
| 2    | Lake Floria           | 8057       |
| 3    | Anarco Argentina      | 7906       |
| 4    | Mikeswill             | 7830       |
| 5    | Kractero              | 7582       |
| 6    | Noah's Second Country | 7264       |
| 7    | Midlands              | 7011       |
| 8    | Yodle                 | 6510       |
| 9    | Vylixan Dora          | 6505       |
| 10   | The Colonial Buccaruu | 6326       |

#### Most Cards Sold Non-Zero

| Rank | Trader                               | Cards Sold |
| ---- | ------------------------------------ | ---------- |
| 1    | War Dogs IV                          | 30903      |
| 2    | Kractero                             | 7300       |
| 3    | Noah's Second Country                | 7246       |
| 4    | Midlands                             | 7002       |
| 5    | The Colonial Buccaruu                | 5894       |
| 6    | Koem Kab                             | 5348       |
| 7    | Il Sonno Della Ragione Genera Mostri | 4958       |
| 8    | Communist-Denmark                    | 4552       |
| 9    | Darklight Girl Sarah                 | 4077       |
| 10   | Mikeswill                            | 4025       |

### Hours, Days, Months

#### Most Active Day

The day in which the most money was transferred on the market was April 14th at 11 PM UTC, which totaled 20,735.73.

These were the top 5 trades on that day.

| Rank | Seller     | Buyer          | Price   | Card                           |
| ---- | ---------- | -------------- | ------- | ------------------------------ |
| 1    | rain_delay | kractero       | 10000.0 | Season 1 Epic 9003             |
| 2    | hujen      | 9006           | 10000.0 | Season 1 Epic 9003             |
| 3    | apexiala   | bank_of_apex   | 650.0   | Season 2 Common Peagususlair   |
| 4    | kractero   | tordek_redfist | 400.0   | Season 3 Legendary The Stalker |
| 5    | 9006       | racoda         | 100.0   | Season 1 Uncommon Racoda       |

The day in which the most trades occured on the market was Aug 17th at 10 PM utc, a total of 3062.

The most active buyer at the time was Vulcan Vylixan, at 250. Conversely, the most active seller was War Dogs IV, at 49.

#### Hour of the Day

Note: UTC

![Hours of the Day](Hourly.png)

| Hour | Total Trades | Bank Moved |
| ---- | ------------ | ---------- |
| 00   | 110722       | 167322.85  |
| 01   | 109597       | 168023.12  |
| 02   | 105102       | 183600.78  |
| 03   | 95940        | 179344.17  |
| 04   | 87911        | 218432.74  |
| 05   | 79910        | 165634.11  |
| 06   | 78257        | 151524.64  |
| 07   | 82415        | 141952.03  |
| 08   | 85590        | 124852.56  |
| 09   | 75501        | 121369.10  |
| 10   | 70617        | 92261.61   |
| 11   | 76537        | 92705.57   |
| 12   | 90573        | 95569.87   |
| 13   | 97019        | 93101.67   |
| 14   | 105960       | 154081.92  |
| 15   | 112885       | 161281.31  |
| 16   | 114045       | 144468.86  |
| 17   | 122667       | 158073.49  |
| 18   | 126354       | 156794.35  |
| 19   | 129177       | 187635.39  |
| 20   | 130450       | 192911.56  |
| 21   | 130294       | 177146.64  |
| 22   | 124859       | 193904.16  |
| 23   | 115254       | 194297.24  |

#### Day of the Week

| Day       | Total Trades | Bank Moved |
| --------- | ------------ | ---------- |
| Sunday    | 389824       | 632630.89  |
| Monday    | 368565       | 622304.58  |
| Tuesday   | 350138       | 530490.99  |
| Wednesday | 337341       | 464781.54  |
| Thursday  | 330731       | 451549.61  |
| Friday    | 332916       | 453370.73  |
| Saturday  | 348121       | 561161.40  |

#### Month of the Year

| Month   | Total Trades | Bank Moved |
| ------- | ------------ | ---------- |
| 2024-01 | 202712       | 267017.30  |
| 2024-02 | 216860       | 343493.05  |
| 2024-03 | 232917       | 303547.11  |
| 2024-04 | 101025       | 182003.12  |
| 2024-05 | 161066       | 179450.28  |
| 2024-06 | 183712       | 278968.27  |
| 2024-07 | 212071       | 296671.32  |
| 2024-08 | 214724       | 384063.01  |
| 2024-09 | 213282       | 269624.35  |
| 2024-10 | 200955       | 300862.83  |
| 2024-11 | 196705       | 375320.26  |
| 2024-12 | 321607       | 535268.84  |

### Cards, Traders

#### Traders Per Month Non-Zero

| Year-Month | Trader              | Total Trades |
| ---------- | ------------------- | ------------ |
| 2024-01    | War Dogs IV         | 2861         |
| 2024-02    | 9006                | 2794         |
| 2024-03    | Card Cleaver        | 12517        |
| 2024-04    | Card Cleaver        | 3577         |
| 2024-05    | Card Cleaver        | 4111         |
| 2024-06    | War Dogs IV         | 2359         |
| 2024-07    | War Dogs IV         | 3236         |
| 2024-08    | Communist-Denmark   | 3611         |
| 2024-09    | Anarco Argentina    | 4901         |
| 2024-10    | Anarco Argentina    | 3054         |
| 2024-11    | Philville Uncommons | 4669         |
| 2024-12    | War Dogs IV         | 18741        |

#### Most Bank Moved Per Month

| Year-Month | Trader                | Bank Moved |
| ---------- | --------------------- | ---------- |
| 2024-01    | Noah's Second Country | 17810.01   |
| 2024-02    | 9003                  | 31052.42   |
| 2024-03    | Koem Kab              | 24426.84   |
| 2024-04    | Giovanniland          | 15139.18   |
| 2024-05    | Kractero              | 7651.48    |
| 2024-06    | Kractero              | 15596.59   |
| 2024-07    | Mikeswill             | 25690.33   |
| 2024-08    | Fauzjhia              | 33588.4    |
| 2024-09    | Upper Tuchoim         | 23290.0    |
| 2024-10    | Kractero              | 19473.86   |
| 2024-11    | Empire of Caldrasa    | 24156.04   |
| 2024-12    | Koem Kab              | 53495.01   |

#### Number of Unique Cards Traded Each Month

| Month   | Unique Cards Traded |
| ------- | ------------------- |
| 2024-01 | 67823               |
| 2024-02 | 68145               |
| 2024-03 | 77461               |
| 2024-04 | 45070               |
| 2024-05 | 60922               |
| 2024-06 | 62737               |
| 2024-07 | 72007               |
| 2024-08 | 69004               |
| 2024-09 | 61774               |
| 2024-10 | 56575               |
| 2024-11 | 56155               |
| 2024-12 | 125035              |

#### Top 3 Legendaries By Bank Each Month

> January 2024

| Card Name        | Total Bank Moved |
| ---------------- | ---------------- |
| Nation of Quebec | 2129.85          |
| Alistia          | 1994.52          |
| Crazy girl       | 1760.00          |

> February 2024

| Card Name    | Total Bank Moved |
| ------------ | ---------------- |
| Testlandia   | 2222.00          |
| Safj         | 2194.00          |
| Giovanniland | 2080.00          |

> March 2024

| Card Name                   | Total Bank Moved |
| --------------------------- | ---------------- |
| Annihilators of Chan Island | 3500.00          |
| Safj                        | 2800.00          |
| Crazy girl                  | 1889.38          |

> April 2024

| Card Name   | Total Bank Moved |
| ----------- | ---------------- |
| S_diego     | 3553.56          |
| Chan Island | 3328.50          |
| The Stalker | 1100.00          |

> May 2024

| Card Name         | Total Bank Moved |
| ----------------- | ---------------- |
| The Stalker       | 1999.98          |
| Mindless contempt | 1810.00          |
| Katganistan       | 1602.50          |

> June 2024

| Card Name           | Total Bank Moved |
| ------------------- | ---------------- |
| New Visayan Islands | 5889.08          |
| Chan Island         | 5000.00          |
| Morover             | 5000.00          |

> July 2024

| Card Name           | Total Bank Moved |
| ------------------- | ---------------- |
| New Visayan Islands | 5845.00          |
| Soops               | 4349.99          |
| Testlandia          | 2374.97          |

> August 2024

| Card Name                   | Total Bank Moved |
| --------------------------- | ---------------- |
| Annihilators of Chan Island | 34394.61         |
| Stoklomolvi                 | 7512.07          |
| New Visayan Islands         | 6500.11          |

> September 2024

| Card Name    | Total Bank Moved |
| ------------ | ---------------- |
| Crazy girl   | 2800.01          |
| Giovanniland | 2587.01          |
| S_diego      | 2333.10          |

> October 2024

| Card Name                   | Total Bank Moved |
| --------------------------- | ---------------- |
| Annihilators of Chan Island | 5000.00          |
| Chan Island                 | 4400.00          |
| SalusaSecondus              | 3859.08          |

> November 2024

| Card Name                   | Total Bank Moved |
| --------------------------- | ---------------- |
| Annihilators of Chan Island | 10000.00         |
| New Visayan Islands         | 5090.02          |
| Heavens Reach               | 3950.00          |

> December 2024

| Card Name                   | Total Bank Moved |
| --------------------------- | ---------------- |
| Annihilators of Chan Island | 12700.00         |
| Chan Island                 | 5000.00          |
| Valkalan                    | 3274.03          |
