'''
Accomplished on 31 July 2022
Jayden LI
'''
# Global Variables
NumberOfStudents = 0
InputFileName = "ResultsData.csv"
OutputFileName = "OutputInformation.txt"

# Read through the file one line at a time. Each whole line goes into the variable Line
def ProcessInformationFile():
    # This subprogram/function will read the information from the input file: InputFileName

    import pandas as pd
    dfExcel = pd.read_csv(InputFileName, names= ['student','score'])

    Names = []
    Scores = []
        
    # Append them to the appropriate Lists
    for name in dfExcel['student']:
        Names.append(name.strip())
    # Increase the number of students
        global NumberOfStudents
        NumberOfStudents += 1
    for score in dfExcel['score']:
        Scores.append(float(score))
    # The input file is automatically closed.

    # For every entry output "Name scored Result" such as "Peter scored 86.4"
    fullList = []
    for i in range (len(Names)):
        fullList.append(f'{Names[i]} scored {Scores[i]}')

    # Output the information in the Names and Scores Lists to the Output File
    # Open the output file for writing to
    with open(OutputFileName,'w') as OutputFile:
        for names in fullList:
            OutputFile.write(names + '\n')

# Main Program starts here
print ("Reading information from: ",  InputFileName)
ProcessInformationFile()
print (NumberOfStudents, " records output to: ", OutputFileName)