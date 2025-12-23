class calci:
    def __init__(self,amt):
        self.amt=amt
        
    def num_of_notes(self):
        notes=[2000,500,200,100,50,20,10,5,2,1]
        notes_dict={}
        for note in notes:
            notes_dict[note]=self.amt//note
            self.amt=self.amt%note
        return notes_dict
amt=int(input())
res=calci(amt)
res1=res.num_of_notes()
for note,count in res1.items():
    print(f"{note}:{count}")
