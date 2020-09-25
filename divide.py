datafile = "small_vocab_en.txt"
valfile = "demo_val_en.txt"
trainfile = "demo_train_en.txt"
testfile = "demo_test_en.txt"

data = open(datafile, encoding = 'UTF-8')
val = open(valfile, 'w', encoding = 'UTF-8')
train = open(trainfile, 'w', encoding = 'UTF-8')
test = open(testfile, 'w', encoding = 'UTF-8')

print('Dividing data')
for i, line in enumerate(data):
    if i < 1000:
        test.write(line)
    elif (i >= 1000) and (i<6000) :
        val.write(line)
    else:
        train.write(line)
    if i%20000 == 0:
        print(i)

data.close()
val.close()
train.close()
test.close()
