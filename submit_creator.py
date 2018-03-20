# Last tested with tkinter v8.6.7 on Python 3.6.3
# Run the script and click the Help button or scroll down to help() function definiton below for more detail

import tkinter as tk
from tkinter import font, filedialog
from os import chdir

class CondorSubmit(tk.Tk):
    def __init__(self, parent):
        tk.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

#############################################################################

    def initialize(self):
        # set window size
        self.geometry('900x600')
        self.grid()
        self.grid_columnconfigure(0,weight=1)
        #################################
        # create font to use in widgets
        self.helv12Bold = font.Font(family="Helvetica",size=12, weight='bold')
        self.helv12 = font.Font(family="Helvetica",size=12)
        self.courier12 = font.Font(family="Courier",size=12)
        #################################
        # Control variable for project name
        self.projControl = tk.StringVar()

        # Create Label Frame for project name
        self.projLabelFrame = tk.LabelFrame(self, text='Project name', font=self.helv12Bold)
        self.projLabelFrame.grid(sticky='EW', padx=2.5, pady=2.5)
        self.projLabelFrame.grid_columnconfigure(0,weight=1)

        # Create text entry for project name
        self.projLabelFrame.projEntry = tk.Entry(self.projLabelFrame, textvariable=self.projControl, width=40, font=self.courier12)
        self.projLabelFrame.projEntry.grid(sticky='EW', row=0)

        #################################

        # Universe control variable
        self.universeControl = tk.StringVar()
        self.universeControl.set('vanilla')

        # Create Label Frame for Universe buttons
        self.universeLabelFrame = tk.LabelFrame(self, text='Universe', font=self.helv12Bold)
        self.universeLabelFrame.grid(sticky=tk.W, padx=2.5, pady=2.5)

        # Create Universe radio buttons: Vanilla and Standard
        self.universeLabelFrame.vanillaRadio = tk.Radiobutton(self.universeLabelFrame, text='vanilla', value='vanilla', variable= self.universeControl, font=self.courier12)
        self.universeLabelFrame.vanillaRadio.grid(column=0, row=0)

        self.universeLabelFrame.standardRadio = tk.Radiobutton(self.universeLabelFrame, text='standard', value='standard', variable= self.universeControl, font=self.courier12)
        self.universeLabelFrame.standardRadio.grid(column=1, row=0)

        #################################

        # Control variable for working directory
        self.dirControl = tk.StringVar()

        # Create Label Frame for working directory
        self.dirLabelFrame = tk.LabelFrame(self, text='Working directory file path', font=self.helv12Bold)
        self.dirLabelFrame.grid(sticky='EW', padx=2.5, pady=2.5)
        self.dirLabelFrame.grid_columnconfigure(0,weight=1)

        # Create text entry for working directory
        self.dirLabelFrame.dirEntry = tk.Entry(self.dirLabelFrame, textvariable=self.dirControl, width=40, font=self.courier12)
        self.dirLabelFrame.dirEntry.grid(sticky='EW')

        #################################

        # Control variable for executable file
        self.execControl = tk.StringVar()

        # Create Label Frame for executable file name
        self.execLabelFrame = tk.LabelFrame(self, text='Executable file', font=self.helv12Bold)
        self.execLabelFrame.grid(sticky='EW', padx=2.5, pady=2.5)
        self.execLabelFrame.grid_columnconfigure(0,weight=1)

        # Create text entry for executable file name
        self.execLabelFrame.execEntry = tk.Entry(self.execLabelFrame, textvariable=self.execControl, width=40, font=self.courier12)
        self.execLabelFrame.execEntry.grid(sticky='EW')

        #################################

        # Control variable for transfer input files
        self.inputControl = tk.StringVar()

        # Create Label Frame for transfer input files
        self.inputLabelFrame = tk.LabelFrame(self, text='Zip directory for input files', font=self.helv12Bold)
        self.inputLabelFrame.grid(sticky='EW', padx=2.5, pady=2.5)
        self.inputLabelFrame.grid_columnconfigure(0,weight=1)

        # Create text entry for transfer input files
        self.inputLabelFrame.inputEntry = tk.Entry(self.inputLabelFrame, textvariable=self.inputControl, width=40, font=self.courier12)
        self.inputLabelFrame.inputEntry.grid(sticky='EW')

        #################################

        # Control variable for log file
        self.logControl = tk.StringVar()

        # Create Label Frame for log file
        self.logLabelFrame = tk.LabelFrame(self, text='Output log file', font=self.helv12Bold)
        self.logLabelFrame.grid(sticky='EW', padx=2.5, pady=2.5)
        self.logLabelFrame.grid_columnconfigure(0,weight=1)

        # Create text entry for log file
        self.logLabelFrame.logEntry = tk.Entry(self.logLabelFrame, textvariable=self.logControl, width=40, font=self.courier12)
        self.logLabelFrame.logEntry.grid(sticky='EW')

        #################################

        # Should transfer files control variable
        self.transControl = tk.StringVar()
        self.transControl.set('YES')

        # Create Label Frame for should transfer files buttons
        self.transLabelFrame = tk.LabelFrame(self, text='Should transfer files?', font=self.helv12Bold)
        self.transLabelFrame.grid(sticky=tk.W, padx=2.5, pady=2.5)

        # Create should transfer files radio buttons: YES and NO
        self.transLabelFrame.YesRadio = tk.Radiobutton(self.transLabelFrame, text='YES', value='YES', variable= self.transControl, font=self.courier12)
        self.transLabelFrame.YesRadio.grid(column=0, row=0)

        self.transLabelFrame.ifNeedRadio = tk.Radiobutton(self.transLabelFrame, text='IF_NEEDED', value='IF_NEEDED', variable= self.transControl, font=self.courier12)
        self.transLabelFrame.ifNeedRadio.grid(column=1, row=0)

        self.transLabelFrame.NoRadio = tk.Radiobutton(self.transLabelFrame, text='NO', value='NO', variable= self.transControl, font=self.courier12)
        self.transLabelFrame.NoRadio.grid(column=2, row=0)

        #################################

        # When transfer output control variable
        self.outControl = tk.StringVar()
        self.outControl.set('ON_EXIT')

        # Create Label Frame for When transfer output buttons
        self.outLabelFrame = tk.LabelFrame(self, text='When to transfer output files?', font=self.helv12Bold)
        self.outLabelFrame.grid(sticky=tk.W, padx=2.5, pady=2.5)

        # Create When transfer output files radio buttons: ON_EXIT and ON_EXIT_OR_EVICT
        self.outLabelFrame.OnExitRadio = tk.Radiobutton(self.outLabelFrame, text='ON_EXIT', value='ON_EXIT', variable= self.outControl, font=self.courier12)
        self.outLabelFrame.OnExitRadio.grid(column=0, row=0)

        self.outLabelFrame.ExitEvictRadio = tk.Radiobutton(self.outLabelFrame, text='ON_EXIT_OR_EVICT', value='ON_EXIT_OR_EVICT', variable= self.outControl, font=self.courier12)
        self.outLabelFrame.ExitEvictRadio.grid(column=1, row=0)

        #################################

        # Control variable for number of jobs
        self.numjobsControl = tk.IntVar()
        self.numjobsControl.set(0)

        # Create Label Frame for num jobs
        self.numjobsLabelFrame = tk.LabelFrame(self, text='Number of jobs', font=self.helv12Bold)
        self.numjobsLabelFrame.grid(sticky='EW', padx=2.5, pady=2.5)
        self.numjobsLabelFrame.grid_columnconfigure(0,weight=1)

        # Create text entry for num jobs
        self.numjobsLabelFrame.numjobsEntry = tk.Entry(self.numjobsLabelFrame, textvariable=self.numjobsControl, width=40, font=self.courier12)
        self.numjobsLabelFrame.numjobsEntry.grid(sticky='EW')

        #################################

        # Create list to store tuples of argument entries
        self.arguments = []

        # Arguments control variables
        self.nameControl = tk.StringVar()
        self.constantControl = tk.StringVar()
        self.constantControl.set('constant')
        self.ConValControl = tk.StringVar()
        self.startControl = tk.DoubleVar()
        self.stepsControl = tk.DoubleVar()

        # Create Label Frame for arguments box
        self.argsFrame = tk.LabelFrame(self, text='Add arguments needed for executable', font=self.helv12Bold)
        self.argsFrame.grid(sticky='NEW', padx=2.5, pady=2.5, row=0, column=2, rowspan=15)
        self.argsFrame.grid_columnconfigure(0,weight=1)

        # Create event button for adding an argument field
        self.argsFrame.argsButton = tk.Button(self.argsFrame, text='Add new argument', command=self.arg_add, font=self.helv12)
        self.argsFrame.argsButton.grid(sticky=tk.W, padx=1.5, pady=1.5)

        # create button to view arguments already entered
        self.argsFrame.viewButton = tk.Button(self.argsFrame, text='View saved arguments', command=self.view_args, font=self.helv12)
        self.argsFrame.viewButton.grid(sticky=tk.W, padx=1.5, pady=1.5)

        #################################

        # Create frame to contain buttons
        self.buttonFrame = tk.Frame(self)
        self.buttonFrame.grid(sticky=tk.W, padx=2.5, pady=2.5)

        # Create button to read in previous submit file parameters
        self.buttonFrame.loadButton = tk.Button(self.buttonFrame, text="Load existing submit file", command=self.load_previous, font=self.helv12)
        self.buttonFrame.loadButton.grid(sticky=tk.W, padx=2.5, pady=2.5)

        # Create close without saving button
        self.buttonFrame.closeButton = tk.Button(self.buttonFrame, text="Close without saving", command=self.destroy, font=self.helv12)
        self.buttonFrame.closeButton.grid(sticky=tk.W, padx=2.5, pady=2.5)

        # Create preview button
        self.buttonFrame.previewButton = tk.Button(self.buttonFrame, text='Preview', command=self.combine_funcs(self.compile_output, self.full_preview), font=self.helv12, state=tk.NORMAL)
        self.buttonFrame.previewButton.grid(sticky=tk.E, padx=2.5, pady=2.5, row=0, column=1)

        # Create DISABLED finish & create submission file button
        self.buttonFrame.finishButton = tk.Button(self.buttonFrame, text='Finish & Create file', command=self.combine_funcs(self.compile_output, self.finish), font=self.helv12, state=tk.DISABLED)
        self.buttonFrame.finishButton.grid(sticky=tk.E, padx=2.5, pady=2.5, row=1, column=1)

        # Create Help button
        self.buttonFrame.helpButton = tk.Button(self.buttonFrame, text='Help', command=self.help, font=self.helv12)
        self.buttonFrame.helpButton.grid(sticky=tk.W, padx=2.5, pady=2.5)

#############################################################################

    #allows for applying more than one function to a widget
    def combine_funcs(self, *funcs):
        def combined_func(*args, **kwargs):
            for f in funcs:
                f(*args, **kwargs)
        return combined_func

    def arg_add(self):
        # add arguments one at a time
        # open a new argument wizard (new window?), display options
        # when finished, add argument and properties to list as tuple
        # display already-entered arguments in original window

        self.argsFrame.argsButton.destroy()
        self.argsFrame.viewButton.destroy()
        #################################
        self.nameControl.set('')
        self.constantControl.set('constant')
        self.ConValControl.set('')
        self.startControl.set(0.0)
        self.stepsControl.set(0.0)
        #################################
        self.argsFrame.argsLabelFrame = tk.Frame(self.argsFrame)
        self.argsFrame.argsLabelFrame.grid(sticky='EW', padx=2.5, pady=2.5)
        self.argsFrame.argsLabelFrame.grid_columnconfigure(0,weight=1)
        #################################
        self.argsFrame.argsLabelFrame.nameLabel = tk.Label(self.argsFrame.argsLabelFrame, text='Name of argument', font=self.helv12Bold)
        self.argsFrame.argsLabelFrame.nameLabel.grid(sticky='W', pady=1.5)
        self.argsFrame.argsLabelFrame.nameEntry = tk.Entry(self.argsFrame.argsLabelFrame, textvariable=self.nameControl, font=self.courier12)
        self.argsFrame.argsLabelFrame.nameEntry.grid(sticky='EW')
        #################################
        self.argsFrame.argsLabelFrame.ConVarLabel = tk.Label(self.argsFrame.argsLabelFrame, text='Is this argument constant or variable?', font=self.helv12Bold)
        self.argsFrame.argsLabelFrame.ConVarLabel.grid(sticky='W', pady=1.5)
        self.argsFrame.argsLabelFrame.ConRadio = tk.Radiobutton(self.argsFrame.argsLabelFrame, text='constant', value='constant', variable=self.constantControl, command=self.disable_variable, font=self.courier12)
        self.argsFrame.argsLabelFrame.ConRadio.grid(sticky='W')
        self.argsFrame.argsLabelFrame.VarRadio = tk.Radiobutton(self.argsFrame.argsLabelFrame, text='variable', value='variable', variable=self.constantControl, command=self.disable_constant, font=self.courier12)
        self.argsFrame.argsLabelFrame.VarRadio.grid(sticky='W')
        #################################
        self.argsFrame.argsLabelFrame.ConValLabel = tk.Label(self.argsFrame.argsLabelFrame, text='What is the value of this constant argument?', font=self.helv12Bold)
        self.argsFrame.argsLabelFrame.ConValLabel.grid(sticky='W', pady=1.5)
        self.argsFrame.argsLabelFrame.ConValEntry = tk.Entry(self.argsFrame.argsLabelFrame, textvariable=self.ConValControl, font=self.courier12)
        self.argsFrame.argsLabelFrame.ConValEntry.grid(sticky='EW')
        #################################
        self.argsFrame.argsLabelFrame.startLabel = tk.Label(self.argsFrame.argsLabelFrame, text='Start value', font=self.helv12Bold)
        self.argsFrame.argsLabelFrame.startLabel.grid(sticky='W', pady=1.5)
        self.argsFrame.argsLabelFrame.startEntry = tk.Entry(self.argsFrame.argsLabelFrame, textvariable=self.startControl, state=tk.DISABLED, font=self.courier12)
        self.argsFrame.argsLabelFrame.startEntry.grid(sticky='EW')
        #################################
        self.argsFrame.argsLabelFrame.stepsLabel = tk.Label(self.argsFrame.argsLabelFrame, text='Step interval', font=self.helv12Bold)
        self.argsFrame.argsLabelFrame.stepsLabel.grid(sticky='W', pady=1.5)
        self.argsFrame.argsLabelFrame.stepsEntry = tk.Entry(self.argsFrame.argsLabelFrame, textvariable=self.stepsControl, state=tk.DISABLED, font=self.courier12)
        self.argsFrame.argsLabelFrame.stepsEntry.grid(sticky='EW')
        #################################
        # Create Save button
        self.argsFrame.argsLabelFrame.saveButton = tk.Button(self.argsFrame.argsLabelFrame, text='Save', command=self.arg_save, font=self.helv12)
        self.argsFrame.argsLabelFrame.saveButton.grid(sticky=tk.W, pady=1.5)

        # Create button to view arguments already entered
        self.argsFrame.viewButton = tk.Button(self.argsFrame, text='View saved arguments', command=self.view_args, font=self.helv12)
        self.argsFrame.viewButton.grid(sticky=tk.W, padx=1.5, pady=1.5)

#############################################################################

    def load_previous(self):
        self.template_name = str(filedialog.askopenfilename(initialdir=self.dirControl, 
                                                            title='Select template file...', 
                                                            filetypes=[('Condor Submission Files', '*.txt'),
                                                                       ('All files', '*.*')]))

        # Set project name (assumes the file ends '_submit.txt')
        self.projControl.set(str.split(self.template_name, '/')[-1][0:-10] + 'new')

        # Set directory (assumes the file ends '_submit.txt')
        fnindex = str.rindex(self.template_name, '/')
        self.dirControl.set(self.template_name[0:fnindex])

        # Open file for reading
        self.template_file = open(self.template_name, mode='r')
        self.template_text = self.template_file.readlines()
        #################################
        # Read and Set Universe parameter
        self.universeControl.set(str.rstrip(str.split(self.template_text[0], '= ')[-1], '\n'))
        # Read and Set executable file name
        self.execControl.set(str.rstrip(str.split(self.template_text[1], '= ')[-1], '\n'))
        # Read and Set input files
        self.inputControl.set(str.rstrip(str.split(self.template_text[2], '= ')[-1], '\n'))
        # Read and Set log file name
        self.logControl.set(str.rstrip(str.split(self.template_text[3], '= ')[-1], '\n'))
        # Read and Set should transfer files
        self.transControl.set(str.rstrip(str.split(self.template_text[4], '= ')[-1], '\n'))
        # Read and Set when to transfer output files
        self.outControl.set(str.rstrip(str.split(self.template_text[5], '= ')[-1], '\n'))
        #################################
        # Count instances of "Queue" and Set as number of jobs
        queueCount = 0
        for line in self.template_text:
            if 'Queue' in line:
                queueCount += 1
        self.numjobsControl.set(queueCount)
        #################################
        # Create lists to store arguments
        self.job1List = []
        self.job2List = []
        self.job1List = str.split(str.rstrip(str.split(self.template_text[8], '= ')[-1], '\n'), ' ')
        self.job2List = str.split(str.rstrip(str.split(self.template_text[12], '= ')[-1], '\n'), ' ')
        #################################
        for item in self.job1List:
            if item == self.job2List[self.job1List.index(item)]:
                self.nameControl.set('arg'+ str(self.job1List.index(item)))
                self.constantControl.set('constant')
                self.ConValControl.set(item)
                self.startControl.set(0.0)
                self.stepsControl.set(0.0)
            else:
                self.nameControl.set('arg'+ str(self.job1List.index(item)))
                self.constantControl.set('variable')
                self.ConValControl.set('NO_VALUE')
                self.startControl.set(float(item))
                self.stepsControl.set(float(self.job2List[self.job1List.index(item)]) - float(item))
            argTup = (self.nameControl.get(), self.constantControl.get(), self.ConValControl.get(), self.startControl.get(), self.stepsControl.get())
            self.arguments.append(argTup)
        self.template_file.close()
        #################################
        # activate Preview button
        self.buttonFrame.previewButton.configure(state=tk.NORMAL)
        # activate Finish and Create file button
        self.buttonFrame.finishButton.configure(state=tk.NORMAL)

#############################################################################

    def arg_save(self):
        # remove Save button
        self.argsFrame.argsLabelFrame.saveButton.destroy()
        # remove button to view arguments already entered
        self.argsFrame.viewButton.destroy()
        # activate Preview button
        self.previewButton.configure(state=tk.NORMAL)
        # activate Finish and Create file button
        self.finishButton.configure(state=tk.NORMAL)
        #################################
        if self.nameControl.get() == '':
            self.nameControl.set('NO_NAME')
        else:
            pass

        if self.ConValControl.get() == '':
            self.ConValControl.set('NO_VALUE')
        else:
            pass
        #################################
        # save info
        argTup = (self.nameControl.get(), self.constantControl.get(), self.ConValControl.get(), self.startControl.get(), self.stepsControl.get())
        self.arguments.append(argTup)
        #################################
        # grey-out info
        self.argsFrame.argsLabelFrame.nameEntry.configure(state=tk.DISABLED)
        self.argsFrame.argsLabelFrame.ConRadio.configure(state=tk.DISABLED)
        self.argsFrame.argsLabelFrame.VarRadio.configure(state=tk.DISABLED)
        self.argsFrame.argsLabelFrame.ConValEntry.configure(state=tk.DISABLED)
        self.argsFrame.argsLabelFrame.startEntry.configure(state=tk.DISABLED)
        self.argsFrame.argsLabelFrame.stepsEntry.configure(state=tk.DISABLED)
        #################################
        # create button to remove old argument entry form then recreate the form
        self.argsFrame.argsLabelFrame.addButton = tk.Button(self.argsFrame.argsLabelFrame, text='Add another argument', command=self.combine_funcs(self.old_remove, self.arg_add), font=self.helv12)
        self.argsFrame.argsLabelFrame.addButton.grid(sticky=tk.W, padx=1.5, pady=1.5)

        # create button to view arguments already entered
        self.argsFrame.argsLabelFrame.viewButton = tk.Button(self.argsFrame.argsLabelFrame, text='View saved arguments', command=self.view_args, font=self.helv12)
        self.argsFrame.argsLabelFrame.viewButton.grid(sticky=tk.W, padx=1.5, pady=1.5)

        # create button for Delete last argument
        self.argsFrame.argsLabelFrame.deleteButton = tk.Button(self.argsFrame.argsLabelFrame, text='Delete last entry', command=self.arg_delete, font=self.helv12)
        self.argsFrame.argsLabelFrame.deleteButton.grid(sticky=tk.W, padx=1.5, pady=1.5)

#############################################################################

    def view_args(self):
        self.argview = tk.Toplevel()
        #################################
        self.labelBox = ''
        for t in self.arguments:
            if t[1] == 'constant':
                self.labelBox += 'Argument '+ str(self.arguments.index(t)) + ':\n' + str(t[0]) + '\n' + str(t[1]) + '\n' + str(t[2]) + '\n\n'
            elif t[1] == 'variable':
                self.labelBox += 'Argument '+ str(self.arguments.index(t)) + ':\n' + str(t[0]) + '\n' + str(t[1]) + '\n' + str(t[3]) + '\n' + str(t[4]) + '\n\n'
        self.labelBox= self.labelBox[:-2].rstrip()
        #################################
        self.argview.Scroll = tk.Scrollbar(self.argview)
        self.argview.Scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.argview.resultsText = tk.Text(self.argview, width=30, font=self.courier12)
        self.argview.resultsText.pack(side=tk.LEFT, fill='both', expand=True)
        self.argview.Scroll.configure(command=self.argview.resultsText.yview)
        self.argview.resultsText.configure(yscrollcommand=self.argview.Scroll.set)
        self.argview.resultsText.insert(tk.END, self.labelBox)
        self.argview.resultsText.configure(state=tk.DISABLED)

#############################################################################

    def full_preview(self):
        self.preview = tk.Toplevel()
        self.preview.Scroll = tk.Scrollbar(self.preview)
        self.preview.Scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.preview.resultsText = tk.Text(self.preview, width=100, font=self.courier12)
        self.preview.resultsText.pack(side=tk.LEFT, fill='both', expand=True)
        self.preview.Scroll.configure(command=self.preview.resultsText.yview)
        self.preview.resultsText.configure(yscrollcommand=self.preview.Scroll.set)
        self.preview.resultsText.insert(tk.END, self.outputText)
        self.preview.resultsText.configure(state=tk.DISABLED)

#############################################################################

    # destroy argument field widgets
    def old_remove(self):
        self.argsFrame.argsLabelFrame.destroy()
        self.argsFrame.argsLabelFrame.nameLabel.destroy()
        self.argsFrame.argsLabelFrame.nameEntry.destroy()
        self.argsFrame.argsLabelFrame.ConVarLabel.destroy()
        self.argsFrame.argsLabelFrame.ConRadio.destroy()
        self.argsFrame.argsLabelFrame.VarRadio.destroy()
        self.argsFrame.argsLabelFrame.ConValLabel.destroy()
        self.argsFrame.argsLabelFrame.ConValEntry.destroy()
        self.argsFrame.argsLabelFrame.startLabel.destroy()
        self.argsFrame.argsLabelFrame.startEntry.destroy()
        self.argsFrame.argsLabelFrame.stepsLabel.destroy()
        self.argsFrame.argsLabelFrame.stepsEntry.destroy()

#############################################################################

    def arg_delete(self):
        if len(self.arguments) > 0:
            self.arguments.pop(-1)
        else:
            pass

#############################################################################

    def disable_constant(self):
        self.argsFrame.argsLabelFrame.ConValEntry.delete(0, tk.END)
        self.argsFrame.argsLabelFrame.ConValEntry.configure(state=tk.DISABLED)
        self.argsFrame.argsLabelFrame.startEntry.configure(state=tk.NORMAL)
        self.argsFrame.argsLabelFrame.stepsEntry.configure(state=tk.NORMAL)

#############################################################################

    def disable_variable(self):
        self.argsFrame.argsLabelFrame.ConValEntry.configure(state=tk.NORMAL)
        self.argsFrame.argsLabelFrame.startEntry.delete(0, len(str(self.startControl))+1)
        self.argsFrame.argsLabelFrame.stepsEntry.delete(0, len(str(self.stepsControl))+1)
        self.argsFrame.argsLabelFrame.startEntry.insert(0, 0.0)
        self.argsFrame.argsLabelFrame.stepsEntry.insert(0, 0.0)
        self.argsFrame.argsLabelFrame.startEntry.configure(state=tk.DISABLED)
        self.argsFrame.argsLabelFrame.stepsEntry.configure(state=tk.DISABLED)

#############################################################################

    def compile_output(self):
        self.outputText = ''
        self.outputText += 'Universe = ' + self.universeControl.get() + '\n'
        self.outputText += 'Executable = ' + self.execControl.get() + '\n'
        self.outputText += 'transfer_input_files = ' + self.inputControl.get() + '\n'
        self.outputText += 'log = ' + self.logControl.get() + '\n'
        self.outputText += 'should_transfer_files = ' + self.transControl.get() + '\n'
        self.outputText += 'when_to_transfer_output = ' + self.outControl.get() + '\n'
        self.outputText += '\n'

        #check length of numjobs
        length = len(str(self.numjobsControl.get()))

        for j in range(1, self.numjobsControl.get()+1):
            #set jobID with leading zeroes
            job_id = str(j).zfill(int(length))
            self.outputText += 'output = out_job' + job_id + '.txt\n'
            self.outputText += 'Arguments ='

            for t in self.arguments:
                if t[1] == 'constant':
                    self.outputText += ' ' + t[2]
                else:
                    if j > 1:
                        self.outputText += ' ' + str(t[3] + ((j-1)*t[4]))
                    else:
                        self.outputText += ' ' + str(t[3])

            self.outputText += '\nQueue\n\n'

#############################################################################

    def finish(self):
        # set workspace to that defined by user
        chdir(self.dirControl.get())

        # open new file for writing
        submitName = self.projControl.get() + '_submit.txt'
        submitFile = open(submitName, 'w')

        # write the output text (created by compile_output function) to text file
        submitFile.write(self.outputText)
        submitFile.close()

#############################################################################

    def help(self):
        self.helpWindow = tk.Toplevel()
        self.helpText = '''BASIC PARAMETERS

*Project name*
	Name to be used for the submission file output; "_submit.txt" will be appended to the end
	Example: "project_A" (results in a file named "project_A_submit.txt")

*Universe*
	Read about choosing a universe here: http://research.cs.wisc.edu/htcondor/manual/v8.3/2_4Running_Job.html#SECTION00341000000000000000

*Working directory file path*
	Location where the submission file should be stored
	Full file path required
	Example: C:\\Users\\user1\\Documents\\HTCondorFiles

*Executable File*
	Name of the script or program that will accept the arguments and run each job on HTCondor
	Include file extension
	Example: program.py

*Zip directory for input files*
	Name of the file that holds any input files for the HTCondor job; usually a .zip file or similar
	Include file extension
	Example: input_files.zip

*Output log file*
	Name of a log file that will be created when the jobs are run on HTCondor
	Include ".txt" extension
	Example: program_log.txt

*Should transfer files?*
	Read about this option here: http://research.cs.wisc.edu/htcondor/manual/v8.3/2_5Submitting_Job.html#SECTION00354000000000000000

*When to transfer output files?*
	Read about this option here: http://research.cs.wisc.edu/htcondor/manual/v8.3/2_5Submitting_Job.html#SECTION00354000000000000000

*Number of jobs*
	Number of jobs that should be created in the submission file
	Must be integer
	Example: 100


ARGUMENTS

*Name of argument*
	Simple name for each argument
	Used only to identify each argument in the "View saved arguments" display
	Example: Landuse file

*Is this argument constant or variable?*
	Does this argument change between jobs (variable) or does it stay the same (constant)?

*What is the value of this constant argument?*
	Text that will be duplicated in the arguments list passed to each HTCondor job
	Example: DEM.img

*Start value*
	For variable arguments, value that should be used in the first job
	Example: 10.0

*Step interval*
	For variable arguments, amount by which the argument should increase in each successive job
	Example: 5.0


BUTTONS

*Load existing submit file*
	Accepts a text file equivalent to one that has been created by this program
	Assumes that the file name ends with "_submit.txt"

*Preview*
	Opens a new window with a preview of the submission file based on information entered

*Finish & Create file*
	Creates the final submission text file and saves it to the specified directory

*Add new argument*
	Displays the Add arguments fields

*View saved arguments*
	See a list of all of the arguments and their attributes entered so far

*Save*
	Saves the current argument and associated attributes

*Add another argument*
	Reactivates the Add arguments fields

*Delete last entry*
	Delete the last argument in the "View saved arguments" list
'''
        #################################
        self.helpWindow.Scroll = tk.Scrollbar(self.helpWindow)
        self.helpWindow.Scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.helpWindow.resultsText = tk.Text(self.helpWindow, width=100, height=30, font=self.courier12)
        self.helpWindow.resultsText.pack(side=tk.LEFT, fill='both', expand=True)
        self.helpWindow.Scroll.configure(command=self.helpWindow.resultsText.yview)
        self.helpWindow.resultsText.configure(yscrollcommand=self.helpWindow.Scroll.set)
        self.helpWindow.resultsText.insert(tk.END, self.helpText)
        self.helpWindow.resultsText.configure(state=tk.DISABLED)

#############################################################################

if __name__ == "__main__":
    app = CondorSubmit(None)
    app.title('Condor Submission File Creator')
    app.mainloop()
