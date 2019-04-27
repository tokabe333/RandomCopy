import numpy as np
import glob
from PIL import Image

inPath = r"C:\Users\べやのん\Desktop\dataset\Forest"
testPath = r"C:\Users\べやのん\Desktop\dataset\Forestテスト用"
learnPath = r"C:\Users\べやのん\Desktop\dataset\Forest学習用"
testNum = 100

images = np.array(glob.glob(inPath+"\\*.png"))
perm = np.random.permutation(len(images))
images = images[perm]

testImages = images[:testNum]
learnImages = images[testNum:]

print(len(images))
print(len(testImages))
print(len(learnImages))

for i in range(len(testImages)):
	img = Image.open(testImages[i])
	img.save(testPath+"\\"+str(i)+"_test.bmp")

for i in range(len(learnImages)):
	img = Image.open(learnImages[i])
	img.save(learnPath+"\\"+str(i)+"_learn.bmp")