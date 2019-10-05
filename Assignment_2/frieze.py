

class FriezeError(Exception):
    def __init__(self, message):
        self.message = message

class Frieze:
    def __init__(self,filename):
        grid = []
        self.a = []
        self.n = []
        self.filename = filename
        self.name = self.filename.split('.')[0]
        with open(self.filename) as file1:
            for i in file1:
                c=i.strip()
                if c:
                    self.a.append(i.split())
        self.check()
        with open(self.filename) as file:
            for L in file:
                b=L.strip()
                if b:
                    grid.append([int(v) for v in b.split()])        
        self.grid=grid
        self.is_frieze()
        
        
    def check_zimu(self):
        for i in range(len(self.a)):
            for j in range(len(self.a[i])):
                if not self.a[i][j].isdigit():
                    raise FriezeError('Incorrect input.')
    
    def check(self):
        if self.a==[]:
            raise FriezeError('Incorrect input.')
            
        if len(self.a)<3 or len(self.a)>17:
            raise FriezeError('Incorrect input.')    
        if len(self.a[0])<5 or len(self.a[0]) >51:
            raise FriezeError('Incorrect input.')
                
        for i in range(len(self.a)):
            if i < len(self.a):
                if len(self.a[i])==len(self.a[0]):
                    continue
                else:
                    raise FriezeError('Incorrect input.')   
        for i in range(len(self.a)):
            for j in range(len(self.a[i])):
                if not self.a[i][j].isdigit():
                    raise FriezeError('Incorrect input.')
                else:
                    if int(self.a[i][j])>=0 and int(self.a[i][j])<=15:
                        continue
                    else:
                        raise FriezeError('Incorrect input.')
    def is_frieze(self):
        a=self.find_period()
        if a<2 or (len(self.grid[0])-1)/a <2:
            raise FriezeError('Input does not represent a frieze.')
        if self.grid[0][-1]!=0:
                raise FriezeError('Input does not represent a frieze.')
        for i in range(len(self.grid)):
            if self.grid[i][-1]!=0 and self.grid[i][-1]!=1:
                raise FriezeError('Input does not represent a frieze.')
            else:
                if self.grid[i][-1]==0 and self.grid[i][0]&1==1:
                        raise FriezeError('Input does not represent a frieze.')
                else:
                    if self.grid[i][-1]==1 and self.grid[i][0]&1!=1:
                        raise FriezeError('Input does not represent a frieze.')
                             
        for i in self.grid[0][0:-1]:
            if i!=4 and i!=12:
                raise FriezeError('Input does not represent a frieze.')
        for j in self.grid[-1][0:-1]:
            if j!=4 and j!=5 and j!=6 and j!=7:
                raise FriezeError('Input does not represent a frieze.')
                
        for i in range(len(self.grid)-1):
            for j in range(len(self.grid[i])):
                if self.grid[i][j]&8==8:
                    if self.grid[i+1][j]&2==2:
                        raise FriezeError('Input does not represent a frieze.')
                        
        
    def _find_period(self):
        period=[]
        for a in range(1,len(self.grid)-1):
            l1=self.grid[a][:]
            l1.pop()
            l=l1
            length = 1
            c=1
            while length <= len(l):
                if len(l)%length!=0:
                    min_period = length
                    length+=1
                else:
                    if length > len(l)//2:
                        min_period = len(l)
                        break
                    min_period = length
                    l1 = l[0:length]
                    for i in range(length):
                        for j in range(i+length,len(l),length):
                            if l1[i]==l[j]:
                                if j < len(l)-1:
                                    continue
                                else:
                                    c=0
                                    break
                            else:
                                break
                        if c == 0:
                            break
                        else:
                            if l1[i]!=l[j]:
                                length +=1
                                break
                    if c==0:
                        break
            period.append(min_period)
        return period
    
    def find_period(self):
        l = sorted(list(set(self._find_period())))
        period = max(l)
        for i in range(len(l)-1):
            if l[i+1]%l[i]!=0:
                period = len(self.grid[0])
        
        return period
                

    def is_horizontal_reflection(self):
        perid=self.find_period()
        duichen = (len(self.grid)-1)
#        middle_line = (len(self.grid)-1)/2 #if len(self.grid)==odd
#        middle_up = (len(self.grid)-1)//2  # if len(self.grid)==even
#        middle_down = (len(self.grid)-1)//2+1 # if len(self.grid)==even
        for i in range(len(self.grid)):
            if self.grid[i][-1]==0:
                continue
            else:
                if self.grid[duichen-i+1][-1]!=1:
                    return False
        for i in range(len(self.grid)):
            for j in range(perid):
                if self.grid[i][j]==0:
                    continue
                else:
                    if self.grid[i][j]&1==1:
                        if self.grid[duichen-i+1][j]&1!=1:
                            return False    
                    if self.grid[i][j]&2==2:
                        if self.grid[duichen-i][j]&8!=8:
                            return False
                    if self.grid[i][j]&4==4:
                        if self.grid[duichen-i][j]&4!=4:
                            return False
                    if self.grid[i][j]&8==8:
                        if self.grid[duichen-i][j]&2!=2:
                            return False
        

    def is_vertical_reflection(self):
        perid=self.find_period()
        vertical_line = 0.5*(perid-1)
        final_line = vertical_line+perid
        r=vertical_line
        c=0
        while r<=final_line:
            duichen = int(r*2)
            if duichen-0>=len(self.grid[0]):
                return False
            for i in range(len(self.grid)):
                for j in range(perid):
                    if self.grid[i][j]==0:
                        continue
                    else:
                        if self.grid[i][j]&1==1:
                            if self.grid[i][duichen-j]&1!=1:
                                r+=0.5
                                c=1
                                break
                            else:
                                pass
                        if self.grid[i][j]&2==2:
                            if self.grid[i-1][duichen-j-1]&8!=8:
                                r+=0.5
                                c=1
                                break
                            else:
                                pass
                        if self.grid[i][j]&4==4:
                            if self.grid[i][duichen-j-1]&4!=4:
                                r+=0.5
                                c=1
                                break
                            else:
                                pass
                        if self.grid[i][j]&8==8:
                            if self.grid[i+1][duichen-j-1]&2!=2:
                                r+=0.5
                                c=1
                                break
                            else:
                                pass
                else:
                    continue
                break
            if r>final_line:
                return False
            if i==len(self.grid)-1 and j==perid-1 and c==0:
                break
            c=0
    
    def is_glided_horizontal(self):
        perid=self.find_period()
        duichen = (len(self.grid)-1)
        if perid%2==1:
            return False
        half_perid = int(perid/2)
        for i in range(len(self.grid)):
            for j in range(perid):
                if self.grid[i][j]==0:
                    continue
                else:
                    if self.grid[i][j]&1==1:
                        if self.grid[duichen-i+1][j+half_perid]&1!=1:
                            return False    
                    if self.grid[i][j]&2==2:
                        if self.grid[duichen-i][j+half_perid]&8!=8:
                            return False
                    if self.grid[i][j]&4==4:
                        if self.grid[duichen-i][j+half_perid]&4!=4:
                            return False
                    if self.grid[i][j]&8==8:
                        if self.grid[duichen-i][j+half_perid]&2!=2:
                            return False
            
    def is_rotation(self):
        if self.is_horizontal_reflection() != False and self.is_vertical_reflection() != False:
            return True
        perid=self.find_period()
        horizon_line = (len(self.grid)-1)
        vertical_line = 0.5*(perid-1)
        final_line = vertical_line+perid
        r=vertical_line
        c=0
        while r<=final_line:
            duichen = int(r*2)
            if duichen-0>=len(self.grid[0]):
                return False
            for i in range(len(self.grid)):
                for j in range(perid):
                    if self.grid[i][j]==0:
                        continue
                    else:
                        if self.grid[i][j]&1==1:
                            if self.grid[horizon_line-i+1][duichen-j]&1!=1:
                                r+=0.5
                                c=1
                                break
                            else:
                                pass
                        if self.grid[i][j]&2==2:
                            if self.grid[horizon_line-i+1][duichen-j-1]&2!=2:
                                r+=0.5
                                c=1
                                break
                            else:
                                pass
                        if self.grid[i][j]&4==4:
                            if self.grid[horizon_line-i][duichen-j-1]&4!=4:
                                r+=0.5
                                c=1
                                break
                            else:
                                pass
                        if self.grid[i][j]&8==8:
                            if self.grid[horizon_line-i-1][duichen-j-1]&8!=8:
                                r+=0.5
                                c=1
                                break
                            else:
                                pass
                else:
                    continue
                break
            if r>final_line:
                return False
            if i==len(self.grid)-1 and j==perid-1 and c==0:
                break
            c=0



    def analyse(self):
        if self.is_horizontal_reflection()==False and self.is_vertical_reflection() == False\
                                and self.is_glided_horizontal() == False and self.is_rotation() == False:
                                    print(f'Pattern is a frieze of period {self.find_period()} that is invariant under translation only.')


        if self.is_vertical_reflection() != False and self.is_horizontal_reflection()==False\
                                and self.is_glided_horizontal() == False and self.is_rotation() == False:
                                    print(f'Pattern is a frieze of period {self.find_period()} that is invariant under translation')
                                    print('        and vertical reflection only.')
            
            
        if self.is_horizontal_reflection() != False and self.is_vertical_reflection() == False\
                                and self.is_glided_horizontal() == False and self.is_rotation() == False:
                                    print(f'Pattern is a frieze of period {self.find_period()} that is invariant under translation')
                                    print('        and horizontal reflection only.')
            
        if self.is_glided_horizontal() != False and self.is_horizontal_reflection()==False\
                                and self.is_vertical_reflection() == False and self.is_rotation() == False:
                                    print(f'Pattern is a frieze of period {self.find_period()} that is invariant under translation')
                                    print('        and glided horizontal reflection only.')
            

        if self.is_rotation() != False and self.is_horizontal_reflection()==False\
                                and self.is_vertical_reflection() == False and self.is_glided_horizontal()==False:
                                    print(f'Pattern is a frieze of period {self.find_period()} that is invariant under translation')
                                    print('        and rotation only.')
        
        if self.is_glided_horizontal() != False and self.is_vertical_reflection() != False\
                                and self.is_rotation() != False and self.is_horizontal_reflection()==False:
                                    print(f'Pattern is a frieze of period {self.find_period()} that is invariant under translation,')
                                    print('        glided horizontal and vertical reflections, and rotation only.')
                                    
        if self.is_horizontal_reflection() != False and self.is_vertical_reflection() != False\
                                and self.is_rotation() != False and self.is_glided_horizontal() == False:
                                    print(f'Pattern is a frieze of period {self.find_period()} that is invariant under translation,')
                                    print('        horizontal and vertical reflections, and rotation only.')



    def display_N_S(self):
        l = self.grid
        N=[]
        for i in range(len(l)):
            N.append([])
            
        for i in range(len(l)):
            for j in range(len(l[i])):
                if l[i][j]&1!=1:
                    N[i].append(0)
                else:
                    N[i].append(1)
        result = []
        for i in range(len(N[0])):
            for j in range(len(N)):
                if j-1>=0 and N[j-1][i]!=1:
                    if N[j][i]==1:
                        a=i
                        b=j
                        start = (a,b-1)
                        end = (a,b)
                        while b+1<len(N) and N[b+1][a]==1:
                            end = (a,b+1)
                            b+=1
                        result.append(f'\draw {start} -- {end};')
        return result
                    
    def display_NW_SE(self):
        l = self.grid
        NW=[]
        for i in range(len(l)):
            NW.append([])
            
        for i in range(len(l)):
            for j in range(len(l[i])):
                if l[i][j]&8!=8:
                    NW[i].append(0)
                else:
                    NW[i].append(1)
        result = []
        for i in range(len(NW)):
            for j in range(len(NW[i])):
                if i-1>=0 and j-1>=0 and NW[i-1][j-1]!=1:
                    if NW[i][j]==1:
                        a=j
                        b=i
                        start = (a,b)
                        end = (a+1,b+1)
                        while b+1<len(NW) and a+1<len(NW[0]) and NW[b+1][a+1]==1:
                            end = (a+2,b+2)
                            b+=1
                            a+=1
                        result.append(f'\draw {start} -- {end};')
                if i-1<0 or j-1<0: 
                    if NW[i][j]==1:
                        a=j
                        b=i
                        start = (a,b)
                        end = (a+1,b+1)
                        while b+1<len(NW) and a+1<len(NW[0]) and NW[b+1][a+1]==1:
                            end = (a+2,b+2)
                            b+=1
                            a+=1
                        result.append(f'\draw {start} -- {end};')
                
        return result
                      
    def display_W_E(self):
        l = self.grid
        W=[]
        for i in range(len(l)):
            W.append([])
            
        for i in range(len(l)):
            for j in range(len(l[i])):
                if l[i][j]&4!=4:
                    W[i].append(0)
                else:
                    W[i].append(1)
        result = []
        for i in range(len(W)):
            for j in range(len(W[i])):
                if j-1>=0 and W[i][j-1]!=1:
                    if W[i][j]==1:
                        a=j
                        b=i
                        start = (a,b)
                        end = (a+1,b)
                        while  a+1<len(W[0]) and W[b][a+1]==1:
                            end = (a+2,b)
                            a+=1
                        result.append(f'\draw {start} -- {end};')   
                if j-1<0:
                    if W[i][j]==1:
                        a=j
                        b=i
                        start = (a,b)
                        end = (a+1,b)
                        while  a+1<len(W[0]) and W[b][a+1]==1:
                            end = (a+2,b)
                            a+=1
                        result.append(f'\draw {start} -- {end};')
        return result
        
    def display_SW_NE(self):
        l = self.grid
        SW=[]
        for i in range(len(l)):
            SW.append([])
            
        for i in range(len(l)):
            for j in range(len(l[i])):
                if l[i][j]&2!=2:
                    SW[i].append(0)
                else:
                    SW[i].append(1)
        result = []
        for i in range(len(SW[0])):
            for j in range(len(SW)):
                if j+1<len(SW) and i-1>=0 and SW[j+1][i-1]!=1:
                    if SW[j][i]==1:
                        a = i
                        b = j
                        start = (a,b)
                        end = (a+1,b-1)
                        while b-1>0 and a+1<len(SW[0]) and SW[b-1][a+1]==1:
                            end = (a+2,b-2)
                            b-=1
                            a+=1
                        result.append([start,end])
                if j+1 == len(SW) or i-1<0:
                    if SW[j][i]==1:
                        a = i
                        b = j
                        start = (a,b)
                        end = (a+1,b-1)
                        while b-1>0 and a+1<len(SW[0]) and SW[b-1][a+1]==1:
                            end = (a+2,b-2)
                            b-=1
                            a+=1
                        result.append([start,end])
        c = sorted(result, key=lambda x:x[0][1])
        results = []
        for i in range(len(c)):
            results.append(f'\draw {c[i][0]} -- {c[i][1]};')
        
        return results
     
    def combain(self,a):
        if a[9]==' ':
            if a[19]==' ':
                c = a[:9]+a[10:19]+a[20:]
            if a[20]==' ':
                c = a[:9]+a[10:20]+a[21:]
            if a[21]==' ':
                c = a[:9]+a[10:21]+a[22:]
        if a[10]==' ': 
            if a[20]==' ':
                c = a[:10]+a[11:20]+a[21:]
            if a[21]==' ':
                c = a[:10]+a[11:21]+a[22:]
            if a[22]==' ':
                c = a[:10]+a[11:22]+a[23:]
        return c
            
    def display(self):
        with open(f'{self.name}.tex','w') as file:
            file.write(r'\documentclass[10pt]{article}'+'\n'+
                       r'\usepackage{tikz}'+'\n'+r'\usepackage[margin=0cm]{geometry}'+'\n'+
                       r'\pagestyle{empty}'+'\n'+'\n'+r'\begin{document}'+'\n'+'\n'+
                       r'\vspace*{\fill}'+'\n'+r'\begin{center}'+'\n'+
                       r'\begin{tikzpicture}[x=0.2cm, y=-0.2cm, thick, purple]'+'\n')
            
            file.write('% North to South lines'+'\n')
            for a in self.display_N_S():
                n = self.combain(a)
                file.write('    '+n+'\n')
            file.write('% North-West to South-East lines'+'\n')
            for a in self.display_NW_SE():
                nw = self.combain(a)
                file.write('    '+nw+'\n')
            file.write('% West to East lines'+'\n')
            for a in self.display_W_E():
                w = self.combain(a)
                file.write('    '+w+'\n')
            file.write('% South-West to North-East lines'+'\n')
            for a in self.display_SW_NE():
                sw = self.combain(a)
                file.write('    '+sw+'\n')
            file.write(r'\end{tikzpicture}'+'\n'+r'\end{center}'+'\n'+
                       r'\vspace*{\fill}'+'\n'+'\n'+r'\end{document}'+'\n')

        
        