import tkinter as tk
from tkinter import *

#Mass Units
AreaMetric_Base = 1.0
AreaImperial_Base = 10.7639
MassMetric_Base = 1.0
MassImperial_Base = 28.3495232125
VolumeMetric_Base = 1
VolumeImperial_Base = 1
LengthMetric_Base = 1
LengthImperial_Base = 25.4
SpeedBase = 1
PressureBase = 1

MassUnits = {
    "Microgram" : MassMetric_Base / 1000000,
    "Milligram" : MassMetric_Base / 1000.0,
    "Gram" : MassMetric_Base,
    "Kilogram" : MassMetric_Base * 1000.0,
    "Tonne" : MassMetric_Base * 1000000,
    "Ounce" : MassImperial_Base,
    "Pound" : MassImperial_Base * 16.0,
    "Stone" : MassImperial_Base * 224,
    "Ton" : MassImperial_Base * 32000
} 

AreaUnits = {
    "SquareMeter" : AreaMetric_Base,
    "SquareKilometer" : AreaMetric_Base * 1000000,
    "Hectare" : AreaMetric_Base * 10000,
    "SquareInch" : AreaImperial_Base / 144,
    "SquareFoot" : AreaImperial_Base, 
    "SquareYard" : AreaImperial_Base * 9,
    "SquareMile" : AreaImperial_Base * 27880000000,
    "Acre" : AreaImperial_Base * 43560

}

VolumeUnits = {
    "Mililitre" : VolumeMetric_Base / 1000,
    "Litre" : VolumeMetric_Base,
    "Cubic Metres" : VolumeMetric_Base * 1000,
    "Ounce" : VolumeImperial_Base,
    "Pint" : VolumeImperial_Base * 16.0,
    "Quart" : VolumeImperial_Base * 32,
    "Gallon" : VolumeImperial_Base * 128,
    "Cubic Foot" : VolumeImperial_Base * 958,
    "Cubic Inch" : VolumeImperial_Base / 1.805

}

LengthUnits = {
    "Millimetre" : LengthMetric_Base,
    "Centimetre" : LengthMetric_Base * 10.0,
    "Metre" : LengthMetric_Base * 1000.0,
    "Kilometre" : LengthMetric_Base * 1000000.0,
    "Inch" : LengthImperial_Base,
    "Foot" : LengthImperial_Base * 12.0,
    "Yard" : LengthImperial_Base * 36.0,
    "Miles" : LengthImperial_Base * 63360.0

}

SpeedUnits = {
    "MilesPerHour" : SpeedBase * 1.151,
    "FeetPerSecond" : SpeedBase * 1.688,
    "Knot" : SpeedBase,
    "MetersPerSecond" : SpeedBase / 1.944,
    "KilometersPerHour" : SpeedBase * 1.852
}

PressureUnits = {
    "Bar" : PressureBase / 100000,
    "Pascal" : PressureBase,
    "PoundsPerSquareInch" : PressureBase / 6895
}

#Functions:
def MassMassConvEquate():
    CurrentConversion = VarMMInsideOne.get()
    CurrentConverter = VarMMInsideTwo.get()
    CurrentConversionFactor = MassMassEntryOne.get()
    
    if CurrentConversion == "Microgram" or "Milligram" or "Gram":
        PreConversionResult = float(CurrentConversionFactor) * float(MassUnits[CurrentConversion])
    else:
        PreConversionResult = float(CurrentConversionFactor) / float(MassUnits[CurrentConversion])
    
    ConversionResult = PreConversionResult / float(MassUnits[CurrentConverter])
    ConversionResult = float(ConversionResult)
    MassMassEntryTwo.delete("1.0", "end")
    MassMassEntryTwo.insert(END, format(ConversionResult, ".6f"))

    #Errors
    if CurrentConversionFactor == "":
        MassErrorText.delete("1.0", "end")
        MassErrorText.insert(END, "Error If Any: No Conversion Factor Given")
    if CurrentConversion or CurrentConverter == "Choose: ":
        MassErrorText.delete("1.0", "end")
        MassErrorText.insert(END, "Error If Any: No Conversion or Converter Given")    

def MassAreaConvEquate():
    CurrentConversion = VarMAInsideOne.get()
    CurrentConverter = VarMAInsideTwo.get()
    CurrentConversionFactor = MassAreaEntryOne.get()
    
    if CurrentConversion == "SquareInch":
        PreConversionResult = float(CurrentConversionFactor) * float(AreaUnits[CurrentConversion])
    else:
        PreConversionResult = float(CurrentConversionFactor) / float(AreaUnits[CurrentConversion])
    
    ConversionResult = PreConversionResult / float(AreaUnits[CurrentConverter])
    ConversionResult = float(ConversionResult)
    MassAreaEntryTwo.delete("1.0", "end")
    MassAreaEntryTwo.insert(END, format(ConversionResult, ".6f"))

    #Errors
    if CurrentConversionFactor == "":
        MassErrorText.delete("1.0", "end")
        MassErrorText.insert(END, "Error If Any: No Conversion Factor Given")
    if CurrentConversion or CurrentConverter == "Choose: ":
        MassErrorText.delete("1.0", "end")
        MassErrorText.insert(END, "Error If Any: No Conversion or Converter Given")    
def MassVolumeConvEquate():
    CurrentConversion = VarMVInsideOne.get()
    CurrentConverter = VarMVInsideTwo.get()
    CurrentConversionFactor = MassVolumeEntryOne.get()
    
    if CurrentConversion == "CubicInch" or "Millimeter":
        PreConversionResult = float(CurrentConversionFactor) * float(VolumeUnits[CurrentConversion])
    else:
        PreConversionResult = float(CurrentConversionFactor) / float(VolumeUnits[CurrentConversion])
    ConversionResult = PreConversionResult / float(VolumeUnits[CurrentConverter])
    ConversionResult = float(ConversionResult)
    MassVolumeEntryTwo.delete("1.0", "end")
    MassVolumeEntryTwo.insert(END, format(ConversionResult, ".6f"))

    #Errors
    if CurrentConversionFactor == "":
        MassErrorText.delete("1.0", "end")
        MassErrorText.insert(END, "Error If Any: No Conversion Factor Given")
    if CurrentConversion or CurrentConverter == "Choose: ":
        MassErrorText.delete("1.0", "end")
        MassErrorText.insert(END, "Error If Any: No Conversion or Converter Given")    

def LengthLengthConvEquate():
    CurrentConversion = VarLLInsideOne.get()
    CurrentConverter = VarLLInsideTwo.get()
    CurrentConversionFactor = LengthLengthEntryOne.get()
    
    PreConversionResult = float(CurrentConversionFactor) / float(LengthUnits[CurrentConversion])
    ConversionResult = PreConversionResult / float(LengthUnits[CurrentConverter])
    ConversionResult = float(ConversionResult)
    LengthLengthEntryTwo.delete("1.0", "end")
    LengthLengthEntryTwo.insert(END, format(ConversionResult, ".6f"))

    #Errors
    if CurrentConversionFactor == "":
        LengthErrorText.delete("1.0", "end")
        LengthErrorText.insert(END, "Error If Any: No Conversion Factor Given")
    if CurrentConversion or CurrentConverter == "Choose: ":
        LengthErrorText.delete("1.0", "end")
        LengthErrorText.insert(END, "Error If Any: No Conversion or Converter Given")    
def LengthSpeedConvEquate():
    CurrentConversion = VarLSInsideOne.get()
    CurrentConverter = VarLSInsideTwo.get()
    CurrentConversionFactor = LengthSpeedEntryOne.get()
    
    if CurrentConversion == "MetersPerSecond":
        PreConversionResult = float(CurrentConversionFactor) * float(SpeedUnits[CurrentConversion])
    else:
        PreConversionResult = float(CurrentConversionFactor) / float(SpeedUnits[CurrentConversion])
    
    ConversionResult = PreConversionResult / float(SpeedUnits[CurrentConverter])
    ConversionResult = float(ConversionResult)
    LengthSpeedEntryTwo.delete("1.0", "end")
    LengthSpeedEntryTwo.insert(END, format(ConversionResult, ".6f"))

    #Errors
    if CurrentConversionFactor == "":
        LengthErrorText.delete("1.0", "end")
        LengthErrorText.insert(END, "Error If Any: No Conversion Factor Given")
    if CurrentConversion or CurrentConverter == "Choose: ":
        LengthErrorText.delete("1.0", "end")
        LengthErrorText.insert(END, "Error If Any: No Conversion or Converter Given")    
def LengthPressureConvEquate():
    CurrentConversion = VarLFInsideOne.get()
    CurrentConverter = VarLFInsideTwo.get()
    CurrentConversionFactor = LengthForceEntryOne.get()
    
    if CurrentConversion == "Bar":
        PreConversionResult = float(CurrentConversionFactor) * float(PressureUnits[CurrentConversion])
    else:
        PreConversionResult = float(CurrentConversionFactor) / float(PressureUnits[CurrentConversion])
    
    ConversionResult = PreConversionResult / float(PressureUnits[CurrentConverter])
    ConversionResult = float(ConversionResult)
    LengthForceEntryTwo.delete("1.0", "end")
    LengthForceEntryTwo.insert(END, format(ConversionResult, ".6f"))
    
    #Errors
    if CurrentConversionFactor == "":
        LengthErrorText.delete("1.0", "end")
        LengthErrorText.insert(END, "Error If Any: No Conversion Factor Given")
    if CurrentConversion or CurrentConverter == "Choose: ":
        LengthErrorText.delete("1.0", "end")
        LengthErrorText.insert(END, "Error If Any: No Conversion or Converter Given")    

def TemperatureConvEquate():
    CurrentConversion = VarLTInsideOne.get()
    CurrentConverter = VarLTInsideTwo.get()
    CurrentConversionFactor = TemperatureEntryOne.get()
    Base = int(CurrentConversionFactor)

    def CelsiusFahrenheit():
        Result = (Base * 9/5) + 32
        TemperatureEntryTwo.delete("1.0", "end")
        TemperatureEntryTwo.insert(END, Result)
    def CelsiusKelvin():
        Result = (Base + 273.15)
        TemperatureEntryTwo.delete("1.0", "end")
        TemperatureEntryTwo.insert(END, Result)
    def FahrenheitCelsius():
        Result = (Base - 32) * 5/9
        TemperatureEntryTwo.delete("1.0", "end")
        TemperatureEntryTwo.insert(END, Result)
    def FahrenheitKelvin():
        Result = (Base - 32) * 5/9
        TemperatureEntryTwo.delete("1.0", "end")
        TemperatureEntryTwo.insert(END, Result)
    def KelvinCelsius():
        Result = (Base - 273.15) 
        TemperatureEntryTwo.delete("1.0", "end")
        TemperatureEntryTwo.insert(END, Result)
    def KelvinFahrenheit():
        Result = (Base - 273.15) * 9/5 + 32
        TemperatureEntryTwo.delete("1.0", "end")
        TemperatureEntryTwo.insert(END, Result)

    CallTempFunction = (CurrentConversion + CurrentConverter)
    
    if CallTempFunction == "CelsiusFahrenheit":
        CelsiusFahrenheit()
    if CallTempFunction == "CelsiusKelvin":
        CelsiusKelvin()
    if CallTempFunction == "FahrenheitCelsius":
        FahrenheitCelsius()
    if CallTempFunction == "FahrenheitKelving":
        FahrenheitKelvin()
    if CallTempFunction == "KelvinCelsius":
        KelvinCelsius()
    if CallTempFunction == "KelvinFahrenheit":
        KelvinFahrenheit()

    #Errors
    if CurrentConversionFactor == "":
        TempErrorText.delete("1.0", "end")
        TempErrorText.insert(END, "Error If Any: No Conversion Factor Given")
    if CurrentConversion or CurrentConverter == "Choose: ":
        TempErrorText.delete("1.0", "end")
        TempErrorText.insert(END, "Error If Any: No Conversion or Converter Given")    

# Starting Main Gui:
GUI = tk.Tk()
GUI.title("Chenden")
GUI.geometry("800x600")
GUI.rowconfigure(0, weight = 1)
GUI.columnconfigure(0, weight = 1)
MassGui = Frame(GUI, bg = "LightGreen")
MGmenu = Menu(MassGui)
LengthGui = Frame(GUI, bg = "LightGreen")
TempGui = Frame(GUI, bg = "LightGreen")
GUI.configure(menu = MGmenu)
MassErrorText = Text(MassGui, height = 1, width = 50, bg = "Grey", fg = "White")
MassErrorText.place(x = 300, y = 2)
LengthErrorText = Text(LengthGui, height = 1, width = 50, bg = "Grey", fg = "White")
LengthErrorText.place(x = 300, y = 2)
TempErrorText = Text(TempGui, height = 1, width = 50, bg = "Grey", fg = "White")
TempErrorText.place(x = 300, y = 2)

#Frames
def ShowFrame(frame):
    if frame == "MassGui":
        MassGui.tkraise()
    if frame == "AreaGui":
        LengthGui.tkraise()
    if frame == "TempGui":
        TempGui.tkraise()

for frameset in (MassGui, LengthGui, TempGui):
    frameset.grid(row = 0, column = 0, sticky = "nsew")

#Lists:
MassMass_List = ["Microgram", "Milligram", "Gram", "Kilogram", "Tonne", "Ounce", "Pound", "Stone", "Ton"]
MassArea_List = ["SquareMeter", "SquareKilometer", "Hectare", "Acre", "SquareInch", "SquareFoot", "SquareYard", "SquareMile"]
MassVolume_List = ["Mililitre", "Litre", "Cubic Meters", "Ounce", "Pint", "Quart", "Gallon", "Cubic Feet", "Cubic Inch"] 
LengthLength_List = ["Millimetre", "Centimetre", "Metre", "Kilometre", "Inch", "Foot", "Yard", "Mile"]
LengthSpeed_List = ["MilesPerHour", "FeetPerSecond", "Knot", "MetersPerSecond", "KilometersPerHour"]
LengthPressure_List = ["Bar", "Pascal", "PoundsPerSquareInch"]
Temp_List = ["Celsius", "Fahrenheit", "Kelvin"]
Main_list = ["Mass", "Length", "Temperature"]

#Menus:
FileMenu = Menu(MGmenu)
OpenMenu = Menu(MGmenu)
MGmenu.add_cascade(label = "File", menu = FileMenu)
FileMenu.add_command(label = "Exit", command = MassGui.quit)
MGmenu.add_cascade(label = "Open", menu = OpenMenu)
OpenMenu.add_command(label = "Mass", command = lambda:ShowFrame("MassGui"))
OpenMenu.add_command(label = "Length", command = lambda:ShowFrame("AreaGui"))
OpenMenu.add_command(label = "Temperature", command = lambda:ShowFrame("TempGui"))
OpenMenu.add_separator()
OpenMenu.add_command(label = "Exit", command = MassGui.quit)

#Mass Widgets: 
MassLabel = Label(MassGui, text = "CHENDEN CONVERTER \n MASS: ")
MassLabel.place(x = 1, y = 1)
MassText = Label(MassGui, text = "WEIGHT: ")
MassText.place(x = 20, y = 45)
MassMassEntryOne = Entry(MassGui, width = 15)
MassMassEntryOne.place(x = 75, y = 75)
MassEquate = Button(MassGui, fg = "Black", bg = "White", text = "EQUATE =", command = lambda:MassMassConvEquate())
MassEquate.place(x = 178, y = 73)
MassMassEntryTwo = Text(MassGui, width = 15, height = 1)
MassMassEntryTwo.place(x = 250, y = 75)
VarMMInsideOne = StringVar(MassGui)
VarMMInsideOne.set("Choose: ")
VarMMInsideTwo = StringVar(MassGui)
VarMMInsideTwo.set("Choose: ")
MassChangeButtonOne = OptionMenu(MassGui, VarMMInsideOne, *MassMass_List)
MassChangeButtonOne.place(x = 77, y = 95)
MassChangeButtonTwo = OptionMenu(MassGui, VarMMInsideTwo, *MassMass_List)
MassChangeButtonTwo.place(x = 252, y = 95)

#Area Widgets:
AreaLabel = Label(MassGui, text = "CHENDEN CONVERTER \n Area: ")
AreaLabel.place(x = 1, y = 130)
AreaText = Label(MassGui, text = "Area: ")
AreaText.place(x = 20, y = 175)
MassAreaEntryOne = Entry(MassGui, width = 15)
MassAreaEntryOne.place(x = 75, y = 205)
AreaEquate = Button(MassGui, fg = "Black", bg = "White", text = "EQUATE =", command = lambda:MassAreaConvEquate())
AreaEquate.place(x = 178, y = 203)
MassAreaEntryTwo = Text(MassGui, width = 15, height = 1)
MassAreaEntryTwo.place(x = 250, y = 205)
VarMAInsideOne = StringVar(MassGui)
VarMAInsideOne.set("Choose: ")
VarMAInsideTwo = StringVar(MassGui)
VarMAInsideTwo.set("Choose: ")
AreaChangeButtonOne = OptionMenu(MassGui, VarMAInsideOne, *MassArea_List)
AreaChangeButtonOne.place(x = 77, y = 225)
AreaChangeButtonTwo = OptionMenu(MassGui, VarMAInsideTwo, *MassArea_List)
AreaChangeButtonTwo.place(x = 252, y = 225)

#Volume Widgets:
VolumeLabel = Label(MassGui, text = "CHENDEN CONVERTER \n Volume: ")
VolumeLabel.place(x = 1, y = 260)
VolumeText = Label(MassGui, text = "Volume: ")
VolumeText.place(x = 20, y = 305)
MassVolumeEntryOne = Entry(MassGui, width = 15)
MassVolumeEntryOne.place(x = 75, y = 335)
VolumeEquate = Button(MassGui, fg = "Black", bg = "White", text = "EQUATE =", command = lambda:MassVolumeConvEquate())
VolumeEquate.place(x = 178, y = 333)
MassVolumeEntryTwo = Text(MassGui, width = 15, height = 1)
MassVolumeEntryTwo.place(x = 250, y = 335)
VarMVInsideOne = StringVar(MassGui)
VarMVInsideOne.set("Choose: ")
VarMVInsideTwo = StringVar(MassGui)
VarMVInsideTwo.set("Choose: ")
VolumeChangeButtonOne = OptionMenu(MassGui, VarMVInsideOne, *MassVolume_List)
VolumeChangeButtonOne.place(x = 77, y = 355)
VolumeChangeButtonTwo = OptionMenu(MassGui, VarMVInsideTwo, *MassVolume_List)
VolumeChangeButtonTwo.place(x = 252, y = 355)

#Length Widgets: 
LengthLabel = Label(LengthGui, text = "CHENDEN CONVERTER \n LENGTH: ")
LengthLabel.place(x = 1, y = 1)
LengthText = Label(LengthGui, text = "LENGTH: ")
LengthText.place(x = 20, y = 45)
LengthLengthEntryOne = Entry(LengthGui, width = 15)
LengthLengthEntryOne.place(x = 75, y = 75)
LengthEquate = Button(LengthGui, fg = "Black", bg = "White", text = "EQUATE =", command = lambda:LengthLengthConvEquate())
LengthEquate.place(x = 178, y = 73)
LengthLengthEntryTwo = Text(LengthGui, width = 15, height = 1)
LengthLengthEntryTwo.place(x = 250, y = 75)
VarLLInsideOne = StringVar(LengthGui)
VarLLInsideOne.set("Choose: ")
VarLLInsideTwo = StringVar(LengthGui)
VarLLInsideTwo.set("Choose: ")
LengthChangeButtonOne = OptionMenu(LengthGui, VarLLInsideOne, *LengthLength_List)
LengthChangeButtonOne.place(x = 77, y = 95)
LengthChangeButtonTwo = OptionMenu(LengthGui, VarLLInsideTwo, *LengthLength_List)
LengthChangeButtonTwo.place(x = 252, y = 95)

#Speed Widgets:
SpeedLabel = Label(LengthGui, text = "CHENDEN CONVERTER \n SPEED: ")
SpeedLabel.place(x = 1, y = 130)
SpeedText = Label(LengthGui, text = "SPEED: ")
SpeedText.place(x = 20, y = 175)
LengthSpeedEntryOne = Entry(LengthGui, width = 15)
LengthSpeedEntryOne.place(x = 75, y = 205)
SpeedEquate = Button(LengthGui, fg = "Black", bg = "White", text = "EQUATE =", command = lambda:LengthSpeedConvEquate())
SpeedEquate.place(x = 178, y = 203)
LengthSpeedEntryTwo = Text(LengthGui, width = 15, height = 1)
LengthSpeedEntryTwo.place(x = 250, y = 205)
VarLSInsideOne = StringVar(LengthGui)
VarLSInsideOne.set("Choose: ")
VarLSInsideTwo = StringVar(LengthGui)
VarLSInsideTwo.set("Choose: ")
SpeedChangeButtonOne = OptionMenu(LengthGui, VarLSInsideOne, *LengthSpeed_List)
SpeedChangeButtonOne.place(x = 77, y = 225)
SpeedChangeButtonTwo = OptionMenu(LengthGui, VarLSInsideTwo, *LengthSpeed_List)
SpeedChangeButtonTwo.place(x = 252, y = 225)

#Force Widgets:
ForceLabel = Label(LengthGui, text = "CHENDEN CONVERTER \n FORCE: ")
ForceLabel.place(x = 1, y = 260)
ForceText = Label(LengthGui, text = "FORCE: ")
ForceText.place(x = 20, y = 305)
LengthForceEntryOne = Entry(LengthGui, width = 15)
LengthForceEntryOne.place(x = 75, y = 335)
ForceEquate = Button(LengthGui, fg = "Black", bg = "White", text = "EQUATE =", command = lambda:LengthPressureConvEquate())
ForceEquate.place(x = 178, y = 333)
LengthForceEntryTwo = Text(LengthGui, width = 15, height = 1)
LengthForceEntryTwo.place(x = 250, y = 335)
VarLFInsideOne = StringVar(LengthGui)
VarLFInsideOne.set("Choose: ")
VarLFInsideTwo = StringVar(LengthGui)
VarLFInsideTwo.set("Choose: ")
ForceChangeButtonOne = OptionMenu(LengthGui, VarLFInsideOne, *LengthSpeed_List)
ForceChangeButtonOne.place(x = 77, y = 355)
ForceChangeButtonTwo = OptionMenu(LengthGui, VarLFInsideTwo, *LengthSpeed_List)
ForceChangeButtonTwo.place(x = 252, y = 355)

#Temperature Widgets: 
TemperatureLabel = Label(TempGui, text = "CHENDEN CONVERTER \n TEMPERATURE: ")
TemperatureLabel.place(x = 1, y = 1)
TemperatureText = Label(TempGui, text = "TEMPERATURE: ")
TemperatureText.place(x = 20, y = 45)
TemperatureEntryOne = Entry(TempGui, width = 15)
TemperatureEntryOne.place(x = 75, y = 75)
TemperatureEquate = Button(TempGui, fg = "Black", bg = "White", text = "EQUATE =", command = lambda:TemperatureConvEquate())
TemperatureEquate.place(x = 178, y = 73)
TemperatureEntryTwo = Text(TempGui, width = 15, height = 1)
TemperatureEntryTwo.place(x = 250, y = 75)
VarLTInsideOne = StringVar(TempGui)
VarLTInsideOne.set("Choose: ")
VarLTInsideTwo = StringVar(TempGui)
VarLTInsideTwo.set("Choose: ")
TemperatureChangeButtonOne = OptionMenu(TempGui, VarLTInsideOne, *Temp_List)
TemperatureChangeButtonOne.place(x = 77, y = 95)
TemperatureChangeButtonTwo = OptionMenu(TempGui, VarLTInsideTwo, *Temp_List)
TemperatureChangeButtonTwo.place(x = 252, y = 95)


#Last Second Functions
MassErrorText.insert(END, "Error If Any: ")
LengthErrorText.insert(END, "Error If Any: ")
TempErrorText.insert(END, "Error If Any: ")
ShowFrame("MassGui")

MassGui.mainloop()