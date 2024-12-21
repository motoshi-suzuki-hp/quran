-- Create phrases table
CREATE TABLE IF NOT EXISTS phrases (
  id INT AUTO_INCREMENT PRIMARY KEY,
  text TEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  phoneme TEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL
) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;

-- Insert initial data
INSERT INTO phrases (text, phoneme) VALUES
('بِسْمِ اللهِ الرَّحْمٰنِ الرَّحِيْمِ', 'bɪsmɪ llɑːhɪ rrɑħmɑːnɪ rrɑħiːm');
