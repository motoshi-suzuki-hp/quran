SET NAMES 'utf8mb4';

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

-- Insert surah 2 (Al-Baqarah) data
INSERT INTO phrases (surah_id, ayah_id, text, phoneme) VALUES
(2, 1, 'الم', 'ʔalm'),
(2, 2, 'ذَٰلِكَ الْكِتَابُ لَا رَيْبَ فِيهِ هُدًى لِّلْمُتَّقِينَ', 'ðɑːlikɑː ʔalkitɑːbu lɑː rayba fīhɪ hudan lil-muttaqīn'),
(2, 3, 'الَّذِينَ يُؤْمِنُونَ بِالْغَيْبِ وَيُقِيمُونَ الصَّلَاةَ وَمِمَّا رَزَقْنَاهُمْ يُنفِقُونَ', 'ʔallɑðɪːna juʔminuːna bilɣajbi wa yuqimuːna ṣ-ṣalɑːta wa mimmɑː razaqnāhum yunfiqūn'),
(2, 4, 'وَالَّذِينَ يُؤْمِنُونَ بِمَا أُنزِلَ إِلَيْكَ وَمَا أُنزِلَ مِن قَبْلِكَ وَبِالْآخِرَةِ هُمْ يُوقِنُونَ', 'wa ʔallɑðɪːna yuʔminuːna bimɑː unzila ʔilajka wa mɑː unzila min qablika wa bilʔɑːxiɾati hum yuwaqinūn'),
(2, 5, 'أُو۟لَٰٓئِكَ عَلَىٰ هُدًى مِن رَّبِّهِمْ ۖ وَأُو۟لَٰٓئِكَ هُمُ الْمُفْلِحُونَ', 'ʔulɑːʔika ʕalɑː hudan min rabbihim wa ʔulɑːʔika humul mufliħūn');