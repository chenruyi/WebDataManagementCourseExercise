### Task:
# Consider the following documents: 
# •  d1 = I like to watch the sun set with my friend. 
# •  d2 = The Best Places To Watch The Sunset.  
# •  d3 = My friend watch the sun come up.  
 
# Write a program which can output the document IDs given an input keyword. 



keyword2id = {}


def calKeyWord(doc:str):

    keyword = 1


    return keyword

def parserDoc(doc:str):
    # to lower

    doc = doc.replace(","," ")
    doc = doc.replace(".", " ")
    doc = doc.lower()
    return doc

def generatorDoc():
    import glob

    file_list = glob.glob("./course1data/*.txt")
    
    for fName in file_list:
        with open(fName,'r') as f:
            
            content = " ".join([line.strip()  for line in f.readlines()])
            content = parserDoc(content)
            id = fName.split("\\")[-1]
            yield (fName, content)
def calTF(doc:str):
    # [[words, tf]]
    words = doc.split(" ")
    bag_words = sorted(set(words))
    result = []
    for w in bag_words:
        item = [w,0]
        result.append(item)
    for w in words:
        word_index_of_result = bag_words.index(w)
        item = result[word_index_of_result]
        item[1] += 1
        result[word_index_of_result] = item

    for i in range(len(result)):
        item = result[i]
        item[1] = item[1]/len(words)
        result[word_index_of_result] = item

    return result

def generateAllKeyWord():
    bag_words = []
    for fName,content in generatorDoc():
        words = content.split(" ")
        bag_words.extend(words)
    bag_words = sorted(set(bag_words))
    return bag_words
        

def generateKeyWord():
    # tf
    word_tf_list =[] #[(keyword, fName, tf)]
    all_key_words = generateAllKeyWord()

    for w in all_key_words:
        word_tf_list.append([w,"",0])
    
    for fName,content in generatorDoc():
        
        doc_w_t_list = calTF(content)
        # for 
        for (w,tf) in doc_w_t_list:
            word_in_all_index = all_key_words.index(w)
            item = word_tf_list[word_in_all_index]
            if tf > item[-1]:
                # update
                item = [w, fName, item[-1]]
                word_tf_list[word_in_all_index] = item

    return word_tf_list



def main():
    # [(keyword, fName, tf)]
    word_tf_list = generateKeyWord()
    while True:
        # read keyword
        keyword = input("keyword(#: exit): ")
        keyword = keyword.strip()
        keyword = keyword.lower()
        if len(keyword) == 0:
            print("please input a keyword.")
            continue
        if keyword == "#":
            break
        succeed_flag = False
        for (w,fName,tf) in word_tf_list:
            if w == keyword:
                succeed_flag = True
                print("keyword: ",keyword," id: ", fName)
                break
        if not succeed_flag:
            print("not find.")

        

    pass




if __name__ == "__main__":
    main()