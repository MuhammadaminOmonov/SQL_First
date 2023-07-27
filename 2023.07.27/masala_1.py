import mysql.connector
import datetime
from os import system


class Databaza:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="unkown" # o'zingizning parolingiz
        )
        self.cursor = self.mydb.cursor()

        self.dbConnection()
        self.createTable()
        self.insertData()

    def dbConnection(self):
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS drugs;")
        self.cursor.execute("USE drugs;")


    def createTable(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS medicine(
                id INTEGER,
                drug_name VARCHAR(255) NOT NULL,
                drug_company VARCHAR(255) NOT NULL,
                drug_datetime DATE NOT NULL,
                drug_country VARCHAR(255) NOT NULL,
                drug_price INTEGER NOT NULL
            );
        """)


    def insertData(self):
        self.cursor.execute(f"""
            insert into medicine (id, drug_name, drug_company, drug_datetime, drug_country, drug_price) values 
            (1, 'Grama Grass', 'Nelco Laboratories, Inc.', '2022-12-08', 'Japan', 825),
            (2, 'Diltiazem Hydrochloride', 'West-ward Pharmaceutical Corp.', '2022-10-08', 'France', 316),
            (3, 'Salicylic Acid', 'Neutrogena Corporation', '2023-07-13', 'United States', 596),
            (4, 'Coumarinum, Quercetin, Rutin, Bamboo, Barley, Corn, Levant cotton, Flax seed, Millet, Milo, Oat, California poppy, Rice, Rye, Safflower,', 'Dr. Donna Restivo DC', '2022-12-25', 'Indonesia', 363),
            (5, 'Dextroamphetamine Saccharate, Amphetamine Aspartate, Dextroamphetamine Sulfate and Amphetamine Sulfate', 'Global Pharmaceuticals, Division of Impax Laboratories Inc.', '2022-08-17', 'Greece', 116),
            (6, 'magnesium chloride', 'Mylan Teoranta', '2022-08-12', 'China', 430),
            (7, 'Doxycycline', 'Ranbaxy Pharmaceuticals Inc.', '2023-06-25', 'China', 687),
            (8, 'Divalproex Sodium', 'American Health Packaging', '2022-12-24', 'Moldova', 944),
            (9, 'Tamoxifen Citrate', 'Mylan Pharmaceuticals Inc.', '2023-02-15', 'Philippines', 462),
            (10, 'interleukin-12 human, interferon gamma-1a', 'VIATREXX BIO INCORPORATED', '2022-10-05', 'Jordan', 299),
            (11, 'Chelidonium Curcuma', 'Uriel Pharmacy Inc.', '2022-08-27', 'Cameroon', 801),
            (12, 'BRYONIA ALBA ROOT, CAUSTICUM, CALCIUM SULFIDE, and ANTIMONY POTASSIUM TARTRATE', 'Hyland''s', '2023-01-29', 'China', 287),
            (13, 'NEISSERIA MENINGITIDIS GROUP A CAPSULAR POLYSACCHARIDE DIPHTHERIA TOXOID CONJUGATE ANTIGEN, NEISSERIA MENINGITIDIS GROUP C CAPSULAR POLYSACCHARIDE DIPHTHERIA TOXOID CONJUGATE ANTIGEN', 'Sanofi Pasteur Inc.', '2023-07-19', 'Bulgaria', 146),
            (14, 'alprazolam', 'Greenstone LLC', '2022-08-06', 'Sweden', 307),
            (15, 'Acetaminophen, Dextromethorphan HBr, Doxylamine Succinate', 'Topco Associates LLC', '2022-12-23', 'Indonesia', 255),
            (16, 'TESTOSTERONE', 'Slate Pharma', '2022-09-09', 'Ecuador', 856),
            (17, 'Labetalol hydrochloride', 'Golden State Medical Supply, Inc.', '2023-06-18', 'Norway', 586),
            (18, 'Carvedilol', 'Teva Pharmaceuticals USA Inc', '2023-03-28', 'China', 933),
            (19, 'Dimethicone', 'NANOPOLY CO., LTD.', '2022-10-18', 'Portugal', 845),
            (20, 'Labetalol hydrochloride', 'Rebel Distributors Corp', '2023-04-08', 'Brazil', 652),
            (21, 'DEXTROSE MONOHYDRATE and POTASSIUM CHLORIDE', 'Hospira, Inc.', '2022-09-23', 'Belarus', 801),
            (22, 'abatacept', 'E.R. Squibb & Sons, L.L.C.', '2023-05-06', 'Indonesia', 789),
            (23, 'Irbesartan', 'Macleods Pharmaceuticals Limited', '2023-07-02', 'Russia', 197),
            (24, 'TOPICAL STARCH', 'KJI Industrial Co Ltd', '2023-07-10', 'China', 707),
            (25, 'Lidocaine Hydrochloride', 'Quest Products, Inc.', '2022-09-10', 'France', 651),
            (26, 'RISPERIDONE', 'Ajanta Pharma Limited', '2022-08-03', 'China', 378),
            (27, 'Tincture of Benzoin', 'Medical Chemical Corporation', '2023-05-19', 'Philippines', 234),
            (28, 'Titanium Dioxide', 'Melaleuca Inc.', '2022-12-22', 'France', 399),
            (29, 'Phenytoin Sodium', 'Parke-Davis Div of Pfizer Inc', '2023-03-09', 'Philippines', 911),
            (30, 'zinc', 'Sanum Kehlbeck GmbH & Co. KG', '2023-04-28', 'Norway', 968),
            (31, 'ETHYL ALCOHOL', 'AMERICAN SALES COMPANY', '2023-02-12', 'China', 868),
            (32, 'Zolpidem Tartrate', 'Aurobindo Pharma Limited', '2022-10-30', 'China', 524),
            (33, 'Trichoderma harzianam', 'Nelco Laboratories, Inc.', '2023-04-07', 'Russia', 635),
            (34, 'Ibuprofen', 'Precision Dose Inc.', '2023-07-03', 'Russia', 760),
            (35, 'HYDROCODONE BITARTRATE AND IBUPROFEN', 'Physicians Total Care, Inc.', '2022-10-03', 'Serbia', 911),
            (36, 'Leucine, Phenylalanine, Lysine, Methionine, Isoleucine, Valine, Histidine, Threonine, Tryptophan, Alanine, Glycine, Arginine, Proline, Serine, Tyrosine, Sodium Acetate, Dibasic Potassium Phosphate, Ma', 'Baxter Healthcare Corporation', '2022-09-05', 'China', 121),
            (37, 'Metformin Hydrochloride', 'REMEDYREPACK INC.', '2022-09-21', 'Finland', 928),
            (38, 'Morphine Sulfate', 'H.J. Harkins Company, Inc.', '2022-11-18', 'China', 318),
            (39, 'Aluminum Zirconium Pentachlorohydrex Gly', 'The Dial Corporation', '2022-12-31', 'China', 110),
            (40, 'PREGABALIN', 'Bryant Ranch Prepack', '2023-05-05', 'Papua New Guinea', 366),
            (41, 'Diltiazem Hydrochloride', 'Actavis Elizabeth LLC', '2022-09-15', 'Ukraine', 664),
            (42, 'Octinoxate, Oxybenzone, Titanium Dioxide', 'JAFRA COSMETICS INTERNATIONAL', '2022-11-07', 'Russia', 465),
            (43, 'OCTINOXATE, Zinc Oxide, Titanium Dioxide', 'LG Household and Healthcare, Inc.', '2022-11-01', 'Egypt', 509),
            (44, 'Barium Sulfate Suspension', 'E-Z-EM Canada Inc', '2022-10-25', 'Macedonia', 752),
            (45, 'Sucralfate', 'McKesson Contract Packaging', '2022-12-02', 'Latvia', 422),
            (46, 'sulindac', 'Major Pharmaceuticals', '2022-10-22', 'China', 233),
            (47, 'Penicillin V Potassium', 'Aidarex Pharmaceuticals LLC', '2023-05-24', 'China', 710),
            (48, 'Triclosan', 'SJ Creations, Inc.', '2022-10-02', 'Russia', 637),
            (49, 'leucovorin calcium', 'Sagent Pharmaceuticals', '2023-02-22', 'Colombia', 627),
            (50, 'BENZALKONIUM CHLORIDE', 'DOLGENCORP INC', '2023-04-01', 'South Korea', 734);
        """)
        self.mydb.commit()
    
    def selectData(self, shart):
        self.cursor.execute(f"SELECT * FROM medicine ORDER BY drug_company {shart} ;")
        malumot = self.cursor.fetchall()
        return malumot
    
    def drop(self):
        self.cursor.execute("DROP TABLE medicine;")
        self.cursor.execute("DROP DATABASE drugs;")




db = Databaza()
# 1-shart
# lst = db.selectData("DESC")
# for l in lst:
#     if len(l[1].split()) == 1 and l[5] > 200 and l[5] < 500:
#         print([l[1], l[2], l[4]])

# 2-shart
lst = db.selectData("ASC")
txt = str()
for n in lst:
    txt += n[4]

for l in lst:
    if (not txt.count(l[4]) > 2) and l[3].month > 2 and l[3].month < 6:
        print([l[1], l[2], l[3], l[4]])
db.drop()