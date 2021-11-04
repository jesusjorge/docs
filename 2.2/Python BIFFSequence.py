#REQUIRES jesusjorge/s13n/1.1
#ALTERNATIVES: use the ONEFILE implementation

#https://github.com/jesusjorge/s13n/wiki/2.2
#
#Writer = BIFFSequenceWriter.Create()
#Writer.WriteLong(12345)
#Writer.Write(b'bunch of bytes')
#Writer.Write(None)
#Result = Writer.GetBytes()
#
#Reader = BIFFSequenceReader.Create(ByteSequence) or...
#Reader = BIFFSequenceReader(SomeStream)
#long = Reader.ReadLong()
#array = Reader.Read()
#another_array = Reader.Read()
#yet_another_array = Reader.Read()

from CUInt import *

class BIFFSequenceWriter:
    def Create():
        return BIFFSequenceWriter(io.BytesIO())
    def __init__(self,Stream):
        self.Stream = Stream
    def GetStream(self):
        return self.Stream
    def GetBytes(self):
        self.Stream.seek(0)
        result = self.Stream.read()
        self.Stream.close()
        return result
    def Write(self,Bytes):
        if Bytes == None:
            self.Stream.write(CUInt.Write(None,CUInts.CUInt128))
        else:
            Size = len(Bytes)
            self.Stream.write(CUInt.Write(Size,CUInts.CUInt128))
            self.Stream.write(Bytes)
    #UNOFFICIAL METHOD, JUST FOR TESTING PURPOSES
    def WriteCUInt(self,Value):
        self.Write(CUInt.Write(Value,CUInts.CUInt128))
            
class BIFFSequenceReader:
    def Create(Bytes):
        return BIFFSequenceReader(io.BytesIO(Bytes))
    def __init__(self,Stream):
        self.Stream = Stream
    def ReadSize(self):
        return CUInt.Read(self.Stream,CUInts.CUInt128)
    def Read(self,Length = None):
        if Length == None:
            Length = self.ReadSize()
        if Length == None:
            return None
        return self.Stream.read(Length)
    def GetStream(self):
        return self.Stream
    def GetBytes(self):
        self.Stream.seek(0)
        result = self.Stream.read()
        self.Stream.close()
        return result
    #UNOFFICIAL METHOD, JUST FOR TESTING PURPOSES
    def ReadCUInt(self):
        Value = self.Read()
        if len(Value) == 1:
            if Value == b'\xff':
                return None
            return int.from_bytes(Value,"big")
        return int.from_bytes(Value[1:],"big")
    def SelfTest():
        Log = []
        Log.append("BIFFSequence did not pass the self check.\n\tTest Results:\n")
        TestCases = "010bff0001410548656c6c6f06576f726c6421f83032303430363038313031323134313631383230323232343236323833303332333433363338343034323434343634383530353235343536353836303632363436363638373037323734373637383830383238343836383839303932393439363938303030323034303630383130313231343136313832303232323432363238333033323334333633383430343234343436343835303532353435363538363036323634363636383730373237343736373838303832383438363838393039323934393639383030303230343036303831303132313431363138323032323234323632383330333233343336333834303432343434363438fa30323034303630383130313231343136313832303232323432363238333033323334333633383430343234343436343835303532353435363538363036323634363636383730373237343736373838303832383438363838393039323934393639383030303230343036303831303132313431363138323032323234323632383330333233343336333834303432343434363438353035323534353635383630363236343636363837303732373437363738383038323834383638383930393239343936393830303032303430363038313031323134313631383230323232343236323833303332333433363338343034323434343634383530fe00fc303230343036303831303132313431363138323032323234323632383330333233343336333834303432343434363438353035323534353635383630363236343636363837303732373437363738383038323834383638383930393239343936393830303032303430363038313031323134313631383230323232343236323833303332333433363338343034323434343634383530353235343536353836303632363436363638373037323734373637383830383238343836383839303932393439363938303030323034303630383130313231343136313832303232323432363238333033323334333633383430343234343436343835303532ffff0141"
        TS = BIFFSequenceWriter.Create()
        RS = BIFFSequenceReader.Create(bytearray.fromhex(TestCases))
        Tests = RS.Read()
        TS.Write(Tests)
        Tests = int.from_bytes(Tests,"big") 
        while Tests > 0:
            Value = RS.Read()
            Log.append(str(Value))
            Log.append("\n")
            TS.Write(Value)
            Tests = Tests - 1
        Result = TS.GetBytes().hex()
        if Result != TestCases:
            Log.append("Source Test String: ")
            Log.append(TestCases)
            Log.append("\nResult Test String: ")
            Log.append(Result)
            Log = ''.join(Log)
            raise Exception(Log)    
        return Result == TestCases

        
BIFFSequenceReader.SelfTest()

