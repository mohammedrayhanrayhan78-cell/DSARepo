class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        res=[]
        current_line=[]
        current_length=0
        for word in words:
            if current_length+len(word)+len(current_line)>maxWidth:
                if len(current_line)==1:
                    res.append(current_line[0]+" "*(maxWidth-len(current_line[0])))
                else:
                    total_spaces=maxWidth-current_length
                    slots=len(current_line)-1
                    space_per_slot, extra_spaces = divmod(total_spaces, slots)
                    line_str=""
                    for i in range(slots):
                        spaces=" "*(space_per_slot+(1 if i<extra_spaces else 0))
                        line_str+=current_line[i]+spaces
                    line_str+=current_line[-1]
                    res.append(line_str)
                current_line=[]
                current_length=0
            current_line.append(word)
            current_length+=len(word)
        last_line=" ".join(current_line)
        last_line+=" "*(maxWidth-len(last_line))
        res.append(last_line)

        return res

