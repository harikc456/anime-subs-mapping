# anime-subs-mapping
 Creating a JP to EN Translation dataset from anime subtitles

 The aim of this project is to create a translation dataset from Japanese to English from anime subs
 
 The japanese subs can be downloaded from <a href = "https://kitsunekko.net/dirlist.php?dir=subtitles%2Fjapanese%2F">here </a> <br>
 The english subs can be downloaded from <a href = "https://kitsunekko.net/dirlist.php?dir=subtitles%2F">here </a>
 
 ```
 python subs.py --anime_name ANIME_NAME --jp_dir JP_DIR --en_dir EN_DIR
 ```
 
 If the subs are simultaneous i.e both japanese and english subs are in the same file, the use the simul_sub.py script
 
 ```
 python simul_subs.py --anime_name ANIME_NAME --dir DIRECTORY
 ```
 
 The requirement is that the subtitles in the both the directories should be sorted in the ascending or descending order of the episode number. 
 
 <strong> Right now only .ass and .srt files are supported </strong>
 
 <strong> Any help on improving the quality of the dataset will be appreciated as i believe there is a lot of room for improvements for my code </strong>
 
 The common titles in both the list are shown below, the checked ones are completed
 
<ul> 
<li> -[x] 07-Ghost</li> 
<li> -[x] 5 Centimeter Per Second</li> 
<li> -[x] 91 Days</li> 
<li> -[x] Accel World</li> 
<li> -[ ] Acchi Kocchi</li> 
<li> -[ ] Ai Shite Knight</li> 
<li> -[x] Ajin</li>  
<li> -[x] Akira</li> 
<li> -[ ] Akuma no Riddle</li> 
<li> -[x] Aldnoah Zero</li> 
<li> -[x] Amaama to Inazuma</li> 
<li> -[x] Amagami SS</li> 
<li> -[x] Amagami SS Plus</li> 
<li> -[ ] Amagi Brilliant Park</li> 
<li> -[x] Ano Natsu de Matteru</li> 
<li> -[x] Another</li> 
<li> -[ ] Ao no Kanata no Four Rhythm</li> 
<li> -[x] Aoharu x Kikanjuu</li> 
<li> -[ ] Aoi Hana</li> 
<li> -[x] Appleseed</li> 
<li> -[x] Arakawa Under the Bridge</li> 
<li> -[x] Assassination Classroom</li> 
<li> -[x] Baccano!</li> 
<li> -[x] Baka to Test to Shoukanjuu</li> 
<li> -[x] Bakemono no Ko</li> 
<li> -[x] Bakemonogatari</li> 
<li> -[x] Bakuman Season 3</li> 
<li> -[x] Barakamon</li> 
<li> -[x] Beelzebub</li> 
<li> -[ ] Berserk</li> 
<li> -[x] Betterman</li> 
<li> -[x] Black Bullet</li> 
<li> -[ ] Black Jack Final</li> 
<li> -[ ] Black Lagoon</li> 
<li> -[ ] Bleach</li> 
<li> -[x] Boku dake ga Inai Machi</li> 
<li> -[x] Bokurano</li> 
<li> -[ ] Bokutachi wa Benkyou ga Dekinai</li> 
<li> -[ ] Btooom!</li> 
<li> -[x] Busou Renkin</li> 
<li> -[x] Busou Shoujo Machiavellianism</li> 
<li> -[x] Campione!</li> 
<li> -[x] Cap Kakumei Bottleman</li> 
<li> -[x] Charlotte</li> 
<li> -[ ] Chihayafuru</li> 
<li> -[x] Chio-chan no Tsuugakuro</li> 
<li> -[ ] Chobits</li> 
<li> -[x] Chuunibyou demo Koi ga Shitai!</li> 
<li> -[x] Citrus</li> 
<li> -[x] City Hunter</li> 
<li> -[x] Classroom Crisis</li> 
<li> -[x] Claymore</li> 
<li> -[x] Clockwork Planet</li> 
<li> -[x] Cowboy Bebop</li> 
<li> -[ ] Cross Game</li> 
<li> -[x] D-Frag!</li> 
<li> -[x] DARLING in the FRANXX</li> 
<li> -[x] Danshi Koukousei no Nichijou</li> 
<li> -[x] Dungeon ni Deai wo_Motomeru no wa Machigatteiru Darou ka </li> 
<li> -[x] Dungeon ni Deai wo Motomeru no wa Machigatte Iru Darou ka Gaiden: Sword Oratoria </li> 
<li> -[x] Deadman Wonderland</li> 
<li> -[x] Death March kara Hajimaru Isekai Kyousoukyoku</li> 
<li> -[x] Death Note</li> 
<li> -[x] Dennou Coil</li> 
<li> -[ ] Detective Conan</li> 
<li> -[x] Devilman Crybaby</li> 
<li> -[x] Diabolik Lovers More, Blood</li> 
<li> -[x] Digimon Adventure</li> 
<li> -[x] Domestic na Kanojo</li> 
<li> -[ ] Doraemon</li> 
<li> -[x] Dr. Stone</li> 
<li> -[ ] Dragon Ball</li> 
<li> -[ ] Dragon Ball Kai</li> 
<li> -[ ] Dragon Ball Super</li> 
<li> -[ ] Dragon Ball Z</li> 
<li> -[x] Drifters</li> 
<li> -[x] EVE no Jikan</li>  
<li> -[x] Eureka Seven</li> 
<li> -[x] Eureka Seven AO</li> 
<li> -[ ] Fairy Tail</li> 
<li> -[x] Fate Apocrypha</li> 
<li> -[x] Fate Stay Night</li> 
<li> -[x] Fate Zero</li> 
<li> -[x] Fractale</li> 
<li> -[x] Free!</li> 
<li> -[x] Freedom</li> 
<li> -[x] Full Metal Panic Fumoffu</li> 
<li> -[x] Full Metal Panic!</li> 
<li> -[x] Full Metal Panic! The Second Raid </li> 
<li> -[x] Full Metal Panic! Invisible Victory</li> 
<li> -[x] Fullmetal Alchemist</li>
<li> -[x] Fullmetal Alchemist Brotherhood</li> 
<li> -[x] Fullmetal Alchemist Conqueror of Shamballa</li>  
<li> -[x] Gakkou Gurashi!</li> 
<li> -[x] Galilei Donna</li> 
<li> -[x] Gantz</li> 
<li> -[x] Genshiken Nidaime</li> 
<li> -[x] Ghost Sweeper Mikami</li> 
<li> -[x] Ghost in the Shell (1995)</li>
<li> -[x] Ghost in the Shell 2: Innocence</li> 
<li> -[x] Ghost in the Shell Arise</li> 
<li> -[x] Ginban Kaleidoscope</li> 
<li> -[ ] Gintama</li> 
<li> -[x] Glass no Hana to Kowasu Sekai</li> 
<li> -[x] Goblin Slayer</li> 
<li> -[x] Golden Kamuy</li> 
<li> -[x] Golgo 13</li> 
<li> -[x] Gosick</li> 
<li> -[x] Great Mazinger</li> 
<li> -[x] Grisaia no Kajitsu</li> 
<li> -[x] Guilty Crown</li> 
<li> -[x] Hachimitsu to Clover</li> 
<li> -[x] Hachimitsu to Clover II</li> 
<li> -[x] Hai to Gensou no Grimgar</li> 
<li> -[x] Haikyuu</li> 
<li> -[x] Haiyore! Nyaruko-san W</li> 
<li> -[ ] Hajime no Ippo</li> 
<li> -[ ] Hajime no Ippo Champion Road</li> 
<li> -[x] Hajime no Ippo New Challenger</li> 
<li> -[x] Hanasakeru Seishounen</li> 
<li> -[x] Hanasaku Iroha</li> 
<li> -[x] Hanayamata</li> 
<li> -[x] Hanzawa Naoki</li> 
<li> -[x] Harmonie</li> 
<li> -[x] Harmony</li>  
<li> -[ ] Hayate no Gotoku!!</li> 
<li> -[x] Heavy Object</li> 
<li> -[x] Hellsing</li> 
<li> -[x] Hentai Ouji to Warawanai Neko</li>  
<li> -[x] Hibike! Euphonium</li> 
<li> -[x] Hibike! Euphonium II</li> 
<li> -[x] Hidamari Sketch</li> 
<li> -[ ] Hidamari Sketch Hoshimitsu</li>
<li> -[x] Higashi no Eden</li> 
<li> -[x] High School Fleet</li> 
<li> -[x] High Score Girl</li> 
<li> -[x] Higurashi no Naku Koro ni</li> 
<li> -[x] Higurashi no Naku Koro ni Gou</li> 
<li> -[ ] Hikaru no Go</li> 
<li> -[x] Himouto! Umaru-chan</li> 
<li> -[x] Hinomaruzumou - Hinomaru Sumo</li> 
<li> -[x] Hourou Musuko</li> 
<li> -[x] Hyouka</li> 
<li> -[x] ID-0</li> 
<li> -[x] Ichiban Ushiro no Daimaou</li> 
<li> -[x] Idoly Pride</li> 
<li> -[ ] InuYasha</li> 
<li> -[x] Inukami!</li> 
<li> -[ ] Inuyashiki</li> 
<li> -[x] Iriya no Sora, UFO no Natsu</li> 
<li> -[ ] Isekai Cheat Magician</li> 
<li> -[x] Isekai Maou to Shoukan Shoujo no Dorei Majutsu</li> 
<li> -[x] Isekai Quartet</li> 
<li> -[x] Isshuukan Friends</li>
<li> -[x] Jojo's Bizarre Adventure</li> 
<li> -[x] Jojo's Bizarre Adventure Stardust Crusader</li> 
<li> -[x] Jojo's Bizarre Adventure Diamond is Unbreakable</li> 
<li> -[x] Jojo's Bizarre Adventure Golden Wind</li> 
<li> -[x] Jigoku Shoujo</li> 
<li> -[x] Jinrui wa Suitai Shimashita</li> 
<li> -[x] Joker Game</li> 
<li> -[x] Jormungand</li> 
<li> -[x] Jujutsu Kaisen</li> 
<li> -[ ] K</li> 
<li> -[ ] Kaiba</li> 
<li> -[x] Kakegurui</li> 
<li> -[x] Kami nomi zo Shiru Sekai</li> 
<li> -[x] Kami nomi zo Shiru Sekai S2</li> 
<li> -[x] Kami nomi zo Shiru Sekai S3</li> 
<li> -[ ] Kantai Collection</li> 
<li> -[ ] Kappa no Coo to Natsuyasumi</li> 
<li> -[ ] Kara no Kyoukai</li> 
<li> -[ ] Karigurashi no Arrietty</li> 
<li> -[x] Katanagatari</li> 
<li> -[ ] Kemono Friends</li> 
<li> -[ ] Kemono no Souja Erin</li> 
<li> -[ ] Keroro Gunsou</li> 
<li> -[ ] Kiki's Delivery Service</li> 
<li> -[x] Kill La Kill</li>  
<li> -[x] Kimagure Orange Road</li> 
<li> -[x] Kimi to Boku</li> 
<li> -[ ] Kindaichi Case Files</li> 
<li> -[x] Kingdom</li> 
<li> -[x] Kishuku Gakkou no Juliet</li> 
<li> -[x] Kiznaiver</li> 
<li> -[x] Kizumonogatari</li> 
<li> -[x] Kobato</li> 
<li> -[x] Kobayashi-san Chi no Maid Dragon</li> 
<li> -[x] Kokoro Connect</li> 
<li> -[x] Kono Sekai no Katasumi ni</li> 
<li> -[x] Kono Subarashii Sekai ni Shukufuku wo!</li> 
<li> -[x] Koukaku Kidoutai Stand Alone Complex</li> 
<li> -[x] Koukaku no Regios</li> 
<li> -[x] Kuiba</li> 
<li> -[x] Kujira no Kora wa Sajou ni Utau</li> 
<li> -[x] Kuroko no Basket S1</li> 
<li> -[x] Kuroko no Basket S3</li> 
<li> -[x] Kuromukuro</li> 
<li> -[ ] Kyoukai No Rinne</li> 
<li> -[x] Kyoukai no Kanata</li> 
<li> -[x] Last Exile</li> 
<li> -[x] Little Witch Academia</li> 
<li> -[ ] Log Horizon S1</li> 
<li> -[ ] Log Horizon S2</li> 
<li> -[ ] Long Riders!</li> 
<li> -[x] Lost Song</li>
<li> -[x] Lovely Complex</li> 
<li> -[x] Lucky Star</li> 
<li> -[ ] Lupin III</li> 
<li> -[ ] Lupin III Part III</li> 
<li> -[ ] Macross Frontier</li> 
<li> -[ ] Macross Plus</li> 
<li> -[x] Magi Labyrinth of Magic</li>
<li> -[x] Magi Kingdom of Magic</li> 
<li> -[ ] Mahou Shoujo Lyrical Nanoha StrikerS</li> 
<li> -[x] Mahouka Koukou no Rettousei</li> 
<li> -[x] Mairimashita! Iruma-kun</li> 
<li> -[ ] Maison Ikkoku</li> 
<li> -[ ] Major</li> 
<li> -[x] Maoyuu Maou Yuusha</li> 
<li> -[ ] Mardock Scramble</li> 
<li> -[x] Marmalade Boy</li> 
<li> -[x] Mawaru Penguindrum</li> 
<li> -[ ] Mazinger Z</li> 
<li> -[x] Mikakunin de Shinkoukei</li> 
<li> -[x] Mitsuboshi Colors</li> 
<li> -[x] Mob Psycho 100</li> 
<li> -[x] Mob Psycho 100 II</li> 
<li> -[ ] Mobile Suit Gundam 0083 Stardust Memory</li> 
<li> -[x] Mondaiji-tachi ga Isekai kara Kuru Sou Desu yo?</li>
<li> -[x] Monster </li> 
<li> -[x] Monogatari Series (TVDB Order)</li> 
<li> -[x] Mononoke</li> 
<li> -[x] Mononoke Hime</li> 
<li> -[x] Moshidora</li> 
<li> -[x] Mouretsu Pirates</li> 
<li> -[x] Moyashimon Returns</li> 
<li> -[x] Musaigen no Phantom World</li> 
<li> -[x] Mushishi</li> 
<li> -[ ] Mushishi Zoku Shou</li> 
<li> -[x] Nagasarete Airantou</li> 
<li> -[x] Nagato Yuki-chan no Shoushitsu</li> 
<li> -[x] Nagi no Asukara</li> 
<li> -[x] Nande Koko ni Sensei ga!?</li> 
<li> -[ ] Naruto</li> 
<li> -[ ] Naruto Shippuuden</li> 
<li> -[ ] Natsume Yuujinchou</li> 
<li> -[ ] Neon Genesis Evangelion</li> 
<li> -[ ] Nerawareta Gakuen</li> 
<li> -[x] Nichijou</li> 
<li> -[ ] Nisekoi</li> 
<li> -[x] No Game No Life</li> 
<li> -[x] Non Non Biyori</li> 
<li> -[x] Noragami</li> 
<li> -[x] Noragami Aragoto</li> 
<li> -[x] Nourin</li> 
<li> -[ ] Nurarihyon no Mago</li> 
<li> -[x] Occultic;Nine</li> 
<li> -[ ] One Piece</li> 
<li> -[ ] One Room</li> 
<li> -[x] Ookami Kakushi</li> 
<li> -[ ] Ookami-san to Shichinin no Nakama-tachi</li> 
<li> -[ ] Ore no Kanojo to Osananajimi ga Shuraba Sugiru</li> 
<li> -[x] Ore no Nounai Sentakushi ga, Gakuen Lovecome o Zenryoku de Jama Shiteiru</li> 
<li> -[ ] Orenchi no Furo Jijou</li> 
<li> -[ ] Overlord</li> 
<li> -[ ] Owari no Seraph</li> 
<li> -[ ] Owarimonogatari</li> 
<li> -[ ] Pandora Hearts</li> 
<li> -[ ] Piano no Mori</li> 
<li> -[ ] Planetarian ~Chiisana Hoshi no Yume~</li> 
<li> -[ ] Pokemon</li> 
<li> -[ ] Pokemon XY</li> 
<li> -[ ] Pop Team Epic</li> 
<li> -[ ] Porco Rosso</li> 
<li> -[ ] Pretty Rhythm Aurora Dream</li> 
<li> -[ ] Pretty Rhythm Rainbow Live</li> 
<li> -[ ] Princess Principal</li> 
<li> -[ ] Psycho-Pass The Movie</li> 
<li> -[ ] Pupa</li> 
<li> -[ ] Rainbow days</li> 
<li> -[ ] ReLIFE</li> 
<li> -[ ] Rewrite</li> 
<li> -[ ] Ristorante Paradiso</li> 
<li> -[ ] Robot Girls Z</li> 
<li> -[ ] Rokudenashi Majutsu Koushi to Akashic Records</li> 
<li> -[ ] Romeo no Aoi Sora</li> 
<li> -[ ] Romeo x Juliet</li> 
<li> -[ ] Sacred Seven</li> 
<li> -[ ] Sailor Moon</li> 
<li> -[ ] Saint Seiya</li> 
<li> -[ ] Saiunkoku Monogatari</li> 
<li> -[ ] Sakasama no Patema</li> 
<li> -[ ] Saki</li> 
<li> -[ ] Sakigake!! Cromartie Koukou</li> 
<li> -[ ] Sakura Quest</li> 
<li> -[ ] Sakura Trick</li> 
<li> -[ ] Sakurako-san no Ashimoto ni wa Shitai ga Umatteiru</li> 
<li> -[ ] Samurai Champloo</li> 
<li> -[ ] Samurai Flamenco</li> 
<li> -[ ] Sankarea</li> 
<li> -[ ] Sarazanmai</li> 
<li> -[ ] Sayonara Zetsubou Sensei</li> 
<li> -[ ] School Days</li> 
<li> -[ ] School Rumble</li> 
<li> -[ ] Scrapped Princess</li> 
<li> -[ ] Seikai no Senki</li> 
<li> -[ ] Seikimatsu Occult Gakuin</li> 
<li> -[ ] Seirei no Moribito</li> 
<li> -[ ] Seiren</li> 
<li> -[ ] Seitokai Yakuindomo</li> 
<li> -[ ] Sekaiichi Hatsukoi</li> 
<li> -[ ] Sekirei</li> 
<li> -[ ] Sengoku Basara</li> 
<li> -[ ] Senki Zesshou Symphogear</li> 
<li> -[ ] Senki Zesshou Symphogear G</li> 
<li> -[ ] Senki Zesshou Symphogear GX</li> 
<li> -[ ] Sennen Joyuu</li> 
<li> -[ ] Serial Experiments Lain</li> 
<li> -[ ] Servant x Service</li> 
<li> -[ ] Shakugan no Shana</li> 
<li> -[ ] Shigofumi</li> 
<li> -[ ] Shiki</li> 
<li> -[ ] Shimoneta to Iu Gainen ga Sonzai Shinai Taikutsu na Sekai</li> 
<li> -[ ] Shingeki no Kyojin</li> 
<li> -[ ] Shingetsutan Tsukihime</li> 
<li> -[ ] Shinigami no Ballad</li> 
<li> -[ ] Shinsekai Yori</li> 
<li> -[ ] Shisha no Teikoku</li> 
<li> -[ ] Shoujo Kakumei Utena</li> 
<li> -[ ] Shoujo Shuumatsu Ryokou</li> 
<li> -[ ] Shoukoku no Altair</li> 
<li> -[ ] Shouwa Genroku Rakugo Shinjuu</li> 
<li> -[ ] Shuumatsu no Izetta</li> 
<li> -[ ] Sirius the Jaeger</li> 
<li> -[ ] Slayers Next</li> 
<li> -[ ] Slayers Revolution</li> 
<li> -[ ] Slayers Try</li> 
<li> -[ ] Sora no Method</li> 
<li> -[ ] Sora no Otoshimono</li> 
<li> -[ ] Sora yori mo Tooi Basho</li> 
<li> -[ ] Soredemo Machi wa Mawatteiru</li> 
<li> -[ ] Soul Eater</li> 
<li> -[ ] Soul land Douluo Dalu</li> 
<li> -[ ] Space Pirate Captain Harlock</li> 
<li> -[ ] Star Driver</li> 
<li> -[ ] Starry Sky</li> 
<li> -[ ] Steamboy</li> 
<li> -[ ] Steins;Gate 0</li> 
<li> -[ ] Strike Witches</li> 
<li> -[ ] Suisei no Gargantia</li> 
<li> -[ ] Summer Wars</li> 
<li> -[ ] Super Cub</li> 
<li> -[ ] Suzumiya Haruhi no Yuuutsu</li> 
<li> -[ ] Sword Art Online</li> 
<li> -[ ] Sword Art Online II</li> 
<li> -[ ] Sword Art Online: Alicization</li> 
<li> -[ ] Tales From Earthsea</li> 
<li> -[ ] Tales of Zestiria the X</li> 
<li> -[ ] Tales of the Abyss</li> 
<li> -[ ] Tamako Love Story</li> 
<li> -[ ] Tamako Market</li> 
<li> -[ ] Tanaka-kun wa Itsumo Kedaruge</li> 
<li> -[ ] Tari Tari</li> 
<li> -[ ] Tate no Yuusha no Nariagari</li> 
<li> -[ ] Telepathy Shoujo Ran</li> 
<li> -[ ] Tensei Shitara Slime Datta Ken</li> 
<li> -[ ] The Big O</li> 
<li> -[ ] The Borrower Arrietty</li> 
<li> -[ ] The Five Star Stories</li> 
<li> -[ ] The Rolling Girls</li> 
<li> -[ ] The Sky Crawlers</li> 
<li> -[ ] Thermae Romae</li> 
<li> -[ ] Toaru Kagaku no Accelerator</li> 
<li> -[ ] Toaru Kagaku no Railgun</li> 
<li> -[ ] Toaru Kagaku no Railgun S</li> 
<li> -[ ] Toaru Majutsu no Index</li> 
<li> -[ ] Toaru Majutsu no Index II</li> 
<li> -[ ] Toaru Majutsu no Index III</li> 
<li> -[ ] Tokimeki Tonight</li> 
<li> -[ ] Tokyo Ghoul</li> 
<li> -[ ] Tokyo Godfathers</li> 
<li> -[ ] Tokyo Magnitude 8.0</li> 
<li> -[ ] Tokyo Marble Chocolate</li> 
<li> -[ ] Tokyo Ravens</li> 
<li> -[ ] Tonari no Seki-kun</li> 
<li> -[ ] Tonari no Totoro</li> 
<li> -[ ] Toriko</li> 
<li> -[ ] Trinity Blood</li> 
<li> -[ ] Trinity Seven</li> 
<li> -[ ] Tsubasa Shunraiki</li> 
<li> -[ ] Tsubasa Tokyo Revelations</li> 
<li> -[ ] Tsugumomo</li> 
<li> -[ ] Tsukimonogatari</li> 
<li> -[ ] Tsuredure Children</li> 
<li> -[ ] Tsuritama</li> 
<li> -[ ] Uchiage Hanabi (2017)</li> 
<li> -[ ] Uchouten Kazoku</li> 
<li> -[ ] Uchuu Senkan Yamato</li> 
<li> -[ ] Uchuu Senkan Yamato 2</li> 
<li> -[ ] Uchuu Senkan Yamato 2199</li> 
<li> -[ ] Uchuu Senkan Yamato 3</li> 
<li> -[ ] Uchuu Show e Youkoso</li> 
<li> -[ ] Uchuu no Stellvia</li> 
<li> -[ ] Ultraman Orb</li> 
<li> -[ ] Ultraman R B</li> 
<li> -[ ] Urara Meirochou</li> 
<li> -[ ] Usagi Drop</li> 
<li> -[ ] Utawarerumono</li> 
<li> -[ ] Vinland Saga</li> 
<li> -[ ] Violet Evergarden</li> 
<li> -[ ] Wagaya no Oinari-sama</li> 
<li> -[ ] Watashi Ga Motete Dou Sunda</li> 
<li> -[ ] Whisper of the Heart</li> 
<li> -[ ] Wonder Egg Priority</li> 
<li> -[ ] World Trigger</li> 
<li> -[ ] Yakusoku no Neverland</li> 
<li> -[ ] Yamada-kun to 7-nin no Majo</li> 
<li> -[ ] Yojouhan Shinwa Taikei</li> 
<li> -[ ] Yokohama Kaidashi Kikou</li>  
<li> -[ ] Youkai Watch</li> 
<li> -[ ] Youkoso Jitsuryoku Shijou Shugi no Kyoushitsu e</li> 
<li> -[x] Your Name</li> 
<li> -[ ] Yu Yu Hakusho</li> 
<li> -[ ] Yu-Gi-Oh! 5D's</li> 
<li> -[ ] Yu-Gi-Oh! ARC-V</li> 
<li> -[ ] Yumekui Merry</li> 
<li> -[ ] Yurikuma Arashi</li> 
<li> -[ ] Yuru Camp</li> 
<li> -[ ] Yuru Yuri S2</li> 
<li> -[ ] Yuru Yuri San Hai!</li> 
<li> -[ ] Zero kara Hajimeru Mahou no Sho</li> 
<li> -[ ] Zero no Tsukaima</li> 
<li> -[ ] Zoids Wild</li> 
<li> -[ ] Zoku Owarimonogatari</li> 
<li> -[ ] ef - a tale of memories</li> 
</ul>

## Things to do while cleaning the data
<ul>
<li> -[ ] If the jp_text rows entry is a number then put the same number to en_text, change score to 1
<li> -[x] Remove/Merge duplicate jp_text to eng_text mappings </li>
<li> -[x] Remove words inside {} and <> in jp_text and en_text</li>
<li> -[x] Remove rows where en_text has less than 3 characters length </li>
<li> -[x] Remove rows with score 0 and number of words greater than 1 </li>
<li> Normalize English translation of duplicate Japanese text i.e same jp text should have same english translation</li>
	<ol>
	<li>Check for Named Entity Tags in the original text and translated text (sanity checks)</li>
	</ol>
</ul>