## AUTHOR: Daniel Asimiakwini

##################################################################################################################
#IMPORTS
import shlex # specifically for replace methods
##################################################################################################################

#MAIN FUNCTION DEFINITION
def main():
        """
        main function call.

        Parameters
        ----------
        None
        

        Returns
        -------
        None
    
        """
        start_message = "Welcome to ed379"
        end_message = "Good-bye"
        edit = True
        file_saved = False
        newfile = "new" #intial file of any name
        textfile = TextFile(newfile)
        whitespaces = [" ","    "]
        
        print(start_message)
        while edit: #process commands from the user until they quit or save
                commands = [None,None,None] # new commands each run
                
                user_input = input()

                try:
                        user_input_list = shlex.split(user_input)
                        
                        for value in user_input_list:
                                if value in whitespaces:
                                        user_input_list.remove(value)
                        for index in range(len(user_input_list)):
                                commands[index] = user_input_list[index].strip()

                except Exception:
                        pass # will handle all input error in main program

                
                
                #COMMANDS
                add_text = commands[0]=="a"
                delete = commands[0]=="d"
                insert = commands[0]=="i"
                load = commands[0]=="l"
                println = commands[0]=="p" # change the print funct of textfile to println for readability and debugging
                quit = commands[0]=="q"
                replace = commands[0]=="r"
                sort = commands[0]=="s"
                write = commands[0]=="w"
                search_fwd = commands[0]=="/"
                search_bck = commands[0]=="?"
                numbers = ["0","1","2","3","4","5","6","7","8","9"]

                try:
                        go_to_line = commands[0][0] in numbers
                except:
                        go_to_line = True # can be none but will handle in block
                print_next_line = commands[0]==None
                
                
                try: # try user input, if not valid, will handle

                        #done TO PRINT NEXT LINE
                        if print_next_line:
                                offset = commands[1] # none
                                try:
                                        textfile.println(offset)
                                except AssertionError as pnae:
                                        print(pnae)
                        #__________________________________________________________________________________________________________________________________________________


                        #done TO GO TO LINE USER SELECTS WITH INTEGER
                        elif go_to_line:
                                try:
                                        lineno = int(commands[0])
                                except:
                                        bad_lineno = commands[0]
                                        raise CommandError(bad_lineno)
                                try:
                                        textfile.linenum(lineno)
                                except Exception as ae:
                                        print(ae)
                        #__________________________________________________________________________________________________________________________________________________
                                
                        #done TO ADD LINE/LINES AFTER THE CURRENT LINE
                        elif add_text:
                                where = commands[0]
                                try:
                                        textfile.add(where)
                                except AssertionError as ae:
                                        print(ae)
                                else:
                                        # print("another2")
                                        pass
                        #__________________________________________________________________________________________________________________________________________________

                        #done TO REMOVE CURRENT LINE AND (DEPENDING ON IF OFFSET IS GIVEN) LINES BEFORE/AFTER CURRENT LINE
                        elif delete:
                                if commands[1] == None:
                                        offset = 0
                                else:
                                        try:
                                                offset = int(commands[1])
                                        except:
                                                bad_offset = commands[1]
                                                raise CommandError(bad_offset)
                                try:
                                        textfile.delete(offset)
                                except AssertionError as dae:
                                        print(dae)
                        #__________________________________________________________________________________________________________________________________________________

                        #done TO ADD LINE/LINES BEFORE THE CURRENT LINE
                        elif insert:
                                where = commands[0]
                                try:
                                        textfile.add(where)
                                except AssertionError as ae:
                                        print(ae)
                        #__________________________________________________________________________________________________________________________________________________

                        #done TO LOAD A NEW FILE INTO THE TEXTFILE
                        elif load:
                                # WAIT! YOU HAVENT SAVED YOUR WORK!
                                end=""
                                if not file_saved:
                                        print("Current textfile NOT saved. File will be discarded.")
                                        end = input("Do you wish to continue? Choose Y/n or press ENTER to continue"+"\n")
                                        end=end.upper()

                                        

                                if file_saved or (end=="Y" or end==""):        # lOAD AWAY
                                        filename = commands[1]
                                        try:
                                                textfile.load(filename)
                                                file_saved = False
                                        except FileNotFoundError as fnfe:
                                                print(fnfe)

                                        except AssertionError as lae:
                                                print(lae)

                                        except FileError as lfe:
                                                print(lfe)
                                        except Exception as e:
                                                print(e)
                        #__________________________________________________________________________________________________________________________________________________
                                
                        #done TO PRINT CURRENT LINE AND (DEPENDING ON ARGUMENT) LINES BEFORE/AFTER THE CURRENT LINE
                        elif println:
                                p = commands[0] == "p"
                                offset = commands[1]

                                # prints if enter
                                if not p and offset==None:
                                        offset = commands[1] #make offset none so the program knows to simply go to next line
                                # print all else
                                elif p and offset==None:
                                        offset = 0 # this means the user wants to print current line
                                elif offset != None:
                                        try:
                                                offset = int(offset) # for all other prints
                                        except Exception:
                                                raise CommandError(offset)

                                try:        
                                        textfile.println(offset)
                                except AssertionError as pae:
                                        print(pae)
                                except Exception:
                                        print("diif")
                        #__________________________________________________________________________________________________________________________________________________
                        
                        #done done TO END THE PROGRAM
                        elif quit:
                                # just end it
                                end=""
                                if not file_saved:
                                        print("Current textfile NOT saved. File will be discarded.")
                                        end = input("Do you wish to continue? Choose Y/n or press ENTER to continue"+"\n")
                                        end=end.upper()

                                        # file_saved = True # temp
                                        
                                                
                                if file_saved or end=="Y" or end =="":        
                                        edit = False
                                        print(end_message)
                        #__________________________________________________________________________________________________________________________________________________
                        
                        #done TO REPLACE A PART OF A LINE (OR FULL LINE) WITH USER'S INPUT OR EMPTY STRING
                        elif replace:
                                text1 = commands[1]
                                text2 = commands[2]
                                try:
                                        textfile.replace(text1,text2)
                                except AssertionError as rae:
                                        print(rae)
                                except Exception as e:
                                        print(e)
                        #__________________________________________________________________________________________________________________________________________________

                        #done TO SEARCH FOR WHAT USER WANTS TO FIND IN TEXTFILE.
                        # SEARCH STARTS FROM LINE BEHIND THE CURRENT LINE AND WRAPS AROUN BACK TO CURRENT LINE IF SEARCH PARAMETER NOT FOUND. 
                        # IF search parameter found, Sets current line to the line with the search parameter.
                        elif search_fwd:
                                # same as back
                                where = commands[0]
                                text_to_find = commands[1]
                                try:
                                        textfile.search(text_to_find,where)
                                except AssertionError as saef:
                                        print(saef)
                        #__________________________________________________________________________________________________________________________________________________

                        #done TO SEARCH FOR WHAT USER WANTS TO FIND IN TEXTFILE.
                        # SEARCH STARTS FROM LINE AFTER THE CURRENT LINE AND WRAPS AROUND BACK TO CURRENT LINE IF SEARCH PARAMETER NOT FOUND. 
                        # IF search parameter found, Sets current line to the line with the search parameter.
                        elif search_bck:
                                #same as forward
                                where = commands[0]
                                text_to_find = commands[1]
                                try:
                                        textfile.search(text_to_find,where)
                                except AssertionError as saeb:
                                        print(saeb)
                        #__________________________________________________________________________________________________________________________________________________
                        
                        #done TO SORT THE LINES IN THE TEXTFILE IN ALPHABETICAL ORDER. The current line is the last line after sorting.
                        elif sort:
                                textfile.sort() # no need for assertions here
                        #__________________________________________________________________________________________________________________________________________________
                        
                        #done TO SAVE ALL EDITS MADE IN THE TEXTFILE TO THE GIVEN FILE WITH THE FILENAME.
                        # IF NO FILENAME GIVEN, THE EDITS ARE SAVED TO THE TEXTFILE'S CURRENT FILENAME
                        elif write:
                                filename = commands[1]
                                textfile.write(filename) # no need for assertions here, will create file if it doesnt exist
                                file_saved = True
                        #__________________________________________________________________________________________________________________________________________________

                        #done if the user gives an invalid command, the user is informed.
                        else:
                                command = commands[0]
                                raise CommandError(command)
                        #__________________________________________________________________________________________________________________________________________________
                        
                except CommandError as ce: # handling all bad input
                        print(ce)
#####################################################################################################################################################
        
                
                

# CLASS DEFINITIONS #################################################################################################################################

class DLinkedListNode:
        def __init__(self, initData, initNext, initPrevious):
                self.data = initData
                self.next = initNext
                self.previous = initPrevious

                if (initPrevious != None):
                        initPrevious.next = self
                if (initNext != None):
                        initNext.previous = self

        def __str__(self):
                return "%s" % (self.data)

        def getData(self):
                return self.data

        def getNext(self):
                return self.next

        def getPrevious(self):
                return self.previous

        def setData(self, newData):
                self.data = newData

        def setNext(self, newNext):
                self.next = newNext

        def setPrevious(self, newPrevious):
                self.previous= newPrevious

class DLinkedList:
        def __init__(self):
                self.head = None
                self.tail = None
                self.size = 0

        def __str__(self):
                s = "[ "
                current = self.head;
                while current != None:
                        s += "%s " % (current)
                        current = current.getNext()
                s += "]"
                return s

        def isEmpty(self):
                return self.size == 0

        def length(self):
                return self.size

        def getHead(self):
                return self.head

        def getTail(self):
                return self.tail

        def search(self, item):
                current = self.head
                found = False
                while current != None and not found:
                        if current.getData() == item:
                                found = True
                        else:
                                current = current.getNext()
                return found

        def index(self, item):
                current = self.head
                found = False
                index = 0
                while current != None and not found:
                        if current.getData() == item:
                                found = True
                        else:
                                current = current.getNext()
                                index = index + 1
                if not found:
                        index = -1
                return index

        def add(self, item):
                temp = DLinkedListNode(item, self.head, None)
                if self.head != None:
                        self.head.setPrevious(temp)
                else:
                        self.tail = temp
                self.head = temp
                self.size += 1

        def append(self, item):
                temp = DLinkedListNode(item, None, None)
                if (self.head == None):
                        self.head = temp
                else:
                        self.tail.setNext(temp)
                        temp.setPrevious(self.tail)
                self.tail = temp
                self.size +=1

        def remove(self, item):
                current = self.head
                previous = None
                found = False
                while not found:
                        if current.getData() == item:
                                found = True
                        else:
                                previous = current
                                current = current.getNext()
                if previous == None:
                        self.head = current.getNext()
                else:
                        previous.setNext(current.getNext())
                if (current.getNext() != None):
                        current.getNext().setPrevious(previous)
                else:
                        self.tail = previous
                self.size -= 1

        def removeitem(self, current):
                previous = current.getPrevious()
                if previous == None:
                        self.head = current.getNext()
                else:
                        previous.setNext(current.getNext())
                if (current.getNext() != None):
                        current.getNext().setPrevious(previous)
                else:
                        self.tail=previous
                if previous:
                        self.curr = previous.getNext()  # MIAY BE ERROR HERE

                else:
                        self.curr = None
                self.size -= 1
#__________________________________________________________________________________________________________________________________________________

        def insert(self, current, item, where):
                """
                Adds a node before/after ther current node in linked list.
    
                Parameters
                ----------
                current : DLinkedListNode
                        node to add before or after to

                item : Any
                        data for inserted new node

                where : int
                        0: insert node before current
                        1: insert node afte current
                

                Returns
                -------
                none
                """    
                # assert current!=None, "%s is not of type DLlinkedNode"%str(current)
                # You write this code
                # NOTE: there is an extra parameter here
                # Where = 0 (before current)
                # Where = 1 (after current)

                if current == None:
                        self.append(item)
                else:
                        if where == 0:
                                if current.getPrevious() == None: #Head
                                        self.add(item)                                        
                                else:
                                        new_line_node = DLinkedListNode(item, current, current.getPrevious())
                                        self.size+=1

                                
                        elif where == 1:
                                if current.getNext() == None: #Tail
                                        self.append(item)
                                else:
                                        new_line_node = DLinkedListNode(item, current.getNext(), current)
                                        
                                        self.size+=1
#__________________________________________________________________________________________________________________________________________________

#################################################################################################################################
#EXCEPTION CLASSES
class CommandError(Exception):
    def __init__(self,command):
        self.error_message = "%s: invalid command" % command
        super().__init__(self.error_message)
        
class FileError(Exception):
    def __init__(self,command):
        self.error_message = "%s: requires a filename parameter" % command
        super().__init__(self.error_message)

#################################################################################################################################

class TextFile:
        """
        Textfile class initilizer function
        
        Parameters
        ----------
        name : str          
                A string denoting the textfile's filename.
        text : DLinkedList          
                A doubly linked list containing an ordered set of lines in the textfile.
        current : DLinkedListNode        
                A node containing the information/data for a given line. The current line in the textfile.
        
        -------
        none
        """ 

        #DONE
        def __init__(self,name):

                assert type(name)==str, "%s is not a string for filename"%str(name)

                self.filename = name
                self.__text = DLinkedList()
                self.current = self.__text.getHead() # WILL BE NONe TO START
                
                # will open a given file but will open an empty file if given file is DNE; STARTS WITH AN EMPTY FILE with given name
                try:
                        filemode = "r"
                        tfile = open(self.filename,filemode)
                except:
                        filemode = "w"
                        tfile = open(self.filename,filemode)
                        
                finally:
                        tfile.close()
                        self.load(self.filename) # no need to try except block because will create file if need be
#__________________________________________________________________________________________________________________________________________________
        

        #DONE
        def load(self,name):
                """
                Loads a different file for editing.
    
                Parameters
                ----------
                name : str          
                        A string denoting the textfile's filename.
                

                Returns
                -------
                none
        
                """  
                load_command = "load"
                if name==None:
                        raise FileError(load_command) # Error for if no filename given
                assert type(name)==str, "%s: %s is not of type str"%(load_command,str(name))

                self.filename = name
                filemode = "r"

                # first remove all items current in self,text if need be
                if self.__text.length()>0:
                        first = self.__text.getHead()
                        self.setCurr(first)


                        current = self.current
                        while current!=None:
                                self.__text.removeitem(current)
                                current=current.getNext()

                try:
                        file = open(self.filename,filemode)
                        for line in file.readlines():
                                self.__text.append(line)
                        file.close()

                        if self.__text.isEmpty():
                                self.lineno = 0 # WILL BE 0 TO START
                        else:
                                first = self.__text.getHead()
                                self.setCurr(first)
                                self.lineno = 1 # WILL BE 1 TO START
                except:
                        raise FileNotFoundError
#__________________________________________________________________________________________________________________________________________________                       
            
        #DONE
        def write(self,name):
                """
                Saves file with the given filename. If no filename given, save all work to current textfile filename.
    
                Parameters
                ----------
                
                name : str          
                        A string denoting the textfile's filename.

                Returns
                -------
                none
                """  
                
                filemode = "w"

                if name==None: 
                        tofile = open(self.filename,filemode) # write to same  file
                else:
                        tofile = open(name,filemode) # write to different file

                first = self.__text.getHead()
                if first!=None:
                        self.setCurr(first) # set current to first line to add all the following lines in order
                        current = self.current
                else:
                        current = first #None
                while current != None:
                        tofile.write(current.getData())
                        current = current.getNext()
                
                tofile.close()

                # display saved file details
                filename = self.getName()
                no_lines = self.__text.length()
                lines = "("+str(no_lines)+")"
                print(filename,lines)
#__________________________________________________________________________________________________________________________________________________

        #DONE
        # changed the print funct of textfile to println for readability and debugging
        def println(self,lines):
                """
                Prints lines in textfile.
    
                Parameters
                ----------
                lines: int          
                        The number of lines to print, if lines > max lines in textfile. print all lines in textfile. 
                        If line argument given, prints current line, if null command, prints next line
                

                Returns
                -------
                none
        
                """ 
                print_command = "print"
                if lines==None:
                        print_command+=" next"
                        assert not self.__text.isEmpty(), "%s: Textfile empty"%print_command
                        assert self.current.getNext()!=None, "%s: End of Textfile"%print_command # FOR WHERN THERE ARE NO MORE LINES TO NEXT TO

                assert not self.__text.isEmpty(), "%s: Textfile empty"%print_command
                assert type(lines)==int or lines==None, "%s: %s must be of type int or NoneType"%(print_command,str(lines))
                
                curr_lineno = self.lineno # start at line number 1
                # max_lineno = self.text.length()
                moves = lines

                # NULL COMMAND PRINT NEXR
                if lines == None:
                        
                        try:
                                current = self.current.getNext() # CHANGE CURRENT LINE
                                curr_lineno+=1
                                print(str(curr_lineno)+":",current.getData())

                                self.current = current
                                self.lineno = curr_lineno
                        except Exception as e:
                                print("b",e)

                # print current line       
                elif lines == 0: # will raise assertion error if textfile empty
                        current = self.current
                        print(str(curr_lineno)+":",current.getData())
                        # DO NOT CHANGE CURRENT LINE
                        
                # print lines(including current) until reach given limit, print to end if given limit>>the lines in the textfile
                elif lines > 0:
                        current = self.current
                        while current != None and moves>0: #+1 for currentline
                                print(str(curr_lineno)+":",current.getData())
                                if current.getNext()==None:
                                        new_current = current
                                        new_lineno = curr_lineno
                                current = current.getNext()
                                curr_lineno+=1
                                moves-=1
                
                        if current!=None:
                                self.current = current # CHANGE CURRENT LINE
                                self.lineno = curr_lineno
                        else:
                                self.current = new_current
                                self.lineno = new_lineno

                        
                # print lines(including current) until reach given(reverse) limit, print to beginning if given limit<<the lines in the textfile       
                elif lines < 0:
                        current = self.current
                        while current.getPrevious() != None and moves<0:
                                current = current.getPrevious()
                                
                                moves+=1
                                if curr_lineno>1:
                                        curr_lineno -=1 # start at 1 always/ subtract all the way to one only if necessary
                        
                                
                        moves = lines        
                        while current != self.current and moves<0:
                                print(str(curr_lineno)+":",current.getData())
                                current = current.getNext()
                                curr_lineno+=1
                                moves+=1

                        print(str(self.lineno)+":",self.current.getData())
                        # DO NOT CHANGE CURRENT LINE
#__________________________________________________________________________________________________________________________________________________


        #DONE
        def linenum(self,lineno):
                """
                Goes to given line.
    
                Parameters
                ----------
                lineno: int          
                        The line the user want to go to, will become the current line and current line number
                

                Returns
                -------
                none
        
                """ 

                # set the current line to be the one at line #.
                linenum_command = "line number"
                assert not self.__text.isEmpty(), "%s: Textfile empty"%linenum_command
                assert type(lineno)==int and lineno >= 1, "%s: %s is not a valid line number"%(linenum_command,str(lineno))
                assert lineno <= self.__text.length(), "%s: %s is above the maximum lines"%(linenum_command,str(lineno))
                
                d = lineno-self.lineno
                moves = d
                current = self.current
                
                if d < 0:
                        while moves<0:
                                current = current.getPrevious()
                                moves += 1
                        
                elif d > 0:
                        while moves>0:
                                current = current.getNext()
                                moves -= 1

                # else: d=0
                #     print("no change") # no need to do anything if already at the postion you want.But prob dont need else per se

                self.current = current  # update current node
                self.lineno = lineno # update current line numebr
 #__________________________________________________________________________________________________________________________________________________
    
        #DONE
        def setLine(self,line):
                """
                Sets the current line number to given line

                Parameters
                ----------
                line: int     
                        The line number to set the current line number to.   

                Returns
                -------
                none
                """ 
                assert type(line)==int and line >= 1 and line <= self.__text.length(), "%s is not a valid line number"%str(line)

                self.lineno = line
#__________________________________________________________________________________________________________________________________________________

        #DONE
        def getLine(self):
                """
                Returns the current line number.

                Parameters
                ----------
                None   

                Returns
                -------
                the textfile's current line number
                """ 

                if self.lineno!=0:
                        return self.lineno
                elif self.lineno==0:
                        no = "Texfile empty"
                        print(no)
#__________________________________________________________________________________________________________________________________________________

        #DONE
        def setCurr(self,current):
                """
                Sets the current line to given line

                Parameters
                ----------
                line: int     
                        The line number to set the current line number to.   

                Returns
                -------
                none
                """ 
                setCurr_command = "setCurrent"
                #� set the current line
                assert type(current)==DLinkedListNode, "%s: %s is not of type DLinkedListNode"%(setCurr_command,str(current))
                self.current = current # change the line in the current node
                
#__________________________________________________________________________________________________________________________________________________

        #DONE DONE
        def getCurr(self):
                """
                Returns the current line's node. The cnode contains the data for the line.

                Parameters
                ----------
                None   

                Returns
                -------
                the textfile's current line node containing the data for the line
                """ 

                return self.current# get the line in the current node
#__________________________________________________________________________________________________________________________________________________

        #DONE DONE
        def search(self,text,where):
                """
                Searches for the line containing the search parameter(first instance), "text". If found in textfile,
                sets the current line to the line containing the search parameter. If not found in textfile, the current line doesnt change
    
                Parameters
                ----------
                text : str
                        The search parameter: the value the user wants to find in the textfile

                where : str
                        ?: insert node before current line
                        /: insert node after current line
                

                Returns
                -------
                none
                """   

                #� where is to look �before� or �after� the current line
                search_command = "search"
                before = "?"
                after = "/"
                back = where == before
                forward = where == after
                if back:
                        search_command+=" backward"
                elif forward:
                        search_command+=" forward"

                assert not self.__text.isEmpty(), "%s: Textfile empty"%search_command
                assert text != None, "%s: Search method requires a search parameter"%search_command
                assert back or forward, "%s: where must be "+before+" or "+after%search_command
                
                found = False # to efficiently break while loops
                line_moves = 0 # used to track line movement if change occurs. INITIALIZED

                # INITIAL first run through to either end
                if where == before:
                        current = self.current.getPrevious()
                        line_moves = -1 # START ONE BACK IF BEFORE

                elif where == after:
                        current = self.current.getNext()
                        line_moves = 1 # START ONE FORWARD IF AFTER
                
                while not found and current != None:
                        try:
                                found = text in current.getData()
                        except:
                                pass # can move one after reaching list end
                        if found:
                                # UPDATE BEFORE PRINITING
                                self.current = current # change current after printing
                                self.lineno+=line_moves
                                offset = 0 # want to preint current line but not change current yet
                                self.println(offset)
                        
                                
                                
                        elif not found:
                                if where == before:
                                        current = current.getPrevious()
                                        if line_moves+self.lineno>1:
                                                line_moves-=1
                                elif where == after:
                                        current = current.getNext()
                                        if line_moves+self.lineno<self.__text.length():
                                                line_moves+=1
                                        
                # still not found?, circle back around,
                if not found:
                        line = 0 # new tracking variable

                        if current == None: # extra security
                                if where == before:
                                        current = self.__text.getTail() #restart at tail and go back all the way to self.cuurent
                                        stop_condition = current.getNext() != self.current
                                        line = self.__text.length() # reset the moves DIFF FOR EACH SCENARIO(The END if before)
                                elif where == after:
                                        current = self.__text.getHead() #restart at head and go forward all the way to self.cuurent
                                        stop_condition = current.getPrevious() != self.current
                                        line = 1 # reset the moves DIFF FOR EACH SCENARIO(The Beginning if after)
                                        
                                while not found and current!=None and stop_condition:
                                        # still need to reset the stop condition with each iterations
                                        if where==before:
                                                stop_condition = current.getNext() != self.current
                                        elif where==after:
                                                stop_condition = current.getPrevious() != self.current

                                        try:
                                                found = text in current.getData()
                                        except:
                                                pass # can pass if end of list

                                        if found:
                                                # UPDATE BEFORE PRINITING
                                                self.current = current # change current after printing
                                                self.lineno = line
                                                offset = 0 # want to preint current line but not change current yet
                                                self.println(offset)
                                                

                                        elif not found:
                                                if where == before:
                                                        current = current.getPrevious()
                                                        line-=1
                                                elif where == after:
                                                        current = current.getNext()
                                                        line+=1         
#__________________________________________________________________________________________________________________________________________________


        # DONE DONE
        def replace(self,text1,text2):
                """
                Replaces the search parameter "text1" with "text2" if search parameter found in textfile.
    
                Parameters
                ----------
                text1 : str
                        The search parameter: the value the user wants to find in the textfile

                text1 : str
                        The replacement: the value the user wants to add in the textfile at desired location.
                
                Returns
                -------
                none
                """ 

                replace_command = "replace"
                assert text1 != None, "%s: replace method requires at least one operand"%replace_command # TEXT2 CAN BE NONE
                assert not self.__text.isEmpty(), "%s: Textfile empty"%replace_command

                #� in the current line, replace �text1� with �text2�, if possible.
                if text1 in self.current.getData():
                        words = shlex.split(self.current.getData())
                        # print(words)
                        replacement_index = None # default to a none index
                        text1_list = text1.split()
                        
                        # to get the index for replacement, also to get any punctuation/commas/colons
                        punctuation = ""
                        for n in range(len(text1_list)):
                                for word in words:
                                        if text1_list[n] in word:
                                                replacement_index = words.index(word)

                                                last_word = words.index(word) == len(words)-1
                                                if last_word and text1_list[n] != word:
                                                        punctuation = word[len(word)-1]

                                                words.remove(word)
                        
                        # print(replacement_index)

                        if replacement_index !=None:
                                newline = "\n"
                                if text2 != None:
                                        replacement = text2
                                elif text2 == None:
                                        replacement = ""
                                        
                                words.insert(replacement_index,replacement)

                                updated_line = " ".join(words)
                                updated_line+=punctuation+newline
                                self.current.setData(updated_line)

                # to see changes
                offset = 0
                self.println(offset)
#__________________________________________________________________________________________________________________________________________________


        # SORT HOWWW!!? -> MOVE THE DATA, #DONE DONE
        def sort(self):
                """
                Sorts the lines in the textfile in alphabetical order. Sets the current line to the last line of the file after sorting..
    
                Parameters
                ----------
                None
                
                Returns
                -------
                none
                """

                #� sort the entire file
                if self.__text.length()>1:
                        current = self.__text.getHead()
                        while current!=None:
                                current_min_node= current
                                nxt = current.getNext()
                                # prev_max_node = prev # initialize

                                while nxt != None:
                                        if nxt.getData()<current_min_node.getData():
                                                current_min_node = nxt
                                                # nxt_min_node = nxt
                                        nxt = nxt.getNext()

                                # THE SWITCH
                                nxt_min = current.getData()
                                current.setData(current_min_node.getData())
                                current_min_node.setData(nxt_min)
                                current=current.getNext()

                # set current to last line
                last = self.__text.getTail()
                if last!=None:
                        self.setCurr(last)
#__________________________________________________________________________________________________________________________________________________

        #DONE DONE
        def add(self,where):
                """
                Adds a new line/ new lines before or after the current line.
    
                Parameters
                ----------

                where : str
                        i: insert node before current line
                        a: insert node after current line
                
                Returns
                -------
                none
                """   

                #� where is �insert� (before) or �add� (after) the current line.
                add_command = "add"
                before = where == "insert"[0]
                after = where == "add"[0]
                assert before or after, "%s: invalid location"%add_command

                newline = "\n"
                divider = "|"
                nothing = ""
                entry = divider
                item = None
                while item!=nothing:
                        item = input()
                        entry += divider+item
                # print(entry)
                
                whereto = None

                # clean the entry list
                dirty_entrylist = entry.split(divider)

                entrylist = []
                for entry_index in range(len(dirty_entrylist)):
                        entry = dirty_entrylist[entry_index].strip()
                        if entry!=nothing:
                                entry+=newline
                                entrylist.append(entry)

                iteration = None 
                if before:
                        iteration = range(len(entrylist)-1,-1,-1) # iterate backwards
                elif after:
                        iteration = range(len(entrylist)) # iterate forwards

                for entry_index in iteration:
                        if self.current == None and self.__text.isEmpty():
                                # THE LIST IS EMPTY TRO SATRAT
                                entry = entrylist[entry_index]
                                self.__text.append(entry)
                                self.current = self.__text.getHead() #getHead()
                                self.lineno = 1

                        else:
                                if before:
                                        whereto = 0
                                        
                                elif after:
                                        whereto = 1
        
                                entry = entrylist[entry_index]
                                self.__text.insert(self.current,entry,whereto)
                                

                                if before:
                                
                                        # self.lineno DOES NOT CHANGE?
                                        self.current =self.current.getPrevious()

                                elif after:
                                        # change lineno to the line inserted
                                        if self.lineno== self.__text.length()-1:
                                                self.lineno = self.__text.length() # DONT CHANGE IF ADDING AFTER TAIL
                                        else:
                                                self.lineno +=1
                                                
                                        
                                        self.current=self.current.getNext()
#__________________________________________________________________________________________________________________________________________________

        #DONE DONE
        def delete(self,offset):
                """
                Deletes lines before or after and including the current line. if no offset provided, 
                the current line is deleted and the next line in the file becomes the current line.
    
                Parameters
                ----------

                offset : int
                        the number of lines before(offset<0) or after(offset>0) the current line to delete. No offset-> delete only current line
                
                Returns
                -------
                none
                """ 

                #� delete line(s), with offset indicating the number of lines
                command = "delete"
                assert type(offset)==int, "%s is not an integer"%str(offset)
                assert not self.__text.isEmpty(), "%s: Textfile empty"%command

                if offset < 0:
                        removes = offset
                        current = self.current.getPrevious()
                        while current != None and removes < 0:
                                self.__text.removeitem(current)
                                current = current.getPrevious()
                                removes+=1

                        new_current = self.current
                        if current == None: # AT HEAD
                                self.current = self.current.getNext()
                                self.lineno = 1
                        elif current !=None:
                                self.current = self.current.getNext()
                                self.lineno+=offset

                        self.__text.removeitem(new_current)

                elif offset > 0:
                        removes = offset
                        current = self.current.getNext()
                        while current != None and removes > 0:
                                self.__text.removeitem(current)
                                current = current.getNext()
                                removes-=1
                        new_current = self.current
                        if current == None: # at tail
                                self.current = self.current.getPrevious()
                                self.lineno = self.__text.length()-1
                        elif current !=None:
                                self.current = current
                                # print(self.current.getData())
                                # self.lineno DOESNT CHANGE

                        self.__text.removeitem(new_current)
                        

                elif offset == 0:
                        current = self.current
                        
                        if current.getPrevious()==None: # The head
                                self.current = self.current.getNext()
                                self.lineno=1
                        elif current.getNext()==None: # The tail
                                self.current = self.current.getPrevious()
                                self.lineno = self.__text.length()-1

                        elif current.getNext()!=None:
                                self.current = self.current.getNext()
                                # self.lineno DOESNT CHANGE

                        self.__text.removeitem(current)

                if self.__text.isEmpty():
                        self.lineno=0
#__________________________________________________________________________________________________________________________________________________    

        def getName(self):
                """
                Replaces the search parameter "text1" with "text2" if search parameter found in textfile.
    
                Parameters
                ----------
                None
                
                Returns
                -------
                The filename of the loaded textfile
                """ 

                #� get the name of the file.
                return self.filename
#__________________________________________________________________________________________________________________________________________________
    
        def setName(self,name):
                """
                Deletes lines before or after and including the current line. if no offset provided, 
                the current line is deleted and the next line in the file becomes the current line.
    
                Parameters
                ----------

                offset : int
                        the number of lines before(offset<0) or after(offset>0) the current line to delete. No offset-> delete only current line
                
                Returns
                -------
                none
                """ 
                
                #� set the name of the file.
                setName_command="setName"
                assert type(name)==str, "%s: %s is not of type str"%(setName_command,str(name))

                self.filename = name
#__________________________________________________________________________________________________________________________________________________
   
main() # main function call
