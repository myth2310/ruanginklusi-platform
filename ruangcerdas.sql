-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 03, 2024 at 11:29 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ruangcerdas`
--

-- --------------------------------------------------------

--
-- Table structure for table `article`
--

CREATE TABLE `article` (
  `article_id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `image` varchar(255) DEFAULT NULL,
  `kategori` varchar(50) NOT NULL,
  `date` date NOT NULL,
  `slug` varchar(255) NOT NULL,
  `description` text NOT NULL,
  `summary` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `article`
--

INSERT INTO `article` (`article_id`, `title`, `image`, `kategori`, `date`, `slug`, `description`, `summary`) VALUES
(1, 'Strategi Pembelajaran Bagi Siswa Tunarungu', 'Strategi_Pembelajaran_Bagi_Siswa_Tunarungu.jpg', 'Pendidikan', '2024-02-28', 'strategi-pembelajaran-bagi-siswa-tunarungu', '<div>Pembelajaran untuk anak berkebutuhan khusus (Student With Special needs) membutuhkan suatu strategi tersendiri sesuai dengan kebutuhan masing – masing. Tunarungu (Communication disorder and deafness) adalah Individu yang memiliki hambatan dalam pendengaran baik permanen maupun tidak permanen, serta memiliki hambatan dalam berbicara sehingga mereka disebut Tunawicara.<br><br></div><div>Cara berkomunikasi dengan anak Tunarungu menggunakan Bahasa Isyarat dan Bahasa tubuh. Untuk abjad jari telah dipatenkan secara internasional , sedangkan untuk isyarat Bahasa berbeda-beda di setiap negara. Anak Tunarungu cenderung kesulitan dalam memahami konsep dari sesuatu yang abstrak. Berikut Identifikasi anak yang mengalami gangguan pendengaran<br><br></div><div>(Tunarungu) diantaranya yaitu :</div><ol><li>Tidak mampu mendengar</li><li>Terlambat perkembangan Bahasa</li><li>Sering menggunakan isyarat dalam berkomunikasi</li><li>Kurang/ tidak tanggap bila diajak bicara</li><li>Ucapan kata tidak jelas</li><li>Kualitas suara aneh/monoton.</li><li>Sering memiringkan kepala kepala dalam usaha mendengar</li><li>Banyak perhatian terhadap getaran</li><li>Keluar nanah dari kedua telinga</li><li>Terdapat kelainan organis telinga.</li></ol><div>Berikut ini strategi yang bisa digunakan untuk anak Tunarungu&nbsp; diantaranya yaitu :</div><ol><li><strong>Strategi Deduktif </strong>yaitu Sebuah pembelajaran dengan metode ceramah, tannya jawab dan simulasi</li><li><strong>Strategi Induktif</strong> yaitu Sebuah pembelajaran yang bersifat langsung sangat efektif untuk mengembangkan keterampilan berfikir tingkat tinggi dan Keterampilan berfikir kritis.</li><li><strong>Strategi Heuristic </strong>yaitu Pembelajaran yang menstimulus siswa agar aktif dalam proses pembelajaran, memahami materi pelajaran, memecahkan masalah, dan dapat mempresentasikannya dengan baik.</li><li><strong>Strategi Ekspositorik </strong>yaitu Pembelajaran yang menekankan kepada proses penyampaian materi secara verbal dari seorang guru kepada sekelompok siswa untuk menguasai materi pembelajaran secara optimal</li><li><strong>Strategi klasikal </strong>yaitu Pembelajaran yang mencakup di satu ruangan kelas dengan jumlah tertentu, waktu dan tempatnya sudah diatur oleh peraturan sekolah.</li><li><strong>Strategi Kelompok </strong>yaitu Rangkaian kegiatan belajar yang dilakukan oleh siswa dalam kelompok – kelompok tertentu untuk mencapai tujuan pembelajaran yang telah dirumuskan.</li><li><strong>Strategi Individual </strong>yaitu Pembelajaran yang memberikan kesempatan kepada peserta didik untuk menentukan sendiri waktu dan tempat belajar siswa indoor maupun outdoor.</li><li><strong>Strategi kooperatif </strong>yaitu Pembelajaran yang mengutamakan kerja sama dalam menyelesaikan permasalahan untuk menerapkan pengetahuan dan ketrampilan siswa.</li><li><strong>Strategi modifikasi perilaku (Behaviorisme) </strong>yaitu Pembelajaran yang dapat merubah perilaku siswa menjadi lebih baik dan sopan.</li></ol>', '<div>Pembelajaran untuk anak berkebutuhan khusus (Student With Special needs) membutuhkan suatu strategi tersendiri sesuai dengan kebutuhan masing – masing. Tunarungu'),
(2, '5 Media Pembelajaran Tunarungu Yang Bisa Diterapkan', '5_Media_Pembelajaran_Tunarungu_Yang_Bisa_Diterapkan.jpg', 'Edukasi', '2024-02-28', '5-media-pembelajaran-tunarungu-yang-bisa-diterapkan', '<div>Media pembelajaran tunarungu digunakan untuk mempermudah penyampaian materi kepada seseorang anak yang mengalami hambatan pendengaran sehingga anak tersebut dapat menguasai materi dengan baik. Sebelum menuju media yang digunakan, kita ulas terlebih dahulu siapakah tunarungu? Jadi tunarungu merupakan seseorang yang mengalami masalah pada sensori pendengaran atau indera pendengaran. Dengan hambatan yang ada, mereka (anak tunarungu) kesulitan untuk hidup seperti orang pada umumnya sehingga memerlukan layanan khusus untuk mengembangkan potensinya.<br><br></div><div>Menurut klasifikasinya, ketunarunguan terbagi menjadi ringan antara 15-30 dB, kemudian sedang antara 31-60 dB, untuk berat antara 61-90 dB, tuli sangat berat antara 91-120 dB, hingga tuli total dimana lebih dari 120 dB. Kemudian ada juga klasifikasi lain berdasarkan waktu terjadinya baik dari bawaan dan tunarungu setelah kelahiran. Agar pembelajaran efektif, dalam mengajar tunarungu harus menggunakan media yang membuat pembelajaran menjadi menyenangkan dan mudah diterima siswa. Berikut ini adalah media untuk mengajar tunarungu yang cocok dan bisa diterapkan.<br><br></div><div><strong>Media Pembelajaran Untuk Siswa Tunarungu</strong></div><div><strong>1</strong>. <strong>Benda Nyata</strong></div><div>Tunarungu mengalami hambatan pada pendengaran sehingga media pembelajaran yang digunakan lebih menekankan ke visual. Nah benda nyata merupakan salah satunya, dimana anak bisa melihat langsung mengenai benda yang dimaksud sambil disajikan nama bendanya melalui tulisan. Media ini bisa digunakan untuk mengajar materi berbagai hal seperti mengenal berbagai benda.<br><br></div><div><strong>2</strong>. <strong>Pias Kata</strong></div><div>Pias kata adalah media pembelajaran yang bisa digunakan untuk melatih anak tunarungu membuat kalimat. Biasanya dalam suatu kalimat terdapat kata yang kosong sehingga tugas anak untuk mencari kata yang tepat.<br><br><strong>3.</strong> <strong>Media Gambar</strong></div><div>Media gambar digunakan untuk mengenal materi nama-nama benda dimana digambar tersebut juga disertakan keterangan tulisan nama benda tersebut. Di kelas SDLB media ini sering digunakan misalnya anak berlatih belajar nama-nama hewan, nama-nama buah, dan nama benda lainnya<br><br><strong>4. Video</strong></div><div>Media video bisa menjadi pilihan dalam mengajar anak dengan hambatan pendengaran misalnya saja tentang fenomena alam seperti proses terjadinya hujan, maupuan proses gunung berapi meletus. Diamana tidak mungkin dijelaskan menggunakan metode ceramah.<br><br></div><div><strong>5.</strong> <strong>Cermin</strong></div><div>Mungkin anda bertanya kenapa cermin masuk media untuk mengajar tunarungu. Namun cermin disini bukan digunakan untuk merias diri ya. Alat ini bisa digunakan untuk mengajar anak mengenai PKPBI dalam pembelajaran anak hambatan pendengaran. Selain cermin biasanya digunakan juga alat lain seperti alat musik drum, rebana, suling, gong dll.<br><br></div><div>Itu tadi media pembelajaran yang bisa diterapkan untuk tunarungu, yang tentunya masih banyak media lain yang bisa digunakan atau bahka dibuat. Pemilihan media tersebut ditentukan berdasarkan materi yang akan disampaikan supaya tepat fungsinya. Demikian artikel ini semoga bermanfaat dan bisa menambah wawasan kita semua, terima kasih.</div>', '<div>Media pembelajaran tunarungu digunakan untuk mempermudah penyampaian materi kepada seseorang anak yang mengalami hambatan pendengaran sehingga anak tersebut dapat menguasai'),
(3, 'Ruanginklusi: Merajut Inklusivitas dalam Pembelajaran Anak Tunarungu', 'Ruanginklusi_Merajut_Inklusivitas_dalam_Pembelajaran_Anak_Tunarungu.png', 'Pendidikan', '2024-02-28', 'ruanginklusi:-merajut-inklusivitas-dalam-pembelajaran-anak-tunarungu', '<div>Di tengah gemuruh Era Teknologi, inovasi terus membentuk wajah pembelajaran modern. Kita berada di ambang perubahan signifikan, dan salah satu solusi terdepan yang layak diperhatikan adalah Sistem Ruanginklusi. Inovasi ini merupakah jawaban cerdas untuk menjembatani kesenjangan komunikasi yang mungkin dialami anak tunarungu dalam lingkungan kelas. Dengan memanfaatkan teknologi speech-to-text real-time, speech-to-sign language, dan text-to-sign language, Sistem Ruanginklusi menggagas era baru pembelajaran yang benar-benar inklusif.<br><br><strong>1. Terjemahan Suara ke Teks: Suara yang Merangkum Ilmu </strong><br>Sistem Ruanginklusi memanfaatkan kecanggihan teknologi speech-to-text untuk merubah setiap kata yang diucapkan di kelas menjadi teks secara langsung. Guru dapat berbicara dengan bebas, dan hasil konversi teks muncul secara real-time di layar, memastikan siswa tunarungu tidak lagi ketinggalan informasi penting.<br><br><strong>2. Bahasa Isyarat dari Suara: Harmoni Komunikasi Tanpa Batas</strong><br>Komunikasi verbal tanpa hambatan menjadi kenyataan dengan integrasi teknologi speech-to-sign language. Sistem ini menerjemahkan suara menjadi bahasa isyarat secara otomatis, memungkinkan guru berkomunikasi dengan kejelasan bahasa tanpa batasan. Bahasa isyarat menjadi jembatan yang menghubungkan guru dan siswa tunarungu.<br><br><strong>3. Teks Menjadi Bahasa Isyarat: Simfoni Inklusivitas</strong><br>Tidak hanya berhenti pada komunikasi verbal, Sistem Ruanginklusi juga mendukung konversi teks menjadi bahasa isyarat. Setiap teks yang ditampilkan di layar dapat dengan mudah dipahami melalui bahasa isyarat, memberikan alternatif komunikasi yang lebih kaya dan efektif.<br><br>Sistem Ruanginklusi membuka lembaran baru dalam pendidikan inklusif. Dengan menyatukan teknologi speech-to-text dan speech-to-sign language secara real-time, serta text-to-sign language, kita menciptakan landasan yang kokoh untuk pendidikan yang setara bagi semua. Inovasi ini adalah komitmen kita untuk menciptakan dunia di mana setiap anak memiliki kesempatan yang sama untuk tumbuh dan berkembang. Mari bersama-sama merangkai masa depan pendidikan yang lebih inklusif.</div>', '<div>Di tengah gemuruh Era Teknologi, inovasi terus membentuk wajah pembelajaran modern. Kita berada di ambang perubahan signifikan, dan salah satu');

-- --------------------------------------------------------

--
-- Table structure for table `sign`
--

CREATE TABLE `sign` (
  `sign_id` int(11) NOT NULL,
  `user_id` int(5) NOT NULL,
  `type_camera` varchar(100) NOT NULL,
  `voice` int(1) NOT NULL,
  `ip_camera` varchar(100) NOT NULL,
  `accept` int(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `sign`
--

INSERT INTO `sign` (`sign_id`, `user_id`, `type_camera`, `voice`, `ip_camera`, `accept`) VALUES
(1, 2, 'Internal', 0, '0', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `speech`
--

CREATE TABLE `speech` (
  `speech_id` int(11) NOT NULL,
  `user_id` int(5) NOT NULL,
  `type_camera` varchar(100) DEFAULT NULL,
  `ip_camera` varchar(100) DEFAULT NULL,
  `bahasa` varchar(100) NOT NULL,
  `accept` int(5) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `speech`
--

INSERT INTO `speech` (`speech_id`, `user_id`, `type_camera`, `ip_camera`, `bahasa`, `accept`) VALUES
(1, 2, 'Internal Camera', '0', 'id', 1);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `user_id` int(11) NOT NULL,
  `username` varchar(100) NOT NULL,
  `image` varchar(255) DEFAULT NULL,
  `email` varchar(100) NOT NULL,
  `institusi` varchar(100) NOT NULL,
  `no_hp` varchar(15) DEFAULT NULL,
  `alamat` varchar(225) DEFAULT NULL,
  `level` varchar(50) NOT NULL,
  `password` varchar(100) NOT NULL,
  `last_login` timestamp NULL DEFAULT NULL,
  `online_status` tinyint(1) DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`user_id`, `username`, `image`, `email`, `institusi`, `no_hp`, `alamat`, `level`, `password`, `last_login`, `online_status`) VALUES
(1, 'Admin-ruanginklusi', NULL, 'achmadmiftahudin2310@gmail.com', 'RuangInklusi', NULL, NULL, 'Admin', '4cc98a15312d88aa34b83acf57607de10308179df85b4a3b1959a7ccd501a38f', '2024-02-28 03:49:19', 0),
(2, 'Achmad Miftahudin', NULL, '19090137.miftahudin@student.poltektegal.ac.id', 'Bisadistartup', NULL, NULL, 'Pengguna', '20cc43ef1b92f746d6671e862060fe687d0c48ef49d7d3260d986e5715fa9ff4', '2024-03-02 12:46:32', 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `article`
--
ALTER TABLE `article`
  ADD PRIMARY KEY (`article_id`);

--
-- Indexes for table `sign`
--
ALTER TABLE `sign`
  ADD PRIMARY KEY (`sign_id`);

--
-- Indexes for table `speech`
--
ALTER TABLE `speech`
  ADD PRIMARY KEY (`speech_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `article`
--
ALTER TABLE `article`
  MODIFY `article_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `sign`
--
ALTER TABLE `sign`
  MODIFY `sign_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `speech`
--
ALTER TABLE `speech`
  MODIFY `speech_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
