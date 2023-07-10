import unittest
import ParseData.Converter as Converter
import pprint


class ConverterTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.excepted_header: list = ['Sem', 'Class Code', 'Learning Module', 'Instructor', 'Venue', 'Period', 'Time',
                                      'Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
        self.excepted_records: list[list[str]] = [['2',
                                                   'COMP221-221',
                                                   'OBJECT ORIENTED TECHNOLOGIES',
                                                   'WONG UN HONG',
                                                   'N_54',
                                                   '2023/01/05-2023/04/22',
                                                   '10:00-11:30',
                                                   '',
                                                   '',
                                                   '',
                                                   '',
                                                   '',
                                                   '',
                                                   ''],
                                                  ['',
                                                   '',
                                                   '',
                                                   'WONG UN HONG',
                                                   'N_54',
                                                   '2023/01/05-2023/04/22',
                                                   '11:30-13:00',
                                                   '',
                                                   '',
                                                   '',
                                                   '',
                                                   '',
                                                   '',
                                                   ''],
                                                  ['2',
                                                   'COMP222-221',
                                                   'INTERNET PROGRAMMING I',
                                                   'CALANA CHAN MEI POU',
                                                   'N_54',
                                                   '2023/01/05-2023/04/22',
                                                   '10:00-11:30',
                                                   '',
                                                   '',
                                                   '',
                                                   '',
                                                   '',
                                                   '',
                                                   ''],
                                                  ['',
                                                   '',
                                                   '',
                                                   'CALANA CHAN MEI POU',
                                                   'N_54',
                                                   '2023/01/05-2023/04/22',
                                                   '11:30-13:00',
                                                   '',
                                                   '',
                                                   '',
                                                   '',
                                                   '',
                                                   '',
                                                   ''],
                                                  ['2',
                                                   'COMP223-221',
                                                   'SOFTWARE ENGINEERING',
                                                   'AMANG KIM SONGKYOO',
                                                   'N_56',
                                                   '2023/01/05-2023/04/22',
                                                   '11:30-13:00',
                                                   '',
                                                   '',
                                                   '',
                                                   '',
                                                   '',
                                                   '',
                                                   ''],
                                                  ['',
                                                   '',
                                                   '',
                                                   'AMANG KIM SONGKYOO',
                                                   'N_56',
                                                   '2023/01/05-2023/04/22',
                                                   '10:00-11:30',
                                                   '',
                                                   '',
                                                   '',
                                                   '',
                                                   '',
                                                   '',
                                                   ''],
                                                  ['2',
                                                   'COMP224-221',
                                                   'DATABASE MANAGEMENT SYSTEMS',
                                                   'YANG XU',
                                                   'A214',
                                                   '2023/01/05-2023/04/22',
                                                   '11:30-13:00',
                                                   '',
                                                   '',
                                                   '',
                                                   '',
                                                   '',
                                                   '',
                                                   ''],
                                                  ['',
                                                   '',
                                                   '',
                                                   'YANG XU',
                                                   'A211',
                                                   '2023/01/05-2023/04/22',
                                                   '10:00-11:30',
                                                   '',
                                                   '',
                                                   '',
                                                   '',
                                                   '',
                                                   '',
                                                   ''],
                                                  ['2',
                                                   'COMP225-221',
                                                   'NETWORK AND SYSTEM ADMINISTRATION',
                                                   'LIAM LEI KIN',
                                                   'N_54',
                                                   '2023/01/05-2023/04/22',
                                                   '14:30-17:30',
                                                   '',
                                                   '',
                                                   '',
                                                   '',
                                                   '',
                                                   '',
                                                   ''],
                                                  ['2',
                                                   'MENG221-221',
                                                   'ENGLISH IV',
                                                   'CHUI SAI CHAK',
                                                   'N_52',
                                                   '2023/01/05-2023/04/22',
                                                   '14:30-17:30',
                                                   '',
                                                   '',
                                                   '',
                                                   '',
                                                   '',
                                                   '',
                                                   ''],
                                                  ['',
                                                   '',
                                                   '',
                                                   'HO SIO WA',
                                                   'B304',
                                                   '2023/02/13-2023/03/18',
                                                   '14:30-17:30',
                                                   '',
                                                   '',
                                                   '',
                                                   '',
                                                   '',
                                                   '',
                                                   '']]
        self.html: str = """
<table align="center" border="1" bordercolor="#EAEAEA" cellpadding="1" cellspacing="0" width="100%">
<tbody><tr>
<td bgcolor="#0000CE" height="25" nowrap="" width="0">
<span class="style26"><font face="Arial, Helvetica, sans-serif">
      
 Sem 
 
      </font></span></td>
<td bgcolor="#0000CE"><span class="style26"><font face="Arial, Helvetica, sans-serif">
      
      Class Code
      
    </font></span></td>
<td bgcolor="#0000CE"><span class="style26"><font face="Arial, Helvetica, sans-serif">
      
      Learning Module
      
    </font></span></td>
<td bgcolor="#0000CE"><span class="style26"><font face="Arial, Helvetica, sans-serif">
      
      Instructor
      
    </font></span></td>
<td bgcolor="#0000CE" width="0"><span class="style26"><font face="Arial, Helvetica, sans-serif">
      
      Venue
      
    </font></span></td>
<td bgcolor="#0000CE" width="0"><div align="center" class="style34"><strong><span class="style5"><font face="Arial, Helvetica, sans-serif">
      
      Period
      
    </font></span></strong></div></td>
<td bgcolor="#0000CE" width="0"><div align="center" class="style34"><strong><span class="style5"><font face="Arial, Helvetica, sans-serif">
      
      Time
      
    </font></span></strong></div></td>
<td bgcolor="#0000CE" width="16"> <div align="center" class="style34"><strong><span class="style35"><font face="Arial, Helvetica, sans-serif">
      
Sun

    </font></span></strong></div></td>
<td bgcolor="#0000CE" width="16"> <div align="center" class="style34"><strong><span class="style5"><font face="Arial, Helvetica, sans-serif">
      
Mon

    </font></span></strong></div></td>
<td bgcolor="#0000CE" width="16"> <div align="center" class="style34"><strong><span class="style5"><font face="Arial, Helvetica, sans-serif">
      
Tue

    </font></span></strong></div></td>
<td bgcolor="#0000CE" width="16"> <div align="center" class="style34"><strong><span class="style5"><font face="Arial, Helvetica, sans-serif">
      
Wed

    </font></span></strong></div></td>
<td bgcolor="#0000CE" width="16"> <div align="center" class="style34"><strong><span class="style5"><font face="Arial, Helvetica, sans-serif">
      
Thu

    </font></span></strong></div></td>
<td bgcolor="#0000CE" width="16"> <div align="center" class="style34 style36">
<div align="center" class="style5"><font face="Arial, Helvetica, sans-serif">
        
  Fri
  
      </font></div>
</div></td>
<td bgcolor="#0000CE" width="16"> <div align="center" class="style37"><span class="style5"><font face="Arial, Helvetica, sans-serif">
      
Sat

    </font></span></div></td>
</tr>
<tr>
<td bgcolor="#FFFFE6"><div align="center" class="style5"><font face="Arial, Helvetica, sans-serif">       2    </font></div></td>
<td bgcolor="#FFFFE6" nowrap=""><span class="style5"><font face="Arial, Helvetica, sans-serif">       COMP221-221    </font></span></td>
<td bgcolor="#FFFFE6"><span class="style5"><font face="Arial, Helvetica, sans-serif">       OBJECT ORIENTED TECHNOLOGIES    </font></span></td>
<td bgcolor="#FFFFE6"><span class="style5"><font face="Arial, Helvetica, sans-serif">       WONG UN HONG     </font></span></td>
<td bgcolor="#FFFFE6"><span class="style5"><font face="Arial, Helvetica, sans-serif">       N_54 </font></span></td>
<td bgcolor="#FFFFE6" width="200"><span class="style5"><font face="Arial, Helvetica, sans-serif">
		2023/01/05-2023/04/22

		</font></span></td>
<td bgcolor="#FFFFE6" nowrap=""><span class="style5"><font face="Arial, Helvetica, sans-serif">       10:00-11:30     </font></span></td>
<td align="center" bgcolor="#FFFFE6"> <div align="center"><font size="1"><b><font face="Arial, Helvetica, sans-serif"> 
	  	
		   
		    

    </font></b></font></div></td>
<td align="center" bgcolor="#FFFFE6"> <div align="center"><font size="1"><b><font face="Arial, Helvetica, sans-serif"> 
	  	
		   
		    
    </font></b></font></div></td>
<td align="center" bgcolor="#FFFFE6"> <div align="center"><font size="1"><b><font face="Arial, Helvetica, sans-serif">
<img align="absmiddle" height="16" src="images/dot.gif" width="16"/>
</font></b></font></div></td>
<td align="center" bgcolor="#FFFFE6"> <div align="center"><font size="1"><b><font face="Arial, Helvetica, sans-serif"> 
	  	
		   
		    
    </font></b></font></div></td>
<td align="center" bgcolor="#FFFFE6"> <div align="center"><font size="1"><b><font face="Arial, Helvetica, sans-serif"> 
	  	
		   
		    
    </font></b></font></div></td>
<td align="center" bgcolor="#FFFFE6"> <div align="center"><font size="1"><b><font face="Arial, Helvetica, sans-serif"> 
	  	
		   
		    
    </font></b></font></div></td>
<td align="center" bgcolor="#FFFFE6"> <div align="center"><font size="1"><b><font face="Arial, Helvetica, sans-serif"> 
	  	
		   
		    
    </font></b></font></div></td>
</tr>
<tr>
<td bgcolor="#FFFFE6" colspan="3"><div align="center" class="style5"><font face="Arial, Helvetica, sans-serif">            </font></div></td>
<td bgcolor="#FFFFE6"><span class="style5"><font face="Arial, Helvetica, sans-serif">       WONG UN HONG     </font></span></td>
<td bgcolor="#FFFFE6"><span class="style5"><font face="Arial, Helvetica, sans-serif">       N_54 </font></span></td>
<td bgcolor="#FFFFE6" width="200"><span class="style5"><font face="Arial, Helvetica, sans-serif">
		2023/01/05-2023/04/22

		</font></span></td>
<td bgcolor="#FFFFE6" nowrap=""><span class="style5"><font face="Arial, Helvetica, sans-serif">       11:30-13:00     </font></span></td>
<td align="center" bgcolor="#FFFFE6"> <div align="center"><font size="1"><b><font face="Arial, Helvetica, sans-serif"> 
	  	
		   
		    

    </font></b></font></div></td>
<td align="center" bgcolor="#FFFFE6"> <div align="center"><font size="1"><b><font face="Arial, Helvetica, sans-serif"> 
	  	
		   
		    
    </font></b></font></div></td>
<td align="center" bgcolor="#FFFFE6"> <div align="center"><font size="1"><b><font face="Arial, Helvetica, sans-serif"> 
	  	
		   
		    
    </font></b></font></div></td>
<td align="center" bgcolor="#FFFFE6"> <div align="center"><font size="1"><b><font face="Arial, Helvetica, sans-serif"> 
	  	
		   
		    
    </font></b></font></div></td>
<td align="center" bgcolor="#FFFFE6"> <div align="center"><font size="1"><b><font face="Arial, Helvetica, sans-serif">
<img align="absmiddle" height="16" src="images/dot.gif" width="16"/>
</font></b></font></div></td>
<td align="center" bgcolor="#FFFFE6"> <div align="center"><font size="1"><b><font face="Arial, Helvetica, sans-serif"> 
	  	
		   
		    
    </font></b></font></div></td>
<td align="center" bgcolor="#FFFFE6"> <div align="center"><font size="1"><b><font face="Arial, Helvetica, sans-serif"> 
	  	
		   
		    
    </font></b></font></div></td>
</tr>
<tr>
<td bgcolor="#FFFFFF"><div align="center" class="style5"><font face="Arial, Helvetica, sans-serif">       2    </font></div></td>
<td bgcolor="#FFFFFF" nowrap=""><span class="style5"><font face="Arial, Helvetica, sans-serif">       COMP222-221    </font></span></td>
<td bgcolor="#FFFFFF"><span class="style5"><font face="Arial, Helvetica, sans-serif">       INTERNET PROGRAMMING I    </font></span></td>
<td bgcolor="#FFFFFF"><span class="style5"><font face="Arial, Helvetica, sans-serif">       CALANA CHAN MEI POU     </font></span></td>
<td bgcolor="#FFFFFF"><span class="style5"><font face="Arial, Helvetica, sans-serif">       N_54 </font></span></td>
<td bgcolor="#FFFFFF" width="200"><span class="style5"><font face="Arial, Helvetica, sans-serif">
		2023/01/05-2023/04/22

		</font></span></td>
<td bgcolor="#FFFFFF" nowrap=""><span class="style5"><font face="Arial, Helvetica, sans-serif">       10:00-11:30     </font></span></td>
<td align="center" bgcolor="#FFFFFF"> <div align="center"><font size="1"><b><font face="Arial, Helvetica, sans-serif"> 
	  	
		   
		    

    </font></b></font></div></td>
<td align="center" bgcolor="#FFFFFF"> <div align="center"><font size="1"><b><font face="Arial, Helvetica, sans-serif">
<img align="absmiddle" height="16" src="images/dot.gif" width="16"/>
</font></b></font></div></td>
<td align="center" bgcolor="#FFFFFF"> <div align="center"><font size="1"><b><font face="Arial, Helvetica, sans-serif"> 
	  	
		   
		    
    </font></b></font></div></td>
<td align="center" bgcolor="#FFFFFF"> <div align="center"><font size="1"><b><font face="Arial, Helvetica, sans-serif"> 
	  	
		   
		    
    </font></b></font></div></td>
<td align="center" bgcolor="#FFFFFF"> <div align="center"><font size="1"><b><font face="Arial, Helvetica, sans-serif"> 
	  	
		   
		    
    </font></b></font></div></td>
<td align="center" bgcolor="#FFFFFF"> <div align="center"><font size="1"><b><font face="Arial, Helvetica, sans-serif"> 
	  	
		   
		    
    </font></b></font></div></td>
<td align="center" bgcolor="#FFFFFF"> <div align="center"><font size="1"><b><font face="Arial, Helvetica, sans-serif"> 
	  	
		   
		    
    </font></b></font></div></td>
</tr>
<tr>
<td bgcolor="#FFFFFF" colspan="3"><div align="center" class="style5"><font face="Arial, Helvetica, sans-serif">            </font></div></td>
<td bgcolor="#FFFFFF"><span class="style5"><font face="Arial, Helvetica, sans-serif">       CALANA CHAN MEI POU     </font></span></td>
<td bgcolor="#FFFFFF"><span class="style5"><font face="Arial, Helvetica, sans-serif">       N_54 </font></span></td>
<td bgcolor="#FFFFFF" width="200"><span class="style5"><font face="Arial, Helvetica, sans-serif">
		2023/01/05-2023/04/22

		</font></span></td>
<td bgcolor="#FFFFFF" nowrap=""><span class="style5"><font face="Arial, Helvetica, sans-serif">       11:30-13:00     </font></span></td>
<td align="center" bgcolor="#FFFFFF"> <div align="center"><font size="1"><b><font face="Arial, Helvetica, sans-serif"> 
	  	
		   
		    

    </font></b></font></div></td>
<td align="center" bgcolor="#FFFFFF"> <div align="center"><font size="1"><b><font face="Arial, Helvetica, sans-serif"> 
	  	
		   
		    
    </font></b></font></div></td>
<td align="center" bgcolor="#FFFFFF"> <div align="center"><font size="1"><b><font face="Arial, Helvetica, sans-serif"> 
	  	
		   
		    
    </font></b></font></div></td>
<td align="center" bgcolor="#FFFFFF"> <div align="center"><font size="1"><b><font face="Arial, Helvetica, sans-serif"> 
	  	
		   
		    
    </font></b></font></div></td>
<td align="center" bgcolor="#FFFFFF"> <div align="center"><font size="1"><b><font face="Arial, Helvetica, sans-serif"> 
	  	
		   
		    
    </font></b></font></div></td>
<td align="center" bgcolor="#FFFFFF"> <div align="center"><font size="1"><b><font face="Arial, Helvetica, sans-serif">
<img align="absmiddle" height="16" src="images/dot.gif" width="16"/>
</font></b></font></div></td>
<td align="center" bgcolor="#FFFFFF"> <div align="center"><font size="1"><b><font face="Arial, Helvetica, sans-serif"> 
	  	
		   
		    
    </font></b></font></div></td>
</tr>
<tr>
<td bgcolor="#FFFFE6"><div align="center" class="style5"><font face="Arial, Helvetica, sans-serif">       2    </font></div></td>
<td bgcolor="#FFFFE6" nowrap=""><span class="style5"><font face="Arial, Helvetica, sans-serif">       COMP223-221    </font></span></td>
<td bgcolor="#FFFFE6"><span class="style5"><font face="Arial, Helvetica, sans-serif">       SOFTWARE ENGINEERING    </font></span></td>
<td bgcolor="#FFFFE6"><span class="style5"><font face="Arial, Helvetica, sans-serif">       AMANG KIM SONGKYOO     </font></span></td>
<td bgcolor="#FFFFE6"><span class="style5"><font face="Arial, Helvetica, sans-serif">       N_56 </font></span></td>
<td bgcolor="#FFFFE6" width="200"><span class="style5"><font face="Arial, Helvetica, sans-serif">
		2023/01/05-2023/04/22

		</font></span></td>
<td bgcolor="#FFFFE6" nowrap=""><span class="style5"><font face="Arial, Helvetica, sans-serif">       11:30-13:00     </font></span></td>
<td align="center" bgcolor="#FFFFE6"> <div align="center"><font size="1"><b><font face="Arial, Helvetica, sans-serif"> 
	  	
		   
		    

    </font></b></font></div></td>
<td align="center" bgcolor="#FFFFE6"> <div align="center"><font size="1"><b><font face="Arial, Helvetica, sans-serif">
<img align="absmiddle" height="16" src="images/dot.gif" width="16"/>
</font></b></font></div></td>
<td align="center" bgcolor="#FFFFE6"> <div align="center"><font size="1"><b><font face="Arial, Helvetica, sans-serif"> 
	  	
		   
		    
    </font></b></font></div></td>
<td align="center" bgcolor="#FFFFE6"> <div align="center"><font size="1"><b><font face="Arial, Helvetica, sans-serif"> 
	  	
		   
		    
    </font></b></font></div></td>
<td align="center" bgcolor="#FFFFE6"> <div align="center"><font size="1"><b><font face="Arial, Helvetica, sans-serif"> 
	  	
		   
		    
    </font></b></font></div></td>
<td align="center" bgcolor="#FFFFE6"> <div align="center"><font size="1"><b><font face="Arial, Helvetica, sans-serif"> 
	  	
		   
		    
    </font></b></font></div></td>
<td align="center" bgcolor="#FFFFE6"> <div align="center"><font size="1"><b><font face="Arial, Helvetica, sans-serif"> 
	  	
		   
		    
    </font></b></font></div></td>
</tr>
<tr>
<td bgcolor="#FFFFE6" colspan="3"><div align="center" class="style5"><font face="Arial, Helvetica, sans-serif">            </font></div></td>
<td bgcolor="#FFFFE6"><span class="style5"><font face="Arial, Helvetica, sans-serif">       AMANG KIM SONGKYOO     </font></span></td>
<td bgcolor="#FFFFE6"><span class="style5"><font face="Arial, Helvetica, sans-serif">       N_56 </font></span></td>
<td bgcolor="#FFFFE6" width="200"><span class="style5"><font face="Arial, Helvetica, sans-serif">
		2023/01/05-2023/04/22

		</font></span></td>
<td bgcolor="#FFFFE6" nowrap=""><span class="style5"><font face="Arial, Helvetica, sans-serif">       10:00-11:30     </font></span></td>
<td align="center" bgcolor="#FFFFE6"> <div align="center"><font size="1"><b><font face="Arial, Helvetica, sans-serif"> 
	  	
		   
		    

    </font></b></font></div></td>
<td align="center" bgcolor="#FFFFE6"> <div align="center"><font size="1"><b><font face="Arial, Helvetica, sans-serif"> 
	  	
		   
		    
    </font></b></font></div></td>
<td align="center" bgcolor="#FFFFE6"> <div align="center"><font size="1"><b><font face="Arial, Helvetica, sans-serif"> 
	  	
		   
		    
    </font></b></font></div></td>
<td align="center" bgcolor="#FFFFE6"> <div align="center"><font size="1"><b><font face="Arial, Helvetica, sans-serif"> 
	  	
		   
		    
    </font></b></font></div></td>
<td align="center" bgcolor="#FFFFE6"> <div align="center"><font size="1"><b><font face="Arial, Helvetica, sans-serif"> 
	  	
		   
		    
    </font></b></font></div></td>
<td align="center" bgcolor="#FFFFE6"> <div align="center"><font size="1"><b><font face="Arial, Helvetica, sans-serif">
<img align="absmiddle" height="16" src="images/dot.gif" width="16"/>
</font></b></font></div></td>
<td align="center" bgcolor="#FFFFE6"> <div align="center"><font size="1"><b><font face="Arial, Helvetica, sans-serif"> 
	  	
		   
		    
    </font></b></font></div></td>
</tr>
<tr>
<td bgcolor="#FFFFFF"><div align="center" class="style5"><font face="Arial, Helvetica, sans-serif">       2    </font></div></td>
<td bgcolor="#FFFFFF" nowrap=""><span class="style5"><font face="Arial, Helvetica, sans-serif">       COMP224-221    </font></span></td>
<td bgcolor="#FFFFFF"><span class="style5"><font face="Arial, Helvetica, sans-serif">       DATABASE MANAGEMENT SYSTEMS    </font></span></td>
<td bgcolor="#FFFFFF"><span class="style5"><font face="Arial, Helvetica, sans-serif">       YANG XU     </font></span></td>
<td bgcolor="#FFFFFF"><span class="style5"><font face="Arial, Helvetica, sans-serif">       A214 </font></span></td>
<td bgcolor="#FFFFFF" width="200"><span class="style5"><font face="Arial, Helvetica, sans-serif">
		2023/01/05-2023/04/22

		</font></span></td>
<td bgcolor="#FFFFFF" nowrap=""><span class="style5"><font face="Arial, Helvetica, sans-serif">       11:30-13:00     </font></span></td>
<td align="center" bgcolor="#FFFFFF"> <div align="center"><font size="1"><b><font face="Arial, Helvetica, sans-serif"> 
	  	
		   
		    

    </font></b></font></div></td>
<td align="center" bgcolor="#FFFFFF"> <div align="center"><font size="1"><b><font face="Arial, Helvetica, sans-serif"> 
	  	
		   
		    
    </font></b></font></div></td>
<td align="center" bgcolor="#FFFFFF"> <div align="center"><font size="1"><b><font face="Arial, Helvetica, sans-serif">
<img align="absmiddle" height="16" src="images/dot.gif" width="16"/>
</font></b></font></div></td>
<td align="center" bgcolor="#FFFFFF"> <div align="center"><font size="1"><b><font face="Arial, Helvetica, sans-serif"> 
	  	
		   
		    
    </font></b></font></div></td>
<td align="center" bgcolor="#FFFFFF"> <div align="center"><font size="1"><b><font face="Arial, Helvetica, sans-serif"> 
	  	
		   
		    
    </font></b></font></div></td>
<td align="center" bgcolor="#FFFFFF"> <div align="center"><font size="1"><b><font face="Arial, Helvetica, sans-serif"> 
	  	
		   
		    
    </font></b></font></div></td>
<td align="center" bgcolor="#FFFFFF"> <div align="center"><font size="1"><b><font face="Arial, Helvetica, sans-serif"> 
	  	
		   
		    
    </font></b></font></div></td>
</tr>
<tr>
<td bgcolor="#FFFFFF" colspan="3"><div align="center" class="style5"><font face="Arial, Helvetica, sans-serif">            </font></div></td>
<td bgcolor="#FFFFFF"><span class="style5"><font face="Arial, Helvetica, sans-serif">       YANG XU     </font></span></td>
<td bgcolor="#FFFFFF"><span class="style5"><font face="Arial, Helvetica, sans-serif">       A211 </font></span></td>
<td bgcolor="#FFFFFF" width="200"><span class="style5"><font face="Arial, Helvetica, sans-serif">
		2023/01/05-2023/04/22

		</font></span></td>
<td bgcolor="#FFFFFF" nowrap=""><span class="style5"><font face="Arial, Helvetica, sans-serif">       10:00-11:30     </font></span></td>
<td align="center" bgcolor="#FFFFFF"> <div align="center"><font size="1"><b><font face="Arial, Helvetica, sans-serif"> 
	  	
		   
		    

    </font></b></font></div></td>
<td align="center" bgcolor="#FFFFFF"> <div align="center"><font size="1"><b><font face="Arial, Helvetica, sans-serif"> 
	  	
		   
		    
    </font></b></font></div></td>
<td align="center" bgcolor="#FFFFFF"> <div align="center"><font size="1"><b><font face="Arial, Helvetica, sans-serif"> 
	  	
		   
		    
    </font></b></font></div></td>
<td align="center" bgcolor="#FFFFFF"> <div align="center"><font size="1"><b><font face="Arial, Helvetica, sans-serif"> 
	  	
		   
		    
    </font></b></font></div></td>
<td align="center" bgcolor="#FFFFFF"> <div align="center"><font size="1"><b><font face="Arial, Helvetica, sans-serif">
<img align="absmiddle" height="16" src="images/dot.gif" width="16"/>
</font></b></font></div></td>
<td align="center" bgcolor="#FFFFFF"> <div align="center"><font size="1"><b><font face="Arial, Helvetica, sans-serif"> 
	  	
		   
		    
    </font></b></font></div></td>
<td align="center" bgcolor="#FFFFFF"> <div align="center"><font size="1"><b><font face="Arial, Helvetica, sans-serif"> 
	  	
		   
		    
    </font></b></font></div></td>
</tr>
<tr>
<td bgcolor="#FFFFE6"><div align="center" class="style5"><font face="Arial, Helvetica, sans-serif">       2    </font></div></td>
<td bgcolor="#FFFFE6" nowrap=""><span class="style5"><font face="Arial, Helvetica, sans-serif">       COMP225-221    </font></span></td>
<td bgcolor="#FFFFE6"><span class="style5"><font face="Arial, Helvetica, sans-serif">       NETWORK AND SYSTEM ADMINISTRATION    </font></span></td>
<td bgcolor="#FFFFE6"><span class="style5"><font face="Arial, Helvetica, sans-serif">       LIAM LEI KIN     </font></span></td>
<td bgcolor="#FFFFE6"><span class="style5"><font face="Arial, Helvetica, sans-serif">       N_54 </font></span></td>
<td bgcolor="#FFFFE6" width="200"><span class="style5"><font face="Arial, Helvetica, sans-serif">
		2023/01/05-2023/04/22

		</font></span></td>
<td bgcolor="#FFFFE6" nowrap=""><span class="style5"><font face="Arial, Helvetica, sans-serif">       14:30-17:30     </font></span></td>
<td align="center" bgcolor="#FFFFE6"> <div align="center"><font size="1"><b><font face="Arial, Helvetica, sans-serif"> 
	  	
		   
		    

    </font></b></font></div></td>
<td align="center" bgcolor="#FFFFE6"> <div align="center"><font size="1"><b><font face="Arial, Helvetica, sans-serif">
<img align="absmiddle" height="16" src="images/dot.gif" width="16"/>
</font></b></font></div></td>
<td align="center" bgcolor="#FFFFE6"> <div align="center"><font size="1"><b><font face="Arial, Helvetica, sans-serif"> 
	  	
		   
		    
    </font></b></font></div></td>
<td align="center" bgcolor="#FFFFE6"> <div align="center"><font size="1"><b><font face="Arial, Helvetica, sans-serif"> 
	  	
		   
		    
    </font></b></font></div></td>
<td align="center" bgcolor="#FFFFE6"> <div align="center"><font size="1"><b><font face="Arial, Helvetica, sans-serif"> 
	  	
		   
		    
    </font></b></font></div></td>
<td align="center" bgcolor="#FFFFE6"> <div align="center"><font size="1"><b><font face="Arial, Helvetica, sans-serif"> 
	  	
		   
		    
    </font></b></font></div></td>
<td align="center" bgcolor="#FFFFE6"> <div align="center"><font size="1"><b><font face="Arial, Helvetica, sans-serif"> 
	  	
		   
		    
    </font></b></font></div></td>
</tr>
<tr>
<td bgcolor="#FFFFFF"><div align="center" class="style5"><font face="Arial, Helvetica, sans-serif">       2    </font></div></td>
<td bgcolor="#FFFFFF" nowrap=""><span class="style5"><font face="Arial, Helvetica, sans-serif">       MENG221-221    </font></span></td>
<td bgcolor="#FFFFFF"><span class="style5"><font face="Arial, Helvetica, sans-serif">       ENGLISH IV    </font></span></td>
<td bgcolor="#FFFFFF"><span class="style5"><font face="Arial, Helvetica, sans-serif">       CHUI SAI CHAK     </font></span></td>
<td bgcolor="#FFFFFF"><span class="style5"><font face="Arial, Helvetica, sans-serif">       N_52 </font></span></td>
<td bgcolor="#FFFFFF" width="200"><span class="style5"><font face="Arial, Helvetica, sans-serif">
		2023/01/05-2023/04/22

		</font></span></td>
<td bgcolor="#FFFFFF" nowrap=""><span class="style5"><font face="Arial, Helvetica, sans-serif">       14:30-17:30     </font></span></td>
<td align="center" bgcolor="#FFFFFF"> <div align="center"><font size="1"><b><font face="Arial, Helvetica, sans-serif"> 
	  	
		   
		    

    </font></b></font></div></td>
<td align="center" bgcolor="#FFFFFF"> <div align="center"><font size="1"><b><font face="Arial, Helvetica, sans-serif"> 
	  	
		   
		    
    </font></b></font></div></td>
<td align="center" bgcolor="#FFFFFF"> <div align="center"><font size="1"><b><font face="Arial, Helvetica, sans-serif"> 
	  	
		   
		    
    </font></b></font></div></td>
<td align="center" bgcolor="#FFFFFF"> <div align="center"><font size="1"><b><font face="Arial, Helvetica, sans-serif"> 
	  	
		   
		    
    </font></b></font></div></td>
<td align="center" bgcolor="#FFFFFF"> <div align="center"><font size="1"><b><font face="Arial, Helvetica, sans-serif"> 
	  	
		   
		    
    </font></b></font></div></td>
<td align="center" bgcolor="#FFFFFF"> <div align="center"><font size="1"><b><font face="Arial, Helvetica, sans-serif">
<img align="absmiddle" height="16" src="images/dot.gif" width="16"/>
</font></b></font></div></td>
<td align="center" bgcolor="#FFFFFF"> <div align="center"><font size="1"><b><font face="Arial, Helvetica, sans-serif"> 
	  	
		   
		    
    </font></b></font></div></td>
</tr>
<tr>
<td bgcolor="#FFFFFF" colspan="3"><div align="center" class="style5"><font face="Arial, Helvetica, sans-serif">            </font></div></td>
<td bgcolor="#FFFFFF"><span class="style5"><font face="Arial, Helvetica, sans-serif">       HO SIO WA     </font></span></td>
<td bgcolor="#FFFFFF"><span class="style5"><font face="Arial, Helvetica, sans-serif">       B304 </font></span></td>
<td bgcolor="#FFFFFF" width="200"><span class="style5"><font face="Arial, Helvetica, sans-serif">
		2023/02/13-2023/03/18

		</font></span></td>
<td bgcolor="#FFFFFF" nowrap=""><span class="style5"><font face="Arial, Helvetica, sans-serif">       14:30-17:30     </font></span></td>
<td align="center" bgcolor="#FFFFFF"> <div align="center"><font size="1"><b><font face="Arial, Helvetica, sans-serif"> 
	  	
		   
		    

    </font></b></font></div></td>
<td align="center" bgcolor="#FFFFFF"> <div align="center"><font size="1"><b><font face="Arial, Helvetica, sans-serif"> 
	  	
		   
		    
    </font></b></font></div></td>
<td align="center" bgcolor="#FFFFFF"> <div align="center"><font size="1"><b><font face="Arial, Helvetica, sans-serif">
<img align="absmiddle" height="16" src="images/dot.gif" width="16"/>
</font></b></font></div></td>
<td align="center" bgcolor="#FFFFFF"> <div align="center"><font size="1"><b><font face="Arial, Helvetica, sans-serif"> 
	  	
		   
		    
    </font></b></font></div></td>
<td align="center" bgcolor="#FFFFFF"> <div align="center"><font size="1"><b><font face="Arial, Helvetica, sans-serif"> 
	  	
		   
		    
    </font></b></font></div></td>
<td align="center" bgcolor="#FFFFFF"> <div align="center"><font size="1"><b><font face="Arial, Helvetica, sans-serif"> 
	  	
		   
		    
    </font></b></font></div></td>
<td align="center" bgcolor="#FFFFFF"> <div align="center"><font size="1"><b><font face="Arial, Helvetica, sans-serif"> 
	  	
		   
		    
    </font></b></font></div></td>
</tr>
<tr>
<td align="right" bgcolor="#0000CE" colspan="14" height="25" nowrap=""><span class="style26"><font face="Arial, Helvetica, sans-serif"><b> <font face="Arial, Helvetica, sans-serif">
      
      Number of classes:
      
    </font></b>6</font><font face="Arial, Helvetica, sans-serif"></font>
</span></td>
</tr>
</tbody></table>
"""

    def tearDown(self) -> None:
        self.html = None

    def test_HTML2CSVConverter(self) -> None:
        converter: Converter.AbstractConverter = Converter.HTML2CSVConverter(self.html)
        header, records = converter.get_data()
        self.assertEqual(header, self.excepted_header)
        self.assertEqual(records, self.excepted_records)
        # self.assertEqual(excepted, result)
