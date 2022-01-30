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
<li> -[x] A.I.C.O._Incarnation</li> 
<li> -[x] Accel World</li> 
<li> -[ ] Acchi Kocchi</li> 
<li> -[x] Aggretsuko</li> 
<li> -[ ] Ai Shite Knight</li>
<li> -[x] Ajin</li> 
<li> -[x] Ajin S2</li>  
<li> -[x] Akira</li> 
<li> -[x] Akarsuki no Yona</li> 
<li> -[ ] Akuma no Riddle</li> 
<li> -[x] Aldnoah Zero</li> 
<li> -[x] Amaama to Inazuma</li> 
<li> -[x] Amagami SS</li> 
<li> -[x] Amagami SS Plus</li> 
<li> -[ ] Amagi Brilliant Park</li>
<li> -[x] Angel Beats</li> 
<li> -[x] Anohana Movie</li> 
<li> -[x] Ano Natsu de Matteru</li> 
<li> -[x] Another</li> 
<li> -[ ] Ao no Kanata no Four Rhythm</li> 
<li> -[ ] Aoi Hana</li> 
<li> -[x] Appleseed</li> 
<li> -[x] Arakawa Under the Bridge</li>
<li> -[x] Arakawa Under the Bridge x Bridge</li> 
<li> -[x] Arslan Senki</li>
<li> -[x] Assassination Classroom</li> 
<li> -[x] Baccano!</li> 
<li> -[x] Baka to Test to Shoukanjuu</li> 
<li> -[x] Bakemono no Ko</li> 
<li> -[x] Bakemonogatari</li> 
<li> -[x] Bakuman Season 3</li> 
<li> -[x] Barakamon</li> 
<li> -[x] Beelzebub</li> 
<li> -[x] Berserk The Golden Age Arc</li> 
<li> -[x] Betterman</li> 
<li> -[x] Black Bullet</li> 
<li> -[ ] Black Jack Final</li> 
<li> -[ ] Black Lagoon</li> 
<li> -[x] Blame</li>
<li> -[x] Blazing Transfer Student</li>
<li> -[x] Bleach</li> 
<li> -[x] Boku dake ga Inai Machi</li> 
<li> -[x] Bokurano</li> 
<li> -[x] Bokura wa Minna Kawaisou</li> 
<li> -[x] Boku no Hero Academia</li> 
<li> -[ ] Bokutachi wa Benkyou ga Dekinai</li> 
<li> -[x] Boku wa Tomodachi ga Sukunai</li> 
<li> -[x] Boku wa Tomodachi ga Sukunai Next</li> 
<li> -[ ] Btooom!</li> 
<li> -[x] Bungou Stray Dogs S1</li>
<li> -[x] Bungou Stray Dogs S2</li> 
<li> -[x] Busou Renkin</li> 
<li> -[x] Busou Shoujo Machiavellianism</li> 
<li> -[x] Campione!</li> 
<li> -[x] Charlotte</li> 
<li> -[ ] Chihayafuru</li> 
<li> -[x] Chio-chan no Tsuugakuro</li> 
<li> -[ ] Chobits</li> 
<li> -[x] Citrus</li> 
<li> -[x] City Hunter</li> 
<li> -[x] Classroom Crisis</li> 
<li> -[x] Claymore</li>  
<li> -[x] Code Geass Akito the Exiled</li>
<li> -[x] Code Geass R1</li>
<li> -[x] Code Geass R2</li> 
<li> -[x] Cowboy Bebop</li> 
<li> -[ ] Cross Game</li> 
<li> -[x] D-Frag!</li> 
<li> -[x] DARLING in the FRANXX</li> 
<li> -[x] Danshi Koukousei no Nichijou</li> 
<li> -[x] Dungeon ni Deai wo_Motomeru no wa Machigatteiru Darou ka </li> 
<li> -[x] Dungeon ni Deai wo Motomeru no wa Machigatte Iru Darou ka Gaiden: Sword Oratoria </li> 
<li> -[x] Deadman Wonderland</li> 
<li> -[x] Dennou Coil</li> 
<li> -[ ] Detective Conan</li> 
<li> -[x] Devilman Crybaby</li> 
<li> -[x] Diabolik Lovers More, Blood</li> 
<li> -[x] Digimon Adventure</li> 
<li> -[ ] Doraemon</li>
<li> -[x] Dororo</li> 
<li> -[x] Dr. Stone</li> 
<li> -[x] Dragon Ball</li> 
<li> -[x] Dragon Ball Super</li>
<li> -[x] Drifters</li> 
<li> -[x] Durarara!!</li> 
<li> -[x] EVE no Jikan</li>  
<li> -[x] Eureka Seven</li> 
<li> -[x] Eureka Seven AO</li> 
<li> -[x] Fairy Tail</li> 
<li> -[x] Fate Apocrypha</li> 
<li> -[x] Fate Stay Night</li> 
<li> -[x] Fate Zero</li> 
<li> -[x] Final Fantasy VII Advent Children</li> 
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
<li> -[x] Gate Jietai Kanochi nite Kaku Tatakaeri</li> 
<li> -[x] Genshiken Nidaime</li> 
<li> -[x] Ghost in the Shell (1995)</li>
<li> -[x] Ghost in the Shell The New Movie</li> 
<li> -[x] Ghost in the Shell 2: Innocence</li> 
<li> -[x] Ghost in the Shell Arise</li>
<li> -[x] Giant Killing</li> 
<li> -[x] Ginban Kaleidoscope</li> 
<li> -[x] Gintama</li> 
<li> -[x] Girls Und Panzer Der Film</li> 
<li> -[x] Glass no Hana to Kowasu Sekai</li> 
<li> -[x] Goblin Slayer</li> 
<li> -[x] Golden Kamuy</li> 
<li> -[x] Golgo 13</li> 
<li> -[x] Gosick</li> 
<li> -[x] Grisaia no Kajitsu</li> 
<li> -[x] Guilty Crown</li> 
<li> -[x] Hachimitsu to Clover</li> 
<li> -[x] Hachimitsu to Clover II</li> 
<li> -[x] Hai to Gensou no Grimgar</li> 
<li> -[x] Haikyuu S1</li>
<li> -[x] Haikyuu S2</li>
<li> -[x] Haikyuu S3</li> 
<li> -[ ] Hajime no Ippo</li> 
<li> -[x] Hajime no Ippo New Challenger</li> 
<li> -[x] Hanasakeru Seishounen</li> 
<li> -[x] Hanasaku Iroha</li> 
<li> -[x] Hanayamata</li> 
<li> -[x] Hanzawa Naoki</li> 
<li> -[x] Harmonie</li> 
<li> -[x] Harmony</li> 
<li> -[x] Hataraku Maou-sama!</li>  
<li> -[ ] Hayate no Gotoku!!</li> 
<li> -[x] Heavy Object</li> 
<li> -[x] Hellsing</li> 
<li> -[x] Hentai Ouji to Warawanai Neko</li>  
<li> -[x] Hibike! Euphonium</li> 
<li> -[x] Hibike! Euphonium II</li> 
<li> -[ ] Hidamari Sketch Hoshimitsu</li>
<li> -[x] Higashi no Eden</li> 
<li> -[x] High School Fleet</li> 
<li> -[x] High Score Girl</li> 
<li> -[x] Higurashi no Naku Koro ni</li> 
<li> -[ ] Hikaru no Go</li> 
<li> -[x] Himouto! Umaru-chan</li> 
<li> -[x] Hinomaruzumou - Hinomaru Sumo</li> 
<li> -[x] Hourou Musuko</li>
<li> -[x] Hoshi wo Ou Kodomo</li>
<li> -[x] Howls Moving Castle</li> 
<li> -[x] Hyouka</li> 
<li> -[x] ID-0</li> 
<li> -[x] Ichiban Ushiro no Daimaou</li> 
<li> -[x] Idoly Pride</li> 
<li> -[x] Initial D Fifth Stage</li>
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
<li> -[x] Jinrui wa Suitai Shimashita</li> 
<li> -[x] Joker Game</li> 
<li> -[x] Jormungand</li> 
<li> -[x] Jujutsu Kaisen</li> 
<li> -[ ] K</li> 
<li> -[ ] Kaiba</li> 
<li> -[x] Kaiji S1</li> 
<li> -[x] Kaiji S2</li> 
<li> -[x] Kakegurui</li> 
<li> -[x] Kami nomi zo Shiru Sekai</li> 
<li> -[x] Kami nomi zo Shiru Sekai S2</li> 
<li> -[x] Kami nomi zo Shiru Sekai S3</li> 
<li> -[x] Kamisama Hajimemashita</li> 
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
<li> -[x] Kimi to Boku</li> 
<li> -[ ] Kindaichi Case Files</li> 
<li> -[x] Kingdom</li> 
<li> -[x] Kishuku Gakkou no Juliet</li> 
<li> -[x] Kiznaiver</li> 
<li> -[x] Kizumonogatari</li> 
<li> -[x] Kobato</li> 
<li> -[x] Kobayashi-san Chi no Maid Dragon</li> 
<li> -[x] Koe no Katachi</li> 
<li> -[x] Kokoro Connect</li> 
<li> -[x] Kokoro ga Sakebitagatterunda</li> 
<li> -[x] Kono Sekai no Katasumi ni</li> 
<li> -[x] Kono Subarashii Sekai ni Shukufuku wo!</li> 
<li> -[x] Kotonoha no Niwa</li> 
<li> -[x] Koukaku Kidoutai Stand Alone Complex</li> 
<li> -[x] Koukaku no Regios</li> 
<li> -[x] Kuiba</li> 
<li> -[x] Kujira no Kora wa Sajou ni Utau</li>
<li> -[x] Kumo no Mukou, Yakusoku no Basho</li>
<li> -[x] Kuroko no Basket S1</li> 
<li> -[x] Kuroko no Basket S3</li> 
<li> -[x] Kuromukuro</li> 
<li> -[ ] Kyoukai No Rinne</li> 
<li> -[x] Kyoukai no Kanata</li>
<li> -[x] Little Witch Academia</li> 
<li> -[ ] Log Horizon S1</li> 
<li> -[ ] Log Horizon S2</li> 
<li> -[ ] Long Riders!</li> 
<li> -[x] Lost Song</li>
<li> -[x] Lucky Star</li> 
<li> -[ ] Lupin III</li> 
<li> -[ ] Lupin III Part III</li> 
<li> -[ ] Macross Frontier</li> 
<li> -[ ] Macross Plus</li> 
<li> -[x] Made in Abyss</li> 
<li> -[x] Magi Labyrinth of Magic</li>
<li> -[x] Magi Kingdom of Magic</li> 
<li> -[ ] Mahou Shoujo Lyrical Nanoha StrikerS</li>
<li> -[x] Mahoutsukai_no_Yome</li> 
<li> -[x] Mahouka Koukou no Rettousei</li> 
<li> -[x] Mairimashita! Iruma-kun</li> 
<li> -[ ] Maison Ikkoku</li> 
<li> -[ ] Major</li> 
<li> -[x] Maoyuu Maou Yuusha</li> 
<li> -[x] March Comes in Like a Lion S1</li> 
<li> -[x] March Comes in Like a Lion S2</li> 
<li> -[x] Marmalade Boy</li> 
<li> -[x] Mawaru Penguindrum</li> 
<li> -[ ] Mazinger Z</li> 
<li> -[x] Mikakunin de Shinkoukei</li>
<li> -[x] Mirai no Mirai</li> 
<li> -[x] Mitsuboshi Colors</li> 
<li> -[x] Mob Psycho 100</li> 
<li> -[x] Mob Psycho 100 II</li> 
<li> -[ ] Mobile Suit Gundam 0083 Stardust Memory</li> 
<li> -[x] Mondaiji-tachi ga Isekai kara Kuru Sou Desu yo?</li>
<li> -[x] Monster </li> 
<li> -[x] Monogatari Series (TVDB Order)</li> 
<li> -[x] Mononoke Hime</li> 
<li> -[x] Mouretsu Pirates</li>  
<li> -[x] Musaigen no Phantom World</li> 
<li> -[x] Mushishi</li> 
<li> -[x] Mushibugyo</li> 
<li> -[ ] Mushishi Zoku Shou</li> 
<li> -[x] Nagasarete Airantou</li> 
<li> -[x] Nagato Yuki-chan no Shoushitsu</li> 
<li> -[x] Nagi no Asukara</li> 
<li> -[x] Nande Koko ni Sensei ga!?</li> 
<li> -[x] Nanatsu no Taizai</li> 
<li> -[x] Naruto</li> 
<li> -[ ] Naruto Shippuuden</li> 
<li> -[x] Natsume Yuujinchou</li> 
<li> -[x] Neko no Ongaeshi</li> 
<li> -[ ] Neon Genesis Evangelion</li> 
<li> -[ ] Nerawareta Gakuen</li> 
<li> -[x] Nichijou</li> 
<li> -[ ] Nisekoi</li> 
<li> -[x] No Game No Life</li> 
<li> -[x] Non Non Biyori</li> 
<li> -[x] Noragami</li> 
<li> -[x] Noragami Aragoto</li> 
<li> -[ ] Nurarihyon no Mago</li> 
<li> -[ ] Nyan Koi!</li> 
<li> -[x] Occultic;Nine</li>
<li> -[x] Omoide Poro-poro</li> 
<li> -[ ] One Piece</li>
<li> -[x] One Punch Man</li> 
<li> -[ ] One Room</li> 
<li> -[x] Ookami-san to Shichinin no Nakama-tachi</li> 
<li> -[ ] Ore no Kanojo to Osananajimi ga Shuraba Sugiru</li> 
<li> -[x] Ore no Nounai Sentakushi ga, Gakuen Lovecome o Zenryoku de Jama Shiteiru</li>  
<li> -[x] Ouran Koukou Host Club</li> 
<li> -[x] Overlord S2</li> 
<li> -[x] Overlord S3</li> 
<li> -[x] Owari no Seraph</li> 
<li> -[ ] Owarimonogatari</li> 
<li> -[ ] Pandora Hearts</li> 
<li> -[x] Phi_Brain Kami no Puzzle S1</li> 
<li> -[x] Phi_Brain Kami no Puzzle S2</li> 
<li> -[x] Phi_Brain Kami no Puzzle S3</li> 
<li> -[ ] Piano no Mori</li> 
<li> -[ ] Planetarian ~Chiisana Hoshi no Yume~</li> 
<li> -[x] Ping Pong The Animation</li> 
<li> -[ ] Pokemon</li> 
<li> -[ ] Pokemon XY</li> 
<li> -[ ] Pop Team Epic</li> 
<li> -[ ] Porco Rosso</li> 
<li> -[ ] Pretty Rhythm Aurora Dream</li> 
<li> -[ ] Pretty Rhythm Rainbow Live</li> 
<li> -[x] Princess Principal</li> 
<li> -[ ] Prison School</li> 
<li> -[x] Psycho-Pass S1</li> 
<li> -[x] Psycho-Pass S2</li> 
<li> -[ ] Psycho-Pass The Movie</li> 
<li> -[x] Pupa</li> 
<li> -[x] Rainbow days</li> 
<li> -[x] ReLIFE</li> 
<li> -[ ] Rewrite</li> 
<li> -[x] ReZero</li>
<li> -[x] Robotics Notes</li> 
<li> -[x] Rokudenashi Majutsu Koushi to Akashic Records</li> 
<li> -[x] Romeo x Juliet</li> 
<li> -[x] Saekano S1</li> 
<li> -[x] Saekano S2</li>
<li> -[ ] Sailor Moon</li> 
<li> -[ ] Saint Seiya</li> 
<li> -[ ] Saiunkoku Monogatari</li> 
<li> -[ ] Sakasama no Patema</li> 
<li> -[ ] Saki</li> - X  
<li> -[ ] Sakurako-san no Ashimoto ni wa Shitai ga Umatteiru</li> 
<li> -[x] Sakurasou no Pet na Kanojo</li>
<li> -[x] Samurai 7</li> 
<li> -[x] Samurai Champloo</li> 
<li> -[x] Samurai Flamenco</li> 
<li> -[x] Sankarea</li> 
<li> -[x] Sarazanmai</li> 
<li> -[x] Sayonara Zetsubou Sensei</li> 
<li> -[ ] School Days</li> 
<li> -[ ] School Rumble</li> 
<li> -[ ] Scrapped Princess</li>  
<li> -[ ] Seikimatsu Occult Gakuin</li> 
<li> -[x] Seirei no Moribito</li> 
<li> -[ ] Seiren</li> 
<li> -[x] Seitokai Yakuindomo</li> 
<li> -[x] Sekaiichi Hatsukoi S1</li>
<li> -[x] Sekaiichi Hatsukoi S2</li>  
<li> -[x] Sekirei</li> 
<li> -[ ] Sengoku Basara</li> 
<li> -[ ] Senki Zesshou Symphogear</li> 
<li> -[ ] Senki Zesshou Symphogear G</li> 
<li> -[ ] Senki Zesshou Symphogear GX</li> 
<li> -[ ] Sennen Joyuu</li> 
<li> -[ ] Serial Experiments Lain</li> 
<li> -[x] Servant x Service</li> 
<li> -[ ] Shakugan no Shana</li> 
<li> -[x] Shigatsu wa Kimi no Uso</li> 
<li> -[ ] Shigofumi</li> 
<li> -[ ] Shiki</li> 
<li> -[x] Shimoneta to Iu Gainen ga Sonzai Shinai Taikutsu na Sekai</li> 
<li> -[ ] Shingeki no Kyojin</li> 
<li> -[ ] Shingetsutan Tsukihime</li> 
<li> -[ ] Shinigami no Ballad</li> 
<li> -[x] Shinsekai Yori</li> 
<li> -[ ] Shisha no Teikoku</li>
<li> -[x] Shirobako</li> 
<li> -[x] Shokugeki no Soma S1</li>
<li> -[ ] Shokugeki no Soma S2</li> 
<li> -[x] Shoujo Kakumei Utena</li> 
<li> -[x] Shoujo Shuumatsu Ryokou</li> 
<li> -[x] Shouwa Genroku Rakugo Shinjuu S1 & S2</li> 
<li> -[x] Shuumatsu no Izetta</li> 
<li> -[ ] Sirius the Jaeger</li> 
<li> -[ ] Slayers Next</li> 
<li> -[ ] Slayers Revolution</li> 
<li> -[ ] Slayers Try</li> 
<li> -[ ] Sora no Method</li> 
<li> -[x] Sora no Otoshimono</li> 
<li> -[x] Sora no Otoshimono Forte</li> 
<li> -[ ] Sora yori mo Tooi Basho</li>  
<li> -[ ] Soul land Douluo Dalu</li> 
<li> -[x] Space Brothers</li>
<li> -[x] Space Pirate Captain Harlock</li>
<li> -[x] Spirted Away</li> 
<li> -[ ] Star Driver</li> 
<li> -[ ] Starry Sky</li> 
<li> -[x] Steamboy</li> 
<li> -[x] Steins;Gate</li>
<li> -[x] Steins;Gate 0</li> 
<li> -[x] Strike Witches</li> 
<li> -[x] Suisei no Gargantia</li> 
<li> -[x] Summer Wars</li> 
<li> -[ ] Super Cub</li> 
<li> -[ ] Suzumiya Haruhi no Yuuutsu</li> 
<li> -[x] Sword Art Online</li> 
<li> -[x] Sword Art Online Alternative Gun Gale Online</li> 
<li> -[ ] Sword Art Online II</li> 
<li> -[x] Sword Art Online: Alicization</li> 
<li> -[x] Tales From Earthsea</li> 
<li> -[x] Tales of Zestiria the X</li> 
<li> -[ ] Tales of the Abyss</li> 
<li> -[x] Tamako Love Story</li> 
<li> -[x] Tamako Market</li> 
<li> -[x] Tanaka-kun wa Itsumo Kedaruge</li> 
<li> -[x] Tari Tari</li> 
<li> -[x] Tate no Yuusha no Nariagari</li> 
<li> -[ ] Telepathy Shoujo Ran</li> - X
<li> -[x] Tensei Shitara Slime Datta Ken</li> 
<li> -[x] The Big O</li>
<li> -[x] The_Book of Bantorra</li> 
<li> -[ ] The Five Star Stories</li> - X
<li> -[ ] The Rolling Girls</li> - X
<li> -[ ] The Sky Crawlers</li> 
<li> -[ ] Thermae Romae</li> 
<li> -[ ] Tiger & Bunny</li> 
<li> -[ ] Toaru Kagaku no Accelerator</li> 
<li> -[x] Toaru Kagaku no Railgun</li> 
<li> -[x] Toaru Kagaku no Railgun S</li> 
<li> -[x] Toaru Majutsu no Index</li> 
<li> -[x] Toaru Majutsu no Index II</li> 
<li> -[ ] Toaru Majutsu no Index III</li> 
<li> -[ ] Tokimeki Tonight</li> 
<li> -[x] Tokyo Ghoul</li>
<li> -[ ] Tokyo Ghoul Root A</li> 
<li> -[ ] Tokyo Godfathers</li> 
<li> -[x] Tokyo Ravens</li> 
<li> -[ ] Tonari no Seki-kun</li> 
<li> -[x] Tonari no Totoro</li> 
<li> -[x] Trigun</li>
<li> -[ ] Trinity Blood</li> - X 
<li> -[x] Trinity Seven</li> 
<li> -[ ] Tsubasa Shunraiki</li> 
<li> -[ ] Tsubasa Tokyo Revelations</li> 
<li> -[x] Tsugumomo</li> 
<li> -[x] Tsuredure Children</li> 
<li> -[ ] Tsuritama</li> 
<li> -[ ] Uchiage Hanabi (2017)</li> 
<li> -[x] Uchouten Kazoku</li> 
<li> -[ ] Uchuu Senkan Yamato</li> 
<li> -[ ] Uchuu Senkan Yamato 2</li> 
<li> -[x] Uchuu Senkan Yamato 2199</li> 
<li> -[ ] Uchuu Senkan Yamato 3</li> 
<li> -[ ] Uchuu Show e Youkoso</li> 
<li> -[ ] Uchuu no Stellvia</li> 
<li> -[ ] Ultraman Orb</li> 
<li> -[ ] Ultraman R B</li> 
<li> -[ ] Urara Meirochou</li> 
<li> -[x] Usagi Drop</li> 
<li> -[x] Utawarerumono</li> 
<li> -[x] Utawarerumono Itsuwari no Kamen</li> 
<li> -[x] Vinland Saga</li> 
<li> -[ ] Violet Evergarden</li> 
<li> -[x] Wagaya no Oinari-sama</li> 
<li> -[ ] Watashi Ga Motete Dou Sunda</li> 
<li> -[ ] Whisper of the Heart</li> 
<li> -[ ] Wonder Egg Priority</li> 
<li> -[x] World Trigger</li> 
<li> -[x] Yakusoku no Neverland</li> 
<li> -[ ] Yamada-kun to 7-nin no Majo</li> - X
<li> -[ ] Yojouhan Shinwa Taikei</li> 
<li> -[ ] Yokohama Kaidashi Kikou</li>  - X
<li> -[x] Youjou Senki</li> 
<li> -[ ] Youkai Watch</li> 
<li> -[x] Youkoso Jitsuryoku Shijou Shugi no Kyoushitsu e</li> 
<li> -[x] Your Name</li> 
<li> -[x] Yu Yu Hakusho</li> 
<li> -[ ] Yu-Gi-Oh! 5D's</li> 
<li> -[ ] Yu-Gi-Oh! ARC-V</li> 
<li> -[x] Yumekui Merry</li> 
<li> -[ ] Yurikuma Arashi</li> - X
<li> -[ ] Yuru Camp</li> 
<li> -[ ] Yuru Yuri S2</li> 
<li> -[ ] Yuru Yuri San Hai!</li> 
<li> -[ ] Zero kara Hajimeru Mahou no Sho</li> 
<li> -[x] Zero no Tsukaima</li> 
<li> -[x] Zetsuen no Tempest</li> 
<li> -[x] Zoids Wild</li> 
<li> -[ ] Zoku Owarimonogatari</li> 
<li> -[ ] ef - a tale of memories</li> 
</ul>

## Things to do while cleaning the data
<ul>
<li> -[x] Remove/Merge duplicate jp_text to eng_text mappings </li>
<li> -[x] Remove words inside {} and <> in jp_text and en_text</li>
<li> -[x] Remove rows where en_text has less than 3 characters length </li>
<li> -[x] Remove rows with score 0 and number of words greater than 1 </li>
<li> Normalize English translation of duplicate Japanese text i.e same jp text should have same english translation</li>
	<ol>
	<li>Check for Named Entity Tags in the original text and translated text (sanity checks)</li>
	</ol>
</ul>