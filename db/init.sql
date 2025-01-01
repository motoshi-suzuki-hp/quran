-- Create phrases table
CREATE TABLE IF NOT EXISTS phrases (
  id INT AUTO_INCREMENT PRIMARY KEY,
  surah_id INT NOT NULL,
  ayah_id INT NOT NULL,
  text TEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  phoneme TEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL
) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;

-- Insert initial data
INSERT INTO phrases (surah_id, ayah_id, text, phoneme) VALUES
(1, 1, 'بِسْمِ اللهِ الرَّحْمٰنِ الرَّحِيْمِ', 'bɪsmɪ llɑːhɪ rrɑħmɑːnɪ rrɑħiːm'),
(1, 2, 'الْحَمْدُ لِلَّهِ رَبِّ الْعَالَمِينَ', 'ʔalħamdu lillɑːhi rabbɪ ʔalʕɑːlɑmiːn'),
(1, 3, 'الرَّحْمٰنِ الرَّحِيمِ', 'ʔɑrrɑħmɑːni ʔɑrrɑħiːm'),
(1, 4, 'مَالِكِ يَوْمِ الدِّينِ', 'mɑːlikɪ jawmi ʔɑddiːn'),
(1, 5, 'إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ', 'ʔijjɑːka naʕbudu waʔijjɑːka nastaʕiːn'),
(1, 6, 'ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ', 'ʔihdɪnɑː ʔɑṣṣɪrɑːṭɑ ʔɑlmustaqiːm'),
(1, 7, 'صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ', 'ṣɪrɑːṭɑ ʔɑllɑðɪːna ʔanʕamta ʕalɑyhim ɣajrɪ ʔɑlmɑɣðuːbi ʕalɑyhim walɑː ʔɑḍḍɑːlliːn');

INSERT INTO phrases (surah_id, ayah_id, text, phoneme) VALUES
(114, 1, 'قُلْ أَعُوذُ بِرَبِّ ٱلنَّاسِ', 'qul ʔaʕuːðu birabbi ʔɑnnɑːs'),
(114, 2, 'مَلِكِ ٱلنَّاسِ', 'maliki ʔɑnnɑːs'),
(114, 3, 'إِلَـٰهِ ٱلنَّاسِ', 'ʔilaːhi ʔɑnnɑːs'),
(114, 4, 'مِن شَرِّ ٱلْوَسْوَاسِ ٱلْخَنَّاسِ', 'min ʃarri ʔalwaswaːsi ʔalxannaːs'),
(114, 5, 'ٱلَّذِى يُوَسْوِسُ فِى صُدُورِ ٱلنَّاسِ', 'ʔallaði juwaswisu fɪː ṣuduːri ʔɑnnɑːs'),
(114, 6, 'مِنَ ٱلْجِنَّةِ وَٱلنَّاسِ', 'mina ʔaljinnati waʔɑnnɑːs');
