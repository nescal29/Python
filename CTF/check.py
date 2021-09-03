import hashlib

ans_hash = [
    'aff02d6ad353ebf547f3b1f8ecd21efd7931e356f3930ab5ee502a391c5802d7',
    '8428f87e4dbbf1e95dba566b2095d989f5068a5465ebce96dcdf0b487edb8ecb',
    'e82f6ff15ddc9d67fc28c4b2c575adf7252d6e829af55c2b7ac1615b304d8962'
]


for i in range(90):
    filename = './pass0'
    i += 1
    if i < 10 :
        filename += ('0' + str(i))
    else:
        filename += str(i)

    filename += '.txt'

    with open(filename, 'rb') as file:
        fileData = file.read()
        hash = hashlib.sha256(fileData).hexdigest()
        
        for ans in ans_hash:
            if ans == hash:
                print(filename)