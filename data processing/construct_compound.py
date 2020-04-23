from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import MACCSkeys
from rdkit.Chem import DataStructs
import csv
i = 1
with open('morgan.csv', 'w') as morgan:
    writer = csv.writer(morgan)
    with open('compound_smile.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            # print(row[1])
            mol = Chem.MolFromSmiles(row[1])
            fp_morgan = AllChem.GetMorganFingerprint(mol,2)
            fp_morgan_hashed = AllChem.GetMorganFingerprintAsBitVect(mol,2,nBits=2048)
            mf = fp_morgan_hashed.ToBitString()
            print(mf)
            writer.writerow([mf])
            print(i)
            i = i+1

# mol = Chem.MolFromSmiles('CCCN')
# fp1 = MACCSkeys.GenMACCSKeys(mol)
# print (fp1.ToBitString())
# fp1_morgan = AllChem.GetMorganFingerprint(mol,2)
# print (fp1_morgan.GetLength())
# fp1_morgan_hashed = AllChem.GetMorganFingerprintAsBitVect(mol,2,nBits=1024)
# fp1_morgan_hashed.ToBitString()
