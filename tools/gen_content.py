# -*- coding: utf-8 -*-
# Generator konten Matematika XI -> src/content.ts (shell BI/PKN, tema merah).
# Materi & langkah dari repo lama (tools/mtk-data/*.json), soal & penjelasan baru.
import re, json, html as h

CH  = json.load(open('tools/mtk-data/chapters.json', encoding='utf-8'))
RICH= json.load(open('tools/mtk-data/rich.json', encoding='utf-8'))
GUID= json.load(open('tools/mtk-data/guides.json', encoding='utf-8'))

# Rumus awal per topik (dari starting-formula.ts repo lama)
STARTING = {'1-2':('1-2',1),'1-3':('1-1',2),'1-5':('1-5',1),'2-1':('2-1',1),'2-2':('2-2',1),
 '3-1':('3-1',1),'3-2':('3-2',1),'4-1':('4-1',2),'5-4':('5-4',1),'5-7':('5-7',1),
 '5-8':('5-8',1),'5-10':('5-10',2),'5-11':('5-11',2)}

def strip_tags(s):
    s = re.sub(r'<[^>]+>', ' ', s)
    return re.sub(r'\s+', ' ', h.unescape(s)).strip().lower()

def section(sid, number, title, chips, lead, details, player):
    search = number + ' ' + title + ' ' + ' '.join(chips) + ' ' + strip_tags(lead) + ' ' + ' '.join(strip_tags(d['title'] + ' ' + d['html']) for d in details)
    search = re.sub(r'\s+', ' ', search).strip()
    chips_html = '<div class="term-chips">' + ''.join('<span>' + x + '</span>' for x in chips) + '</div>'
    search = re.sub(r"\\[a-zA-Z]+", " ", search)
    return {"id": sid, "number": number, "title": title, "lead": chips_html + lead.strip(), "details": details, "search": search, "player": player}

def d(title, html):
    return {"title": title, "html": html.strip()}

CHIPS = lambda *t: tuple(t)
TIP  = lambda isi: '<div class="tip-box"><b>CATATAN</b>' + isi + '</div>'
WARN = lambda isi: '<div class="warn-box"><b>JEBAKAN SOAL</b>' + isi + '</div>'
TBL  = lambda head, rows: ('<div class="table-scroll"><table><thead><tr>' + ''.join('<th>' + x + '</th>' for x in head) +
        '</tr></thead><tbody>' + ''.join('<tr>' + ''.join('<td>' + c + '</td>' for c in r) + '</tr>' for r in rows) + '</tbody></table></div>')

def q(qid, chapter, prompt, benar, explanation):
    opts = [{"id": qid + "-B", "html": "<p>Benar</p>", "text": "Benar"},
            {"id": qid + "-S", "html": "<p>Salah</p>", "text": "Salah"}]
    return {"id": qid, "chapter": chapter, "prompt": "<p>" + prompt + "</p>", "options": opts,
            "correct": qid + ("-B" if benar else "-S"), "explanation": "<p>" + explanation + "</p>", "group": chapter}

def pgk(qid, chapter, prompt, items, explanation):
    opts, correct = [], []
    for i, (txt, is_true) in enumerate(items, 1):
        oid = qid + "-" + str(i)
        opts.append({"id": oid, "html": "<p>" + txt + "</p>", "text": txt})
        if is_true: correct.append(oid)
    return {"id": qid, "chapter": chapter, "prompt": "<p>" + prompt + "</p>", "options": opts,
            "correct": correct[0], "correctSet": correct, "explanation": "<p>" + explanation + "</p>", "group": chapter}

# =============================== SOAL ===============================
BS = lambda qid, ch, p, ok, e: q(qid, ch, p, ok, e)
PG = lambda qid, ch, p, items, e: pgk(qid, ch, p, items, e)

ch1 = [
 BS("BD1-01",1,"Pada bunga tunggal, bunga setiap periode dihitung dari modal awal.", True,
    "Bunga tunggal selalu memakai modal awal sebagai dasar perhitungan setiap periode."),
 BS("BD1-02",1,"Pada bunga majemuk, dasar perhitungan bunga periode berikutnya adalah saldo yang sudah bertambah.", True,
    "Bunga majemuk menghitung bunga dari saldo terkini, sehingga bunga ikut menghasilkan bunga."),
 BS("BD1-03",1,"Modal Rp2.000.000 dengan bunga tunggal 12% per tahun selama 6 bulan menghasilkan bunga Rp144.000.", False,
    "6 bulan = 0,5 tahun, jadi B = 2.000.000 × 12% × 0,5 = Rp120.000, bukan Rp144.000."),
 BS("BD1-04",1,"Untuk bunga tunggal, saldo akhir M<sub>n</sub> = M<sub>0</sub> + B dengan B = M<sub>0</sub> × i × n.", True,
    "Saldo akhir bunga tunggal adalah modal awal ditambah total bunga."),
 BS("BD1-05",1,"Konversi 72 hari ke tahun dengan basis 360 hari menghasilkan 0,25 tahun.", False,
    "72/360 = 0,2 tahun, bukan 0,25 tahun."),
 PG("BD1-06",1,"Pernyataan yang tepat mengenai bunga tunggal adalah …", [
    ("B = M<sub>0</sub> × i × n.", True),
    ("Besarnya bunga setiap periode tetap.", True),
    ("Saldo akhirnya M<sub>n</sub> = M<sub>0</sub>(1 + i)<sup>n</sup>.", False),
    ("Dasar perhitungannya adalah saldo yang berjalan.", False)],
    "Bunga tunggal: dasar perhitungan modal awal, bunga per periode tetap. Rumus pangkat adalah bunga majemuk."),
 PG("BD1-07",1,"M<sub>0</sub> = Rp5.000.000, bunga tunggal 10% per tahun, selama 2 tahun. Pernyataan yang benar …", [
    ("Bunga per tahun Rp500.000.", True),
    ("Total bunga dua tahun Rp1.000.000.", True),
    ("Saldo akhir Rp6.000.000.", True),
    ("Saldo tumbuh mengikuti pangkat waktu.", False)],
    "B/tahun = 5.000.000 × 10% = Rp500.000; dua tahun Rp1.000.000; M₂ = Rp6.000.000. Pertumbuhan tunggal bersifat linier."),
 PG("BD1-08",1,"Perbandingan bunga majemuk dan tunggal yang tepat …", [
    ("Bunga majemuk dihitung dari saldo terkini.", True),
    ("Untuk n ≥ 1, hasil majemuk tidak lebih kecil dari tunggal.", True),
    ("Bunga majemuk tidak memakai pangkat.", False),
    ("Bunga tunggal memakai rumus M<sub>0</sub>((1 + i)<sup>n</sup> − 1).", False)],
    "Majemuk: dasar saldo, rumus pangkat. Tunggal: dasar modal, tanpa pangkat."),
]
uk1 = [
 BS("UK1-01",1,"Bunga tunggal dapat dirumuskan B = M<sub>0</sub> × i × n.", True, "Itulah rumus bunga tunggal: modal × suku bunga × waktu."),
 BS("UK1-02",1,"Bunga tunggal Rp800.000 dengan i = 8% per tahun selama 5 tahun berasal dari modal Rp2.000.000.", True, "2.000.000 × 8% × 5 = Rp800.000 — pernyataan benar."),
 BS("UK1-03",1,"30 hari dengan basis 360 hari setara dengan 1/12 tahun.", True, "30/360 = 1/12 tahun."),
 BS("UK1-04",1,"Pada bunga majemuk, bunga yang sudah diperoleh ikut menghasilkan bunga pada periode berikutnya.", True, "Itulah ciri penumpukan (compounding) bunga majemuk."),
 BS("UK1-05",1,"M<sub>0</sub> = Rp4.000.000, majemuk 10% per tahun selama 2 tahun memberi M<sub>2</sub> = Rp4.840.000.", True, "M₂ = 4.000.000 × 1,1² = Rp4.840.000."),
 PG("UK1-06",1,"M<sub>0</sub> = Rp1.800.000, tunggal 15% per tahun, selama 8 bulan. Yang benar …", [
    ("Waktu = 8/12 tahun.", True),
    ("Bunganya Rp162.000.", True),
    ("Saldo akhirnya Rp1.962.000.", True),
    ("Suku bunga per bulan 15%/8.", False)],
    "n = 8/12; B = 1.800.000 × 15% × 8/12 = Rp162.000; saldo = Rp1.962.000. Suku bunga per bulan tetap 15%/12."),
 PG("UK1-07",1,"Ciri bunga majemuk yang tepat …", [
    ("Menggunakan faktor (1 + i)<sup>n</sup>.", True),
    ("Dasar perhitungan saldo terkini.", True),
    ("Selalu sama besar hasilnya dengan bunga tunggal.", False),
    ("Satuan i dan n harus konsisten.", True)],
    "Majemuk memakai (1 + i)ⁿ dengan satuan konsisten; hasilnya berbeda dari tunggal untuk n ≥ 2."),
 PG("UK1-08",1,"Konversi waktu berikut yang benar (basis 360 hari) …", [
    ("90 hari = 1/4 tahun.", True),
    ("2,5 tahun = 30 bulan.", True),
    ("Basis 360 boleh diganti 365 sesuka hati dalam soal.", False),
    ("18 bulan = 1,5 tahun.", True)],
    "90/360 = 1/4; 2,5 × 12 = 30 bulan; 18/12 = 1,5. Basis diikuti ketentuan soal, bukan diganti sembarangan."),
]
ch2 = [
 BS("BD2-01",2,"Anuitas adalah pembayaran berbesar sama tiap periode yang terdiri atas bunga dan pokok.", True,
    "Anuitas: angsuran tetap tiap periode, terdiri atas komponen bunga dan pokok."),
 BS("BD2-02",2,"Pada anuitas, porsi bunga tiap angsuran semakin besar dari waktu ke waktu.", False,
    "Porsi bunga justru mengecil karena sisa pinjaman berkurang; porsi pokok membesar."),
 BS("BD2-03",2,"Bunga pada angsuran pertama dihitung dari pinjaman awal.", True, "Angsuran pertama: bunga = pinjaman awal × i."),
 BS("BD2-04",2,"Pokok yang dibayar pada suatu angsuran = anuitas − bunga periode tersebut.", True, "Pokok = angsuran − bunga; itulah yang mengurangi sisa pinjaman."),
 BS("BD2-05",2,"Total bunga selama anuitas = seluruh pembayaran − pinjaman awal.", True, "Selisih total bayar dengan pinjaman memang seluruh bunganya."),
 PG("BD2-06",2,"Pernyataan yang tepat mengenai anuitas …", [
    ("A = M<sub>0</sub> · i / (1 − (1 + i)<sup>−n</sup>).", True),
    ("Bunga angsuran ke-n = sisa pinjaman sebelumnya × i.", True),
    ("Porsi pokok tiap angsuran semakin kecil.", False),
    ("Sisa pinjaman berkurang setiap angsuran.", True)],
    "Rumus anuitas benar; bunga dari sisa pinjaman; porsi pokok justru membesar; sisa pinjaman berkurang."),
 PG("BD2-07",2,"Pinjaman Rp10.000.000, anuitas bulanan Rp1.800.000, bunga 2% per bulan. Untuk angsuran pertama …", [
    ("Bunganya Rp200.000.", True),
    ("Pokoknya Rp1.600.000.", True),
    ("Sisa pinjaman menjadi Rp8.400.000.", True),
    ("Bunga angsuran kedua tetap Rp200.000.", False)],
    "Bunga₁ = 2% × 10jt = Rp200.000; pokok = 1,8jt − 200rb = Rp1,6jt; sisa Rp8,4jt. Bunga₂ = 2% × 8,4jt = Rp168.000."),
 PG("BD2-08",2,"Ciri anuitas yang benar …", [
    ("Besar angsuran tiap periode tetap.", True),
    ("Porsi bunga menurun.", True),
    ("Porsi pokok meningkat.", True),
    ("Sisa pinjaman bertambah setelah tiap angsuran.", False)],
    "Angsuran tetap; bunga turun, pokok naik, sisa pinjaman turun."),
]
uk2 = [
 BS("UK2-01",2,"Pada anuitas, komponen pokok dihitung dengan mengurangkan bunga dari anuitas.", True, "Pokok = anuitas − bunga periode tersebut."),
 BS("UK2-02",2,"Sisa pinjaman setelah tiap angsuran berkurang sebesar pokok yang dibayar.", True, "Yang mengurangi pinjaman adalah komponen pokoknya."),
 BS("UK2-03",2,"Pada anuitas, bunga angsuran berikutnya dihitung dari sisa pinjaman terbaru.", True, "Dasar hitung bunga selalu sisa pinjaman terkini."),
 BS("UK2-04",2,"Angsuran pertama anuitas Rp12.000.000 dengan bunga 1,5% per bulan memiliki bunga Rp180.000.", True, "1,5% × 12jt = Rp180.000."),
 BS("UK2-05",2,"Jika anuitas Rp2.400.000 dan bunga angsuran pertama Rp180.000, pokok angsuran pertamanya Rp2.220.000.", True, "2,4jt − 180rb = Rp2.220.000."),
 PG("UK2-06",2,"Sifat anuitas yang benar …", [
    ("Angsuran periode-ke-n terdiri atas bunga dan pokok.", True),
    ("Porsi bunga menurun tiap periode.", True),
    ("Porsi pokok menurun tiap periode.", False),
    ("Setelah angsuran terakhir sisa pinjaman nol.", True)],
    "Porsi pokok justru meningkat; sisa pinjaman lunas setelah angsuran terakhir."),
 PG("UK2-07",2,"Pinjaman Rp12.000.000, anuitas Rp2.400.000 per bulan, bunga 1,5% per bulan. Angsuran pertama …", [
    ("Bunga Rp180.000.", True),
    ("Pokok Rp2.220.000.", True),
    ("Sisa pinjaman Rp9.780.000.", True),
    ("Bunga angsuran kedua Rp180.000.", False)],
    "Bunga₂ = 1,5% × 9.780.000 = Rp146.700, bukan Rp180.000."),
 PG("UK2-08",2,"Terlampir pada anuitas yang tepat …", [
    ("Rumus anuitas memuat faktor (1 + i)<sup>−n</sup>.", True),
    ("Total bunga = total angsuran − pinjaman.", True),
    ("Bunga tiap periode dihitung dari pinjaman awal terus-menerus.", False),
    ("Sisa pinjaman berkurang setiap angsuran.", True)],
    "Bunga dihitung dari sisa pinjaman terkini, bukan dari pinjaman awal sepanjang waktu."),
]
ch3 = [
 BS("BD3-01",3,"Relasi disebut fungsi jika setiap anggota domain memiliki tepat satu pasangan.", True, "Definisi fungsi: satu domain, satu pasangan — tidak boleh bercabang."),
 BS("BD3-02",3,"Semua relasi antarhimpunan adalah fungsi.", False, "Relasi yang domain-nya bercabang ke banyak pasangan bukan fungsi."),
 BS("BD3-03",3,"Grafik fungsi selalu lulus uji garis vertikal: satu nilai x hanya memotong grafik di satu titik.", True, "Itulah uji garis vertikal untuk memastikan relasi grafik adalah fungsi."),
 BS("BD3-04",3,"Jika f(x) = 3x − 2, maka f(5) = 13.", True, "f(5) = 3(5) − 2 = 13."),
 BS("BD3-05",3,"Domain f(x) = √(x − 4) adalah semua bilangan real.", False, "Domainnya x ≥ 4 agar isi akar tidak negatif."),
 PG("BD3-06",3,"Relasi yang merupakan fungsi …", [
    ("(1,2), (2,4), (3,6).", True),
    ("(1,2), (1,5), (2,6).", False),
    ("(a,b), (b,c), (c,d).", True),
    ("(0,1), (0,2), (1,3).", False)],
    "Domain yang berulang dengan pasangan berbeda membuat relasi bukan fungsi."),
 PG("BD3-07",3,"Diketahui pasangan (1,3), (2,5), (4,7). Pernyataan yang benar …", [
    ("Domainnya {1, 2, 4}.", True),
    ("Rangenya {3, 5, 7}.", True),
    ("Anggota 2 memiliki dua pasangan.", False),
    ("Relasi ini adalah fungsi.", True)],
    "Domain = {1,2,4}, range = {3,5,7}; setiap domain satu pasangan → fungsi."),
 PG("BD3-08",3,"Ciri fungsi yang tepat …", [
    ("Lulus uji garis vertikal.", True),
    ("Setiap domain punya tepat satu hasil.", True),
    ("Boleh ada satu domain dengan dua hasil berbeda.", False),
    ("Grafik y = x merupakan fungsi.", True)],
    "Satu domain satu hasil; y = x lulus uji garis vertikal."),
]
uk3 = [
 BS("UK3-01",3,"Jika satu anggota domain dipasangkan dengan dua nilai berbeda, relasinya bukan fungsi.", True, "Domain bercabang ke dua hasil melanggar definisi fungsi."),
 BS("UK3-02",3,"Grafik lingkaran penuh adalah fungsi.", False, "Satu x memotong lingkaran di dua y — gagal uji garis vertikal."),
 BS("UK3-03",3,"Domain f(x) = √(x − 2) adalah x ≥ 2.", True, "Isi akar harus tak negatif: x − 2 ≥ 0."),
 BS("UK3-04",3,"Jika g(x) = x² + 1, maka g(3) = 10.", True, "g(3) = 9 + 1 = 10."),
 BS("UK3-05",3,"Range adalah himpunan semua nilai keluaran (hasil) dari fungsi.", True, "Range = kumpulan semua y yang dihasilkan."),
 PG("UK3-06",3,"Dari pasangan (2,1), (3,3), (5,3), pernyataan yang benar …", [
    ("Ini adalah fungsi.", True),
    ("Domainnya {2, 3, 5}.", True),
    ("Rangenya {1, 3}.", True),
    ("Anggota 3 dipetakan ke dua nilai.", False)],
    "Domain 3 hanya sekali — nilai range yang berulang tidak masalah; tetap fungsi."),
 PG("UK3-07",3,"Penentuan domain yang tepat …", [
    ("f(x) = √x → domain x ≥ 0.", True),
    ("f(x) = √(x + 6) → domain x ≥ −6.", True),
    ("f(x) = √(x − 9) → domain x ≥ 9.", True),
    ("f(x) = √(x + 1) → domain semua bilangan real.", False)],
    "Isi akar ≥ 0 menentukan domain; √(x+1) butuh x ≥ −1."),
 PG("UK3-08",3,"Penilaian fungsi yang benar …", [
    ("y = x² adalah fungsi.", True),
    ("x = y² bukan fungsi terhadap x.", True),
    ("Satu x boleh menghasilkan banyak y pada fungsi.", False),
    ("Fungsi boleh memiliki nilai range yang berulang.", True)],
    "y = x² lulus uji vertikal; x = y² tidak; range boleh berulang, domain tidak."),
]
ch4 = [
 BS("BD4-01",4,"Invers fungsi diperoleh dengan menukar x dan y, lalu menyelesaikan persamaan terhadap y.", True, "Itulah prosedur standar mencari f⁻¹."),
 BS("BD4-02",4,"(g ∘ f)⁻¹ = f⁻¹ ∘ g⁻¹.", True, "Invers komposisi: urutan dibalik."),
 BS("BD4-03",4,"Untuk fungsi yang punya invers, berlaku f⁻¹(f(x)) = x.", True, "Invers mengembalikan ke nilai awal."),
 BS("BD4-04",4,"Invers dari f(x) = 2x + 8 adalah f⁻¹(x) = (x − 8)/2.", True, "Tukar x,y: x = 2y + 8 → y = (x − 8)/2."),
 BS("BD4-05",4,"Setiap fungsi pasti memiliki fungsi invers.", False, "Invers ada jika fungsi bijektif (satu-satu dan pada)."),
 PG("BD4-06",4,"Sifat invers yang benar …", [
    ("f⁻¹ memetakan kembali range f ke domain f.", True),
    ("Grafik f dan f⁻¹ saling dicerminkan terhadap garis y = x.", True),
    ("(f⁻¹)⁻¹ = f.", True),
    ("Semua fungsi linear memiliki invers tanpa syarat.", False)],
    "Linear naik/turun murni punya invers, tetapi bukan semua fungsi (mis. konstanta tidak)."),
 PG("BD4-07",4,"Mencari invers f(x) = (3x + 6)/5. Langkah yang benar …", [
    ("Tulis x = (3y + 6)/5.", True),
    ("Kalikan kedua ruas dengan 5.", True),
    ("Kurangkan 6, lalu bagi dengan 3.", True),
    ("Hasilnya f⁻¹(x) = (5x + 6)/3.", False)],
    "x = (3y+6)/5 → 5x = 3y+6 → y = (5x − 6)/3. Hasil yang benar memuat −6, bukan +6."),
 PG("BD4-08",4,"f(x) = x + 2 dan g(x) = 3x. Pernyataan yang benar …", [
    ("(g ∘ f)(x) = 3x + 6.", True),
    ("(g ∘ f)⁻¹(x) = (x − 6)/3.", True),
    ("(g ∘ f)⁻¹ = f⁻¹ ∘ g⁻¹.", True),
    ("(g ∘ f)(1) = 8.", False)],
    "(g∘f)(1) = 3(1)+2 → g(3) = 9, bukan 8."),
]
uk4 = [
 BS("UK4-01",4,"Jika f(x) = 5x − 10, maka f⁻¹(x) = (x + 10)/5.", True, "x = 5y − 10 → y = (x + 10)/5."),
 BS("UK4-02",4,"Invers invers sebuah fungsi mengembalikan fungsi aslinya.", True, "(f⁻¹)⁻¹ = f."),
 BS("UK4-03",4,"Grafik f dan f⁻¹ simetris terhadap garis y = x.", True, "Pencermenan y = x adalah ciri grafik invers."),
 BS("UK4-04",4,"Fungsi konstan f(x) = 4 memiliki invers.", False, "Banyak x dipetakan ke satu nilai — tidak satu-satu, invers tidak ada."),
 BS("UK4-05",4,"Domain f⁻¹ adalah range dari f.", True, "Invers menukar peran domain dan range."),
 PG("UK4-06",4,"Tahap mencari invers yang benar …", [
    ("Ganti notasi f(x) dengan y.", True),
    ("Tukar peran x dan y.", True),
    ("Selesaikan persamaan untuk y.", True),
    ("Tukar kembali y menjadi x tanpa menyelesaikan.", False)],
    "Urutan benar: y → tukar → selesaikan. Hasil akhir dinyatakan sebagai f⁻¹(x)."),
 PG("UK4-07",4,"f(x) = (2x + 4)/5 dan g(x) = x − 1. Yang benar …", [
    ("f⁻¹(x) = (5x − 4)/2.", True),
    ("g⁻¹(x) = x + 1.", True),
    ("(g ∘ f)(2) = 3.", True),
    ("(g ∘ f)⁻¹(x) = (5x − 9)/2.", False)],
    "(g∘f)(x) = (2x+4)/5 − 1 = (2x −1)/5; inversnya (5x + 1)/2, bukan (5x − 9)/2."),
 PG("UK4-08",4,"Tentang invers, yang tepat …", [
    ("f⁻¹(f(x)) = x.", True),
    ("(g ∘ f)⁻¹ = f⁻¹ ∘ g⁻¹.", True),
    ("Invers hanya ada untuk fungsi bijektif.", True),
    ("Invers menggandakan nilai domain dua kali.", False)],
    "Tiga sifat pertama benar; pernyataan terakhir tidak bermakna."),
]
ch5 = [
 BS("BD5-01",5,"Orde matriks ditulis banyak baris × banyak kolom.", True, "Matriks dengan 2 baris 3 kolom berorde 2 × 3."),
 BS("BD5-02",5,"Jika A = [[1,2],[3,4]], maka det A = 1×4 − 2×3 = −2.", True, "Determinan 2×2 = ad − bc = 4 − 6 = −2."),
 BS("BD5-03",5,"Dua matriks dikatakan sama jika ordennya sama.", False, "Harus juga semua elemen seletak sama besar."),
 BS("BD5-04",5,"Matriks persegi memiliki invers hanya jika determinannya tidak nol.", True, "det = 0 berarti singular — invers tidak ada."),
 BS("BD5-05",5,"Untuk matriks persegi, perkalian AB selalu sama dengan BA.", False, "Perkalian matriks umumnya tidak komutatif."),
 PG("BD5-06",5,"Operasi matriks yang benar …", [
    ("Transpose Aᵀ menukar baris menjadi kolom.", True),
    ("k(A + B) = kA + kB untuk skalar k.", True),
    ("A + B hanya bisa jika orde A dan B sama.", True),
    ("A − B bisa dilakukan meski orde berbeda.", False)],
    "Penjumlahan/pengurangan menuntut orde sama; transpose dan skalar benar."),
 PG("BD5-07",5,"A = [[2,5],[1,3]]. Pernyataan yang benar …", [
    ("det A = 2×3 − 5×1 = 1.", True),
    ("Karena det ≠ 0, A memiliki invers.", True),
    ("det A = a + d − b − c.", False),
    ("Matriks dengan det = 0 disebut singular.", True)],
    "det = ad − bc; rumus a+d−b−c salah. det ≠ 0 → punya invers; det = 0 → singular."),
 PG("BD5-08",5,"A = [[2,5],[1,3]] dengan det A = 1. Pernyataan yang benar …", [
    ("A⁻¹ = 1/det × [[3,−5],[−1,2]].", True),
    ("A⁻¹ = [[3,−5],[−1,2]].", True),
    ("Elemen −5 berasal dari −b.", True),
    ("A⁻¹ = [[3,5],[1,2]].", False)],
    "Invers 2×2: 1/det × [[d,−b],[−c,a]] = [[3,−5],[−1,2]]."),
]
uk5 = [
 BS("UK5-01",5,"Matriks [[1,2,3],[4,5,6]] berorde 2 × 3.", True, "2 baris, 3 kolom."),
 BS("UK5-02",5,"Aᵀ dari [[1,2],[3,4]] adalah [[1,3],[2,4]].", True, "Transpose menukar baris menjadi kolom."),
 BS("UK5-03",5,"Jika det suatu matriks persegi nol, matriks itu disebut singular.", True, "Singular = tidak punya invers."),
 BS("UK5-04",5,"Perkalian matriks AB terdefinisi hanya jika banyak kolom A sama dengan banyak baris B.", True, "Syarat perkalian matriks."),
 BS("UK5-05",5,"A⁻¹ · A = I (matriks identitas).", True, "Definisi invers: hasil kali dengan aslinya adalah identitas."),
 PG("UK5-06",5,"Untuk A = [[3,1],[2,4]], yang benar …", [
    ("det A = 10.", True),
    ("A punya invers karena det ≠ 0.", True),
    ("det A = 3×4 − 1×2.", True),
    ("A adalah matriks singular.", False)],
    "det = 12 − 2 = 10 ≠ 0 → tidak singular, punya invers."),
 PG("UK5-07",5,"Invers 2×2 [[a,b],[c,d]] memakai pola …", [
    ("Skala 1/(ad − bc).", True),
    ("Diagonal utama ditukar dan tetap.", True),
    ("Diagonal sisi bertanda negatif.", True),
    ("Semua elemen tetap tanpa perubahan.", False)],
    "Pola: 1/det × [[d,−b],[−c,a]] — diagonal utama ditukar, sisi diberi negatif."),
 PG("UK5-08",5,"Matriks B = [[4,2],[2,1]] …", [
    ("det B = 0.", True),
    ("B singular.", True),
    ("B tidak memiliki invers.", True),
    ("B punya invers karena persegi.", False)],
    "det = 4−4 = 0 → singular, tidak ada invers walau persegi."),
]

questions = ch1 + uk1 + ch2 + uk2 + ch3 + uk3 + ch4 + uk4 + ch5 + uk5

# =============================== SECTIONS ===============================
# ---------- konversi TeX mentah -> teks unicode rapi untuk kartu ----------
SUB = str.maketrans('0123456789+-=()nxab', '₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎ₙₓₐᵦ')
SUP = str.maketrans('0123456789+-=()nx', '⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾ⁿˣ')

def plain_tex(s):
    if not isinstance(s, str):
        return s
    t = s
    t = re.sub(r'\\mathbb\s*\{?R\}?', ' bilangan real ', t)
    t = re.sub(r'\\begin\{(aligned|pmatrix|cases|array)\}', '', t)
    t = t.replace('\\end{aligned}', '').replace('\\end{pmatrix}', '').replace('\\end{cases}', '').replace('\\end{array}', '')
    t = re.sub(r'\\arraystretch\{[^}]*\}|\\def[^\\]*(\\\\)?', '', t)
    t = re.sub(r'\\qquad|\\quad', ',  ', t)
    t = t.replace('\\,', ' ').replace('\\;', ' ').replace('\\!', '').replace('&', ' ')
    # \frac{A}{B} dan \fracAB
    def frac(m):
        a, b = m.group(1), m.group(2)
        a = a if re.fullmatch(r'[0-9a-zA-Z]+', a) else '(' + a + ')'
        b = b if re.fullmatch(r'[0-9a-zA-Z]+', b) else '(' + b + ')'
        return a + '/' + b
    for _ in range(3):
        t = re.sub(r'\\frac\s*\{([^{}]+)\}\s*\{([^{}]+)\}', frac, t)
        t = re.sub(r'\\frac\s*(\d|[a-zA-Z])\s*(\d|[a-zA-Z])', r'\1/\2', t)
    t = re.sub(r'\\sqrt\s*\{([^{}]+)\}', r'√(\1)', t)
    t = re.sub(r'\\sqrt\s*(\d|[a-zA-Z])', r'√\1', t)
    t = re.sub(r'\^\{([^{}]+)\}', lambda m: '^' + m.group(1).translate(SUP), t)
    t = re.sub(r'\^([0-9a-zA-Z])', lambda m: m.group(1).translate(SUP), t)
    t = re.sub(r'_\{([^{}]+)\}', lambda m: m.group(1).translate(SUB), t)
    t = re.sub(r'_([0-9a-zA-Z])', lambda m: m.group(1).translate(SUB), t)
    t = t.replace('\\ne', '≠').replace('\\circ', '∘').replace('\\times', '×').replace('\\le', '≤').replace('\\ge', '≥').replace('\\cdot', '·')
    t = re.sub(r'\\[a-zA-Z]+', ' ', t)
    t = t.replace('{', '').replace('}', '').replace('$', '')
    t = re.sub(r'\s{2,}', ' ', t).strip()
    t = t.replace(' ,', ',').replace(' .', '.')
    return t

COLORS = ['#b03a2b', '#b98a1e', '#2e7d74', '#7d4b8e']  # hasil/utama, gold, teal, plum
def katex_batch(texs):
    import subprocess
    r = subprocess.run(['node', 'tools/kx.cjs'], input=json.dumps({'texs': texs}).encode(), capture_output=True)
    try:
        return json.loads(r.stdout.decode())['out']
    except Exception:
        return [None] * len(texs)

def colorize_formula(f_tex):
    """B=M_0\times i\times n -> per-token warna. None jika tak sederhana."""
    if not f_tex or '\\begin' in f_tex or '=' not in f_tex:
        return None
    lhs, _, rhs = f_tex.partition('=')
    if '=' in rhs or lhs.count('=') > 1:
        return None
    parts = re.split(r'\\times|\\cdot', rhs)
    if not (2 <= len(parts) <= 4):
        return None
    if any(('\\' in p and '\\left' not in p and '\\right' not in p) for p in parts):
        return None
    out = '\\textcolor{%s}{%s}=%s' % (COLORS[0], lhs.strip(),
        '\\times'.join('\\textcolor{%s}{%s}' % (COLORS[(i + 1) % 4], p.strip()) for i, p in enumerate(parts)))
    return out

def colorize_step(step_tex, f_tex):
    """Row substitusi angka diberi warna simbol pada posisi sama. None jika tak cocok."""
    if not f_tex or '\\begin' in f_tex:
        return None
    lhs, _, rhs = f_tex.partition('=')
    ftoks = [p.strip() for p in re.split(r'\\times|\\cdot', rhs) if p.strip()]
    if not (2 <= len(ftoks) <= 4) or '=' in rhs:
        return None
    m = re.match(r'\\begin\{aligned\}(.+)\\end\{aligned\}$', step_tex or '', re.S)
    if not m:
        return None
    rows = [r.strip() for r in re.split(r'\\\\', m.group(1)) if r.strip()]
    if not rows:
        return None
    r0 = rows[0].replace('&', '')
    rl, _, rr = r0.partition('=')
    stoks = [p.strip() for p in re.split(r'\\times|\\cdot', rr) if p.strip()]
    if len(stoks) != len(ftoks):
        return None
    # token langkah harus murni angka
    num = re.compile(r'^[\d.,{}()\s]+|[0-9]')
    for p in stoks:
        if re.search(r'[A-Za-z]', p.replace('{,}', '')):
            return None
    new_rows = []
    for i, row in enumerate(rows):
        if i == 0:
            _, _, rr2 = row.replace('&', '').partition('=')
            toks = [p.strip() for p in re.split(r'\\times|\\cdot', rr2) if p.strip()]
            rebuilt = '\\textcolor{%s}{%s}&=%s' % (COLORS[0], rl.strip() or lhs.strip(),
                '\\times'.join('\\textcolor{%s}{%s}' % (COLORS[(j + 1) % 4], t) for j, t in enumerate(toks)))
            new_rows.append(rebuilt)
        else:
            core = row.replace('&', '')
            _, _, val = core.partition('=')
            val = val.strip()
            if re.search(r'[A-Za-z]', val.replace('{,}', '')):
                return None
            amp = '&' if row.lstrip().startswith('&') else ''
            new_rows.append('%s=\\textcolor{%s}{%s}' % (amp, COLORS[0], val))
    return '\\begin{aligned}%s\\end{aligned}' % '\\\\'.join(new_rows)

def colorize_step_gold(step_tex):
    """Fallback universal: angka soal -> emas, nilai akhir murni -> merah."""
    m = re.match(r'\\begin\{aligned\}(.+)\\end\{aligned\}$', step_tex or '', re.S)
    if not m:
        return None
    rows = [r.strip() for r in re.split(r'\\\\', m.group(1)) if r.strip()]
    if not rows or any('\\textcolor' in r for r in rows):
        return None
    num_re = re.compile(r'(?<![\w{])\d+(?:\{\,\}\d+)*(?![\w}])')
    def paint(row, color):
        return num_re.sub(lambda mm: '\\textcolor{%s}{%s}' % (color, mm.group(0)), row)
    out = []
    for i, row in enumerate(rows):
        core = row.replace('&', '').strip()
        _, _, val = core.partition('=')
        val = val.strip()
        is_final = re.fullmatch(r'[\d.,]+(?:\{\,\}[\d.]+)*', val or '')
        if is_final and '=' in core:
            amp = '&' if row.lstrip().startswith('&') else ''
            out.append('%s=\\textcolor{%s}{%s}' % (amp, COLORS[0], val))
        else:
            out.append(paint(row, COLORS[1]))
    if not any('\\textcolor' in r for r in out):
        return None
    return '\\begin{aligned}%s\\end{aligned}' % '\\\\'.join(out)

def parse_vb(scene_html):
    m = re.search(r'viewBox="[^"]*?([\-\d.]+)\s+([\-\d.]+)\s+([\d.]+)\s+([\d.]+)"', scene_html or '')
    return [float(m.group(3)), float(m.group(4))] if m else [500, 360]

def build_sections(c):
    secs = []
    for t in c['topics']:
        rich = RICH.get(t['id'], {}); guid = GUID.get(t['id'], {})
        chips = tuple(dict.fromkeys([s['title'] for s in t['steps'][:3]])) or (c['short'],)
        known = rich.get('known') or guid.get('known') or []
        idea  = rich.get('idea') or guid.get('idea') or ''
        check = rich.get('check') or guid.get('check') or ''
        avoid = guid.get('avoid') or ''
        route = guid.get('route') or []
        why   = rich.get('why') or []
        start_ref = STARTING.get(t['id'])
        if start_ref:
            ref_topic = next(tt for x in CH for tt in x['topics'] if tt['id'] == start_ref[0])
            start_html = ref_topic['formulas'][start_ref[1]]['html']
            start_tex = ref_topic['formulas'][start_ref[1]]['tex']
        else:
            start_html = t['formulas'][0]['html']
            start_tex = t['formulas'][0]['tex']
        details = []
        if t['id'] in ('1-1', '2-1', '3-1', '4-1', '5-1') and c.get('legendHtml'):
            details.append(d("Arti simbol yang dipakai", '<div class="mtk-legend">' + c['legendHtml'] + '</div>'))
        det1 = ''
        if known: det1 += TBL(["Simbol", "Nilai"], [[k['symbol'], k['value']] for k in known])
        if idea: det1 += '<p><strong>Inti strategi:</strong> ' + idea + '</p>'
        if det1: details.append(d("Diketahui & strategi", det1))
        det2 = ''
        for f in t['formulas']:
            det2 += '<div class="mtk-formula"><b>' + f['label'] + '</b><div class="math-scroll">' + f['html'] + '</div></div>'
        if det2: details.append(d("Rumus inti", det2))
        if route: details.append(d("Alur penyelesaian", '<ol class="mtk-route">' + ''.join('<li><span>' + str(i+1).zfill(2) + '</span>' + x + '</li>' for i, x in enumerate(route)) + '</ol>'))
        det4 = t['finishHtml']
        if check: det4 += '<p><strong>Periksa kembali:</strong> ' + check + '</p>'
        details.append(d("Hasil akhir", det4))
        if avoid: details.append(d("Jebakan soal", WARN('<p>' + avoid + '</p>')))
        # ---- player v2: papan pengerjaan berwarna ----
        given, goal = [], ''
        for k in (known or []):
            sym = str(k.get('symbol', ''))
            val = str(k.get('value', ''))
            if 'Cari' in sym or 'Ditanya' in sym:
                goal = plain_tex(val)
            else:
                given.append({"sym": sym, "val": plain_tex(val)})
        if not goal:
            goal = 'Jawab pertanyaan soal.'
        f_col = colorize_formula(start_tex)
        step_texs = []
        for s in t['steps']:
            cstep = colorize_step(s.get('tex', ''), start_tex) or colorize_step_gold(s.get('tex', ''))
            step_texs.append(cstep or '')
        renders = katex_batch([c for c in ([f_col] if f_col else []) + [x for x in step_texs if x]])
        ridx = 0
        f_row = None
        if f_col:
            f_row = renders[ridx]; ridx += 1
        step_htmls = []
        for s, cstep in zip(t['steps'], step_texs):
            step_htmls.append(renders[ridx] if cstep else None)
            if cstep: ridx += 1
        rows = []
        for i, s in enumerate(t['steps']):
            rows.append({"title": s['title'], "math": step_htmls[i] if step_htmls[i] else s['mathHtml'],
                         "colored": bool(step_htmls[i]),
                         "tip": plain_tex(s.get('tipPlain') or strip_tags(s.get('tipHtml', ''))),
                         "why": why[i] if i < len(why) else ''})
        player = {"scene": t['scene'], "vb": parse_vb(t['scene']), "soal": plain_tex(t.get('questionPlain', '')),
                  "given": given, "goal": goal, "fRow": f_row if f_row else start_html, "fColored": bool(f_col),
                  "finish": t['finishHtml'], "finishPlain": plain_tex(t.get('finishPlain', '')), "rows": rows}
        lead = '<p><strong>Soal:</strong> ' + t['questionHtml'] + '</p>'
        secs.append(section('m' + t['id'], t['number'], t['title'], chips, lead, details, player))
    return secs

sections_by_ch = {c['id']: build_sections(c) for c in CH}

META = {
 1: {"fullTitle": "Bunga", "subtitle": "Bunga tunggal · majemuk · konversi waktu",
     "example": "Modal Rp10.000.000, bunga 18% per tahun → bunga satu tahun Rp1.800.000.",
     "translation": "Bunga tunggal selalu dari modal awal: B = M₀ × i × n."},
 2: {"fullTitle": "Anuitas", "subtitle": "Angsuran tetap · bunga · pokok · sisa pinjaman",
     "example": "Pinjaman Rp10.000.000, anuitas Rp1.800.000 per bulan, bunga 2% per bulan.",
     "translation": "Angsuran tetap; bunga turun, pokok naik, sisa pinjaman berkurang."},
 3: {"fullTitle": "Relasi & Fungsi", "subtitle": "Domain · range · uji garis vertikal · substitusi",
     "example": "f(x) = 3x − 2 → f(5) = 13.",
     "translation": "Fungsi: satu domain, tepat satu pasangan — lulus uji garis vertikal."},
 4: {"fullTitle": "Fungsi Invers", "subtitle": "Menukar x dan y · invers komposisi",
     "example": "f(x) = 2x + 8 → f⁻¹(x) = (x − 8)/2.",
     "translation": "Invers: tukar x dan y, selesaikan untuk y."},
 5: {"fullTitle": "Matriks", "subtitle": "Orde · operasi · determinan · invers",
     "example": "det [[1,2],[3,4]] = 4 − 6 = −2.",
     "translation": "Invers 2×2: 1/det × [[d,−b],[−c,a]] — ada hanya jika det ≠ 0."},
}

chapters = []
q_by_ch = {}
for qq in questions: q_by_ch.setdefault(qq["chapter"], []).append(qq["id"])
for c in CH:
    m = META[c['id']]
    chapters.append({"id": c['id'], "title": c['short'], "fullTitle": m['fullTitle'], "subtitle": m['subtitle'],
                     "intro": c.get('intro', ''), "example": m['example'], "translation": m['translation'],
                     "sections": sections_by_ch[c['id']], "questions": q_by_ch[c['id']]})

summary = """
<h3>Bunga</h3>
<ul><li><strong>Tunggal:</strong> B = M₀ × i × n; Mₙ = M₀ + B; dasar hitung modal awal.</li><li><strong>Majemuk:</strong> dasar saldo terkini; Bₙ = M₀((1 + i)ⁿ − 1).</li><li><strong>Konversi waktu:</strong> hari/360, bulan/12 — satuan i dan n harus konsisten.</li></ul>
<h3>Anuitas</h3>
<ul><li>Angsuran tetap = bunga + pokok.</li><li>Bunga angsuran = sisa pinjaman sebelumnya × i.</li><li>Pokok = anuitas − bunga; porsi bunga turun, pokok naik.</li><li>A = M₀ · i / (1 − (1 + i)⁻ⁿ).</li></ul>
<h3>Relasi & Fungsi</h3>
<ul><li>Fungsi: setiap anggota domain punya tepat satu pasangan.</li><li>Uji garis vertikal untuk grafik.</li><li>Domain akar: isi akar ≥ 0.</li></ul>
<h3>Fungsi Invers</h3>
<ul><li>Cari invers: tukar x dan y, selesaikan untuk y.</li><li>(g ∘ f)⁻¹ = f⁻¹ ∘ g⁻¹; f⁻¹(f(x)) = x.</li><li>Invers ada jika fungsi bijektif.</li></ul>
<h3>Matriks</h3>
<ul><li>Orde = baris × kolom; sama jika orde dan semua elemen seletak sama.</li><li>det 2×2 = ad − bc; det = 0 → singular (tidak ada invers).</li><li>Invers 2×2 = 1/det × [[d,−b],[−c,a]]; A⁻¹A = I.</li></ul>
<div class="warn-box"><b>STRATEGI SOAL</b><p>Tulis <strong>diketahui</strong> dan <strong>ditanyakan</strong> lebih dulu, samakan <strong>satuan waktu</strong> dengan satuan suku bunga, bedakan <strong>bunga</strong> dengan <strong>saldo</strong>, dan periksa syarat sebelum memakai rumus (invers: bijektif; matriks: det ≠ 0).</p></div>
"""

course = {"chapters": chapters, "questions": questions, "summary": summary.strip(),
          "counts": {"chapters": len(chapters), "sections": sum(len(c["sections"]) for c in chapters), "questions": len(questions)}}
json_str = json.dumps(course, ensure_ascii=False, indent=1)
open("src/content.ts", "w", encoding="utf-8").write("import type { Course } from './types';\nexport const COURSE: Course = " + json_str + ";\n")
print("chapters:", len(chapters), "| sections:", course["counts"]["sections"], "| questions:", len(questions))
print("soal per bab:", [len(c["questions"]) for c in chapters])
uk_total = len([x for x in questions if x['id'].startswith('UK')])
print("bank uji kemampuan:", uk_total, "| PGK:", len([x for x in questions if x.get('correctSet')]))
