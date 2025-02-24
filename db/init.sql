SET NAMES 'utf8mb4';

-- Create phrases table
CREATE TABLE IF NOT EXISTS phrases (
  id INT AUTO_INCREMENT PRIMARY KEY,
  surah_id INT NOT NULL,
  ayah_id INT NOT NULL,
  text TEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  phoneme TEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL
) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;

-- Insert surah 1 (Al-Fatihah) data (ChatGPT)
INSERT INTO phrases (surah_id, ayah_id, text, phoneme) VALUES
(1, 1, 'بِسْمِ اللهِ الرَّحْمٰنِ الرَّحِيْمِ', 'bɪsmɪ llɑːhɪ rrɑħmɑːnɪ rrɑħiːm'),
(1, 2, 'الْحَمْدُ لِلَّهِ رَبِّ الْعَالَمِينَ', 'ʔalħamdu lillɑːhi rabbɪ ʔalʕɑːlɑmiːn'),
(1, 3, 'الرَّحْمٰنِ الرَّحِيمِ', 'ʔɑrrɑħmɑːni ʔɑrrɑħiːm'),
(1, 4, 'مَالِكِ يَوْمِ الدِّينِ', 'mɑːlikɪ jawmi ʔɑddiːn'),
(1, 5, 'إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ', 'ʔijjɑːka naʕbudu waʔijjɑːka nastaʕiːn'),
(1, 6, 'ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ', 'ʔihdɪnɑː ʔɑṣṣɪrɑːṭɑ ʔɑlmustaqiːm'),
(1, 7, 'صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ', 'ṣɪrɑːṭɑ ʔɑllɑðɪːna ʔanʕamta ʕalɑyhim ɣajrɪ ʔɑlmɑɣðuːbi ʕalɑyhim walɑː ʔɑḍḍɑːlliːn');

-- Insert surah 1 (Al-Fatihah) data (recognition & phonemizer)
INSERT INTO phrases (surah_id, ayah_id, text, phoneme) VALUES
(2, 1, 'بسم الله الرحمن الرحيم', 'bismillaah ʔarɹaħmaan ʔarɹaħiːm'),
(2, 2, 'الْحَمْد لِلدَّايرَ مِلعلَمن', 'alħamd lidːaːjɹa milʕlamn'),
(2, 3, 'أررحمانرحيب', 'ʔrrħmaːnrħiːb'),
(2, 4, 'مَالِيكيمِدِ', 'maːliːkiːmidi'),
(2, 5, 'إِيَّا كَانَمُودُ وَإِيَا كَنَ ستَع', 'ʔiːaː kaːnamuːdu waʔiːaː kana staʕ'),
(2, 6, 'إِذْدِينَ الصِرَاقًامُستَقِ', 'ʔiðdiːna ʔas̪s̪i.ɹaːqaːmustaqi'),
(2, 7, 'صِرَاطًالَّذِينَا أَنَّعَمْتَلَ إِهِ غَمِيرلْمَضُو بِعَادَ إِهود إم', 's̪i.ɹaːt̪aːllaðiːnaː ʔannaʕamtala ʔihi ɣamiːrlmadˤu.ː biʕaːda ʔihuːd ʔim');
