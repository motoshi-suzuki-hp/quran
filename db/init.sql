-- Create phrases table
CREATE TABLE IF NOT EXISTS phrases (
  id INT AUTO_INCREMENT PRIMARY KEY,
  surah_id INT NOT NULL,
  ayah_id INT NOT NULL,
  text TEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  phoneme TEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  audio_path VARCHAR(255) NOT NULL
) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;

-- Insert initial data
INSERT INTO phrases (surah_id, ayah_id, text, phoneme, audio_path) VALUES
(1, 1, 'بِسْمِ اللهِ الرَّحْمٰنِ الرَّحِيْمِ', 'bɪsmɪ llɑːhɪ rrɑħmɑːnɪ rrɑħiːm', 'surah_1_ayah_1'),
(1, 2, 'الْحَمْدُ لِلَّهِ رَبِّ الْعَالَمِينَ', 'ʔalħamdu lillɑːhi rabbɪ ʔalʕɑːlɑmiːn', 'surah_1_ayah_2'),
(1, 3, 'الرَّحْمٰنِ الرَّحِيمِ', 'ʔɑrrɑħmɑːni ʔɑrrɑħiːm', 'surah_1_ayah_3'),
(1, 4, 'مَالِكِ يَوْمِ الدِّينِ', 'mɑːlikɪ jawmi ʔɑddiːn', 'surah_1_ayah_4'),
(1, 5, 'إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ', 'ʔijjɑːka naʕbudu waʔijjɑːka nastaʕiːn', 'surah_1_ayah_5'),
(1, 6, 'ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ', 'ʔihdɪnɑː ʔɑṣṣɪrɑːṭɑ ʔɑlmustaqiːm', 'surah_1_ayah_6'),
(1, 7, 'صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ', 'ṣɪrɑːṭɑ ʔɑllɑðɪːna ʔanʕamta ʕalɑyhim ɣajrɪ ʔɑlmɑɣðuːbi ʕalɑyhim walɑː ʔɑḍḍɑːlliːn', 'surah_1_ayah_7');

-- INSERT INTO phrases (surah_id, ayah_id, text, phoneme, audio_path) VALUES
-- (114, 1, 'قُلْ أَعُوذُ بِرَبِّ ٱلنَّاسِ', 'qul ʔaʕuːðu birabbi ʔɑnnɑːs', 'surah_114_ayah_1'),
-- (114, 2, 'مَلِكِ ٱلنَّاسِ', 'maliki ʔɑnnɑːs', 'surah_114_ayah_2'),
-- (114, 3, 'إِلَـٰهِ ٱلنَّاسِ', 'ʔilaːhi ʔɑnnɑːs', 'surah_114_ayah_3'),
-- (114, 4, 'مِن شَرِّ ٱلْوَسْوَاسِ ٱلْخَنَّاسِ', 'min ʃarri ʔalwaswaːsi ʔalxannaːs', 'surah_114_ayah_4'),
-- (114, 5, 'ٱلَّذِى يُوَسْوِسُ فِى صُدُورِ ٱلنَّاسِ', 'ʔallaði juwaswisu fɪː ṣuduːri ʔɑnnɑːs', 'surah_114_ayah_5'),
-- (114, 6, 'مِنَ ٱلْجِنَّةِ وَٱلنَّاسِ', 'mina ʔaljinnati waʔɑnnɑːs', 'surah_114_ayah_6');
