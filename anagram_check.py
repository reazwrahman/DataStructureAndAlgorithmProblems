
class anagram_check():

    def __init__ (self): 

        self.a=None
        self.b=None
        self.match1=[]
        self.match2=[]
        self.new_a=None
        self.new_b=None
        self.possible_whitespace=[]
        
    def whitespace_remover(self,a,b):
        self.a=a
        self.b=b
        
        self.new_a=self.a.strip()
        self.new_b=self.b.strip()


        #self.possible_whitespace=[]

        for i in range (100):
            self.possible_whitespace.append(" "*i)

        for i in self.possible_whitespace:
            if i in self.new_a:
                self.new_a=self.a.replace(i,"")
                
            
            if i in self.new_b:
                self.new_b=self.b.replace(i,"")

        

        return [self.new_a,self.new_b]

    def anagram_match(self,string1,string2):
        
        
        self.new_a=self.whitespace_remover(string1,string2)[0] 
        self.new_b=self.whitespace_remover(string1,string2)[1] 
        
        for i in range (len(self.new_a)):
            if self.new_a[i] in self.new_b:
                #print ('True')
                self.match1.append(1)
            else:
                #print ('false')
                pass
        print (len(self.match1))

        for i in range (len(self.new_b)):
            if self.new_b[i] in self.new_a:
                self.match2.append(1)
                #print ('true')
            else:
                #print ('false')
                pass
        print (len(self.match2))

        if self.match1!=[] and self.match2!=[] and self.match1==self.match2 and \
           len(self.new_a)==len(self.new_b):
            print ('YES ITS AN ANAGRAM')
        else:
            print ('NO ITS NOT AN ANAGRAM') 
        
        
            
#test_case.anagram_match("client eastwood","old west action")
