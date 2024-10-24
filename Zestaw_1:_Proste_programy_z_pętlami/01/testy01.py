import unittest
import io
import os
import sys
from contextlib import redirect_stdout
import importlib

from szablon01 import Zadanie_1


def komenda(k: str, *args, **kwargs):
    sciezka_pliku_wykonalnego = os.path.abspath(sys.argv[0])
    skrypty_dir = os.path.join( os.path.dirname(sciezka_pliku_wykonalnego), "../../skrypty")
    sys.path.append(skrypty_dir)
    nr_zadania = os.path.dirname(sciezka_pliku_wykonalnego)
    return importlib.import_module("WykonajKomende").wykonaj_komende(
        k, sciezka_pliku_wykonalnego, nr_zadania, *args, **kwargs
    )


class Testy01:
    class testy(unittest.TestCase):


        def test_Nr1_Zadanie_1_parametry_0(self):
            f = io.StringIO()
            with redirect_stdout(f):
                Zadanie_1(0)
            wynik = f.getvalue().strip()

            oczekiwany_wynik = ['']
            self.assertIn(wynik, oczekiwany_wynik)

        def test_Nr2_Zadanie_1_parametry_1(self):
            f = io.StringIO()
            with redirect_stdout(f):
                Zadanie_1(1)
            wynik = f.getvalue().strip()

            oczekiwany_wynik = ['']
            self.assertIn(wynik, oczekiwany_wynik)

        def test_Nr3_Zadanie_1_parametry_5(self):
            f = io.StringIO()
            with redirect_stdout(f):
                Zadanie_1(5)
            wynik = f.getvalue().strip()

            oczekiwany_wynik = ['']
            self.assertIn(wynik, oczekiwany_wynik)

        def test_Nr4_Zadanie_1_parametry_6(self):
            f = io.StringIO()
            with redirect_stdout(f):
                Zadanie_1(6)
            wynik = f.getvalue().strip()

            oczekiwany_wynik = ['3 4 5']
            self.assertIn(wynik, oczekiwany_wynik)

        def test_Nr5_Zadanie_1_parametry_10(self):
            f = io.StringIO()
            with redirect_stdout(f):
                Zadanie_1(10)
            wynik = f.getvalue().strip()

            oczekiwany_wynik = ['3 4 5']
            self.assertIn(wynik, oczekiwany_wynik)

        def test_Nr6_Zadanie_1_parametry_11(self):
            f = io.StringIO()
            with redirect_stdout(f):
                Zadanie_1(11)
            wynik = f.getvalue().strip()

            oczekiwany_wynik = ['3 4 5\n6 8 10']
            self.assertIn(wynik, oczekiwany_wynik)

        def test_Nr7_Zadanie_1_parametry_100(self):
            f = io.StringIO()
            with redirect_stdout(f):
                Zadanie_1(100)
            wynik = f.getvalue().strip()

            oczekiwany_wynik = ['3 4 5\n5 12 13\n6 8 10\n7 24 25\n8 15 17\n9 12 15\n9 40 41\n10 24 26\n11 60 61\n12 16 20\n12 35 37\n13 84 85\n14 48 50\n15 20 25\n15 36 39\n16 30 34\n16 63 65\n18 24 30\n18 80 82\n20 21 29\n20 48 52\n21 28 35\n21 72 75\n24 32 40\n24 45 51\n24 70 74\n25 60 65\n27 36 45\n28 45 53\n30 40 50\n30 72 78\n32 60 68\n33 44 55\n33 56 65\n35 84 91\n36 48 60\n36 77 85\n39 52 65\n39 80 89\n40 42 58\n40 75 85\n42 56 70\n45 60 75\n48 55 73\n48 64 80\n51 68 85\n54 72 90\n57 76 95\n60 63 87\n65 72 97']
            self.assertIn(wynik, oczekiwany_wynik)

        def test_Nr8_Zadanie_1_parametry_300(self):
            f = io.StringIO()
            with redirect_stdout(f):
                Zadanie_1(300)
            wynik = f.getvalue().strip()

            oczekiwany_wynik = ['3 4 5\n5 12 13\n6 8 10\n7 24 25\n8 15 17\n9 12 15\n9 40 41\n10 24 26\n11 60 61\n12 16 20\n12 35 37\n13 84 85\n14 48 50\n15 20 25\n15 36 39\n15 112 113\n16 30 34\n16 63 65\n17 144 145\n18 24 30\n18 80 82\n19 180 181\n20 21 29\n20 48 52\n20 99 101\n21 28 35\n21 72 75\n21 220 221\n22 120 122\n23 264 265\n24 32 40\n24 45 51\n24 70 74\n24 143 145\n25 60 65\n26 168 170\n27 36 45\n27 120 123\n28 45 53\n28 96 100\n28 195 197\n30 40 50\n30 72 78\n30 224 226\n32 60 68\n32 126 130\n32 255 257\n33 44 55\n33 56 65\n33 180 183\n34 288 290\n35 84 91\n35 120 125\n36 48 60\n36 77 85\n36 105 111\n36 160 164\n39 52 65\n39 80 89\n39 252 255\n40 42 58\n40 75 85\n40 96 104\n40 198 202\n42 56 70\n42 144 150\n44 117 125\n44 240 244\n45 60 75\n45 108 117\n45 200 205\n48 55 73\n48 64 80\n48 90 102\n48 140 148\n48 189 195\n48 286 290\n49 168 175\n50 120 130\n51 68 85\n51 140 149\n52 165 173\n54 72 90\n54 240 246\n55 132 143\n56 90 106\n56 105 119\n56 192 200\n57 76 95\n57 176 185\n60 63 87\n60 80 100\n60 91 109\n60 144 156\n60 175 185\n60 221 229\n63 84 105\n63 216 225\n63 280 287\n64 120 136\n64 252 260\n65 72 97\n65 156 169\n66 88 110\n66 112 130\n68 285 293\n69 92 115\n69 260 269\n70 168 182\n70 240 250\n72 96 120\n72 135 153\n72 154 170\n72 210 222\n75 100 125\n75 180 195\n77 264 275\n78 104 130\n78 160 178\n80 84 116\n80 150 170\n80 192 208\n81 108 135\n84 112 140\n84 135 159\n84 187 205\n84 245 259\n85 132 157\n85 204 221\n87 116 145\n88 105 137\n88 165 187\n88 234 250\n90 120 150\n90 216 234\n93 124 155\n95 168 193\n95 228 247\n96 110 146\n96 128 160\n96 180 204\n96 247 265\n96 280 296\n99 132 165\n99 168 195\n100 105 145\n100 240 260\n102 136 170\n102 280 298\n104 153 185\n104 195 221\n105 140 175\n105 208 233\n105 252 273\n108 144 180\n108 231 255\n110 264 286\n111 148 185\n112 180 212\n112 210 238\n114 152 190\n115 252 277\n115 276 299\n117 156 195\n117 240 267\n119 120 169\n120 126 174\n120 160 200\n120 182 218\n120 209 241\n120 225 255\n123 164 205\n126 168 210\n128 240 272\n129 172 215\n130 144 194\n132 176 220\n132 224 260\n133 156 205\n135 180 225\n136 255 289\n138 184 230\n140 147 203\n140 171 221\n140 225 265\n141 188 235\n144 165 219\n144 192 240\n147 196 245\n150 200 250\n153 204 255\n156 208 260\n159 212 265\n160 168 232\n160 231 281\n161 240 289\n162 216 270\n165 220 275\n168 224 280\n171 228 285\n174 232 290\n176 210 274\n177 236 295\n180 189 261\n192 220 292\n195 216 291\n200 210 290']
            self.assertIn(wynik, oczekiwany_wynik)

        def test_Nr9_Zadanie_1_parametry_21(self):
            f = io.StringIO()
            with redirect_stdout(f):
                Zadanie_1(21)
            wynik = f.getvalue().strip()

            oczekiwany_wynik = ['3 4 5\n5 12 13\n6 8 10\n8 15 17\n9 12 15\n12 16 20']
            self.assertIn(wynik, oczekiwany_wynik)

        def test_Nr10_Zadanie_1_parametry_14(self):
            f = io.StringIO()
            with redirect_stdout(f):
                Zadanie_1(14)
            wynik = f.getvalue().strip()

            oczekiwany_wynik = ['3 4 5\n5 12 13\n6 8 10']
            self.assertIn(wynik, oczekiwany_wynik)

        def test_Nr11_Zadanie_1_parametry_21(self):
            f = io.StringIO()
            with redirect_stdout(f):
                Zadanie_1(21)
            wynik = f.getvalue().strip()

            oczekiwany_wynik = ['3 4 5\n5 12 13\n6 8 10\n8 15 17\n9 12 15\n12 16 20']
            self.assertIn(wynik, oczekiwany_wynik)

    @staticmethod
    def Uruchom():
        suite = unittest.TestLoader().loadTestsFromTestCase(Testy01.testy)
        unittest.TextTestRunner(verbosity=2).run(suite)