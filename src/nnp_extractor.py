import nltk

def sentence_cleaner(sentences):
        cleaned_sentences=[]
        for sentence in sentences:
            sentence=sentence.replace("/","")
            cleaned_sentences.append(sentence)
        return cleaned_sentences

def lower_case(list_of_items):

    lower_case_items=[]

    for  item in list_of_items:
        lower_case_items.append(str(item).lower())
    
    return lower_case_items

class NNP:

    nnp=[]

    def __init__(self,list_of_sentences):
        self.sentences=list_of_sentences

    def execute(self):
        self.nnp=[]
        for sentence in self.sentences:
            tokens = nltk.word_tokenize(sentence)
            tagged = nltk.pos_tag(tokens)
            for item in tagged:
                if(item[1]=="NNP"):
                    item=item[0]
                    self.nnp.append(item)
        self.nnp=sentence_cleaner(self.nnp)
        self.nnp=lower_case(self.nnp)

def array_nnp_extractor(sentences):
    all_nnp=[]
    nnp=NNP(sentences)
    nnp.execute()
    all_nnp.append(nnp.nnp)
    return all_nnp